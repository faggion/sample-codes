
env setup
------------------------------------

on debian 6

::
  
  % aptitude install liblua5.1-0-dev

lib install
------------------------------------

::
  
  % cd lib
  % make install


test
------------------------------------

::
  
  % cd test
  % make
  % % cat test.lua
  print("hello")
  return 0
  % valgrind ./main compile test.lua > /tmp/bin
  ==12013== Memcheck, a memory error detector
  ==12013== Copyright (C) 2002-2010, and GNU GPL'd, by Julian Seward et al.
  ==12013== Using Valgrind-3.6.0.SVN-Debian and LibVEX; rerun with -h for copyright info
  ==12013== Command: ./main compile test.lua
  ==12013==
  test.lua
  ==12013==
  ==12013== HEAP SUMMARY:
  ==12013==     in use at exit: 0 bytes in 0 blocks
  ==12013==   total heap usage: 437 allocs, 437 frees, 43,609 bytes allocated
  ==12013==
  ==12013== All heap blocks were freed -- no leaks are possible
  ==12013==
  ==12013== For counts of detected and suppressed errors, rerun with: -v
  ==12013== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 4 from 4)
  % cat /tmp/bin | perl -MMIME::Base64 -e 'print encode_base64(<>)'
  G0x1YVEAAQQIBAgADAAAAAAAAABzYW1wbGVfbmFtZQAAAAAAAAAAAAAAAgIGAAAABQAAAEFAAAAc
  QAABAYAAAB4AAAEeAIAAAwAAAAQGAAAAAAAAAHByaW50AAQGAAAAAAAAAGhlbGxvAAMAAAAAAAAA
  AAAAAAAGAAAAAQAAAAEAAAABAAAAAgAAAAIAAAACAAAAAAAAAAAAAAA=
  % ls -l /tmp/bin
  -rw-r--r-- 1 satoshi-tanaka satoshi-tanaka 155 Oct 10 08:56 /tmp/bin
  % lua /tmp/bin
  hello
