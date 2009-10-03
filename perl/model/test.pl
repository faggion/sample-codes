use strict;
use warnings;
use Data::Dumper;

use User;

my $u = new User({name=>'Satoshi', age=>'19'});

warn Dumper($u->validate());

