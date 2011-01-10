
実行方法
---------------------

::
  
  java \
  -classpath build/classes/:/usr/share/java/commons-logging.jar \
  -Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.SimpleLog \
  -Dorg.apache.commons.logging.simplelog.defaultlog=error \
  com.tanarky.sample.TestLog

- document
  http://commons.apache.org/logging/guide.html
  http://commons.apache.org/logging/guide.html#Creating%20a%20Log%20Implementation
