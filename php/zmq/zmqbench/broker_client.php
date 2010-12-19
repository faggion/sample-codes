<?php

if(!isset($argv[1])){
    error_log("invalid argv");
    exit(1);
}

require_once('common.php');

$readable  = array();
$writable  = array();
$pollids   = array();
$empty     = "";
$my_uri    = $BROKERS['CLIENTS'][$argv[1]];
$my_sockid = genSockID($my_uri);
$poll      = new ZMQPoll();
$ctxt      = new ZMQContext();
$sock      = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$sock->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $my_sockid);
$sock->bind($my_uri);
$pollids[] = $poll->add($sock, ZMQ::POLL_IN);

error_log("i am $my_sockid");

while(true){
    $events = $poll->poll($readable, $writable, -1);
    $errors = $poll->getLastErrors();

    if ($events > 0) {
        foreach ($readable as $r) {
            if($r === $sock){
                $client_id = $r->recv();
                $empty     = $r->recv();
                $request   = $r->recv();
                error_log('cliend id is '. $client_id);
                error_log('request   is '. $request);
                //sleep(3);
                $r->send($client_id, ZMQ::MODE_SNDMORE);
                $r->send('', ZMQ::MODE_SNDMORE);
                $r->send("$my_sockid got message");
            }
        }
    }
}

