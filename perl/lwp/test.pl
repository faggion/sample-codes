#!/usr/bin/perl

use strict;
use warnings;
use utf8;
use Data::Dumper;

use LWP::UserAgent;

my $ua = LWP::UserAgent->new;
my $res = $ua->get(
  "http://img.tanarky.com",
  "User-Agent" => "myUA/0.1",
    );
#print $res->as_string; # サーバからの返答を、ヘッダも含めて文字列として得る
#print $res->content;   # コンテントボディ
warn $res->content_type;   # コンテントボディ
