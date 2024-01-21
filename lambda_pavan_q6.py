import boto3

def lambda_handler(event, context):
    # Get the instance ID from the event
    instance_id = event['detail']['instance-id']

    # Define the tags you want to add
    tags = [
        {
            'Key': 'Batch',
            'Value': 'DevOp2B3'
        },
        {
            'Key': 'Source',
            'Value': 'ForBoto3'
        }
        # Add more tags as needed
    ]

    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Add tags to the instance
    ec2.create_tags(Resources=[instance_id], Tags=tags)

    print(f'Tags added to instance {instance_id}')