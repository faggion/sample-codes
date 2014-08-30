var links = [];
var casper = require('casper').create();

casper.start('http://localhost:5000/', function() {
    var needLogin = this.evaluate(function(){
        return document.querySelector('#name') ? true : false;
    });
    console.log(needLogin);

    if(needLogin){
        this.fill('form[action="/login"]',
                  { name: 'valid_user',
                    password: 'invalid_password' },
                  false);

        this.evaluate(function() {
            document.querySelector('form[action="/login"] input[type="submit"]').click();
        });
    }
});

casper.then(function() {
    this.capture('mail.png');
});
casper.run();