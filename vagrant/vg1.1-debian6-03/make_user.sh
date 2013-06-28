#!/bin/sh

/usr/sbin/useradd $1
/usr/bin/passwd -d $1
/usr/bin/gpasswd -a $1 root
mkdir -p /home/$1/.ssh
chmod 700 /home/$1/.ssh
cat /root/.ssh/authorized_keys > /home/$1/.ssh/authorized_keys
cat /root/.ssh/config > /home/$1/.ssh/config
cat /root/.zshrc > /home/$1/.zshrc
mkdir /home/$1/.zshrc.d
chown -R $1:$1 /home/$1
chsh $1 -s `which zsh`
