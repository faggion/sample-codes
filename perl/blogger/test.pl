#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
#use utf8;

#GetOptions('-pass=s' => \$::opts{pass});
#die if(!defined $::opts{pass});

use WebService::Blogger;

my $blogger = WebService::Blogger->new();

my @blogs = $blogger->blogs;
#print Dumper(\@blogs);
foreach my $blog (@blogs) {
    print join ', ', $blog->id, $blog->title, $blog->public_url, "\n";
}

my $blog = $blogs[3];
#my @entries = $blog->entries;
#my ($entry) = @entries;
##print $entry->title, "\n", $entry->content;

#my $new_entry = WebService::Blogger::Blog->add_entry(
#     title   => 'New entry',
#     content => 'New content',
#     blog    => $blog,
#    );

my $new_entry = $blog->add_entry(
     title   => '日本語utf8タイトル',
     content => '日本語utf8 New content',
    );

warn 'finished';
