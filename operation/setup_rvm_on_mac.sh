#!/bin/bash

sudo curl -L get.rvm.io | sudo bash -s stable
source /etc/profile.d/rvm.sh
rvm install 1.9.3
