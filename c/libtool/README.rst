=================
on Ubuntu
=================

build 
-----------------

::
  
  % libtool --mode=link gcc -o libone.la -c one.c -rpath `pwd`

clean
-----------------

::
  
  % libtool --mode=clean rm libone.la

=================
on Mac
=================

オプションが違うらしい

あとで調べる
