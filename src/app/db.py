import boto3
import os
# from dotenv import load_dotenv

# load_dotenv()

DYNAMO_ID = os.getenv('DYNAMO_ID')
DYNAMO_KEY = os.getenv('DYNAMO_KEY')
DYNAMO_TABLE = "RowdyTable"

def get_item(id):
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1',
        aws_access_key_id=DYNAMO_ID,
        aws_secret_access_key=DYNAMO_KEY
    )
    try:
        table = dynamodb.Table(DYNAMO_TABLE) 
        response = table.get_item(Key={"userID": id})
        item = response.get("Item")
        return item["Query"]
    except Exception:
        return -1


def add_item(id, value):
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1',
        aws_access_key_id=DYNAMO_ID,
        aws_secret_access_key=DYNAMO_KEY
    )

    table = dynamodb.Table(DYNAMO_TABLE)

    response = table.put_item(
        Item={
            'userID': id,
            'Query' : value,
        }
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Item added successfully!")
    else:
        print("Error adding item.")

add_item("1234", 5)
print(get_item("1234"))