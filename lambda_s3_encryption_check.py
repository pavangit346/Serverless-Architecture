import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # List all S3 buckets
    response = s3.list_buckets()
    
    # Iterate through each bucket
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        # Get bucket encryption status
        encryption_response = s3.get_bucket_encryption(Bucket=bucket_name)

        # Check if any server-side encryption is enabled
        if 'ServerSideEncryptionConfiguration' not in encryption_response:
            print(f"Bucket {bucket_name} is unencrypted!")
            # You can take further actions here, e.g., send notifications, apply encryption, etc.
        else:
            print(f"Bucket {bucket_name} is encrypted.")
