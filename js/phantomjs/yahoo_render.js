var page = require('webpage').create();
var url = 'http://www.yahoo.co.jp/';
page.open(url, function(status) {
    console.log(status);
    var ret = page.render('/tmp/yahoo.png');
    console.log(ret);
    phantom.exit();
});