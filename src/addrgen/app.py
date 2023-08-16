import json
import os

def lambda_handler(event, context):
    # openai key is in Parameter Store "dev__openai"
    openai_key = os.environ['openai_key']
    sys_mpt = os.environ['sys_mpt']
    usr_mpt = os.environ['usr_mpt']
    body_json = json.loads(event['body'])
    
    # check if "cur_user" is in event['requestContext']['authorizer'] and authorizer is in event['requestContext']
    if 'requestContext' not in event or 'authorizer' not in event['requestContext'] or 'cur_user' not in event['requestContext']['authorizer']:
        cur_user = 'unknown'
    else:
        cur_user = event['requestContext']['authorizer']['cur_user']

    # replace all "[[key]]" with the value in usr_mpt        
    for key, value in body_json.items():
        usr_mpt = usr_mpt.replace(f'[[{key}]]', value)
    
    return {
        'statusCode': 200,
        'body': f'Hello from Addrgen Lambda! User: {cur_user}, usr_mpt: {usr_mpt}, openai_key: {openai_key}'
    }