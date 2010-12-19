<?php

$BROKERS = array(
    'SERVERS' => array(
        'tcp://127.0.0.1:6665',
        'tcp://127.0.0.1:6666',
        ),
    'CLIENTS' => array(
        'tcp://127.0.0.1:5555',
        'tcp://127.0.0.1:5556',
        ),
    );

function genSockID($addr=""){
    return getmypid(). ",". $addr;
}