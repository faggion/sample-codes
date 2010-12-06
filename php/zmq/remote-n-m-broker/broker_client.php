<?php
$poll = new ZMQPoll();
$ctxt = new ZMQContext();

$fs  = "ipc:///tmp/zmq_clients.sock";
$bs  = "tcp://127.0.0.1:5555";

$fe  = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$fe->bind($fs);

// remote broker serverに接続
$be = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$be->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $id);
$be->connect($bs);
$be->send("READY");

$readable  = array();
$writable  = array();

while (true) {
    try {
        $beid   = $poll->add($be, ZMQ::POLL_IN);
        $feid   = $poll->add($fe, ZMQ::POLL_IN);

        // イベントが発生するまで待機
        $events = $poll->poll($readable, $writable, -1);

        $errors = $poll->getLastErrors();
    } catch (ZMQPollException $e) {
        echo "poll failed: " . $e->getMessage() . "\n";
        exit();
    }

    if ($events > 0) {
        foreach ($readable as $r) {
            //var_dump($r->getEndpoints());
            // point1
            $ep = $r->getEndpoints();

            // point1
            // be(worker)側でイベント発生
            //if($ep["bind"][0] === $bs){
            if($r === $be){
                try {
                    $worker_addr = $be->recv();
                    $empty       = $be->recv();
                    $cli_addr    = $be->recv();

                    error_log("WORKER:".implode(",", array($worker_addr, $empty, $cli_addr)));

                    // 新規workerプロセスが追加された
                    if($cli_addr === "READY"){
                        // 追加されただけなので何も処理しない
                    }
                    // worker側で処理が完了したので値を返却
                    else {
                        $empty = $be->recv();
                        $reply = $be->recv();
                        $fe->send($cli_addr, ZMQ::MODE_SNDMORE);
                        $fe->send("", ZMQ::MODE_SNDMORE);
                        $fe->send($reply);
                    }

                    // workerプロセスの処理が完了しているので、
                    // 処理可能なworker process queueに入れる
                    array_push($worker_queue, $worker_addr);

                } catch (ZMQException $e) {
                    echo "recv failed: " . $e->getMessage() . "\n";
                }
            }
            // fe(client)側でイベント発生
            //if($ep["bind"][0] === $fs){
            if($r === $fe){
                try {
                    // client側からのメッセージを受け取る
                    $cli_addr = $fe->recv();
                    $empty    = $fe->recv();
                    $req      = $fe->recv();

                    error_log("CLIENT:".implode(",", array($cli_addr, $empty, $req, $worker_queue[0])));

                    // point2
                    // worker側に値を投げる
                    $be->send($worker_queue[0], ZMQ::MODE_SNDMORE);
                    $be->send("", ZMQ::MODE_SNDMORE);
                    $be->send($cli_addr, ZMQ::MODE_SNDMORE);
                    $be->send("", ZMQ::MODE_SNDMORE);
                    $be->send($req);

                    // workerからレスポンスが返ってくるまでqueueから除いておく
                    array_shift($worker_queue);

                } catch (ZMQException $e) {
                    echo "send failed: " . $e->getMessage() . "\n";
                }
            }
        }
    }
}
