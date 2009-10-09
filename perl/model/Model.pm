package Model;
use strict;
use warnings;
use Data::Dumper;
use base qw/Class::Accessor/;

my $DEF = {};

sub mk_attrs {
    my ($self, $def) = @_;
    $self->mk_accessors(keys %$def);
    $DEF = $def;
}

sub validate {
    my ($self) = @_;
    my @error  = ();
    while(my ($field, $cond) = each %$DEF){
        my $v = $cond->{valid};
        my $e = map {
            if(&$v){
                warn "$field:ok";
            }
            else{
                warn "$field:ng";
            }
        } ($self->$field());
        push @error, $e;
    }
    return \@error;
}

sub find {}
sub serialize {}
sub deserialize {}
sub save {}
sub delete {}

1;
