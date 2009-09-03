use strict;
use warnings;
use Data::Dumper;
use Net::Twitter;
use Getopt::Long;

GetOptions('-user=s'=>\$::opts{user},
           '-pass=s'=>\$::opts{pass},
           '-mes=s' =>\$::opts{mes});

eval{
    die if(!defined $::opts{user} ||
           !defined $::opts{pass} ||
           !defined $::opts{mes});
    my $nt = Net::Twitter->new(
        traits   => [qw/API::REST/],
        username => $::opts{user},
        password => $::opts{pass}
        );
    my $result = $nt->update($::opts{mes});
};
if($@){
    warn "Twitter post error.[$@]";
}
