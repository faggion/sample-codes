package User;
use base qw/Model/;

#__PACKAGE__->mk_attrs({
#    name => { valid   => sub { $_[0] =~ /^[\w\d]*$/ },
#              message => '半角英数で入力してください' },
#    age  => { valid   => sub { $_[0] =~ /^[0-9]{1,3}$/ },
#              message => '3桁以内の数字で入力してください'},
#});

__PACKAGE__->mk_attrs({
    age  => { valid    => sub { /^[0-9]{1,3}$/ },
              defalut  => 0,
              required => 1,
              message  => '3桁以内の数字で入力してください'},
    foo  => { valid    => sub { /^[\d\w]{1,}$/ },
              message  => '0-9の数字で入力してください'},
    name => { valid    => sub { /^[\w\d]*$/ },
              message  => '半角英数で入力してください' },
});


1;
