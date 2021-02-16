const aws = require('aws-sdk')

const ec2 = new aws.EC2()

ec2.describeNetworkAcls(params = {}, ( function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);           // successful response
 });

// for nacl in nacl_df.loc[index,'Entries']:
//         if nacl['RuleAction'] == 'allow' and nacl["CidrBlock"] == "0.0.0.0/0":
//             if 'PortRange' in nacl:
//                         if not ((nacl['PortRange']['From']==80 and nacl['PortRange']['To']==80) or (nacl['PortRange']['From']==443 and nacl['PortRange']['To']==443)or (nacl['PortRange']['From']>=1024 and nacl['PortRange']['To']>=65535) or (nacl['PortRange']['From']>=32768 and nacl['PortRange']['To']>=32768)):


// for index,val in nacl_df.iterrows():
//    for nacl in nacl_df.loc[index,'Entries']:
//       if nacl['RuleAction'] == 'allow'and nacl['Protocol'] == '-1':
//          failflag = True

// exports.handler = async (event) => {
//     // TODO implement
//     const response = {
//         statusCode: 200,
//         body: JSON.stringify('Hello from Lambda!')
//         // body : ec2.describeNetworkAcls()
//     };
//     return response;
// };
