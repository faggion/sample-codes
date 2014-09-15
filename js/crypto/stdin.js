function read_from_stdin(cb){
    process.stdin.setEncoding('utf8');
    process.stdin.on('readable', function() {
        var chunk = process.stdin.read();
        if (chunk !== null) {
            cb(chunk);
        }
    });
}

module.exports.read = read_from_stdin;

