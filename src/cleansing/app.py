import json
import re
import os
from typing import Optional
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
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
    
    addresses_dict = json.loads(_)
    cleansed_addresses_dict = {}
    # change each item in the dict
    for key, value in addresses_dict.items():
        # create a dict {original: str, cleansed: {apt_nbr: str, strt_nbr: str, strt_nm: str, prov: str, cntry:str, pstl_cd: str}}
        cleansed_address = {"apt_nbr": "", "strt_nbr": "", "strt_nm": "", "prov": "", "cntry":"", "pstl": ""}
        cleansed_addresses_dict[key] = {"original": value, "cleansed": cleansed_address}
    
    openai_key = os.environ['openai_key']
    sys_mpt = os.environ['sys_mpt']
    usr_mpt = os.environ['usr_mpt']
    
    # keep the original language
    # translate it to English 
    
    print(re.sub('\n', '', json.dumps(cleansed_addresses_dict   , separators=(',', ':'))))
    return cleansed_addresses_dict