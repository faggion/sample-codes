use strict;
use warnings;
use CDB_File;

tie my %data, 'CDB_File', '/tmp/t.cdb' or die;
while(my ($k, $v) = each %data) {
    print join("\t", $k, $v). "\n";
}
