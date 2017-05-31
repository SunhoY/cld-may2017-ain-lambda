import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    client.put_item(TableName='AinSurveyByUser', Item={
        'Username': {
            'S': event['username']
        },
        'ImageFileName': {
            'S': event['imageFilename']
        },
        'Favorability': {
            'N': str(event['favorability'])
        }
    })
    return 'OK'