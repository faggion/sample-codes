#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;

my %hash = (
    abc => 5,
    efg => 3,
    hij => 1,
    klm => 7,
);

my @sorted = sort {$hash{$b} <=> $hash{$a}} keys %hash;
foreach my $k (@sorted){
    print join("\t", "http://example.com/show?id=".$k, $hash{$k}). "\n";
}
