#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

my $i=0;
while(<>){
    chomp;
    #my $res = gethostbyname $_ || print $_. "\n";
    my $res = gethostbyname $_ || next;
    print $_. "\n";
    warn "finished:$i" if($i % 50 == 0);$i++;
}

