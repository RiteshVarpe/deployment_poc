import json
import boto3


def getallauthors(event, context):
    ddb_client = boto3.resource("dynamodb")
    table_name = ddb_client.Table('RV_Deployment_POC_Authors')
    ddb_response = table_name.scan()
    print(type(ddb_response))
    print([ddb_response])
    return ddb_response['Items']
    # response = {
    #     "statusCode": 200,
    #     "body": ))
    # }
    # print(response)
    # return response
    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Access-Control-Allow-Origin": "*"
    #     },
    #     "body": json.dumps(ddb_response['Items'])
    # }


def getallcourses(event, context):
    ddb_client = boto3.resource("dynamodb")
    table_name = ddb_client.Table('RV_Deployment_POC_Courses')
    ddb_response = table_name.scan()
    print(type(ddb_response))
    print([ddb_response])
    return ddb_response['Items']
    # response = {
    #     "statusCode": 200,
    #     "body": ))
    # }
    # print(response)
    # return response
    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Access-Control-Allow-Origin": "*"
    #     },
    #     "body": json.dumps(ddb_response['Items'])
    # }

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
    table_name = ddb_client.Table('RV_Deployment_POC_Courses')
    response = table_name.put_item(
        Item = item
    )
    return response



