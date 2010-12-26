<?php

if(empty($argv[1])){
    error_log('ERROR: empty argv');
    exit();
}
$m = new Memcache();
$n = $argv[1];
for($i=0;$i<$n;$i++){
    $m->connect('localhost', 11211);
    $m->set('hoge', '1234567890', 0, 0);
    $m->get('hoge');
    $m->close();
}