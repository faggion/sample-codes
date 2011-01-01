#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use TokyoCabinet;

my $hdb = TokyoCabinet::HDB->new();
$hdb->open('./file.tch', $hdb->OCREAT | $hdb->OWRITER | $hdb->OREADER) or die "open failed";

$hdb->put("foo", "bar");
warn $hdb->get("foo");
