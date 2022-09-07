
import boto3
import AWS_config

def main():
    client = boto_dynamo_connect()
    #table_creation_test(client)
    #table_check_alt()
    #boto_example("test_table")
    print("------")
    ScannedTables = table_scan(client)
    print(ScannedTables)




# Dynamodb connection
def boto_dynamo_connect():
    client = boto3.client('dynamodb',
        aws_access_key_id=AWS_config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_config.AWS_SECRET_ACCESS_KEY,
        region_name=AWS_config.AWS_REGION)
    return client

# Table Creation
# May not need this section...
'''
app = Flask(__name__)
app.config['DYNAMO_TABLES'] = [
    {
         TableName = 'users',
         KeySchema=[dict(AttributeName='username', KeyType='HASH')],
         AttributeDefinitions=[dict(AttributeName='username', AttributeType='S')],
         ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
        }, {
         TableName='groups',
         KeySchema=[dict(AttributeName='name', KeyType='HASH')],
         AttributeDefinitions=[dict(AttributeName='name', AttributeType='S')],
         ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }
]
'''

def table_creation_test(client):
    dynamodb = boto3.resource('dynamodb', region_name=AWS_config.AWS_REGION)
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'createdAt',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print("Table status:", table.table_status)

# Information Extraction -------
"""
# Table Checking
def table_check():
    for table_name, table in Dynamo.tables.items():
        print(table_name, table)"""

def table_check_alt():
    dynamodb = boto3.resource('dynamodb', region_name=AWS_config.AWS_REGION)

    tables = list(dynamodb.tables.all())
    print(tables)
    for table in tables:
        print(table)

# Example of boto3 table usage ------->> Generates an error...

def boto_example(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    print(table)
    creation_time = str(table.creation_date_time)
    print(table_name + " was created at:   " + creation_time)

def table_scan(client):
    return client.scan(
        TableName='Test_table'
    )

def describe_table(client):
    return client.describe_table(
        TableName='Test_table'
    )


main()