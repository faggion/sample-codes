<?php
require_once('common.php');

$poll = new ZMQPoll();
$ctxt = new ZMQContext();

$fs  = "tcp://127.0.0.1:5555";
$fe  = $ctxt->getSocket(ZMQ::SOCKET_PAIR);
$fe->bind($fs);

$readable = array();
$writable = array();

while (true) {
    try {
        $feid   = $poll->add($fe, ZMQ::POLL_IN);
        L("polling...");
        $events = $poll->poll($readable, $writable, -1);
        $errors = $poll->getLastErrors();
    } catch (ZMQPollException $e) {
        echo "poll failed: " . $e->getMessage() . "\n";
        exit();
    }

    if ($events > 0) {
        foreach ($readable as $r) {
            L("broker_client is sending message...");
            if($r === $fe){
                try {
                    L("receiving...");
                    $rcv = $fe->recv();
                    L("received message[". $rcv. "]");
                    // sleep(3);
                    $fe->send($rcv);
                } catch (ZMQException $e) {
                    L("rcv failed:". $e->getMessage());
                }
            }
        }
    }
}
