use Data::Dumper;

package foo;

sub new {
    # 名前付きArray ref
    bless [], shift;
}
sub push {
    my ($self, $val) = @_;
    # 名前付きArray refにデータをpush
    push @$self, $val;
}

use Data::Dumper;
my $f = new foo();
$f->push(1);
$f->push(2);
$f->push(3);
warn Dumper($f);
