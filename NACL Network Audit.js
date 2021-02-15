const aws = require('aws-sdk')

const ec2 = new aws.EC2()

ec2.describeNetworkAcls(params = {}, ( function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);           // successful response
 });



// exports.handler = async (event) => {
//     // TODO implement
//     const response = {
//         statusCode: 200,
//         body: JSON.stringify('Hello from Lambda!')
//         // body : ec2.describeNetworkAcls()
//     };
//     return response;
// };
