package ExtractUniqueBlock;

use strict;
use warnings;

use Digest::MD5;
use Encode;
use Encode::Guess;
use HTML::TokeParser;
use IO::File;

our $VERSION = '0.01';

# Tagset (HTML4.01 Transitional block-like elements)
our %TS = map { $_ => 1 } qw(p h1 h2 h3 h4 h5 h6 ul ol dir menu pre dl div center noscript noframes blockquote form isindex hr table fieldset address);
our %NS = map { $_ => 1 } qw(script style);

# TokeParser Text Map
our %TP = ('S' => 4, 'E' => 2, 'T' => 1, 'C' => 1, 'D' => 1, 'PI' => 2);

sub new {
	my ($class, %opt) = @_;

	my $self;
	$self->{'opt'} = {
		'sim_threshold'      => (defined $opt{'sim_threshold'}) ? $opt{'sim_threshold'} : 0.85,
		'bdf_threshold'      => (defined $opt{'bdf_threshold'}) ? $opt{'bdf_threshold'} : 0,
		'utf8_decode'        => (defined $opt{'utf8_decode'})   ? $opt{'utf8_decode'}   : 1,
		'block_id_attribute' => $opt{'block_id_attribute'},
	};

	$self->{'md5'}       = [];
	$self->{'encoding'}  = [];
	$self->{'blockset'}  = [];
	$self->{'vectorset'} = [];
	$self->{'extract'}   = {
		'text'     => [],
		'html'     => [],
		'block_id' => [],
	};

	return bless $self, $class;
}

sub add_html {
	my ($self, $html, $encoding) = @_;

	if (utf8::is_utf8($html)) {
		utf8::encode($html);
		$encoding = 'utf8';
	} elsif ($self->{'opt'}->{'utf8_decode'}) {
		$encoding = html_to_encoding($html);

		if (! $encoding) {
			$encoding = 'utf8';
		}
	} else {
		undef $encoding;
	}

	my ($blockset, $vectorset) = _get_blockset($html);

	push @{$self->{'md5'}}, Digest::MD5::md5_hex($html);
	push @{$self->{'encoding'}}, $encoding;
	push @{$self->{'blockset'}}, $blockset;
	push @{$self->{'vectorset'}}, $vectorset;

	return $self;
}

sub add_file {
	my ($self, $file, $encoding) = @_;

	my $io1 = IO::File->new($file) or die $!;

	my $html = join("\n", $io1->getlines);

	$io1->close;

	$self->add_html($html, $encoding);

	return $self;
}

sub extract {
	my ($self, @lists) = @_;

	foreach my $html (@lists) {
		$self->add_html($html);
	}
	$self->_compute_bdf();

	my $max_set = scalar(@{$self->{'bdf'}});

	for (my $i = 0; $i < $max_set; $i++) {
		my (@html, @text, %block_id);

		my $max_block = scalar(@{$self->{'bdf'}->[$i]});

		for (my $j = 0; $j < $max_block; $j++) {
			if ($self->{'bdf'}->[$i]->[$j] <= $self->{'opt'}->{'bdf_threshold'}) {
				my (@block_text, @block_html);

				# ブロックをHTML/TEXTに展開
				foreach my $token (@{$self->{'blockset'}->[$i]->[$j]}) {
					my $html = ($self->{'encoding'}->[$i]) ? Encode::decode($self->{'encoding'}->[$i], $token->[$TP{$token->[0]}]) : $token->[$TP{$token->[0]}];

					if ($token->[0] eq 'T') {
						$html =~ s/^\n+//o;
						$html =~ s/\n+$//o;

						push @block_text, $html;
					}

					push @block_html, $html;
				}

				push @text, \@block_text;
				push @html, \@block_html;

				# BlockID を記録（実験用, ブロック先頭タグ内の block 属性リスト）
				if ($self->{'opt'}->{'block_id_attribute'}) {
					if ($self->{'blockset'}->[$i]->[$j]->[0]->[2]) {;
						my $block_id = $self->{'blockset'}->[$i]->[$j]->[0]->[2]->{$self->{'opt'}->{'block_id_attribute'}};

						$block_id{$block_id} = $self->{'bdf'}->[$i]->[$j] if $block_id;
					}
				} else {
					$block_id{$j} = $self->{'bdf'}->[$i]->[$j];
				}
			}
		}

		push @{$self->{'extract'}->{'text'}}, \@text;
		push @{$self->{'extract'}->{'html'}}, \@html;
		push @{$self->{'extract'}->{'block_id'}}, \%block_id;
	}

	return $self;
}

sub list_text {
	my $self = shift;

	return @{$self->{'extract'}->{'text'}};
}

sub list_html {
	my $self = shift;

	return @{$self->{'extract'}->{'html'}};
}

sub list_block_id {
	my $self = shift;

	return map { [ sort { $a <=> $b } keys %{$_} ] } @{$self->{'extract'}->{'block_id'}};
}

sub text {
	my $self = shift;

	return _to_text($self->{'extract'}->{'text'});
}

