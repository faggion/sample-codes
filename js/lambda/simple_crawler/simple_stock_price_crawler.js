var aws     = require("aws-sdk");
var cheerio = require('cheerio');
var http    = require ('http');
var s3      = new aws.S3({apiVersion: "2006-03-01"});
aws.config.update({region: "us-west-2"});

exports.handler = function(event, context){
    var bucket = event.Records[0].s3.bucket.name;
    var key    = event.Records[0].s3.object.key;
    console.log(JSON.stringify(event, null, '  '));
    s3.getObject(
        {Bucket:bucket, Key:key},
        function(err, data){
            if(err){
                console.log('error occured !!');
            }
            else {
                //console.log(data);
                console.log(data.Body.toString());
                // "http://stocks.finance.yahoo.co.jp/stocks/history/?code=9984.T"
                http.get(data.Body.toString(), function(res) {
                    var body;
                    console.log("Got response: " + res.statusCode);
                    res.on("data", function(chunk) {
                        body += chunk;
                    });
                    res.on('end', function(res) {
                        console.log('end');
                        //console.log(body);
                        var $ = cheerio.load(body);
                        var title = $("title").text();
                        var stockPrice = $('td[class=stoksPrice]').text();
                        console.log('title: '+title);
                        console.log('stockPrice: '+stockPrice+' 円');
                    });
                });
            }
        }
    );
};
