#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use URI::Encode qw(uri_encode uri_decode);

my $url = 'http://7netshopping.jp/all/?foo=+/.!"#$%&()';
my $encoded = uri_encode($url);
my $decoded = uri_decode($url);

warn "[$url]";
warn "[$encoded]";
warn "[$decoded]";
