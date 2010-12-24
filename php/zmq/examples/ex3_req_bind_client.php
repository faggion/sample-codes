<?php

$pid = getmypid();
$req = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$req->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$req->bind("tcp://127.0.0.1:5555");

error_log("my pid id ".  $pid);

while (true){
    error_log('send message');
    $req->send("hello from $pid ". time());
    sleep(1);
    error_log($req->recv());
}
