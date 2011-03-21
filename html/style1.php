<?php
header('Content-type: text/css');

function issetor(&$var, $def){
    return isset($var) ? $var : $def;
}

$pos         = issetor($_GET['pos'],   'top');
$width       = issetor($_GET['width'], '-1%');
$head        = issetor($_GET['head'],  10);
$bordercolor = issetor($_GET['bordercolor'],  '000');
$color       = issetor($_GET['color'], 'white');
$leftmargin  = issetor($_GET['leftmargin'], ($pos=='top'||$pos=='bottom')? 10 : 0);
$headmargin  = $head + $leftmargin;

?>
.bubble {
  float:left;
  margin:<?php if($pos=='top'||$pos=='bottom'){echo '0';}else{echo '10px'  ;}?> 0 0 <?php echo $leftmargin;?>px;
  border-<?php if($pos=='top'||$pos=='bottom'){echo 'left';}else{echo 'top';}?>: <?php echo $head;?>px solid #<?php echo $bordercolor;?>;
  border-<?php if($pos=='top'||$pos=='bottom'){echo $pos;  }else{echo $pos ;}?>: <?php echo $head;?>px solid transparent;
  -border-<?php if($pos=='top'||$pos=='bottom'){echo $pos; }else{echo $pos ;}?>-color: <?php echo $color;?>;

    /*
  右
  border-top: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-left: <?php echo $head;?>px solid transparent;
  -border-left-color: <?php echo $color;?>;

  左
  border-top: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-left: <?php echo $head;?>px solid transparent;
  -border-left-color: <?php echo $color;?>;

  下
  border-left: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-bottom: <?php echo $head;?>px solid transparent;
  -border-bottom-color: <?php echo $color;?>;

  上
  border-left: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-top: <?php echo $head;?>px solid transparent;
  -border-top-color: <?php echo $color;?>;

  -----
  border-top: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-left: <?php echo $head;?>px solid transparent;
  -border-left-color: <?php echo $color;?>;

  border-top: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-left: <?php echo $head;?>px solid transparent;
  -border-left-color: <?php echo $color;?>;

  border-left: <?php echo $head;?>px solid <?php echo $bordercolor;?>;
  border-bottom: <?php echo $head;?>px solid transparent;
  -border-bottom-color: <?php echo $color;?>;
    */
}
.bubble .body {
  <?php echo "  width: $width;\n";?>
  background: none repeat scroll 0 0 white;
  color: black;
  border:  2px solid #<?php echo $bordercolor;?>;
  padding: 5px 10px;
<?php
  if($pos=='top'||$pos=='bottom'){
    echo '  margin: 0 0 0 -'. $headmargin. "px;\n";
  }
  else {
    echo '  margin: -'. ($headmargin+10). "px 0 0 0;\n";
  }
?>
  -moz-border-radius: 6px;
  -position: relative; /* for IE6 */
}
.clearfix:after{content: ""; display: block; clear: both;}
td.user{vertical-align:top}
