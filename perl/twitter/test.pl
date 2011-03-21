#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;

use AnyEvent::HTTP 'http_request';
use Config::Pit 'pit_get';
use Encode 'encode_utf8';
use MIME::Base64 'encode_base64';

my $config = pit_get(
    "twitter.com",
    require => {
        "username" => "tanarky",
        "password" => "Mtsa5wnh",
    }
    );

my $cv = AE::cv;
http_request(
    #'GET', 'http://chirpstream.twitter.com/2b/user.json',
    'GET', 'http://stream.twitter.com/1/statuses/sample.json',
    headers => {
        Authorization => "Basic " . encode_base64(join ':', @$config{qw/username password/}),
    },
    want_body_handle => 1,
    sub {
        #print Dumper(@_);
        my $hdl = shift;
        my $r = sub {
            my (undef, $json) = @_;
            if (my $text = $json->{text}) {
                print encode_utf8 "$json->{user}{screen_name}: $text\n";
            }
        };
        #$hdl->on_read(sub { $hdl->push_read( json => $r ); });
        $hdl->on_read(sub { warn Dumper(@_); });
    }
    );
$cv->recv;
