<?php
$pid = getmypid();
error_log("i am $pid");

$ctxt  = new ZMQContext();

$fe = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$fe->bind("tcp://127.0.0.1:5555");

$be = $ctxt->getSocket(ZMQ::SOCKET_PUSH);
$be->setSockOpt(ZMQ::SOCKOPT_IDENTITY, "foo:".$pid);
$be->bind("ipc:///tmp/queue.sock");

while(true){
    error_log("waiting for fe connection...");
    $addr = $fe->recv();
    $msg2 = $fe->recv();
    $msg3 = $fe->recv();
    $msg  = "[$addr][$msg2][$msg3]";
    error_log("message received.[$addr][$msg2][$msg3]");
    //$be->send($msg, ZMQ::MODE_NOBLOCK);
    $be->send($addr, ZMQ::MODE_SNDMORE);
    $be->send("", ZMQ::MODE_SNDMORE);
    $be->send("OK");

    // beからは、戻ってこないのでOKを返す
    $fe->send($addr, ZMQ::MODE_SNDMORE);
    $fe->send("", ZMQ::MODE_SNDMORE);
    $fe->send("OK");
}
