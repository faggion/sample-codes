#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use Data::Dumper;

use MeCab;

my $m = new MeCab::Tagger("");

while(<>){
    chomp;
    next if(!$_);
    my $n = $m->parseToNode($_);
    warn Dumper($n);
#    while ($n = $n->{next}) {
#        printf("%s\t%s\t%d\n",
#               $n->{surface},          # 表層
#               $n->{feature},          # 現在の品詞
#               $n->{cost}              # その形態素までのコスト
#            );
#    }
}
