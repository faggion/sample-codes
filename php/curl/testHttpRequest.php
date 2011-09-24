<?php
require('./HttpRequest.php');
$http = new HttpRequest();

//$t = array();
//$t[] = mt();
//$http->add("top",  "http://www.yahoo.co.jp/");
//$http->add("top2", "http://yahoo.jp/");
//$http->add("shop", "http://shopping.yahoo.co.jp/");
//$t[] = mt();
////error_log("add       :". ($t[count($t)-1] - $t[count($t)-2]));
//$http->execute();
//$t[] = mt();
////error_log("exec      :". ($t[count($t)-1] - $t[count($t)-2]));
//error_log("total     :". ($t[count($t)-1] - $t[0]));
////var_dump($http->info('shop'));

$t = array();
$t[] = mt();
$http->add("top",  "http://www.yahoo.co.jp/");
$http->add("top2", "http://yahoo.jp/");
$http->add("shop", "http://shopping.yahoo.co.jp/");
$t[] = mt();
//error_log("add       :". ($t[count($t)-1] - $t[count($t)-2]));
$http->execute_nowait();
$t[] = mt();
//sleep(5);
//error_log("execnowait:". ($t[count($t)-1] - $t[count($t)-2]));
$http->wait();
$t[] = mt();
//error_log("wait      :". ($t[count($t)-1] - $t[count($t)-2]));
error_log("total     :". ($t[count($t)-1] - $t[0]));
////var_dump($http->info('shop'));
////var_dump($t);

function mt(){
    list($usec, $sec) = explode(" ", microtime());
    return ((float)$usec + (float)$sec);
}


