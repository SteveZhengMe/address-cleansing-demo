import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    method_arn = event['methodArn']
    auth_token = event['authorizationToken']
    # method_arn = arn:aws:execute-api:us-east-1:12345668:abcd1234/ESTestInvoke-stage/GET/
    
    # get "us-east-1" from method_arn
    region = method_arn.split(':')[3]
    # get "12345668" from method_arn
    account_id = method_arn.split(':')[4]
    # get "abcd1234" from method_arn
    api_id = method_arn.split(':')[5].split('/')[0]
    
    return {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": f"arn:aws:execute-api:{region}:{account_id}:{api_id}/*/*"
                }
            ]
        },
        "context": {
            "cur_user": "steve"
        }
    }