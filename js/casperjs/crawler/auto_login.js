var links = [];
var casper = require('casper').create();
//var domain = 'localhost';
var domain = '.localhost';

casper.echo('Cookies enabled?: ' + phantom.cookiesEnabled);

phantom.addCookie({
    domain: domain,
    name: 'name',
    value: 'testname'
});
phantom.addCookie({
    domain: domain,
    name: 'name2',
    value: 'testname2'
});

casper.start('http://localhost:5000/', function() {
    var needLogin = this.evaluate(function(){
        return document.querySelector('#name') ? true : false;
    });
    console.log('need to login => ' + needLogin);

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
    var cookie = this.evaluate(function() {
        return document.cookie;
    });
    //casper.echo(cookie);
    console.log(cookie);
    this.capture('mail.png');
});
casper.run();