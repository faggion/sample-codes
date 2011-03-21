#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use AnyEvent::Twitter::Stream;

my $done = AnyEvent->condvar;
my @following_ids = ('kazaken');
#local $ENV{'ANYEVENT_TWITTER_STREAM_SSL'} = 0;
#$AnyEvent::Twitter::Stream::STREAMING_SERVER = "127.0.0.1:10091";
#$AnyEvent::Twitter::Stream::USERSTREAM_SERVER = "userstream.twitter.com";
#$AnyEvent::Twitter::Stream::US_PROTOCOL = "http";

my $listener = AnyEvent::Twitter::Stream->new(
    consumer_key    => 'FFPFZ8ai4ivvSE3QlTKRQ',
    consumer_secret => 'bCh0IYf5lZSFB2uwnMhwPl3j9ZIJW59xBcTctsvncD4',
    token           => '7968492-p7PBSX9vp3yMVFE1UtdsEmMIO4buFAuIRZM4M9MTBG',
    token_secret    => 'OD1TIPIMzlwQmh51WUueSYmcLxoRskjadg1Q0xg',
    method          => "filter",
    track => 'reading',
    on_tweet => sub {
        my $tweet = shift;
        #warn "$tweet->{user}{screen_name}: $tweet->{text}\n";
        warn Dumper($tweet);
    },
    on_keepalive => sub {
        warn "ping\n";
    },
    timeout => 45,
    on_error => sub {
        my $error = shift;
        warn "ERROR: $error";
        $done->send;
    },
    on_eof => sub {
        $done->send;
    },
    );
$done->recv;

