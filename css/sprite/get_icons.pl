#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
use IO::File;

GetOptions('-css=s'    => \$::opts{css},
           '-img=s'    => \$::opts{img},
           '-vertical' => \$::opts{vertical},
);

#my $output     = "./css/icons.png";
my $output     = $::opts{img};
#my $output_css = "./css/icons.css";
my $output_css = $::opts{css};

die if(!defined $output);

my @icon_names = ();
my @icon_files = ();
while(<>){
    chomp;
    my ($name, $url) = split(/\t/, $_);
    next unless(defined $name && defined $url);
    next unless($url =~ m|/(.*?)(\.gif)$| || $url =~ m|/(.*?)(\.png)$| );
    my $ext = $2;
    my $file = "./$name$ext";

    if(!-f $file){
        my $cmd = "/usr/bin/wget $url -O $file";
        system($cmd);
    }

    push @icon_names, $name;
    push @icon_files, $file;
}

my $dir = (defined $::opts{vertical}) ? '-' : '+';
my $convert = "/usr/bin/convert $dir". "append ". join(" ", @icon_files). " $output";
system($convert);

my $optimize = "/usr/bin/optipng $output";
system($optimize);

if(defined($output_css)){
    &gen_css((defined $::opts{vertical}), $output_css, @icon_names);
}

sub gen_css {
    my ($is_vertical, $file, @names) = @_;
    my $fh = new IO::File "> $file" or die;
    my $head = "span.icon{overflow:hidden;display:inline-block;height:0;background:url(icons.png) no-repeat;width:16px;padding-top:16px;margin-right:2px;margin-left:2px;vertical-align:middle}";
    print $fh $head;

    my $i=0;
    foreach my $n (@names){
        my $p = ($i) ? $i * 16 * (-1) : 0; $i++;
        if($is_vertical){
            print $fh "span.$n"."{background-position:0 $p"."px}";
        }
        else{
            print $fh "span.$n"."{background-position:$p"."px 0}";
        }
    }
    $fh->close;
}
