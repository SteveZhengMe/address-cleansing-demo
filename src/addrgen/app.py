import json

def lambda_handler():
    print("In Addrgen Handler")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Addrgen Lambda!')
    }