<?php

if(!isset($argv[1])){
    error_log("invalid argv");
    exit(1);
}

require_once('common.php');

$readable      = array();
$writable      = array();
$pollids       = array();
$empty         = "";
$my_uri        = $BROKERS['CLIENTS'][$argv[1]];
$my_sockid     = genSockID($my_uri);
$poll          = new ZMQPoll();
$ctxt          = new ZMQContext();

// local clientとのsocket
$sock = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$sock->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $my_sockid);
$sock->bind($my_uri);

// remote broker serverとのsocket
// FIXME: connectなので1つのソケットで連続connectすればいい。foreachする
$remote        = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$remote_uri    = $BROKERS['SERVERS'][$argv[1]];
$remote_sockid = genSockID($my_uri);
$remote->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $remote_sockid);
$remote->connect($remote_uri);

$pollids[] = $poll->add($sock,   ZMQ::POLL_IN);
$pollids[] = $poll->add($remote, ZMQ::POLL_IN);

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
                $remote->send($client_id, ZMQ::MODE_SNDMORE);
                $remote->send('', ZMQ::MODE_SNDMORE);
                $remote->send("$my_sockid got message");
            }
            if($r === $remote){
                $client_id = $r->recv();
                $empty     = $r->recv();
                $request   = $r->recv();
                error_log('cliend id is '. $client_id);
                error_log('request   is '. $request);
                //sleep(3);
                $sock->send($client_id, ZMQ::MODE_SNDMORE);
                $sock->send('', ZMQ::MODE_SNDMORE);
                $sock->send("$my_sockid got message");
            }
        }
    }
}

