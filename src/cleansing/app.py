import json
import re
import os
import time
from typing import Optional
import openai
from aws_lambda_powertools.event_handler import (
    APIGatewayRestResolver,
    Response
)
from aws_lambda_powertools.event_handler.exceptions import (
    BadRequestError,
    InternalServerError,
    NotFoundError,
    ServiceError,
)

app = APIGatewayRestResolver()

def lambda_handler(event, context):
    return app.resolve(event, context)

# Add "Accept-Encoding: *" to the request header to use "compress=True"
@app.post("/cleanse/gpt", compress=True)
def openai_handler():
    _: Optional[str] = app.current_event.body
    
    if _ is None:
        raise BadRequestError("Missing required parameter")
    
    # get parameters from the request body
    body_json = json.loads(_)
    addresses_dict = body_json["addresses"]
    params = body_json["params"]
    
    # prepare openai request
    pre_process_instructuions = "translate it to English" if params["translate_output"].lower() == "true" else "keep the original language"
    openai_key = os.environ['openai_key']
    sys_mpt = os.environ['sys_mpt']
    usr_mpt = os.environ['usr_mpt']
    usr_mpt = usr_mpt.replace('[[keep_or_translate]]', pre_process_instructuions)
    # use ensure_ascii=False to keep non-English characters
    usr_mpt += re.sub('\n', '', json.dumps(addresses_dict, ensure_ascii=False, separators=(',', ':')))
    
    cleansed_addresses = ""
    
    # set openai api key and execute openai request
    openai.api_key = openai_key
    # try 5 times if openai is not available
    for i in range(5):
        try:
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system","content": sys_mpt},
                    {"role": "user", "content": usr_mpt}
                ],
                temperature=0
            )

            cleansed_addresses = chat_completion.choices[0].message.content.strip()
            #print(f"addresses: {cleansed_addresses}")
            #split the addresses by newline
            if cleansed_addresses != "":
                break
        except Exception as e:
            try_again_in = 2*(i+1)
            print(f"OpenAI is not available, try again in {try_again_in} seconds, {5-i} times left")
            time.sleep(2*(i+1))
            continue
    
    print(cleansed_addresses)

    # we cannot return JSON here because the cleansed_addresses may have non-English characters
    return Response(
        status_code=200,
        content_type="application/json",
        body = cleansed_addresses
    )