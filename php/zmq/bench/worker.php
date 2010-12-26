<?php
require_once('common.php');
checkinput($argv);

$ctxt   = new ZMQContext();
$fe_uri = $BROKERS['SERVERS'][$argv[1]]['be'];
//$fe     = $ctxt->getSocket(ZMQ::SOCKET_XREQ);
//$fe     = $ctxt->getSocket(ZMQ::SOCKET_REQ);
$fe     = $ctxt->getSocket(ZMQ::SOCKET_REP);
$fe_id  = genSockID($fe_uri);
$fe->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $fe_id);
$fe->connect($fe_uri);

$m = new Memcache();

dbg("i am worker[$fe_id].");
//$fe->send('READY');

$m->connect('localhost', 11211);
while(true){
    dbg('wait recv...');
    $bc_id     = $fe->recv();
    dbg("bcid =$bc_id");
    $empty     = $fe->recv();
    dbg("empty=$empty");
    $client_id = $fe->recv();
    dbg("clid =$client_id");
    $empty     = $fe->recv();
    dbg("empty=$empty");
    $request   = $fe->recv();
    dbg("req  =$request");
    //list($key, $val) = explode('=', $request);
    //$m->set($key, $val, 0, 0);
    $m->set($request, '1234567890', 0, 0);
    $fe->send($bc_id,     ZMQ::MODE_SNDMORE);
    $fe->send("",         ZMQ::MODE_SNDMORE);
    $fe->send($client_id, ZMQ::MODE_SNDMORE);
    $fe->send("",         ZMQ::MODE_SNDMORE);
    $fe->send($m->get($request));
}
$m->close();
