<?php
require_once('common.php');
checkinput($argv);

$readable      = array();
$writable      = array();
$pollids       = array();
$empty         = "";
$fe_uri        = $BROKERS['SERVERS'][$argv[1]]['fe'];
$poll          = new ZMQPoll();
$ctxt          = new ZMQContext();

// remote broker_clientとのsocket(tcp)
$fe = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$fe->setSockOpt(ZMQ::SOCKOPT_IDENTITY, genSockID($fe_uri));
$fe->bind($fe_uri);

// local workerとのsocket(ipc)
$be     = $ctxt->getSocket(ZMQ::SOCKET_XREQ);
$be_uri = $BROKERS['SERVERS'][$argv[1]]['be'];
$be->setSockOpt(ZMQ::SOCKOPT_IDENTITY, genSockID($be_uri));
$be->bind($be_uri);

$pollids[] = $poll->add($be, ZMQ::POLL_IN);
$pollids[] = $poll->add($fe, ZMQ::POLL_IN);

dbg("i have 2 bind sockets[$fe_uri][$be_uri]:". getmypid());

while(true){
    dbg('polling...');
    $events = $poll->poll($readable, $writable, -1);
    $errors = $poll->getLastErrors();

    if ($events > 0) {
        foreach ($readable as $r) {
            if($r === $be){
                $worker_id = $r->recv();
                dbg("woid = $worker_id");
                $empty     = $r->recv();
                dbg("empt = $empty");
                if($empty === 'READY'){
                    dbg('new worker comes.');
                }
                else {
                    $bc_id     = $r->recv();
                    dbg("bcid = $bc_id");
                    $empty     = $r->recv();
                    dbg("empt = $empty");
                    $client_id = $r->recv();
                    dbg("clid = $client_id");
                    $empty     = $r->recv();
                    dbg("empt = $empty");
                    $response  = $r->recv();
                    dbg('res  = '. $response);
                    $fe->send($bc_id,     ZMQ::MODE_SNDMORE);
                    $fe->send('',         ZMQ::MODE_SNDMORE);
                    $fe->send($client_id, ZMQ::MODE_SNDMORE);
                    $fe->send('',         ZMQ::MODE_SNDMORE);
                    $fe->send($response);
                }
            }
            if($r === $fe){
                $bc_id     = $r->recv();
                dbg("bcid = $bc_id");
                $client_id = $r->recv();
                dbg("clid = $client_id");
                $empty     = $r->recv();
                dbg("empt = $empty");
                $request   = $r->recv();
                dbg('req  = '. $request);
                //sleep(3);
                $be->send('anyworker',ZMQ::MODE_SNDMORE);
                $be->send('',         ZMQ::MODE_SNDMORE);
                $be->send($bc_id,     ZMQ::MODE_SNDMORE);
                $be->send('',         ZMQ::MODE_SNDMORE);
                $be->send($client_id, ZMQ::MODE_SNDMORE);
                $be->send('',         ZMQ::MODE_SNDMORE);
                $be->send($request);
            }
        }
    }
}

