#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
use Atompub::Client;
use XML::Atom::Entry;

GetOptions(
    '-user=s'=>\$::opts{user},
    '-pass=s'=>\$::opts{pass},
    );

my $client = Atompub::Client->new;
$client->username($::opts{user});
$client->password($::opts{pass});

my $service     = $client->getService("http://livedoor.blogcms.jp/atom/");
my $article_url = $service->workspace->collection->href;
#warn Dumper($service->workspace->collection->href);

my $entry    = XML::Atom::Entry->new;
my $category = XML::Atom::Category->new;
my $content  = 
    '<a target="_blank" href="http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=mdyd00587/tanarky-001">'.
    '<img src="http://pics.dmm.co.jp/digital/video/mdyd00587/mdyd00587ps.jpg"></a><br>';
$category->term('test');
$entry->title('テストタイトル');
$entry->content($content);
$entry->category($category);
$client->createEntry( $article_url, $entry );
