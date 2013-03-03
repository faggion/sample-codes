#!/bin/bash

# 以下の手順をコピペしてログイン後実行

rm -f /var/lib/dpkg/info/smadmin.* &&\
echo insecure >> ~/.curlrc &&\
curl -L get.rvm.io | bash -s stable&&\
aptitude update &&\
aptitude purge apache2 apache2-doc apache2-mpm-prefork apache2-utils apache2-common apache2.2-bin smadmin libc6-i386 -y &&\
aptitude install g++ zlib1g-dev libcurl4-openssl-dev libcurl3-dev git libssl-dev libyaml-dev -y &&\
source /etc/profile.d/rvm.sh &&\
rvm install 1.9.3 &&\
rvm use 1.9.3 &&\
rvm gemset create chef &&\
rvm gemset use chef &&\
gem install merb-assets merb-core merb-helpers merb-param-protection merb-slices thin merb-haml haml coderay chef knife-solo --no-rdoc --no-ri
