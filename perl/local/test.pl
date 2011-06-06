#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

my @foo = (1,2,3);
my @ret = ();
foreach my $i (@foo){
    push @ret, $i;
}

warn Dumper(\@ret);
