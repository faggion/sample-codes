#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use MIME::Base64;

#my $org     = 'Aladdin:open sesame...?foo=あああいいい';
my $org     = 'http://7netshopping.jp/all/?foo=+/.!"#$%&()';
my $encoded = encode_base64($org,'');
my $decoded = decode_base64($encoded);

my $s = 'X3oDMTB0NWxnaGxsBF9TAzIwNzcyOTYyNjUEdGlkAzEyBHRtcGwDZ2Ex';
warn decode_base64($s);

warn "[$org]";
warn "[$encoded]";
warn "[$decoded]";
