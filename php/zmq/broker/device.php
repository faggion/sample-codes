<?php

$ctxt  = new ZMQContext();

$xrep = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$xrep->bind("tcp://127.0.0.1:5555");

$xreq = $ctxt->getSocket(ZMQ::SOCKET_XREQ);
$xreq->bind("tcp://127.0.0.1:5556");

$dev  = new ZMQDevice(ZMQ::DEVICE_QUEUE, $xreq, $xrep);

exit();
