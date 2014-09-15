var q = require('q');

function read_from_stdin(){
    var d = q.defer();
    process.stdin.setEncoding('utf8');
    process.stdin.on('readable', function() {
        var chunk = process.stdin.read();
        if (chunk !== null) {
            d.resolve(chunk);
            //data = chunk;
            //process.stdout.write('data: ' + data);
            //return chunk;
        }
    });

    return d.promise;
}

function dump_stdin(data){
    console.log(data);
}

q.when()
    .then(read_from_stdin)
    .then(dump_stdin)
    .done(function(v) {
        console.log('... done.');
    });