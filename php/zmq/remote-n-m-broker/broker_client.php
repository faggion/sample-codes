<?php
//$id = "broker_server:". php_uname("n"). ":". getmypid();
$host = "127.0.0.1";
$id = "broker_client:$host:". getmypid();
error_log("i am '$id'");

$poll = new ZMQPoll();
$ctxt = new ZMQContext();

$fs  = "ipc:///tmp/zmq_clients.sock";
$bs  = "tcp://$host:5556";

$fe  = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$be  = $ctxt->getSocket(ZMQ::SOCKET_XREP);

$fe->bind($fs);
$be->bind($bs);

// 処理可能なworkerのpid list
$workers        = array();
$broker_clients = array();

$readable = array();
$writable = array();

while (true) {
    try {
        if(empty($workers)){
            // broker serverがない場合はFrontendからのPOLL_INを受けない
            $beid   = $poll->add($be, ZMQ::POLL_IN);

            // broker serverに接続
            $server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_PUSH);
            $server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $id);
            $server->connect("tcp://127.0.0.1:5555");

            $server->send("$id",   ZMQ::MODE_SNDMORE);
            $server->send("",      ZMQ::MODE_SNDMORE);
            //$server->send("READY", ZMQ::MODE_NOBLOCK);
            $server->send("READY");
            error_log("connect request");
        }
        else{
            // broker serverがあるのでFrontendとBackend両方のPOLL_INを受ける
            $beid   = $poll->add($be, ZMQ::POLL_IN);
            $feid   = $poll->add($fe, ZMQ::POLL_IN);
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

            // broker server側でイベント発生
            //if($ep["bind"][0] === $bs){
            if($r === $be){
                try {
                    $worker_id = $be->recv();
                    $empty     = $be->recv();
                    $packet    = $be->recv();

                    $recv = implode(",", array($worker_id,$packet));

                    // 1. 新規broker_serverからの接続要求がきた
                    if($packet === "READY"){
                        error_log("New worker connected.");
                        error_log("I have accepted $worker_id.");
                    }
                    // 4. worker側で処理が完了したので値を返却
                    else {
                        $broker_clients[$broker_client_id]->send($packet);
                        error_log("bc res:". $broker_clients[$broker_client_id]->recv());
                    }

                    // workerプロセスの処理が完了しているので、
                    // 処理可能なworker process queueに入れる
                    array_push($workers, $worker_id);

                } catch (ZMQException $e) {
                    echo "recv failed: " . $e->getMessage() . "\n";
                }
            }
            // fe(remote)側でイベント発生
            //if($ep["bind"][0] === $fs){
            if($r === $fe){
                try {
                    $broker_client_id = $fe->recv();
                    $empty            = $fe->recv();
                    $packet           = $fe->recv();

                    // 2. 新規remote broker clientが追加された
                    if($packet === "READY"){
                        //$broker_client_host = $fe->recv();
                        $broker_client_host = "tcp:127.0.0.1:5556";
                        error_log("New broker client has come.");
                        error_log("I have connected $broker_client_id.");

                        $cli = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
                        $cli->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $id);
                        $cli->connect($broker_client_host);

                        $broker_clients[$broker_client_id] = $cli;
                    }
                    // 3. remote broker clientからリクエストが来た
                    else {
                        $be->send($workers[0], ZMQ::MODE_SNDMORE);
                        $be->send("",          ZMQ::MODE_SNDMORE);
                        $be->send($packet);
                        // workerからレスポンスが返ってくるまでqueueから除いておく
                        array_shift($workers);
                    }
                } catch (ZMQException $e) {
                    echo "send failed: " . $e->getMessage() . "\n";
                }
            }
        }
    }
}
