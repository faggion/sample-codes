
起動方法
-----------------

::
  
  % cat servers.ini 
  
  servers[] = "tcp://127.0.0.1:5565"
  servers[] = "tcp://127.0.0.1:5566"
  
  % php broker_server.php 'tcp://127.0.0.1:5565'
  % php broker_server.php 'tcp://127.0.0.1:5566'
  % php broker_client.php 'tcp://127.0.0.1:5555'
  % php client.php

- 注意

  - php broker_client.php 'tcp://127.0.0.1:5556'
    などを追加するとbroder_serverが落ちる



