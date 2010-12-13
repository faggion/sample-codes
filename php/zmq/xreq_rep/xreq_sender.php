<?php
$pid    = getmypid();
$rep  = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REP);
$xreq = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_XREQ);
$xreq->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $pid);
$xreq->bind("tcp://127.0.0.1:5555");
$rep->bind("tcp://127.0.0.1:5556");

error_log("i am $pid");
//var_dump($xreq->send("OK"));

while(true){
    $msg = $rep->recv();
    $res = "[$msg]";
    error_log($res);
    //$ret = $xreq->send($res)->recv();
    $xreq->send($pid, ZMQ::MODE_SNDMORE);
    $xreq->send("",   ZMQ::MODE_SNDMORE);
    $xreq->send($res);

    $sid   = $xreq->recv();
    $empty = $xreq->recv();
    $mes   = $xreq->recv();

    //error_log(implode("\t", array($sid, $mes)));
    //$rep->send(implode("\t", array($sid, $mes)));
    error_log("[$mes]");
    $rep->send("[$mes]");
}

