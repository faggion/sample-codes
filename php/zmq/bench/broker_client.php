<?php

require_once('common.php');
checkinput($argv);

$readable      = array();
$writable      = array();
$pollids       = array();
$empty         = "";
$poll          = new ZMQPoll();
$ctxt          = new ZMQContext();

// local clientとのsocket
$fe = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$fe_uri = $BROKERS['CLIENTS'][$argv[1]]['fe'];
$fe->setSockOpt(ZMQ::SOCKOPT_IDENTITY, genSockID($fe_uri));
$fe->bind($fe_uri);

// remote broker serverとのsocket
// FIXME: connectなので1つのソケットで連続connectすればいい。foreach
$be        = $ctxt->getSocket(ZMQ::SOCKET_XREQ);
$be_uri    = $BROKERS['SERVERS'][$argv[1]]['fe'];
$be->setSockOpt(ZMQ::SOCKOPT_IDENTITY, genSockID($be_uri));
$be->connect($be_uri);

$pollids[] = $poll->add($fe, ZMQ::POLL_IN);
$pollids[] = $poll->add($be, ZMQ::POLL_IN);

dbg("i have 1 bind socket[$fe_uri], 1 connect socket[$be_uri]:".getmypid());

while(true){
    $events = $poll->poll($readable, $writable, -1);
    $errors = $poll->getLastErrors();

    if ($events > 0) {
        foreach ($readable as $r) {
            if($r === $fe){
                $client_id = $r->recv();
                $empty     = $r->recv();
                $request   = $r->recv();
                dbg('cliend id is '. $client_id);
                dbg('empty is '.     $empty);
                dbg('request   is '. $request);
                //sleep(3);
                //$remote->send($client_id, ZMQ::MODE_SNDMORE);
                //$remote->send('', ZMQ::MODE_SNDMORE);
                $be->send($client_id, ZMQ::MODE_SNDMORE);
                $be->send('',         ZMQ::MODE_SNDMORE);
                $be->send($request);
            }
            if($r === $be){
                //$bs_id     = $r->recv();
                //dbg('bs id is '. $bs_id);
                $empty     = $r->recv();
                dbg("empt = $empty");
                $client_id = $r->recv();
                dbg('cl id is '. $client_id);
                $empty     = $r->recv();
                dbg("empt = $empty");
                $response  = $r->recv();
                dbg('response   is '. $response);
                //sleep(3);
                $fe->send($client_id, ZMQ::MODE_SNDMORE);
                $fe->send('',         ZMQ::MODE_SNDMORE);
                $fe->send($response);
            }
        }
    }
}

