use strict;
use warnings;
use CDB::TinyCDB;

# open/load for updating - loads all existing records into temp file
my $file = "/tmp/my.tcdb";
my $cdb = CDB::TinyCDB->create( $file, $file. ".$$" );

# add new records (allows duplicates)
warn "records added: ", $cdb->put_add( key1 => 'value1',
                                       key2 => 'value2',
                                       key3 => 'value2' );

$cdb->finish();
