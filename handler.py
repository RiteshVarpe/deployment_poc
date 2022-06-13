import json


def hello(event, context):
    body = {
        "message": "Hello World! Testing with Manual approval for prod deploy",
        "input": event,
    }

    return {"statusCode": 200, "body": body}
