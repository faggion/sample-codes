<?php

class HttpRequest
{
    protected $queue;
    protected $results;

    private $curlmulti = null;
    private $chlist    = array();

    public function __construct()
    {
        $this->queue   = array();
        $this->results = array();
    }

    public function add($id, $url, $opts=array())
    {
        if(empty($id) || empty($url)) return false;
        $this->results = array();
        $this->queue[] = array('id'   => $id,
                               'url'  => $url,
                               'opts' => $opts);
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
        $i=1;
        do { 
            $n=curl_multi_exec($curlmulti, $active);
            $i++;
        } while ($active);
        error_log($i);

        foreach($this->queue as $q){
            $id = $q['id'];
            $this->results[$id]['data']   = curl_multi_getcontent($chlist[$id]);
            $this->results[$id]['info']   = curl_getinfo($chlist[$id]);
            curl_close($chlist[$id]);
        }
        curl_multi_close($curlmulti);
        $this->queue = array();
    }

    public function execute_nowait()
    {
        if(count($this->queue) === 0) {
            return true;
        }
        if($this->curlmulti !== null){
            // running another curlmulti
            return false;
        }
        $this->results = array();
        $this->curlmulti = curl_multi_init();
        $this->chlist = array();
        foreach($this->queue as $q){
            $curl = curl_init();
            curl_setopt ($curl, CURLOPT_URL, $q['url']);
            curl_setopt ($curl, CURLOPT_RETURNTRANSFER, 1);
            curl_multi_add_handle($this->curlmulti, $curl);
            $this->chlist[$q['id']] = $curl;
        }
        $n = curl_multi_exec($this->curlmulti, $active);
        return true;
    }
    public function wait(){
        if($this->curlmulti === null){
            // not running curl multi
            return false;
        }

        $i=1;
        do { 
            $n=curl_multi_exec($this->curlmulti, $active);
            usleep(300);
            $i++;
        } while ($active);
        error_log($i);
        //do {
        //    $n = curl_multi_exec($this->curlmulti, $active);
        //} while ($active);

        foreach($this->queue as $q){
            $id = $q['id'];
            $this->results[$id]['data']=curl_multi_getcontent($this->chlist[$id]);
            $this->results[$id]['info']=curl_getinfo($this->chlist[$id]);
            //$this->results[$id]['status'] = $q['execinfo']['http_code'];
            //curl_multi_remove_handle($this->curlmulti, $this->chlist[$id]);
            curl_close($this->chlist[$id]);
        }
        curl_multi_close($this->curlmulti);
        $this->curlmulti = null;
        $this->queue     = array();
        $this->chlist    = array();
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