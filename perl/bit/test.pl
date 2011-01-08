#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use speckv;

my @bit;

$bit[0] = 2 ** 16 - 1;
$bit[1] = 2 ** 16 - 1;

my $max = 2 ** 32 - 1;

warn $max;

warn $bit[0];
warn $bit[1];

warn ($bit[0] << 16 | $bit[1]);

warn Dumper(\@speckv::kvstr);

my $k;
my $tall = 180;
$k = &speckv::KEY_TALL;
warn $k << 16 | $tall;

my $bust = 88;
$k = &speckv::KEY_BUST;
warn $k << 16 | $bust;
