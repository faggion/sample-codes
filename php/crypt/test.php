<?php

$p1 = "12345678";
$p2 = "1234567890";
$p3 = "1234567890abcdefghijklmnopqrstuvwxyz";

error_log(crypt($p1));
error_log(crypt($p2));
error_log(crypt($p3));