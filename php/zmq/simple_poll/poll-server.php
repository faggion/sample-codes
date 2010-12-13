<?php
$poll = new ZMQPoll();
$ctxt = new ZMQContext();

$fs  = "tcp://127.0.0.1:5555";
$fe  = $ctxt->getSocket(ZMQ::SOCKET_REP);
$fe->bind($fs);

$readable = array();
$writable = array();

while (true) {
    try {
        error_log("add socket");
        $feid   = $poll->add($fe, ZMQ::POLL_IN | ZMQ::POLL_OUT);
        // イベントが発生するまで待機
        error_log("poll socket");
        $events = $poll->poll($readable, $writable, -1);
        error_log("poll socket finished");
        $errors = $poll->getLastErrors();
    } catch (ZMQPollException $e) {
        echo "poll failed: " . $e->getMessage() . "\n";
        exit();
    }

    if ($events > 0) {
        foreach ($readable as $r) {
            error_log("readable socket has come.");
            if($r === $fe){
                try {
                    error_log("receiving...");
                    error_log("received message[". $fe->recv(). "]");
                } catch (ZMQException $e) {
                    error_log("rcv failed:". $e->getMessage());
                }
            }
        }
        foreach ($writable as $w) {
            error_log("writable socket has come.");
            if($w === $fe){
                try {
                    error_log("sending...");
                    $fe->send("OK");
                } catch (ZMQException $e) {
                    error_log("send failed:". $e->getMessage());
                }
            }
        }
    }
}
