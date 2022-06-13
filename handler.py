import json


def hello(event, context):
    body = {
        "message": "Hello World! This is the Serverless deployment POC",
        "input": event,
    }

    return {"statusCode": 200, "body": body}
