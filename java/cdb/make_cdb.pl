use strict;
use warnings;
use CDB_File;

my $t = new CDB_File ('/tmp/t.cdb', "t.$$") or die;
$t->insert('key1', 'value1');
$t->insert('key2', 'value2');
$t->insert('key3', 'value3');
$t->finish;
