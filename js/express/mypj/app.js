var express = require('express');
var app = express();

app.set('view engine', 'jade');

app.use(express.static(__dirname + '/public'));
app.set('views', __dirname + '/views');

app.get('/', function (req, res) {
    res.render('index', { title: 'Express Sample' });
});

app.listen(3000);
