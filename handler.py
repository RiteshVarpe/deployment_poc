import json
import boto3
import os


def getallcourses(event, context):
    ddb_client = boto3.resource("dynamodb")
    table_name = ddb_client.Table(os.environ['ddb_table_name'])
    ddb_response = table_name.scan()
    print(type(ddb_response))
    print([ddb_response])
    return ddb_response['Items']


def addcourse(event, context):
    with open("data.json") as fp:
        data = json.load(fp)
    item = {
        "title": event['title'],
        "length": event['length'],
        "category": event['category'],
        "watchHref": data['watchHref'],
        "authorId": data['authorId'],
        "id": event['title'].lower()
    }
    ddb_client = boto3.resource("dynamodb")
    table_name = ddb_client.Table(os.environ['ddb_table_name'])
    response = table_name.put_item(
        Item=item
    )
    return response
