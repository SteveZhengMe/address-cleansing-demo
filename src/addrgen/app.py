import json

def lambda_handler(event, context):
    # get context from authorizer for key "cur_user"
    
    cur_user = event['requestContext']['authorizer']['cur_user']
    body_json = json.loads(event['body'])
    return {
        'statusCode': 200,
        'body': f'Hello from Addrgen Lambda! User: {cur_user}, Request: {body_json}'
    }