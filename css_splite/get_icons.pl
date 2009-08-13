#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

my $output     = "icons.png";
#my @icons      = ();
my @icon_names = ();
my @icon_files = ();
while(<>){
    chomp;
    my ($name, $url) = split(/\t/, $_);
    next unless(defined $name && defined $url);
    next unless($url =~ m|/(.*?)(\.gif)$| || $url =~ m|/(.*?)(\.png)$| );
    my $ext = $2;

    my $cmd = "/usr/bin/wget $url -O $name$ext";
    system($cmd);
    #push @icons, {'name'=>$name, 'file'=>"$name$ext"};
    push @icon_names, $name;
    push @icon_files, "$name$ext";
}

my $convert = "/usr/bin/convert +append ". join(" ", @icon_files). " $output";
system($convert);

my $optimize = "/usr/bin/optipng $output";
system($optimize);
