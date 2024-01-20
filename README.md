# Serverless-Architecture
Some AWS Cloud best practice tasks automation through boto3 - lambda - cloud watch - aws event bridge - SNS

Each task has been performed and submitted through separate branches.
/////////////////////////////////////////////////////////////////////////////////
Assignment 4: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
Objective: To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side
encryption.
Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.
Instructions:
1. S3 Setup:
- Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.
2. Lambda IAM Role:
- In the IAM dashboard, create a new role for Lambda.
- Attach the `AmazonS3ReadOnlyAccess` policy to this role.
3. Lambda Function:
- Navigate to the Lambda dashboard and create a new function.
- Choose Python 3.x as the runtime.

- - Assign the IAM role created in the previous step.
- Write the Boto3 Python script to:
1. Initialize a boto3 S3 client.
2. List all S3 buckets.
3. Detect buckets without server-side encryption.
4. Print the names of unencrypted buckets for logging purposes.
4. Manual Invocation:
- After saving your function, manually trigger it.
- Review the Lambda logs to identify the buckets without server-side encryption

# Solution 

Created th IAM role : AWSS3ReadOnlyAccess-Lambda-Q4

Created the Lambda function : lambda-pavan-s3check-q4 and assigned the IAM role.

Checked the S3 buckets.

Deployed the lambda function and tested.

Able to track all the buckets are Encrypted.

Added the comments to the code.

Attached all the snapshots.
Boto3 coo


