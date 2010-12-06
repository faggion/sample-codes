<?php
$pid = getmypid();
//error_log("i am $pid");

$cli = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$cli->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$cli->connect("tcp://127.0.0.1:5555");

error_log($cli->send("from ".$argv[1])->recv());

