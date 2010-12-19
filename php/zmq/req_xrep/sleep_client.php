<?php
$pid  = getmypid();

$req  = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);

//$req->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);

error_log("i am $pid");

$req->connect("tcp://127.0.0.1:5556");

sleep(10);

error_log($req->send("i am $pid")->recv());
