#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;

GetOptions('-root=s' => \$::opts{root});
die unless(defined $::opts{root});

while(<>){
    chomp;
    if(m|img src="(icons/(.*?)\.png)"|){
        my $url  = $::opts{root}. "/". $1;
        my $name = $2;
        print join("\t", $name,$url)."\n";
    }
}
