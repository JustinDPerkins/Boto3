import boto3

#This script creates a iam user with s3 read only policy attached for each entry as listed in file

# Define a filename if in same directory or file path.

def create_iam_user(user):
    iam_client = boto3.client('iam')
    iam_client.create_user(UserName=user)
    iam_client.attach_user_policy(UserName=user, PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')