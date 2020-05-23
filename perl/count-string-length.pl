#!/usr/bin/env perl

# counting string length together with line number
# Ye Kyaw Thu, AI Lab., OPU, Japan
# How to run: perl ./count-string-length.pl <input-file>
# e.g. $ perl count-string-length.pl ui.my

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $count = 1;
while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        my $string_len =  length($line);
        print "$count\t$line\t$string_len\n";
    }
$count = $count+1;
}

close ($inputFILE);

