import boto3

print('Loading function')


ec2 = boto3.client('ec2')



def lambda_handler(event, context):


    failed_sg = []
    failed_rt = []
    
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
    
    print('----------------')
    print('All Route Tables:')
    print('----------------')
    
    
    
    rt_all = ec2.describe_route_tables()
    for rt in rt_all['RouteTables']:
        igw_flag = False
        vgw_flag = False
        for rule in rt['Routes']:
            if "igw" in rule['GatewayId']:
                igw_flag = True
            if "vgw" in rule['GatewayId']:
                vgw_flag = True
        if igw_flag and vgw_flag:
            failed_rt.append(rt['RouteTableId'])
    
    print (failed_rt)
            

