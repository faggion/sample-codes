use strict;
use warnings;
use JSON;
use Data::Dumper;
use utf8;

my $data = { "foo" => 123, "unicode" => "あいう"};

print JSON->new->utf8(0)->encode($data). "\n";

print encode_json($data). "\n";

#print JSON->new->utf8(1)->encode($data). "\n";

my $l = JSON->new->latin1->encode($data);
print $l. "\n";

print encode_json(decode_json($l)). "\n";

# たぶんCPAN moduleがありそう
warn pack("U",hex("\u30af"));

# あった
#use Encode::Escape::Unicode;
#use Encode::Escape;
use Unicode::Escape;

my $uni = '{"foo":"\u30af\u30ea\u30ce\u30c3\u30da"}';
warn Unicode::Escape::unescape($uni, 'utf-8');
