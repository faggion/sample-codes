#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use utf8;
use Encode;
use LWP::Simple;

# http://azlucky.s25.xrea.com/2chboard/bbsmenu2.html
# http://menu.2ch.net/bbstable.html
# http://menu.2ch.net/bbsmenu.html

my $url = 'http://menu.2ch.net/bbsmenu.html';
my $html = Encode::decode_utf8(get($url));
#print $html;
while($html =~ m|<a href=(http.*?/)>([^<>]*?)</a>|ig ){
    print Encode::encode("Shift_JIS", join("\t", $1, $2))."\n";
}




