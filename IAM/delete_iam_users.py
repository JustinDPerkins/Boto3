import os.path
import boto3

#removes login profile, detaches user policy, and deletes the iam user.

def delete_iam_user(uname, account, policy):
    iam_client = boto3.client('iam')
    iam_client.delete_login_profile(UserName=uname)
    iam_client.detach_user_policy(UserName=uname, PolicyArn='arn:aws:iam::'+account+':policy/'+policy)
    iam_client.delete_user(UserName=uname)

def delete_user_iampolicy(account, policy):
    iam_client = boto3.client('iam')
    iam_client.delete_policy(PolicyArn='arn:aws:iam::'+account+':policy/'+policy)

def delete_rp(rolename, account):
    iam_client = boto3.client('iam')
    iam_client.detach_role_policy(RoleName=rolename, PolicyArn='arn:aws:iam::'+account+':policy/'+rolename)
    iam_client.delete_policy(PolicyArn='arn:aws:iam::'+account+':policy/'+rolename)
    iam_client.remove_role_from_instance_profile(InstanceProfileName= rolename ,RoleName=rolename)
    iam_client.delete_instance_profile(InstanceProfileName=rolename)
    iam_client.delete_role(RoleName=rolename)


delete_iam_user(uname='<user>', account='<account_id>',policy='<policy_name>')
delete_user_iampolicy(account='<account_id>',policy='<policy_name>')
delete_rp(rolename='<rolename>', account='<account_id>')