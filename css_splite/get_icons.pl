#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
use IO::File;

GetOptions('-css=s', \$::opts{css});

my $output     = "icons.png";
my @icon_names = ();
my @icon_files = ();
while(<>){
    chomp;
    my ($name, $url) = split(/\t/, $_);
    next unless(defined $name && defined $url);
    next unless($url =~ m|/(.*?)(\.gif)$| || $url =~ m|/(.*?)(\.png)$| );
    my $ext = $2;
    my $file = "$name$ext";

    if(!-f $file){
        my $cmd = "/usr/bin/wget $url -O $name$ext";
        system($cmd);
    }

    push @icon_names, $name;
    push @icon_files, "$name$ext";
}

my $convert = "/usr/bin/convert +append ". join(" ", @icon_files). " $output";
system($convert);

my $optimize = "/usr/bin/optipng $output";
system($optimize);

if(defined $::opts{css}){
    gen_css($::opts{css}, @icon_names);
}

sub gen_css {
    my ($file, @names) = @_;
    my $fh = new IO::File "> $file" or die;
    my $head = "span.icon{overflow:hidden;display:inline-block;height:0;background:url(icons.png) no-repeat;width:16px;padding-top:16px;margin-right:2px;margin-left:2px;vertical-align:top}";
    print $fh $head;

    my $i=0;
    foreach my $n (@names){
        my $p = ($i) ? $i * 16 * (-1) : 0; $i++;
        print $fh "span.$n"."{background-position:$p"."px 0}";
    }
    $fh->close;
}
