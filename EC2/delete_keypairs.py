import os.path
import boto3

#This script deletes ec2 key pairs.
def delete_kp(kpname):
    ec2_client = boto3.client('ec2')
    ec2_client.delete_key_pair(KeyName=kpname)

delete_kp(kpname='<name-of-kp>')
    
