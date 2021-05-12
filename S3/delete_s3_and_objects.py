import os.path
import boto3

#This script deletes all s3 objects inside a bucket and then deletes the s3 bucket itself. 
        
def empty_s3objects(bucket):
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket)
    if 'Contents' in response:
        for s3_object in response['Contents']:
            s3_client.delete_object(Bucket=bucket, Key=s3_object['Key'])

def delete_bucket(bucket):
    s3_client = boto3.client('s3')
    s3_client.delete_bucket(Bucket=bucket)


empty_s3objects(bucket='<name-of-bucket>')
delete_bucket(bucket='<name-of-bucket>')
    
