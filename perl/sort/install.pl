use strict;
use warnings;
use Data::Dumper;

my %app = (
    '1' => 100,
    '3' =>  20,
    '5' => 300,
    '7' =>  10,
);

my $user = [3,2,7,8,9,1];

#warn Dumper(sort {$a <=> $b} @$user);

sub comp {
    #warn Dumper(\@_);
    $a <=> $b;
}
#warn Dumper(sort comp @$user);

my $user2 = [7,5,3,1];
my @a = sort { $app{$b} <=> $app{$a} } @$user2;
#warn Dumper(\@a);
warn Dumper(splice(@a, 0, 2));





