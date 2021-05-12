import boto3
import json

def create_role_and_trust(policy_name, account):
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
    iam_client.create_policy(PolicyName=policy_name,PolicyDocument=json.dumps(ec2_role_policy))

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
    #per aws need to attach role policy, create a instance profile and add a role to ip
    iam_client.create_role(RoleName=policy_name,AssumeRolePolicyDocument=trust_policy)
    iam_client.attach_role_policy(PolicyArn='arn:aws:iam::'+account+':policy/'+policy_name, RoleName=policy_name)
    iam_client.create_instance_profile(InstanceProfileName=policy_name)
    iam_client.add_role_to_instance_profile(InstanceProfileName=policy_name, RoleName=policy_name)
    

