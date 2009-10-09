#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
sub golden_ratio { return (1.618, 1) } # FIXME:
GetOptions('-len=s'  => \$::opts{length},
           '-type=s' => \$::opts{type});
if($::opts{type} ne 'all'   &&
   $::opts{type} ne 'long'  &&
   $::opts{type} ne 'short'){
    warn 'set type "all"';
    $::opts{type} = 'all';
}
my ($l, $s) = golden_ratio();
if($::opts{type} eq 'all'){
    print "all:\t".   $::opts{length}. "\n";
    print "long:\t".  $::opts{length}*$l/($l+$s). "\n";
    print "short:\t". $::opts{length}*$s/($l+$s). "\n";
}
elsif($::opts{type} eq 'long'){
    print "all:\t".   $::opts{length}*($l+$s)/$l. "\n";
    print "long:\t".  $::opts{length}. "\n";
    print "short:\t". $::opts{length}*$s/$l. "\n";
}
elsif($::opts{type} eq 'short'){
    print "all:\t".   $::opts{length}*($l+$s)/$s. "\n";
    print "long:\t".  $::opts{length}*$l/$s. "\n";
    print "short:\t". $::opts{length}. "\n";
}
else{die}

