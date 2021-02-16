const aws = require('aws-sdk')

const ec2 = new aws.EC2()

ec2.describeNetworkAcls(params = {}, function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
//   else  console.log(data);        //   console.log(data['NetworkAcls'][1]['Entries']);           // successful response
   
   for (let nacl of data['NetworkAcls'])
   {
      for (let rule of nacl['Entries']) 
      {
        //   console.log(data['NetworkAcls'][i]['Entries'][j]);
        //   console.log(rule);
          
           if (rule['RuleAction'] == 'allow' && rule["CidrBlock"] == "0.0.0.0/0")
            if ('PortRange' in rule)
                       {
                           if (! ((rule['PortRange']['From']==80 && rule['PortRange']['To']==80) || (rule['PortRange']['From']==443 && rule['PortRange']['To']==443) || (rule['PortRange']['From']>=1024 && rule['PortRange']['To']>=65535) || (rule['PortRange']['From']>=32768 && rule['PortRange']['To']>=32768))  )
                                console.log(nacl['NetworkAclId'] + " Port Range " + rule['PortRange']['From'].toString() + " - " + rule['PortRange']['To'].toString());
                       }
                       else { console.log(nacl['NetworkAclId'] + " Allowing all IPs on all ports " ) }

      }
   }
   
 });


// for index,val in nacl_df.iterrows():
//    for nacl in nacl_df.loc[index,'Entries']:
//       if nacl['RuleAction'] == 'allow'and nacl['Protocol'] == '-1':
//          failflag = True

exports.handler =  (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!')
        // body : ec2.describeNetworkAcls()
    };
    return response;
};
