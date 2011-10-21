<?php

$url  = "http://localhost:10080/test";
//$data = '{"foo":"bar","baz":"車"}';
$data = 'foo=bar&baz=%E8%BB%8A';

//$headers[] = "Content-type: application/json: charset=UTF-8";
$headers[] = "Content-type: application/x-www-form-urlencoded";

$conn = curl_init();
curl_setopt($conn, CURLOPT_URL, $url);
curl_setopt($conn, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($conn, CURLOPT_POST, True);
curl_setopt($conn, CURLOPT_POSTFIELDS, $data);

$ret = curl_exec($conn);
if(!$ret){
    error_log("failed");
}
else{
    error_log("success");
    var_dump($ret);
}

