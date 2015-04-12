var CrawlerExampleCom = {
    get: function(parser){
        var url = 'http://example.com';
        
        // http get url...
        console.log('getting... [' + url + ']');

        var html = "<h1>hello</h1>";
        return parser.parse(html);
    }
};
module.exports = CrawlerExampleCom;
