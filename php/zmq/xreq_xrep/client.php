<?php

$pid     = getmypid();
$req     = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREQ);
$req->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$req->connect("tcp://127.0.0.1:5556");
$req->connect("tcp://127.0.0.1:5555");

error_log("my pid id ".  $pid);

while (true){
    //$req->send($pid, ZMQ::MODE_SNDMORE);
    //$req->send('',   ZMQ::MODE_SNDMORE);
    $req->send("hello from $pid ". time());
    sleep(1);
}

