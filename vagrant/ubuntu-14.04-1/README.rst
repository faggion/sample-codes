
Rules
---------------------

perl/python/ruby 自体は以下の環境にinstallされる

::
  
  /opt/plenv
  /opt/pyenv
  /opt/rbenv

必要な環境変数やPATHなどは、以下のファイルを読み込めばOK

::
  
  source /opt/llenv.sh

Perl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

build, cpanm, carton install には時間がかかる

Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

virtualenvは以下にある(= /opt/pyenv/shims以下にはない)

::
  
  /opt/pyenv/versions/2.7.6/bin/virtualenv

