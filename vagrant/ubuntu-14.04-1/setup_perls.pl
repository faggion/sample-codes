#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;

GetOptions(
    '-root=s' => \$::{root},
    '-install-versions=s' => \$::{install_versions},
    );

my $PLENV_ROOT   = $::{root};
my $PLENV_BIN    = $PLENV_ROOT . '/bin/plenv';
my @INSTALL_PERL_VERS = split ",", $::{install_versions};

my $ret = 0;

# setup plenv
if(!-d $PLENV_ROOT){
    $ret |= system("rm -rf $PLENV_ROOT");
    $ret |= system("git clone git://github.com/tokuhirom/plenv.git $PLENV_ROOT");
    $ret |= system("git clone git://github.com/tokuhirom/Perl-Build.git $PLENV_ROOT/plugins/perl-build/");
}

# install perl versions
foreach my $ver (@INSTALL_PERL_VERS){
    $ret |= system("PLENV_ROOT=$PLENV_ROOT $PLENV_BIN install $ver");
    $ret |= system("PLENV_ROOT=$PLENV_ROOT $PLENV_BIN global  $ver");
    #$ret |= system("PLENV_ROOT=$PLENV_ROOT $PLENV_BIN install-cpanm");
    $ret |= system("wget http://xrl.us/cpanm -O $PLENV_ROOT/shims/cpanm");
    $ret |= system("chmod +x $PLENV_ROOT/shims/cpanm");
    $ret |= system("LANG=C $PLENV_ROOT/shims/cpanm Carton");
}

if(0 < scalar(@INSTALL_PERL_VERS)){
    $ret |= system("PLENV_ROOT=$PLENV_ROOT $PLENV_BIN global ". $INSTALL_PERL_VERS[0]);
}

exit($ret);
