
LXC
---------------------

::
  
  # 初回なのですごく時間がかかる
  sudo lxc-create -t ubuntu -n p1
  
  # ubuntuは2回目なのですぐ終わる
  sudo lxc-create -t ubuntu -n p2
  
  # fancy mode ls
  sudo lxc-ls -f
  
  # daemon modeでp1を起動
  sudo lxc-start -n p1 -d
  
  # daemon modeでp2を起動
  sudo lxc-start -n p2 -d
  
  # stop
  sudo lxc-stop -n p1
  sudo lxc-stop -n p2
  
  # debian 7 wheezy(7.5) create
  sudo lxc-create -t debian -n p3
  
  # debian 6 squeeze create
  sudo lxc-create -t debian -n p4 -- -r squeeze

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

