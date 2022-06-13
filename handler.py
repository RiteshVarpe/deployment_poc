import json


def hello(event, context):
    body = {
        "message": "Hello World! Today is Monday.",
        "input": event,
    }

    return {"statusCode": 200, "body": body}
