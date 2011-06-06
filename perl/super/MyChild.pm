package MyChild;

use strict;
use warnings;
use base qw/MyParent/;

sub init {
    my ($self) = @_;
    warn 'init!';
}

1;

