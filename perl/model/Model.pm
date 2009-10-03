package Model;
use strict;
use warnings;
use Data::Dumper;
use base qw/Class::Accessor/;

my $DEF = {};

sub mk_attrs {
    my ($self, $def) = @_;
    $DEF = $def;
}

sub validate {
    my ($self) = @_;
    foreach(keys %$DEF){
        if($DEF->{$_}->{valid}($self->{$_})){
            warn $_.":ok";
        }
        else{
            warn $_.":ng";
        }
    }
}

1;
