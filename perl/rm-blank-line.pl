#!/usr/bin/env perl

# removing blank lines, space only lines, tab only lines
# Ye Kyaw Thu, LST, NECTEC, Thailand
#
# e.g. $ perl print-blank-lines.pl <input-file>

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    chomp($line);
    if (($line ne '') || ($line !~ /^[ |\t]*$/)) {
        print "$line\n";
    }
}

close ($inputFILE);
