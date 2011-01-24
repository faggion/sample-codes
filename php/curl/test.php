<?php
if(!empty($_GET['q']) || !empty($_GET['type']) || !empty($_GET['domain'])){
    require_once('./SimpleCurl.php');
    $req = array();
    if(!empty($_GET['q'])){
        $req[] = $_GET['q'];
    }
    if(!empty($_GET['type'])){
        $req[] = 'type:'.$_GET['type'];
    }
    if(!empty($_GET['domain'])){
        $req[] = 'domain:'.$_GET['domain'];
    }
    $curl = new SimpleCurl();
    $url  = 'http://localhost:8080/solr/select/?q='. rawurlencode(implode(" ", $req));
    error_log($url);
    $xml  = simplexml_load_string($curl->get($url), 'SimpleXMLElement', LIBXML_NOCDATA | LIBXML_NOBLANKS);
    //var_dump($xml);
}
?><!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Search Test Page</title>
  <link rel="stylesheet" href="http://yui.yahooapis.com/2.8.0r4/build/reset-fonts-grids/reset-fonts-grids.css" type="text/css">
  <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
<div id="doc2" class="yui-t6">
  <div id="hd"><h1>Search Test Page</h1></div>
  <div id="bd">
    <div id="yui-main">
      <div class="yui-b"><div class="yui-g">
          <!-- YOUR DATA GOES HERE -->
<?php
    if($xml){
        foreach($xml->result->doc as $d){
            foreach($d->str as $s){
                // http://pics.dmm.co.jp/digital/video/btwd00011/btwd00011ps.jpg
                $attr = (string)$s->attributes()->name;
                if($attr === 'id'){
                    $ids = explode("-", (string)$s);
                    //http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=oned939/
                    $link = 'http://www.dmm.co.jp/digital/videoa/-/detail/=/cid='.$ids[2].'/';
                    echo '<p><a target="_blank" href="'.$link.'">'.(string)$s.'</a></p>';
                    //$imgurl = 'http://pics.dmm.co.jp/digital/video/'.$ids[2].'/'.$ids[2].'ps.jpg';
                    //echo '<img src="'. $imgurl. '">';
                }
                else {
                    echo '<p>'. (string)$s. '</p>';
                }
            }
            echo "<hr>";
        }
    }
?>
        </div>
      </div>
    </div>
    <div class="yui-b">
      <h2>Search Parameters</h2>
      <form method="GET" action="./test.php">
        <p>query</p>
        <p><input type="text" name="q" size="30" value="<?php echo $_GET['q']; ?>"></p>
        <p>type</p>
        <p>
          <select name="type">
            <option value="0"<?php if(!empty($_GET['type']) && $_GET['type'] == 0) echo " selected"; ?>>指定無し</option>
            <option value="1"<?php if(!empty($_GET['type']) && $_GET['type'] == 1) echo " selected"; ?>>動画</option>
            <option value="2"<?php if(!empty($_GET['type']) && $_GET['type'] == 2) echo " selected"; ?>>人</option>
          </select>
        </p>
        <p>domain</p>
        <p>
          <select name="domain">
            <option value="0"<?php if(!empty($_GET['domain']) && $_GET['domain'] == 0) echo " selected"; ?>>指定無し</option>
            <option value="1"<?php if(!empty($_GET['domain']) && $_GET['domain'] == 1) echo " selected"; ?>>dmm</option>
          </select>
        </p>
        <p><input type="submit" value="検索"></p>
      </form>
    </div>
  </div>
  <div id="ft"><p>tanarky all rights reserved.</p></div>
</div>
</body>
</html>
