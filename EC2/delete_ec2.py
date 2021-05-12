import os.path
import boto3

#This script list all ec2 instance filtered by specified tags and appends to list. Next the indexed ec2 instances are terminated. 

#filter by tag key/value and return a list of associated ids.
def list_instances_by_tag_value(key, value):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+key,
                'Values': [value]
            }
        ]
    )
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])
    return instancelist

#terminate instance by id
def delete_identified_instances(cattle):
    ec2_client = boto3.client('ec2')
    ec2_client.terminate_instances(InstanceIds=cattle)


kill_the_cattle = list_instances_by_tag_value(key='Name', value='DeleteMe')
delete_identified_instances(cattle=kill_the_cattle)
    
    
