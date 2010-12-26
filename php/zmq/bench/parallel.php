<?php

$pid   = 1;
$count = $argv[1];
$cmd   = isset($argv[2]) ? 1 : 0;
$max   = 10000;
$loop  = $max / $count;

while($pid && $count--){
    $pid = pcntl_fork();
    if($pid == -1) exit('cant fork');
}

$status = null;
if( $pid ){
    error_log('PARENT: waiting...');
    //pcntl_wait($status);
    //pcntl_waitpid(-1, $status, WNOHANG);
    pcntl_waitpid(-1, $status);
}
else{
    error_log("CHILD : loop=$loop, ". getmypid());
    if($cmd){
        exec("php memcached_client.php $loop");
    }
    else {
        exec("php client.php 0 $loop");
    }
}
