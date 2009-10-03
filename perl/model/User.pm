package User;
use base qw/Model/;

__PACKAGE__->mk_attrs({
    name => { valid   => sub { $_[0] =~ /^[\w\d]*$/ },
              message => '半角英数で入力してください' },
    age  => { valid   => sub { $_[0] =~ /^[0-9]{1,3}$/ },
              message => '3桁以内の数字で入力してください'},
});

1;
