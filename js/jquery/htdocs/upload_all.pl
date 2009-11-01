#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use Net::FTP::Recursive;
use Getopt::Long;

GetOptions(
    '-host=s'=>\$::opts{host},
    '-user=s'=>\$::opts{user},
    '-pass=s'=>\$::opts{pass},
    '-dir=s' =>\$::opts{dir},
    '-file=s'=>\$::opts{file},
    '-dbg' =>\$::opts{dbg},
 );

my $ftp = Net::FTP::Recursive->new($::opts{host}, Debug => $::opts{dbg})
    or die "Cannot connect to some.host.name: $@";

$ftp->login($::opts{user}, $::opts{pass})
    or die "Cannot login ", $ftp->message;

$ftp->binary
    or die "Cannot change binary mode ", $ftp->message;

$ftp->cwd($::opts{dir}) or die "Cannot change working directory ", $ftp->message;
$ftp->rput() or die "put failed ", $ftp->message;

$ftp->quit;
