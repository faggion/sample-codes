var crypto  = require('crypto');
var stdin = require('./stdin.js');
stdin.read(function(data){
    var input = data.replace(/[\n\r]/g,"");
    var cipher  = crypto.createCipher('aes-256-cbc', 'password');
    var crypted = cipher.update(input, 'utf-8', 'hex');
    crypted    += cipher.final('hex');
    console.log(crypted);
});
