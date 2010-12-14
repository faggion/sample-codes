<?php
$pid    = getmypid();
$server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REP);
$server->bind("tcp://127.0.0.1:5556");

error_log("i am $pid");

while (true){
    //$id    = $server->recv();
    //$empty = $server->recv();
    $mes   = $server->recv();
    error_log("[$mes]");
    $server->send("[$mes]");
}
