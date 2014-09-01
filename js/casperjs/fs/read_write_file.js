var fs    = require('fs');
var utils = require('utils');
var data  = fs.read('sample.json');
//console.log(data);
//console.log(utils);
utils.dump(data);

fs.write('/tmp/output.txt', data + ' // this is additional message', 'w');

var casper = require('casper').create();
casper.start('http://localhost:3000/', function() { });
casper.run();
