<?php
if(!isset($argv[1])){
    exit(1);
}
$group   = $argv[1];
$pid     = getmypid();
$server  = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREP);
$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $group);
$server->connect("tcp://127.0.0.1:5555");

error_log("my addr is ". $group);
error_log("my pid id ".  $pid);

while (true){
    $from  = $server->recv();
    $mes   = $server->recv();
    error_log("from=[$from], mes=[$mes]");
}