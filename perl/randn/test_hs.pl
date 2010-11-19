#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

use Net::HandlerSocket;

my $dbname = "test";
my $hsargs = { 'host' => 'localhost', 'port' => '9999' };
my $hs = new Net::HandlerSocket($hsargs);


#my $table  = "user";
#$hs->open_index(1, $dbname, $table, 'PRIMARY', 'id,name');
my $table  = "test1";
$hs->open_index(1, $dbname, $table, 'user', 'userid,adid,count');

for(my $i=0;$i<10000;$i++){
#for(my $i=0;$i<1;$i++){
    #my $r = $hs->execute_single(1, '>=', [ '500' ], 100, 0);
    #my $r = $hs->execute_single(1, '>=', [ '500' ], 1000, 0);
    my $r = $hs->execute_single(1, '=', [ '1',"$i" ], 1, 0);
    #my $r = $hs->execute_single(1, '=', [ '1',"1000" ], 1, 0);
    $r = $hs->execute_single(1, '=', [ '1','1000' ], 1, 0, 'U', [ '1', '1000', '2']);
    #$r = $hs->execute_single(1, '=', [ '1',"$i" ], 1, 0, 'U', [ '1', "$i", '1']);
    #warn Dumper($r);
}

