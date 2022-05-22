#!/usr/bin/env perl

# cleaning punctuation characters for Burmese and other languages of Myanmar with their own characters
# Ye Kyaw Thu, Affiliated Professor, IDRI, CADT, Cambodia
# Note: We are removing frequently used punctuation symbols and not including ၏, ၍
# Note: Consider for using normalize-punctuation.perl (from moses scripts) before running this perl script.
# Preparation for giving a lecture at Mahidol University
# Last updated: 22 May 2022
# How to use:
# e.g. $ perl clean-punctuation.pl <input-file>

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        $line =~ s/၊|။|-|\(|\)|\[|\]|\/|\\|\!|\?|,|\"//g;
        $line =~ s/^\s+|\s+$//g;
        $line =~ s/ +/ /g;        
        print "$line\n";
    }
}

close ($inputFILE);
