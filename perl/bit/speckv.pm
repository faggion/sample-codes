package speckv;

use strict;
use warnings;

@speckv::kvstr = ();
$speckv::kvstr[0] = "CUP=C";


@speckv::kvint = ();
sub KEY_TALL  { return 0; }
sub KEY_BUST  { return 1; }
sub KEY_WAIST { return 2; }
sub KEY_HIP   { return 3; }

1;
