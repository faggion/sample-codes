<?php

// my name
if(empty($argv[1])){
    error_log("empty my name");
    exit(1);
}

$myname  = $argv[1];
$conf    = parse_ini_file("servers.ini");
$poll    = new ZMQPoll();
$ctxt    = new ZMQContext();

// remote tcp 
$all_bs       = array(); // 全server list
$available_bs = array(); // 処理可能なserver list
foreach($conf["servers"] as $c){
    //error_log($c);
    $sock = $ctxt->getSocket(ZMQ::SOCKET_XREP);
    $sock->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $c);
    $sock->connect($c);
    $server = array("name"=>$c, "sock"=>$sock);
    array_push($all_bs,       $server);
    array_push($available_bs, $server);
}

if(empty($all_bs) || empty($available_bs)){
    error_log("empty all_bs or available_bs");
    exit(1);
}

// local tcp
$local = $ctxt->getSocket(ZMQ::SOCKET_XREP);
$local->setSockOpt(ZMQ::SOCKOPT_IDENTITY, $myname);
$local->bind($myname);

$readable = array();
$writable = array();

while (true) {
    $ids = array();

    try {
        $id[] = $poll->add($local, ZMQ::POLL_IN);
        foreach($all_bs as $bs){
            $id[] = $poll->add($bs["sock"], ZMQ::POLL_IN);
        }

        // イベントが発生するまで待機
        error_log("waiting for socket event...");
        $events = $poll->poll($readable, $writable, -1);
        error_log("got event !");
        $errors = $poll->getLastErrors();

    } catch (ZMQPollException $e) {
        echo "poll failed: " . $e->getMessage() . "\n";
        exit();
    }

    // イベント処理
    if ($events > 0) {
        foreach ($readable as $r) {

            // localからリクエストが到着
            if($r === $local){
                try {

                    $clientid = $r->recv();
                    $empty    = $r->recv();
                    $request  = $r->recv();

                    // $available_serversが空だったらエラーを返す
                    if(0){
                        // 未実装
                    }

                    $bs = array_shift($available_bs);
                    $bs["sock"]->send($bs["name"],ZMQ::MODE_SNDMORE); // どこに
                    $bs["sock"]->send("",         ZMQ::MODE_SNDMORE);
                    $bs["sock"]->send($clientid,  ZMQ::MODE_SNDMORE); // どこから
                    $bs["sock"]->send("",         ZMQ::MODE_SNDMORE);
                    $bs["sock"]->send($request);

                } catch (ZMQException $e) {
                    error_log("failed request: " . $e->getMessage());
                }
            }
            // serverからのレスポンスが到着
            else {
                foreach($all_bs as $bs){
                    if($r === $bs["sock"]){
                        //
                        try {

                            $from_bs     = $bs["sock"]->recv();
                            $empty       = $bs["sock"]->recv();
                            $from_client = $bs["sock"]->recv();
                            $empty       = $bs["sock"]->recv();
                            $response    = $bs["sock"]->recv();

                            $local->send($from_client, ZMQ::MODE_SNDMORE);
                            $local->send("",           ZMQ::MODE_SNDMORE);
                            $local->send($response);

                            array_push($available_bs, $bs);

                        } catch (ZMQException $e) {
                            error_log("failed response: " . $e->getMessage());
                        }
                    }
                }
            }
        }
    }
}
