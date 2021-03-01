#Register and start the instance
import boto3
client = boto3.client('ec2')
response = client.start_instances(
    InstanceIds=[
        'i-0a62974g748f35801',
    ]
)
 
import time
time.sleep(30)
 
import boto3
client = boto3.client('elbv2')
response = client.register_targets(
    TargetGroupArn='arn:aws:elasticloadbalancing:ap-southeast-1:045475842620:targetgroup/testing/df625de58481ccc0',
    Targets=[
        {
            'Id': 'i-0a62974g748f35801',
        },
    ],
)
