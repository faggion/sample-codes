<?php

if(!isset($argv[1])){
    error_log("invalid argv");
    exit(1);
}

require_once('common.php');

$broker_client_uri = $BROKERS['CLIENTS'][$argv[1]];
$my_sockid         = genSockID($broker_client_uri);
$ctxt              = new ZMQContext();
$sock              = $ctxt->getSocket(ZMQ::SOCKET_REQ);
$sock->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $my_sockid);
$sock->connect($broker_client_uri);

error_log("i am $my_sockid");
error_log($sock->send("connected from $my_sockid")->recv());
