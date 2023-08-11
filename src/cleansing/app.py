import json

def lambda_handler():
    print("In Cleansing Handler")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Cleansing Lambda!')
    }