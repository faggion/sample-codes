// We will put dummy objects for event and context;
var event = {
    crawler: './lib/crawler_example_com',
    parser: './lib/parser_example_com'
};
var context = {
    invokeid: 'string',
    done: function(err,data){
        return;
    }
};
var my_lambda = require('./rss_crawler');
my_lambda.handler(event,context);
