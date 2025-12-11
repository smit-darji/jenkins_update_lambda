import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Lambda Deployment Success - Updated!12122121221")
    }


