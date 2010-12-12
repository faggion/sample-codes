<?php
$id = "worker:". php_uname("n"). ":". getmypid();
error_log("i am '$id'");

$worker = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$worker->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $id);
$worker->connect("ipc:///tmp/zmq_workers.sock");

// broker_serverに接続要求
$worker->send("READY");

// clientからの要求に対する処理をするループ
while (true){
    error_log(1);
    $broker_server_id  = $worker->recv();
    error_log($broker_server_id);
    $empty             = $worker->recv();
    error_log($empty);
    $broker_client_id  = $worker->recv();
    error_log($broker_client_id);
    $empty             = $worker->recv();
    error_log($empty);
    $client_id         = $worker->recv();
    error_log($client_id);
    $empty             = $worker->recv();
    $message           = $worker->recv();

    error_log("WORKER:". implode(",", array($broker_server_id,
                                            $broker_client_id,
                                            $client_id,
                                            $message)));

    $worker->send($broker_server_id, ZMQ::MODE_SNDMORE);
    $worker->send("",    ZMQ::MODE_SNDMORE);
    $worker->send($broker_client_id, ZMQ::MODE_SNDMORE);
    $worker->send("",    ZMQ::MODE_SNDMORE);
    $worker->send($client_id, ZMQ::MODE_SNDMORE);
    $worker->send("",    ZMQ::MODE_SNDMORE);
    $worker->send("i am server($pid). message is ($message)");
}
