<?php

$BROKERS = array(
    'SERVERS' => array(
        array('fe'=>'tcp://127.0.0.1:6665', 'be'=>'ipc:///tmp/workers.sock'),
        ),
    'CLIENTS' => array(
        array('fe'=>'ipc:///tmp/clients.sock'),
        ),
    );

function genSockID($addr=""){
    return getmypid(). ",". $addr;
}
function checkinput(&$a){
    if(!isset($a[1])){
        error_log("invalid argv");
        exit(1);
    }
}
function dbg($msg){
    if(1) error_log($msg);
}