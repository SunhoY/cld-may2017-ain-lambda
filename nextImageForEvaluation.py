import boto3

def lambda_handler(event, context):
    bucket = boto3.resource('s3').Bucket('ain-images')
    return {
        'files': [o.key for o in bucket.objects.all()]
    }
