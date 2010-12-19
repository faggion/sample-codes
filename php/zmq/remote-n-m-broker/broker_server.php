<?php

// my name
if(empty($argv[1])){
    error_log("empty my name");
    exit(1);
}

$myname = $argv[1];
$poll   = new ZMQPoll();
$ctxt   = new ZMQContext();

error_log("my name is '$myname'");

// local tcp
$local = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$local->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $myname);
$local->bind($myname);

$readable = array();
$writable = array();

while(true){
    $from_bc     = $local->recv();
    $empty       = $local->recv();
    $from_client = $local->recv();
    $empty       = $local->recv();
    $request     = $local->recv();

    $response = "$myname got request [$request] from [$from_client]";
    error_log($response);

    $local->send($from_bc,     ZMQ::MODE_SNDMORE);
    $local->send("",           ZMQ::MODE_SNDMORE);
    $local->send($from_client, ZMQ::MODE_SNDMORE);
    $local->send("",           ZMQ::MODE_SNDMORE);
    $local->send($response);
}
