package MyClass;

use strict;
use warnings;
use Data::Dumper;

sub new {
    my ($class) = @_;
    return bless {}, $class;
}

sub is_hashref {
    my ($self, $var) = @_;
    return ref($var) eq 'HASH' ? 1 : 0;
}

1;
