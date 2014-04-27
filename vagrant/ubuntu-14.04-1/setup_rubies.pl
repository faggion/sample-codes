#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;

GetOptions(
    '-root=s' => \$::{root},
    '-install-versions=s' => \$::{install_versions},
    );

my $RBENV_ROOT   = $::{root};
my $RBENV_BIN    = $RBENV_ROOT . '/bin/rbenv';
my @INSTALL_RUBY_VERS = split ",", $::{install_versions};

my $ret = 0;

# setup plenv
if(!-d $RBENV_ROOT){
    $ret |= system("rm -rf $RBENV_ROOT");
    $ret |= system("git clone https://github.com/sstephenson/rbenv.git $RBENV_ROOT");
    $ret |= system("git clone https://github.com/sstephenson/ruby-build.git $RBENV_ROOT/plugins/ruby-build/");
    # curl -fsSL https://gist.github.com/mislav/a18b9d7f0dc5b9efc162.txt | sudo RBENV_ROOT=/opt/rbenv /opt/rbenv/bin/rbenv install --patch 2.1.1
}

# install perl versions
foreach my $ver (@INSTALL_RUBY_VERS){
    $ret |= system("RBENV_ROOT=$RBENV_ROOT $RBENV_BIN install $ver");
    $ret |= system("RBENV_ROOT=$RBENV_ROOT $RBENV_BIN global  $ver");
}

if(0 < scalar(@INSTALL_RUBY_VERS)){
    $ret |= system("RBENV_ROOT=$RBENV_ROOT $RBENV_BIN global ". $INSTALL_RUBY_VERS[0]);
}

exit($ret);
