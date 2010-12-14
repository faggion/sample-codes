<?php
require_once('common.php');

$pid = getmypid();
$req = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_PAIR);
$req->connect("tcp://127.0.0.1:5555");

for($i=0;$i<4;$i++){
    //L("sleeping 1sec");
    sleep(1);
    L("sending msg$i");
    $req->send("msg$i:". date('c'));
}

L("sleeping 3sec");
sleep(3);
L("receiving 4 messages");

for($i=0;$i<4;$i++){
    L($req->recv());
}
