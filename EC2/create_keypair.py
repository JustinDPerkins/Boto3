import boto3

#create kp for ec2 and write it to local system file
def create_a_kp(keypair):
    ec2_client = boto3.client('ec2')
    create_kp = ec2_client.create_key_pair(KeyName=keypair)
    pem_key = create_kp['KeyMaterial']
    open_new_file = open(keypair+'.pem', 'w')
    open_new_file.write(pem_key)

create_a_kp(keypair='name-of-kp')