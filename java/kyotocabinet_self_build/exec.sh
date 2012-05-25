#!/bin/sh

javac -cp /usr/local/lib/kyotocabinet.jar TestKc.java && java -Djava.library.path=/usr/local/lib -cp /usr/local/lib/kyotocabinet.jar:. TestKc 


