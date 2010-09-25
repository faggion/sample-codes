<?php
$mem = new Memcache;
//$mem->connect('localhost', 11211);
$mem->connect('192.168.1.233', 11211);
$mem->set('foo', '111あああ', MEMCACHE_COMPRESSED, 50);
var_dump($mem->get('foo'));