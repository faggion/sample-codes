
使い方
----------------

1. server起動。第1引数がサーバ名
2. client起動。第1引数が送信先サーバ名

::
  
  % php client.php foo
  send to foo
  my pid id 11854
  
  % php server.php foo
  my addr is foo
  my pid id 11849
  [11854][][hello from 11854]
  [11854][][hello from 11854]
  [11854][][hello from 11854]
  [11854][][hello from 11854]
  [11854][][hello from 11854]
  [11854][][hello from 11854]
  ^C

