<?php
$id = php_uname("n"). ":". getmypid();
error_log("i am '$id'");

$server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREP);
$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $id);
$server->bind("tcp://127.0.0.1:5555");

while ($client_id = $server->recv()) {
    $empty = $server->recv();

    echo "Got message: $message\n";
    /* echo back the message */
    $server->send($message);
}