sub html {
	my $self = shift;

	return _to_text($self->{'extract'}->{'html'});
}

sub block_id {
	my $self = shift;

	return @{$self->{'extract'}->{'block_id'}};
}

sub html_to_encoding {
	my ($html) = @_;
	my $enc;

	my @encoding = (($html =~ /charset=([\w_-]+)/g), ($html =~ /encoding="([\w_-]+)"/g));
	foreach my $val (@encoding) {
		if (Encode::find_encoding($val)) {
			$enc = $val;

			last;
		}
	}

	if (! $enc) {
		my $guess = Encode::Guess::guess_encoding($html);

		if (ref $guess) {
			$enc = $guess->name;
		}
	}

	return $enc;
}

sub _compute_bdf {
	my $self = shift;
	my @bdf;
	my @sim;

	my $max = scalar(@{$self->{'blockset'}});

	# 比較元HTML
	for (my $i = 0; $i < $max; $i++) {
		my $max_block_i = scalar(@{$self->{'blockset'}->[$i]});

		# 比較元ブロック
		for (my $j = 0; $j < $max_block_i; $j++) {
			$bdf[$i][$j] = 0;

			# キャッシュ使用を監視
			my @used;

			# キャッシュ利用
			foreach my $cache (@{$sim[$i][$j]}) {
				$used[$cache->[0]] = 1;
				$bdf[$i][$j]++;
			}

			# 比較先HTML
			foreach my $k ($i + 1 ... $max - 1, 0 ... $i) {
				if ($i == $k || defined $used[$k]) {
					next;
				}

				# HTML(MD5)比較（同じページはスキップ）
				if ($self->{'md5'}->[$i] eq $self->{'md5'}->[$k]) {
					next;
				}

				# 探索打ち切り
				if ($bdf[$i][$j] > $self->{'opt'}->{'bdf_threshold'}) {
					last;
				}

				my $max_block_k = scalar(@{$self->{'blockset'}->[$k]});

				# 比較先ブロック
				for (my $l = 0; $l < $max_block_k; $l++) {
					my $sim = _cosine_similarity($self->{'vectorset'}->[$i]->[$j], $self->{'vectorset'}->[$k]->[$l]);

					# ブロックの一致判断
					if ($sim >= $self->{'opt'}->{'sim_threshold'}) {
						$bdf[$i][$j]++;

						# 結果をキャッシュ
						push @{$sim[$k][$l]}, [ $i, $j, $sim ];

						last;
					}
				}
			}
		}
	}

	$self->{'bdf'} = \@bdf;
}

sub _get_blockset {
	my ($html) = @_;
	my (@blockset, @vectorset);

	my $p = HTML::TokeParser->new(\$html);

	my @stack;
	while (my $token = $p->get_token()) {
		push @stack, $token;

		if ($token->[0] eq 'E' && $TS{$token->[1]}) {
			my (@block, $vector);

			my $is_skip = 0;
			while (scalar(@stack)) {
				my $token = pop @stack;

				unshift @block, $token;

				# Create Vector
				if ($token->[0] eq 'S') {
					if ($is_skip) {
						$is_skip = 0;
						next;
					}

					# Tag Name Vector (Number of Tags)
					$vector->{'|T|' . $token->[1]}++;

					foreach my $key ('alt', 'title') {
						if ($token->[2]{$key}) {
							map { $vector->{$_}++ } _string_to_token($token->[2]{$key});
						}
					}

					if ($TS{$token->[1]}) {
						last;
					}
				} elsif ($token->[0] eq 'T' && ! $is_skip) {
					map { $vector->{$_}++ } _string_to_token($token->[1]);
				} elsif ($token->[0] eq 'E' && $NS{$token->[1]}) {
					$is_skip = 1;
				}
			}

			push @blockset, \@block;
			push @vectorset, $vector;
		}
	}

	return \@blockset, \@vectorset;
}

sub _string_to_token {
	my @tmp = split(/\r|\n/o, lc $_[0]);
#	my @tmp = split(/\s+/o, lc $_[0]);
	my @token;
	foreach my $token (@tmp) {
		$token =~ s/\s+/ /go;

		if ($token) {
			push @token, $token;
		}
	}

	return @token;
}

sub _cosine_similarity {
	my ($vector_1, $vector_2) = @_;

	# Inner Product
	my $inner_product = 0.0;
	map {
		if ($vector_2->{$_}) {
			$inner_product += $vector_1->{$_} * $vector_2->{$_};
		}
	} keys %{$vector_1};

	# Euclidean Norm
	my $norm_1 = 0.0;
	map { $norm_1 += $_ ** 2 } values %{$vector_1};
	$norm_1 = sqrt($norm_1);

	my $norm_2 = 0.0;
	map { $norm_2 += $_ ** 2 } values %{$vector_2};
	$norm_2 = sqrt($norm_2);

	return ($norm_1 && $norm_2) ? $inner_product / ($norm_1 * $norm_2) : 0.0;
}

sub _to_text {
	my $list = shift;

	return map { join("\n", map { join("\n", @{$_}) } @{$_}) } @{$list};
}

1;
