#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use Daemon::Generic;
use base qw(Daemon::Generic::While1);

newdaemon(
    progname        => 'ticktockd',
    pidfile         => '/tmp/ticktockd.pid',
    );

sub gd_preconfig {}

sub gd_run_body {
    warn scalar(localtime());
    sleep 1;
}
