from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')


table = dynamodb.create_table(
    TableName='Movies10',
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
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)

# Add Index if you want to search via Movie Title
#update = dynamodb.update_table(
##    TableName = 'Movies5',
 #   GlobalSecondaryIndexUpdates=[
 #       {
 #           'Create': {
 ##               'IndexName': 'title-index',
#                'KeySchema': [
#                    {
##                        'AttributeName': 'title',
 #                       'KeyType': 'HASH'
#                    }
#                ],
#                'Projection': {
#                    'ProjectionType': 'ALL'
#                },
#                'ProvisionedThroughput': {
#                    'ReadCapacityUnits': 1,
#                    'WriteCapacityUnits': 1
 #               }
#            }
#        }
#    ],
#    
#)
