<?php

if(empty($argv[1])){
    exit(1);
}

$my_addr = $argv[1];
$pid     = getmypid();
$server  = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREP);
$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $my_addr);
$server->bind("tcp://127.0.0.1:5556");

error_log("my addr is ". $my_addr);
error_log("my pid id ".  $pid);

while (true){
    $from  = $server->recv();
    $empty = $server->recv();
    $mes   = $server->recv();
    error_log("[$from][$empty][$mes]");
}
