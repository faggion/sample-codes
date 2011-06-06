package MyParent;

use strict;
use warnings;
use Class::Accessor::Fast;
use base qw/Class::Accessor::Fast/;

__PACKAGE__->mk_accessors(qw/name title/);

sub foo {
    my ($self) = @_;
    warn 'parent foo';
}

1;
