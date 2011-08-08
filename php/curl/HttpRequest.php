<?php

class HttpRequest
{
    protected $queue;
    protected $results;

    public function __construct()
    {
        $this->queue   = array();
        $this->results = array();
    }

    public function add($id, $url, $cookie=null)
    {
        if(empty($id) || empty($url)) return false;
        $this->results = array();
        $this->queue[] = array('id'    => $id,
                               'url'   => $url,
                               'cookie'=> $cookie);
        return true;
    }

    public function execute()
    {
        if(count($this->queue) === 0) {
            return true;
        }
        $this->results = array();
        $curlmulti = curl_multi_init();
        $chlist = array();
        foreach($this->queue as $q){
            $curl = curl_init();
            curl_setopt ($curl, CURLOPT_URL, $q['url']);
            curl_setopt ($curl, CURLOPT_RETURNTRANSFER, 1);
            curl_multi_add_handle($curlmulti, $curl);
            $chlist[$q['id']] = $curl;
        }
        do { 
            $n=curl_multi_exec($curlmulti, $active);
        } while ($active);

        foreach($this->queue as $q){
            $id = $q['id'];
            $this->results[$id]['data']   = curl_multi_getcontent($chlist[$id]);
            $this->results[$id]['info']   = curl_getinfo($chlist[$id]);
            $this->results[$id]['status'] = $q['execinfo']['http_code'];
            curl_close($chlist[$id]);
        }
        curl_multi_close($curlmulti);
        $this->queue = array();
    }

    public function get($id)
    {
        return isset($this->results[$id]['data']) ? $this->results[$id]['data'] : null;
    }
    public function info($id)
    {
        return isset($this->results[$id]['info']) ? $this->results[$id]['info'] : null;
    }
    public function status($id)
    {
        return isset($this->results[$id]['status']) ? $this->results[$id]['status'] : null;
    }
}