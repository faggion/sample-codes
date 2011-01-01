#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper;
use HTML::Selector::XPath qw/selector_to_xpath/;
use HTML::TreeBuilder::XPath;

while(<>){
    chomp;
    next if(!-f $_);
    my $html;
    open(my $fh, $_) or die;
    $html = join("", <$fh>) ;
    close($fh);

    next if($_ !~ m|/([^/]*?)$|);
    my $tree = HTML::TreeBuilder::XPath->new;
    $tree->parse($html);
    my $id     = $1;
    my @title  = $tree->findnodes(selector_to_xpath('h1'));
    my @desc   = $tree->findnodes(selector_to_xpath('div.lh4'));
    my @spec   = $tree->findnodes(selector_to_xpath('td>a'));
    my @sample = $tree->findnodes(selector_to_xpath('div>a>img.mg-t6'));
    my %ids    = ();
    foreach my $s (@spec){
        # /digital/videoa/-/list/=/article=keyword/id=1031/
        if($s->attr('href') =~ m|/article=([^/]*?)/id=([^/]*?)/|){
            my $type = $1;
            $ids{$type} = [] if(!defined $ids{$type});
            push @{$ids{$type}}, $2;
        }
    }
    my $ID    = $id;
    my $TITLE = (defined $title[0] && $title[0]->as_text) ? $title[0]->as_text : next;
    my $SMPL  = (defined $sample[0]) ? "[1]" : "[0]";
    my $MAKER = (defined $ids{maker}   && @{$ids{maker}})   ? ":". join(":", sort @{$ids{maker}})  . ":" : "";
    my $ACTRS = (defined $ids{actress} && @{$ids{actress}}) ? ",". join(",", sort @{$ids{actress}}). "," : "";
    my $KEYWD = (defined $ids{keyword} && @{$ids{keyword}}) ? "|". join("|", sort @{$ids{keyword}}). "|" : "";
    my $SRS   = (defined $ids{series}  && @{$ids{series}})  ? "/". join("/", sort @{$ids{series}}) . "/" : "";
    my $DESC  = (defined $desc[0]  && $desc[0]->as_text)  ? $desc[0]->as_text  : next;
    print join("\t", $ID, $TITLE, $SMPL, $MAKER, $ACTRS, $KEYWD, $SRS, $DESC)."\n";
}
