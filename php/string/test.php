<?php

$str = '{"hogehoge":"foobar"}';

error_log($str);

if(isset($str["test"])){
    error_log("true");
}

$str2 = trim($str, "}");
error_log($str2);

$str3 = trim($str, "]");
error_log($str3);

$str  = null;
$str3 = trim($str, "]");
error_log($str3);

