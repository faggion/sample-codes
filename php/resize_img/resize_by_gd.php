<?php
//$img_url = "http://i.yimg.jp/c/logo/f/2.0/shopping_r_34_2x.png";
//$img_url = 'http://bit.ly/203V3Uy';
$img_url = "http://jp.i.news.gree.net/img/article/88/70/2128870_org_01.jpg";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $img_url);
//curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 1);
$data = curl_exec($ch);
$info = curl_getinfo($ch);
curl_close($ch);

$im = imagecreatefromstring($data);
if ($im !== false) {
    header('Content-Type: ' . $info['content_type']);

    list($width, $height, $type, $attr) = getimagesizefromstring($data);
    $resized   = false;
    if(!empty($_GET['width']) && $_GET['width'] < $width){
        // resize(smallen)
        $resized    = true;
        $new_width  = $_GET['width'];
        $new_height = $height*$new_width/$width;
        $thumb      = imagecreatetruecolor($new_width, $new_height);
        imagecopyresized($thumb, $im, 0, 0, 0, 0, $new_width, $new_height, $width, $height);
        dump_img($thumb, $type);
        imagedestroy($thumb);
    }
    if($resized === false){
        dump_img($im, $type);
    }
    imagedestroy($im);
}

function dump_img($i, $t){
    if($t === IMAGETYPE_PNG){
        imagepng($i);
    }
    elseif($t === IMAGETYPE_JPEG){
        imagejpeg($i);
    }
    elseif($t === IMAGETYPE_GIF){
        imagegif($i);
    }
}

