#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

while(<>){
    chomp;
    my ($asin, $mid, $uid, $text) = split "\t";
    if(defined $text && $asin =~ /^[\w\d]{1,}$/ ){
        print "\n". $text;
    }
    elsif($asin){
        print $asin;
    }
}
