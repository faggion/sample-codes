#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

die "Empty user name at argument" if !$ARGV[0];
die "Invalid user name at argument: '$ARGV[0]'" if $ARGV[0] !~ /^[\w\.-]+$/;
die "Please execute this script as root." if $> != 0;

my $user = $ARGV[0];
my $ret  = 0;
if(`grep -c $user /etc/shadow` =~ /^0/){
    $ret |= system("/usr/sbin/useradd $user");
    $ret |= system("/usr/bin/passwd -d $user");
    $ret |= system("/usr/bin/chsh $user -s /usr/bin/zsh");
}
$ret |= system("/usr/bin/gpasswd -a $user root");
$ret |= system("mkdir -p /home/$user/.ssh");
$ret |= system("mkdir -p /home/$user/.zshrc.d && touch /home/$user/.zshrc.d/empty");
$ret |= system("chmod 0700 /home/$user/.ssh");
$ret |= system("cat /root/.ssh/authorized_keys > /home/$user/.ssh/authorized_keys");
$ret |= system("cat /root/.ssh/config > /home/$user/.ssh/config");
$ret |= system("cat /root/.zshrc > /home/$user/.zshrc") if -e "/root/.zshrc";
$ret |= system("cat /root/.emacs.el > /home/$user/.emacs.el") if -e "/root/.emacs.el";
$ret |= system("chown -R $user:$user /home/$user");

exit($ret);
