use strict;
use warnings;
use CDB::TinyCDB;

# open/load for updating - loads all existing records into temp file
my $file = "/tmp/my.tcdb";

# load ( loads file into memory )
my $cdb = CDB::TinyCDB->load($file);

# iterates over all entries
while ( my ($key, $value) = $cdb->each ) {
    # same as cdb -d my.cdb, but skips null keys
    printf("+%d,%d:%s->%s\n", length($key), length($value), $key, $value);
}
