<?php

$now_dates  = array(
    '2011/11/08 00:00:20', // 2
    '2011/11/08 18:00:20', // 2
    '2011/11/09 12:00:20', // 1
    '2011/11/09 22:00:20', // 1
    '2011/11/10 00:00:20', // 0
    '2011/11/10 18:00:20', // 開催中
    '2011/11/11 18:00:20', // 開催中
    '2011/11/11 22:00:20', // 終了
    );
$start_date = '2011/11/10 17:00';
$end_date   = '2011/11/11 21:00';
$zero_date  = substr($start_date,0,10);

$start_time = strtotime($start_date);
$zero_time  = strtotime($zero_date);
$end_time   = strtotime($end_date);

error_log("start => $start_date, end => $end_date ");

$message = "";
foreach($now_dates as $now){
    $time = strtotime($now);

    if($end_time < $time){
        $message = "終了しています";
    }
    else if($start_time < $time && $time <= $end_time){
        $message = "開催中です";
    }
    else {
        if($zero_time <= $time){
            $message = "残り0日";
        }
        else {
            $last = 1 + (int)(($zero_time - $time)/(60*60*24));
            //error_log($zero_time. ":". $time . ":". $last);
            $message = "残り".$last."日";
        }
    }
    error_log($now . ":". $message);
}