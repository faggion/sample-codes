use strict;
use warnings;
use Data::Dumper;

my $max = $ARGV[0];
my @a = (1..$max);

#warn Dumper(\@a);

sub kai {
    my ($nn) = @_;
    return 2 if($nn == 2);
    return $nn * kai($nn-1);
}

sub kai2 {
    my ($head, $body) = @_;
    my $len = scalar(@$body);
    if($len == 1){
        my @r = (@$head,@$body);
        return \@r;
    }

    my @ret=();
    for(my $i=0;$i<$len;$i++){
        my @tmp = @$body;
        push @$head, splice @tmp, $i, 1;
        my $aa = kai2($head, \@tmp);
        push @ret, @$aa;
        pop @$head;
    }
    print Dumper(\@ret);
    return \@ret;
}

my $ans = kai3([], \@a);
#warn Dumper(scalar(@$ans));
#print Dumper(\@$ans);
foreach my $p (@$ans){
    print join(",", @$p). "\n";
}

#
# 順列のパターンを作成する
#
sub kai3 {
    my ($head, $body) = @_;
    my $len = scalar(@$body);
    if($len == 1){
        my @r = (@$head,@$body);
        return [\@r];
    }

    my @ret=();
    for(my $i=0;$i<$len;$i++){
        my @tmp = @$body;
        push @$head, splice @tmp, $i, 1;
        my $aa = kai3($head, \@tmp);
        push @ret, @$aa;
        pop @$head;
    }
    return \@ret;
}
