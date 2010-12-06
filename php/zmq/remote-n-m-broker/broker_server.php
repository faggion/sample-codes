<?php
$id = php_uname("n"). ":". getmypid();
error_log("i am '$id'");

$poll = new ZMQPoll();
$ctxt = new ZMQContext();

$fs  = "tcp://127.0.0.1:5555";
$bs  = "ipc:///tmp/zmq_workers.sock";
//$bs  = "tcp://127.0.0.1:5556";

// NOTICE: 複数remote clientの可能性があるのでXREP
$fe  = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$be  = $ctxt->getSocket(ZMQ::SOCKET_XREP);

$fe->bind($fs);
$be->bind($bs);

// 処理可能なworkerのpid list
$worker_queue      = array();

$readable          = array();
$writable          = array();

while (true) {
    try {
        if(!empty($worker_queue)){
            // IN eventをpollしたい。OUTは不要
            $beid   = $poll->add($be, ZMQ::POLL_IN);
            $feid   = $poll->add($fe, ZMQ::POLL_IN);
            error_log($beid);
            error_log($feid);
        }
        else{
            $beid   = $poll->add($be, ZMQ::POLL_IN);
        }

        // イベントが発生するまで待機
        error_log("WAITING FOR SOCKET EVENT.");
        $events = $poll->poll($readable, $writable, -1);
        error_log("... GOT EVENT !");
        $errors = $poll->getLastErrors();

    } catch (ZMQPollException $e) {
        echo "poll failed: " . $e->getMessage() . "\n";
        exit();
    }

    // イベント処理
    if ($events > 0) {
        foreach ($readable as $r) {

            // backend(worker)側でイベント発生
            //if($ep["bind"][0] === $bs){
            if($r === $be){
                try {
                    $worker_id = $be->recv();
                    $empty     = $be->recv();
                    $packet    = $be->recv();

                    $recv = implode(",", array($worker_id,$packet));

                    // 1. 新規workerプロセスからの接続要求がきた
                    if($packet === "READY"){
                        error_log("NEW WORKER HAS CONNECTED.[$recv]");
                        //// 追加許可メッセージを返しておく
                        //$be->send($worker_id, ZMQ::MODE_SNDMORE);
                        //$be->send("",         ZMQ::MODE_SNDMORE);
                        //$be->send("OK");
                        ////$be->send("OK", ZMQ::MODE_SNDMORE);
                    }
                    // 4. worker側で処理が完了したので値を返却
                    else {
                        error_log("WORKER RESPONSE HAS COME.[$recv]");
                        $broker_client_id = $packet;
                        $empty            = $be->recv();
                        $client_id        = $be->recv();
                        $empty            = $be->recv();
                        $reply            = $be->recv();

                        $fe->send($broker_client_id, ZMQ::MODE_SNDMORE);
                        $fe->send("",                ZMQ::MODE_SNDMORE);
                        $fe->send($client_id,        ZMQ::MODE_SNDMORE);
                        $fe->send("",                ZMQ::MODE_SNDMORE);
                        $fe->send($reply);
                    }

                    // workerプロセスの処理が完了しているので、
                    // 処理可能なworker process queueに入れる
                    array_push($worker_queue, $worker_id);

                } catch (ZMQException $e) {
                    echo "recv failed: " . $e->getMessage() . "\n";
                }
            }
            // fe(remote)側でイベント発生
            //if($ep["bind"][0] === $fs){
            if($r === $fe){
                try {
                    // remote側からのメッセージを受け取る
                    error_log(1);
                    $broker_client_id = $fe->recv();
                    error_log(2);
                    $empty            = $fe->recv();
                    error_log(3);
                    $packet           = $fe->recv();

                    $recv = implode(",", array($broker_client_id,
                                               $packet));

                    // 2. 新規remote broker clientが追加された
                    if($packet === "READY"){
                        error_log("NEW BROKER CLIENT HAS CONNECTED.[$recv]");
                        // remote broker clientが接続されたので
                        // OKを返す
                        $fe->send($broker_client_id, ZMQ::MODE_SNDMORE);
                        $fe->send("",                ZMQ::MODE_SNDMORE);
                        $fe->send("OK");
                        //$fe->send("OK", ZMQ::MODE_SNDMORE);
                    }
                    // 3. remote broker clientからリクエストが来た
                    else {
                        $client_id = $packet;
                        $empty     = $fe->recv();
                        $message   = $fe->recv();
                        error_log("CLIENT REQUEST HAS COME.[$recv][$message]");

                        // worker側に値を投げる
                        $fe->send($broker_client_id, ZMQ::MODE_SNDMORE);
                        $fe->send("",                ZMQ::MODE_SNDMORE);
                        $fe->send($client_id,        ZMQ::MODE_SNDMORE);
                        $fe->send("",                ZMQ::MODE_SNDMORE);
                        $fe->send($message);
                    }
                    // workerからレスポンスが返ってくるまでqueueから除いておく
                    array_shift($worker_queue);

                } catch (ZMQException $e) {
                    echo "send failed: " . $e->getMessage() . "\n";
                }
            }
        }
    }
}
