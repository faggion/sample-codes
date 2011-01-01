#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use Compress::Zlib;

my $str = "hello world 日本語";
my $str_compress   = Compress::Zlib::memGzip($str. " + alpha");
my $str_uncompress = Compress::Zlib::memGunzip($str_compress);

warn "origin:". $str;
warn "length:". length($str_compress);
warn "uncomp:". $str_uncompress;

# result
# origin:hello world 日本語 at test.pl line 13.
# length:0 at test.pl line 14.
# uncomp:hello world 日本語 + alpha at test.pl line 15.
