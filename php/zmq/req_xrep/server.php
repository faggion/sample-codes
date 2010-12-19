<?php
$pid    = getmypid();

$server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREP);

//$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);

$server->bind("tcp://127.0.0.1:5556");

error_log("i am $pid");

while (true){
    $id    = $server->recv();
    $empty = $server->recv();
    $mes   = $server->recv();
    error_log("[$mes][". strlen($id). "]");
    $server->send($id, ZMQ::MODE_SNDMORE);
    $server->send("",  ZMQ::MODE_SNDMORE);
    $server->send("[$mes]");
    error_log("send finished");
}
