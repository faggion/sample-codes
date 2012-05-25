
Mac で build する手順

::
  
  % cd /tmp
  % wget http://fallabs.com/kyotocabinet/pkg/kyotocabinet-1.2.76.tar.gz
  % tar xvzf kyotocabinet-1.2.76.tar.gz
  % cd kyotocabinet-1.2.76/
  % ./configure
  % make
  % sudo make install
  % cd ../
  % wget http://fallabs.com/kyotocabinet/javapkg/kyotocabinet-java-1.24.tar.gz
  % tar xvzf kyotocabinet-java-1.24.tar.gz
  % cd ../kyotocabinet-java-1.24/
  % export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK/Home
  % CPPFLAGS="-I /System/Library/Frameworks/JavaVM.framework/Versions/Current/Headers" ./configure
  % INCLUDEDIR=/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers/ make
  % sudo make install

