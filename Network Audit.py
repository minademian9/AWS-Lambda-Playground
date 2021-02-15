import boto3

print('Loading function')


ec2 = boto3.client('ec2')



def lambda_handler(event, context):


    failed_sg = []
    
    print('All Security Groups:')
    print('----------------')
    
    sg_all = ec2.describe_security_groups()
    for sg in sg_all['SecurityGroups'] :
        # print(sg['GroupName'])
        # print(sg)
        for rule in sg['IpPermissions']:
            
            # Checking if all protocols are allowed
            
            if rule['IpProtocol'] == '-1':
                failed_sg.append({'Name': sg['GroupName'], 'Id': sg['GroupId']  , "Reason": "All Protocols Allowed"  })
                
                
            # Checking if All IPs are allowed on specfic ports
            
            for ip in rule['IpRanges']:
                if ip['CidrIp'] == "0.0.0.0/0":
                    if (rule['FromPort'] not in [80,443]) or (rule['ToPort'] not in [80,443]):
                        failed_sg.append({'Name': sg['GroupName'], 'Id': sg['GroupId']  , "Reason": "All IPs allowed from port " + str(rule['FromPort']) + " to port " + str(rule['ToPort'])  })
                
            


    print(failed_sg)

    # print('All Route Tables:')
    # print('----------------')
    
    # rt_all = ec2.describe_route_tables()
    # for rt in rt_all['RouteTables']:
    #     print(rt)

