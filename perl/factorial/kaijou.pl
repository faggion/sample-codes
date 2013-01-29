use strict;
use warnings;
use Data::Dumper;

my $max = $ARGV[0];
my $cnt = $ARGV[1];

# 
# N!を求める
# 
sub kai {
    my ($nn) = @_;
    die if($nn < 0);
    return 1 if($nn == 1);
    return 2 if($nn == 2);
    return $nn * kai($nn-1);
}
