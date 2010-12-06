<?php
$id = php_uname("n"). ":". getmypid();
error_log("i am '$id'");

$server = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$server->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $id);
$server->connect("tcp://127.0.0.1:5555");
//$server->connect("ipc:///tmp/zmq_workers.sock");

// 接続要求テスト
//$server->send("READY", ZMQ::MODE_SNDMORE);
$server->send("READY");

//error_log($server->recv()); // expects broker_server_id
//error_log($server->recv()); // expects empty
//error_log($server->recv()); // expects OK

error_log($server->recv()); // expects broker_server_id

// データ送信テスト
$message = "hello";
$server->send("client_host:123", ZMQ::MODE_SNDMORE); // dummy client id
$server->send("",                ZMQ::MODE_SNDMORE);
$server->send($message);

//error_log($server->recv()); // expects broker server id
//error_log($server->recv()); // expects empty
error_log($server->recv()); // expects broker client id
error_log($server->recv()); // expects empty
error_log($server->recv()); // expects client id
error_log($server->recv()); // expects empty
error_log($server->recv()); // expects some message




