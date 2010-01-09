#!/usr/bin/perl

use strict;
use warnings;

use Test::More;

my $obj = new MyClass;
ok($obj, 'construct');

my $hashref = {};
is($obj->is_hashref($hashref),  1, 'expect 1 at is_hashref()');

my $arrayref = [];
is($obj->is_hashref($arrayref), 0, 'expect 0 at is_hashref()');

BEGIN {
    done_testing(4);
    use_ok('MyClass');
}
