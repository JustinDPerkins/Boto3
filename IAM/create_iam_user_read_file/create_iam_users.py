import os.path
import boto3

#This script reads a txt file in line by line and creates a iam user with s3 read only policy attached for each entry as listed in file

# Define a filename if in same directory or file path.
filename = "sample_users.txt"

if not os.path.isfile(filename):
    print('File does not exist.')
else:
# Open the file.
    with open(filename) as f:
        content = f.read().splitlines()

for users in content:
    iam_client = boto3.client('iam')
    iam_client.create_user(UserName=users)
    iam_client.attach_user_policy(UserName=users, PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')

