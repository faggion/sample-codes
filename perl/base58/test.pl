#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use Encode::Base58;

my $num = 12345678901234567890; # big number

warn "そのまま表示 :\t\t".         $num;
warn "base58 encode:\t\t".         encode_base58($num);
warn "base58 encode->decode:\t". decode_base58(encode_base58($num));
warn "ちゃんともどるか確認 :\t". decode_base58(encode_base58($num))/100000;

my @a = (1,2,3,4,5,6,7,8,9,0); # 10
my $i = @a;
warn $i;

my $str = "abc";
warn chop $str;
