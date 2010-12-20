<?php

$group   = 'bar';
$pid     = getmypid();
$server  = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREP);
$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $group);
$server->bind("tcp://127.0.0.1:5556");

error_log("my addr is ". $group);
error_log("my pid id ".  $pid);

while (true){
    $from  = $server->recv();
    //$empty = $server->recv();
    $mes   = $server->recv();
    error_log("from=[$from], mes=[$mes]");
}
