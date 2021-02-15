import json
import urllib.parse
import boto3

print('Loading function')

ec2 = boto3.client('ec2')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    
    print('All Security Groups:')
    print('----------------')
    
    sg_all = ec2.describe_security_groups()
    for sg in sg_all['SecurityGroups'] :
        # print(sg['GroupName'])
        print(sg)


    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
