<?php
if(!isset($argv[2])){
    error_log("invalid argv");
    exit(1);
}

require_once('common.php');
checkinput($argv);

$broker_client_uri = $BROKERS['CLIENTS'][$argv[1]]['fe'];
$my_sockid         = genSockID($broker_client_uri);
$ctxt              = new ZMQContext();
$sock              = $ctxt->getSocket(ZMQ::SOCKET_REQ);
$sock->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $my_sockid);
$sock->connect($broker_client_uri);

dbg("i am $my_sockid");
for($i=0;$i<$argv[2];$i++){
    dbg($sock->send("hoge")->recv());
}
