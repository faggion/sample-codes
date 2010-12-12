<?php
$pid = getmypid();
error_log("i am $pid");

$ctxt  = new ZMQContext();

$cl = $ctxt->getSocket(ZMQ::SOCKET_REQ);
$cl->setSockOpt(ZMQ::SOCKOPT_IDENTITY, "cli:".$pid);
$cl->connect("tcp://127.0.0.1:5555");

$cl->send("from $pid", ZMQ::MODE_NOBLOCK);
error_log($cl->recv());
//error_log($cl->send("from $pid")->recv());
