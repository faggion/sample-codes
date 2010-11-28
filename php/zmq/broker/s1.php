<?php
$server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REP);
$server->connect("tcp://127.0.0.1:5556");
$pid = getmypid();
error_log("i am $pid");

/* Loop receiving and echoing back */
while (true){
    $message = $server->recv();
    echo "Got message: $message\n";
    $server->send("$pid received: ". $message);
}
