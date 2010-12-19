<?php
$pid = getmypid();

$cli = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$cli->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$cli->connect("tcp://127.0.0.1:5555");

error_log("i am $pid");
error_log("RESPONSE IS '". $cli->send("hello")->recv(). "'");

