<?php
$pid = getmypid();
error_log("i am $pid");

$server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$server->connect("tcp://127.0.0.1:5556");

$server->send("READY");
/* Loop receiving and echoing back */
while (true){
    $addr  = $server->recv();
    $empty = $server->recv();
    $req   = $server->recv();

    error_log("SERVER:". implode(",", array($addr, $empty, $req)));
    if($req==="from 0"){
        sleep(3);
    }

    $server->send($addr, ZMQ::MODE_SNDMORE);
    $server->send("", ZMQ::MODE_SNDMORE);
    $server->send($req. ":$pid:OK");
}
