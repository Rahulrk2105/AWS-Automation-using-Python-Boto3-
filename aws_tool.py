import boto3
import logging

# Setup logging
logging.basicConfig(
    filename='aws_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def list_running_instances():
    response = ec2.describe_instances()
    print("\nRunning EC2 Instances:\n")

    for r in response['Reservations']:
        for i in r['Instances']:
            if i['State']['Name'] == 'running':
                print(f"Instance: {i['InstanceId']} | State: running")
                logging.info(f"Checked instance {i['InstanceId']}")

def start_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print("Instance started")
    logging.info(f"Started instance {instance_id}")

def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print("Instance stopped")
    logging.info(f"Stopped instance {instance_id}")

def upload_to_s3(file_name, bucket):
    s3.upload_file(file_name, bucket, file_name)
    print("File uploaded to S3")
    logging.info(f"Uploaded {file_name} to {bucket}")

while True:
    print("\n1. List Running EC2")
    print("2. Start EC2")
    print("3. Stop EC2")
    print("4. Upload file to S3")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        list_running_instances()

    elif choice == "2":
        id = input("Enter Instance ID: ")
        start_instance(id)

    elif choice == "3":
        id = input("Enter Instance ID: ")
        stop_instance(id)

    elif choice == "4":
        file = input("Enter file name: ")
        bucket = input("Enter bucket name: ")
        upload_to_s3(file, bucket)

    elif choice == "5":
        break