var cheerio = require('cheerio');
var http    = require ('http');

exports.handler = function(event, context){
    var crawler = require(event.crawler);
    var parser  = require(event.parser);

    var r = crawler.get(parser);
    console.log("response is [" + r + ']');
};
