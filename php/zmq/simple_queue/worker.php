<?php
$pid = getmypid();
error_log("i am $pid");

$ctxt  = new ZMQContext();

$wo = $ctxt->getSocket(ZMQ::SOCKET_PULL);
$wo->connect("ipc:///tmp/queue.sock");

while(true){
    error_log("waiting for wo connection...");
    //$msg1 = $wo->recv();
    $addr  = $wo->recv();
    $empty = $wo->recv();
    $body  = $wo->recv();
    error_log("message received.($addr)($body)");
}

