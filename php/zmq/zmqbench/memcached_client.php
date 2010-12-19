<?php

// need 'sudo aptitude install php5-memcache'
$m = new Memcache();
$m->connect('localhost', 11211);
//        key    value, flg, expire(sec)
//$m->set('foo', 'bar', 0, 0);
error_log($m->get('foo')); // loop
$m->close();