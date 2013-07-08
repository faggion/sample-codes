#!env perl

use strict;
use warnings;
use Data::Dumper;
use utf8;
use Encode;

use Text::LevenshteinXS qw/distance/;
use Text::Fuzzy;

my $answer = '銀座馬喰一代';
my @tests  = ('飛騨牛 一頭家 銀座 馬喰一代',
              '飛騨牛 一頭家 馬喰一代',
              '銀座焼肉 じゅーじゅー',
              '銀座焼肉 じゅーじゅー 飛騨牛のおいしいA5肉を使用しております',
              '銀座牛角',
              '飛騨牛焼肉');

=item

warn distance('あ', 'い');
warn distance('あ', 'あい');
warn distance('あ', 'いあ');

my $tf = Text::Fuzzy->new('あ');

warn $tf->distance('い');
warn $tf->distance('あい');
warn $tf->distance('いあ');

=cut

my $tf = Text::Fuzzy->new($answer);

foreach my $t (@tests){
    my $long_len = (length($t) < length($answer)) ? length($answer) : length($t);
    my $dis = $tf->distance($t);
    warn join("\t", $answer, $t, $dis, $dis/$long_len);
}


my $answer2 = 'ぎんざばくろいちだい';
my $tf_kana = Text::Fuzzy->new($answer2);
foreach my $t ('ひだぎゅういっとうやぎんざばくろいちだい',
               'ひだぎゅういっとうやばくろいちだい',
               'ぎんざやきにくじゅうじゅう',
               'ぎんざぎゅうかく'){
    my $long_len = (length($t) < length($answer)) ? length($answer) : length($t);
    my $dis = $tf_kana->distance($t);
    warn join("\t", $answer2, $t, $dis, $dis/$long_len);
}

