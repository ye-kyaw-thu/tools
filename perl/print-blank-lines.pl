#!/usr/bin/env perl

# for printing blank lines, space only lines, tab only lines
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

my $line_no = 1;
while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line eq '') || ($line =~ /^[ |\t]*$/)) {
        print "$line_no\t$line";
    }
    $line_no++;
}

close ($inputFILE);
