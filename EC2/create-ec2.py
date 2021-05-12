import boto3
import json
import time

'''
This Script will create a ec2 instance, deploy in default vpc,generates a key pair and saves the pem locally. 
s3 role attached with put and get permission to *!!. trust policy and role creation as well. AWS cli is installed on t2.micro windows 2016 server.
'''
#gather account/resource info
account_id = input("AWS AccountID: ")
policy_name = input("Name for role/trust Policy: ")
kp_name = input("Name for Key Pair: ")

iam_client = boto3.client('iam')
#create permissions the ec2 will need to function
ec2_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "s3:PutObject",
               "s3:GetObject"   
            ],
            "Resource": "*"
        }
    ]
}
response2 = iam_client.create_policy(
  PolicyName=policy_name,
  PolicyDocument=json.dumps(ec2_role_policy)
)

#create a trust policy to assume role
trust_policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal":{"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
})
response3 = iam_client.create_role(
  RoleName=policy_name,
  AssumeRolePolicyDocument=trust_policy
)

#per aws need to attach role policy, create a instance profile and add a role to ip
iam_client.attach_role_policy(PolicyArn='arn:aws:iam::'+account_id+':policy/'+policy_name, RoleName=policy_name)
iam_client.create_instance_profile(InstanceProfileName=policy_name)
iam_client.add_role_to_instance_profile(InstanceProfileName=policy_name, RoleName=policy_name)


ec2_client = boto3.client('ec2')
def create_a_kp(keypair):
    #create kp for ec2 and write it to local system file
    create_kp = ec2_client.create_key_pair(KeyName=keypair)
    pem_key = create_kp['KeyMaterial']
    open_new_file = open(keypair+'.pem', 'w')
    open_new_file.write(pem_key)


def create_instance(keypair,account,policy):
    #create an ec2 instance
    ec2_client = boto3.client('ec2')
    ec2_client.run_instances(
        ImageId='ami-0f93c815788872c5d',
        KeyName=keypair,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        UserData='<powershell> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi </powershell>',
        IamInstanceProfile={'Arn':'arn:aws:iam::'+account+':instance-profile/'+policy}
    )
#sleep for role and policy to create before attaching to ec2
create_a_kp(keypair=kp_name)
time.sleep(5)
create_instance(keypair=kp_name,account=account_id, policy=policy_name)

