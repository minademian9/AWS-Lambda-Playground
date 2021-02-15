import re
import boto3

print('Loading function')


ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    all_ip = False #flag to find 0.0.0.0/0 IP addresses

    failed_sg = []
    
    print('All Security Groups:')
    print('----------------')
    
    sg_all = ec2.describe_security_groups()
    for sg in sg_all['SecurityGroups'] :
        # print(sg['GroupName'])
        for rule in sg['IpPermissions']:
            for ip in rule['IpRanges']:
                if ip['CidrIp'] == "0.0.0.0/0":
                    all_ip=True
                    break
            if all_ip:
                if (rule['FromPort'] not in [80,443]) and (rule['ToPort'] not in [80,443]):
                    failed_sg.append({'Name': sg['GroupName'], 'Id': sg['GroupId']  , "Reason": "All IPs allowed from port " + str(rule['FromPort']) + " to port " + str(rule['ToPort'])  })


    print(failed_sg)

    # print('All Route Tables:')
    # print('----------------')
    
    # rt_all = ec2.describe_route_tables()
    # for rt in rt_all['RouteTables']:
    #     print(rt)

