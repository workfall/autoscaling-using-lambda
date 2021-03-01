#Deregister and Stop the instance
 
import boto3
client = boto3.client('elbv2')
response = client.deregister_targets(
    TargetGroupArn='arn:aws:elasticloadbalancing:ap-southeast-1:045936542620:targetgroup/testing/df625de58481ccc0',
    Targets=[
        {
            'Id': 'i-0a62974g748f35801',
        },
    ],
)
 
import time
time.sleep(310)
 
import boto3
client = boto3.client('ec2')
response = client.stop_instances(
    InstanceIds=[
        'i-0a62974g748f35801',
    ]
)
