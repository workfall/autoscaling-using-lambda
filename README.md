# Lambda - AWS

AWS Lambda is a Serverless approach which means a compute service that allows us to run application code without the need of provisioning and managing servers.

In this guide , We will using AWS services such as Lambda , Cloudwatch Event Rules which will automatically Deregister & Stop , Start & Register EC2 instances that are running behind the Application Load Balancer.

Repository consists of the following files:

   1) deregister-stop-ec2.py - create a lambda function and import this code. This code is responsible for dereregistering and stopping of EC2 instances behing ALB.

   2) start-register-ec2.py - create a lambda function and import this code. This code is responsible for starting and registering of EC2 instances behind ALB.

   3) iam-policy-lambda-ec2-access - consists of IAM policy which will grant permission for the lambda to manage EC2 instances.

What's Next:

1) Clone this repo into your local machine of desired folder.

2) Edit the files by replacing the instance details , Target Group ARN and AWS Account Number.


Contact: contact@workfall.com
