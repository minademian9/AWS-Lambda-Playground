const aws = require('aws-sdk')

const ec2 = new aws.EC2()

ec2.describeNetworkAcls(params = {}, () => {console.log("I am in")} )



// console.log(ec2.describeNetworkAcls())

console.log("HELOOOOO")

// exports.handler = async (event) => {
//     // TODO implement
//     const response = {
//         statusCode: 200,
//         body: JSON.stringify('Hello from Lambda!')
//         // body : ec2.describeNetworkAcls()
//     };
//     return response;
// };
