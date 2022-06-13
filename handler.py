import json


def hello(event, context):
    body = {
        "message": "Hello World! Good evening!",
        "input": event,
    }

    return {"statusCode": 200, "body": body}
