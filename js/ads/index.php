<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
 "http://www.w3.org/TR/html4/strict.dtd"> 
<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link href="bootstrap.css" rel="stylesheet">
<link href="style.css" rel="stylesheet">
<title>サンプルページ</title>
<body>
<div class="container">

<div class="row">
  <div class="span12">
    <div class="logo"><img src="logo_shopping.gif"></div>
  </div>
</div>

<div class="row">
  <div class="span4">
    <div class="adlantis adlantis_pos_side">
      <iframe src="ad.php"
              width="300"
              height="100"
              frameborder="0"
              scrolling="no">
      </iframe>
    </div>
    <div class="adlantis adlantis_pos_llec">
      <iframe src="ad.php"
              marginheight="0"
              marginwidth="0"
              width="300"
              height="250"
              frameborder="0"
              scrolling="no"></iframe>
    </div>
    <?php include('module.php'); ?>
    <div class="adlantis adlantis_pos_side"></div>
    <div class="adlantis adlantis_pos_side"></div>
  </div>
  <div class="span8">
    <?php include('module.php'); ?>
    <?php include('module.php'); ?>
    <?php include('module.php'); ?>
  </div>
</div>

<div class="row">
  <div class="span12">
    <hr>
    <p style="text-align:center">copyright tanarky</p>
  </div>
</div>

</div>
<script type="text/javascript" src="get_ads.js"></script>
</body>
</html>
