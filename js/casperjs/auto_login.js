var links = [];
var casper = require('casper').create();

casper.start('http://localhost:5000/', function() {
    this.fill('form[action="/update"]',
              { username: 'valid_user',
                password: 'invalid_password' },
              false);
    this.evaluate(function() {
        //document.querySelector('#submit').click();
        //document.querySelector('input[type="submit"]').click();
        document.querySelector('form[action="/update"] input[type="submit"]').click();
    }); 
    this.capture('mail0.png');
});

casper.then(function() {
    this.capture('mail.png');
});
casper.run();