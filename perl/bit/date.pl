#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

sub encode_date {
    my $type = shift @_;
    my $year = shift @_;
    my $mon  = shift @_;
    my $day  = shift @_;
    return ($type << 21 | $year << 9 | $mon << 5 | $day);
}

sub decode_date {
    my $intdate = shift @_;
    my $day  = ($intdate &     0x1f);
    my $mon  = ($intdate &    0x1ff) >> 5;
    my $year = ($intdate & 0x1fffff) >> 9;
    my $type = $intdate >> 21;
    return ($type, $year, $mon, $day);
}

my $type = 2;
my ($year, $mon, $day);
#$year = 4095; # max
$year = 2011;
$mon  = 1;
$day  = 20;

warn sprintf("%04d/%02d/%02d", $year, $mon, $day);
my $e = encode_date($type, $year, $mon, $day);
warn Dumper(decode_date($e));

warn '-----';

$year = 2010;
$mon  = 12;
$day  = 9;

warn sprintf("%04d/%02d/%02d", $year, $mon, $day);
warn encode_date($type, $year, $mon, $day);
warn Dumper(decode_date(encode_date($type, $year, $mon, $day)));



