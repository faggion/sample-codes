#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use Data::Dumper;
use Encode;

use Tenjin;

my $title   = "タイトル";
my $entries = [
    {name=>'ヤフー', url=>'http://www.yahoo.co.jp'},
    {name=>'mixi',   url=>'http://mixi.jp'},
    {name=>'DMM.com',url=>'http://www.dmm.co.jp'},
    ];

my $engine = new Tenjin();
my $out    = $engine->render('sample.pl.html', { title => $title, entries => $entries });
print encode("utf8", $out);
