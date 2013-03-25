#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use utf8;
use Encode;
use LWP::Simple qw/:DEFAULT $ua/;
$ua->agent('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25');

while(<>){
    chomp;
    my ($url, $name) = split "\t";
    warn $url;
    my $raw = get($url."subject.txt");
    next if(!defined $raw || !$raw);
    my @html;
    eval {
        @html = split("\n", Encode::decode("Shift_JIS", $raw));
    };
    if($@){
        warn $url;
        warn $raw;
        warn $@;
        next;
    }
    foreach my $l (@html){
        if($l =~ m|^(\d+.dat)<>(.*)\s+\(([\d]*)\)$|){
            print Encode::encode_utf8(join("\t", $url."dat/".$1, $3, $2))."\n"
        }
    }
    sleep(1);
}

