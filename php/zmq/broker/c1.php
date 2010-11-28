<?php
//var_dump($argv);

$queue = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$queue->connect("tcp://127.0.0.1:5555");

for($i=0;$i<10;$i++){
    var_dump($queue->send($i)->recv());
}
