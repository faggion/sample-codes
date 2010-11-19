#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use Math::Trig qw(pi);

sub randn {
    my ($m, $sigma) = @_;
    my ($r1, $r2) = (rand(), rand());
    while ($r1 == 0) { $r1 = rand(); }
    return ($sigma * sqrt(-2 * log($r1)) * sin(2 * pi() * $r2)) + $m;
}

my $ad_count    = 10000;
my $ad_variance = 1500;  # 平均は5000とする
my $user_count  = 1000;

srand(time());
for(my $i=0;$i<$user_count;$i++){
    my $userid = $i + 1;
    my $ads    = int(randn($ad_count/2, $ad_variance));
    for(my $j=0;$j<$ads;$j++){
        #my $count  = int(rand(5)) + 1;
        my $count  = 1;
        print join("\t", $userid, $j+1, $count)."\n"; # 平均値5、標準偏差3
    }
}
