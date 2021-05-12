import boto3

#create a ec2 instance - win 16 base server - aws cli configured
def create_instance(keypair,account,policy):
    #create an ec2 instance
    ec2_client = boto3.client('ec2')
    ec2_client.run_instances(
        ImageId='ami-0f93c815788872c5d',
        KeyName=keypair,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        UserData='<powershell> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi </powershell>'
    )