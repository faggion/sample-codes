use strict;
use warnings;
use Data::Dumper;

use User;

my $u = new User({name=>'Satoshi', age=>'30', foo=>'1'});

warn Dumper($u->validate());

