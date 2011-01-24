#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
use utf8;
use Encode;

use WebService::Blogger;

GetOptions(
    '-title=s' => \$::opts{title},
    '-body=s'  => \$::opts{body}
    );
die if(!defined $::opts{title});
die if(!defined $::opts{body});

my $blogger = WebService::Blogger->new();
my @blogs   = $blogger->blogs;
my $blogid  = 'tag:blogger.com,1999:user-282620250206.blog-3356441096222615825';
my $blog;
foreach my $b (@blogs) {
    print $b->id. ":". Encode::encode_utf8($b->title). "\n";
    if($b->id eq $blogid){
        $blog = $b;
        last;
    }
}
#my @entries = $blog->entries;

my $new_entry = $blog->add_entry(
     title   => $::opts{title},
     content => $::opts{body},
    );

warn 'finished';
