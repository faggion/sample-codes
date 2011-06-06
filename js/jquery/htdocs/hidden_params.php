<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>隠しパラメータ</title>
  <link rel="stylesheet" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" type="text/css">
  <script type="text/javascript"src="http://www.google.com/jsapi"></script>
  <script type="text/javascript">google.load("jquery", "1.6");</script>
</head>
  <body>
    <div id="doc2" class="yui-t6">
      <div id="hd">
        <br>
      </div>
      <div id="bd">
        <div id="yui-main">
          <div class="yui-b">
            <div class="yui-g">

<div id="fixed" style="display:none">disney</div>
<form name="test" action="" method="GET" onsubmit="doSubmit();">
<input type="text" name="p" value="foo"><br>
<input type="submit">
</form>
<script>
function doSubmit(){
  // innerTextはIEだけ
  document.test.p.value += ' ' + document.getElementById('fixed').innerHTML;
}
</script>

            </div>
          </div>
        </div>
        <div class="yui-b">
        </div>
      </div>
      <div id="ft"><p style="text-align:center;margin-top:10px">Copyright (C) 2009 tanarky All Rights Reserved.</p>
      </div>
    </div>
  </body>
</html>
