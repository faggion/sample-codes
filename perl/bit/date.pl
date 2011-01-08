#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

#my $year = 2010;
my $year = 4095;
my $mon  = 16;
my $day  = 9;

warn sprintf("%04d/%02d/%02d", $year, $mon, $day);

warn $year << 9;
warn $mon  << 5;
warn $day;

my $intdate = (($year << 9) | ($mon << 5) | $day);

warn "-------";
warn $intdate;
warn "-------";

$day  = ($intdate &     0x1f);      # 0,0000,0000,0000,0001,1111
$mon  = ($intdate &    0x1ff) >> 5; # 0,0000,0000,0001,1111,1111
$year = ($intdate & 0x1fffff) >> 9; # 1,1111,1111,1111,1111,1111
warn $day;
warn $mon;
warn $year;
