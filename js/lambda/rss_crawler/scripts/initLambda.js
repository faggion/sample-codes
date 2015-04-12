var fs = require('fs');
var config = {
    region: "us-west-2",
    description: '',
    role: 'arn:aws:iam::378014361406:role/lambda_exec_role',
    memorySize: '128',
    handlerFile:"simple_stock_price_crawler",
    handlerMethod:"handler",
    timeout: '10'
};
fs.writeFileSync('./lambdaConfig.json',JSON.stringify(config));
