#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;

GetOptions(
    '-root=s' => \$::{root},
    '-install-versions=s' => \$::{install_versions},
    );

my $PYENV_ROOT   = $::{root};
my $PYENV_BIN    = $PYENV_ROOT . '/bin/pyenv';
my @INSTALL_PYTHON_VERS = split ",", $::{install_versions};

my $ret = 0;

# setup pyenv
if(!-d $PYENV_ROOT){
    $ret |= system("rm -rf $PYENV_ROOT");
    $ret |= system("git clone git://github.com/yyuu/pyenv.git $PYENV_ROOT");
}

# install python versions
foreach my $ver (@INSTALL_PYTHON_VERS){
    $ret |= system("PYENV_ROOT=/opt/pyenv $PYENV_BIN install $ver");
}

if(0 < scalar(@INSTALL_PYTHON_VERS)){
    $ret |= system("PYENV_ROOT=$PYENV_ROOT $PYENV_BIN global ". $INSTALL_PYTHON_VERS[0]);
}

exit($ret);
