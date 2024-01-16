# Serverless-Architecture
Some AWS Cloud best practice tasks automation through boto3 - lambda - cloud watch - aws event bridge - SNS

Each task has been performed and submitted through separate branches.

/////////////////////////////////////////////////////////////////////////////////////////////////////

Q1 - 

Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. Specifically:

1. Setup:

   - Create two EC2 instances.

   - Tag one of them as `Auto-Stop` and the other as `Auto-Start`.

2. Lambda Function Creation:

   - Set up an AWS Lambda function.

   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.

3. Coding:

   - Using Boto3 in the Lambda function:

     - Detect all EC2 instances with the `Auto-Stop` tag and stop them.

     - Detect all EC2 instances with the `Auto-Start` tag and start them.

4. Testing:

   - Manually invoke the Lambda function.

   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.

Instructions:

1. EC2 Setup:

   - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).

   - Tag the first instance with a key `Action` and value `Auto-Stop`.

   - Tag the second instance with a key `Action` and value `Auto-Start`.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 EC2 client.
     2. Describe instances with `Auto-Stop` and `Auto-Start` tags.
     3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
     4. Print instance IDs that were affected for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.
  
   - //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
   - Solution
   - 
- Created two ec2 instances with tag manually - tag:Auto-Start and tag:Auto-Stop
      i-0bbc126416ea8fff8 -- Q1-Auto-Start-Inst-Pavan
      i-09c798b90bc6b8e0c -- Q2-Auto-Stop-Inst-Pavan
- Verfied that instances are running 
- At IAM, created a role, and attached AmazonEc2FullAccess
     -  Lambda_IAM_EC2_Full_Access : IAM Role
- Created a Lambda Function with Python 3.x and attached the IAM role that was created for the Lambda function.
- Wrote te code using boto3 module, and https://boto3.amazonaws.com/v1/documentation
- Deployed the Code on the Lambda function and configured the test configuration.
- Manually tested the function and run.
- Lambda function execution went successful-
- Resultant, The function is stopping the ec2 instance with tag Auto-Stop and starting the instances with tag Auto-Start
- Added all Artifacts to the repository.



