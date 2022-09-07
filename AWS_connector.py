import boto3
import json
import AWS_config

def main():
    client, dynamo_resource = boto_dynamo_connect()
    #table_creation_test(client)
    #table_check_alt()
    #boto_example("test_table")
    print("------")
    #ScannedTables = table_scan(client)
    #print(ScannedTables)

    #get_all_tables()
    get_all_items(dynamo_resource)




# Dynamodb connection
def boto_dynamo_connect():
    client = boto3.client('dynamodb',
        aws_access_key_id=AWS_config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_config.AWS_SECRET_ACCESS_KEY,
        region_name=AWS_config.AWS_REGION)
    dynamodb_resource = boto3.resource('dynamodb', region_name = AWS_config.AWS_REGION)
    print(client)
    return client, dynamodb_resource

def table_check_alt():
    dynamodb = boto3.resource('dynamodb', region_name=AWS_config.AWS_REGION)

    tables = list(dynamodb.tables.all())
    print(tables)
    for table in tables:
        print(table)

def table_scan(client):
    return client.scan(
        TableName='Test_table'
    )

def describe_table(client):
    return client.describe_table(
        TableName='Test_table'
    )

def get_all_tables():
    dynamodb = boto3.resource('dynamodb', region_name=AWS_config.AWS_REGION)

    tables = list(dynamodb.tables.all())
    print(tables)

def get_all_items(dynamo_resource):
    dynamodb_resource = boto3.resource('dynamodb', region_name = AWS_config.AWS_REGION)
    table = dynamodb_resource.Table('Test_table')

    response = table.scan()
    table_data = response['Items']

    while 'LastEvaluatedkey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        table_data.extend(response['Items'])

    if(len(table_data) <1):
        print("No Items in table")

    print(table_data)

main()