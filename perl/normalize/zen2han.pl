
use strict;
use warnings;
use utf8;
use Encode;

sub zen2han {
    my $str = shift;
    $str =~ tr/　！”＃＄％＆’（）＊＋，－．／０-９：；＜＝＞？＠Ａ-Ｚ［￥］＾＿｀ａ-ｚ｛｜｝/ -}/;
    return $str;
}

my $s = $ARGV[0];
if(!utf8::is_utf8($s)){
    $s = Encode::decode_utf8($s);
}

warn Encode::encode_utf8(zen2han($s));

