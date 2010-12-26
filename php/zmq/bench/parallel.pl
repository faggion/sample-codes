#!/usr/bin/perl

use strict;
use warnings;
use Getopt::Long;

GetOptions('-n=s' => \$::opts{n});
die if(!defined $::opts{n});

my $pid   = 1;
my $count = $::opts{n};
my $max   = 10000;
my $loop  = $max / $count;

while($pid && $count--){
    $pid = fork;
    die "Cannot fork: $!" unless defined $pid;
}

if( $pid ){
    # 子プロセスの終了を待機する。
    warn "親プロセス[$$]: waiting...";
    wait;
}
else{
    # 子プロセスで2秒待つ
    warn "子プロセス[$$]: 処理開始";
    #sleep 1;
    #system("php client.php 0 $loop")
    system("php memcached_client.php $loop")
}
