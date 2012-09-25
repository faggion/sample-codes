#!env perl

# 同じディレクトリに ExtractUniqueBlock.pm がある場合
use FindBin;
use lib $FindBin::Bin;
use ExtractUniqueBlock;

use LWP::Simple;
 
my $html_1 = get('http://blog.livedoor.jp/dqnplus/archives/1731693.html');
my $html_2 = get('http://blog.livedoor.jp/dqnplus/archives/1731433.html');
my $html_3 = get('http://blog.livedoor.jp/dqnplus/archives/1731258.html');

my $extractor = ExtractUniqueBlock->new();
$extractor->extract($html_1, $html_2, $html_3);
my ($content_1, $content_2, $content_3) = $extractor->text;

print $content_1; # $html_1 からコンテンツを抽出した結果
#print $content_2; # $html_2 からコンテンツを抽出した結果
#print $content_3; # $html_3 からコンテンツを抽出した結果
