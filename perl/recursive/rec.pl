#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;

my @data = split //, $ARGV[0];

echo_rec([], @data);

sub echo_rec {
    my ($pref, @arr) = @_;

    if(scalar(@arr) == scalar(@$pref)){
        print join(",", @$pref). "\n";
        return;
    }

    for(my $i=0;$i<scalar(@arr);$i++){
        my @pref_new = (@$pref, $arr[$i]);
        echo_rec(\@pref_new, @arr);
    }
}
