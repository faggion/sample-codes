<?php

$b = array(true, false, array(), 23.5, '23.5', '', 0, '0', 'abc', array('a') );

foreach($b as $a){
    error_log('result: '. (is_scalar($a) && !is_bool($a)));
}
