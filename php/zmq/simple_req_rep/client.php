<?php
$pid = getmypid();
$req = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$req->connect("tcp://127.0.0.1:5555");
error_log($req->send($pid)->recv());
