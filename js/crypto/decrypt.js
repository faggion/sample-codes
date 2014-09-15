var crypto  = require('crypto');
var stdin = require('./stdin.js');
stdin.read(function(data){
    var input = data.replace(/[\n\r]/g,"");
    decipher   = crypto.createDecipher('aes-256-cbc', 'password');
    dec  = decipher.update(input, 'hex', 'utf-8');
    dec += decipher.final('utf-8');
    console.log(dec);
});
