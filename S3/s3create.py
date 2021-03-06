import re
import logging
import boto3
from botocore.exceptions import ClientError



#create s3 function to be called
def create_bucket(bucket_name, region):
    
    try:
        # if region left blank
        if region == "" :
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        #specify default region
        elif region == "us-east-1":
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        # any other specified region
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)

    except ClientError as e:
        logging.error(e)
        return False
    return True

# call function
create_bucket(bucket_name='name_your_bucket', region='')