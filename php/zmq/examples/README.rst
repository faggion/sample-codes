
ex1
------------

::
  
  % php ex1_xreq_bind_client.php
  % php ex1_xrep_connect_server.php foo
  % php ex1_xrep_connect_server.php bar

- 一度つないだbar socketを切断すると、
  client側でbarに対するリクエストがQueuingされてしまう

ex2
------------

- PUSH/PULLでもex1と同様の現象が起きるか確認

::
  
  % php ex2_push_bind_client.php
  % php ex2_pull_connect_server.php bar
  % php ex2_pull_connect_server.php baz

- 一度つないだbar socketを切断すると、
  client側でbarに対するリクエストがQueuingされてしまう
  -> PUSH/PULLでも同様の動き

失敗コード
------------

1. req client / xrep server
   -> req なので、sendしっぱなしができない。
2. xrep connect client / xrep bind server
   -> serverが複数になったときに、client側で送信先を指定するのが煩雑 + fail overに問題


