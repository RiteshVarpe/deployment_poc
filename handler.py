import json


def hello(event, context):
    body = {
        "message": "Hello World! This is the Rainy day",
        "input": event,
    }

    return {"statusCode": 200, "body": body}
