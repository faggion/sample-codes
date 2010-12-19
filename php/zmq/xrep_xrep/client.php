<?php

if(empty($argv[1])){
    exit(1);
}

$to_addr = $argv[1];
$pid     = getmypid();
$req     = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREP);
$req->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$req->connect("tcp://127.0.0.1:5556");

error_log("send to ".    $to_addr);
error_log("my pid id ".  $pid);

while (true){
    $req->send($to_addr, ZMQ::MODE_SNDMORE);
    $req->send("",       ZMQ::MODE_SNDMORE);
    $req->send("hello from $pid");
    sleep(1);
}

