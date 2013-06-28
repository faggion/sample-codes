
.. code-block:: none

  $ sudo aptitude install sun-java6-jdk hbase hadoop-conf-pseudo -y  
  $ sudo -u hdfs hdfs namenode -format
  $ for x in `cd /etc/init.d ; ls hadoop-hdfs-*` ; do sudo service $x start ; done
