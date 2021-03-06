var exec = require('child_process').exec,
    package = require('../package');

var COMMAND_PREFIX = 'rm -fr pkg; mkdir pkg; zip -r';
var MYLIB = 'lib';

var target = package.name,
    main = package.main,
    npm_dir = 'node_modules',
    excludes_str = '';

Object.keys(package.devDependencies).forEach(function(key){
    excludes_str = excludes_str + build_exclude_str(key);
});

var cmd = build_command_str(target,main,excludes_str);
console.log(cmd);
exec(cmd,function(err,stdout,stderr){
    if(err) console.log(err);
    //console.log(stdout);
    //console.log(stderr);
});

function build_exclude_str (key){
    return npm_dir + '/' + key + '\\* ';
}

function build_command_str(target,main,excludes_str){
    return COMMAND_PREFIX
        + ' pkg/' +
        target
        + '.zip ' +
        main
        + ' ' +
        npm_dir
        + ' ' +
        MYLIB
        + ' -x ' +
        excludes_str;
}
