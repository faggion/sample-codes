<?php

class SimpleCurl {
    private $ch = null;

    public function __construct(){
        $this->ch = curl_init();
    }

    public function __descruct(){
        curl_close($this->ch);
    }

    public function get($url){
        curl_setopt($this->ch, CURLOPT_URL, $url);
        curl_setopt($this->ch, CURLOPT_HEADER, 0);
        curl_setopt($this->ch, CURLOPT_RETURNTRANSFER, 1);
        return curl_exec($this->ch);
    }
}