#!/usr/bin/env perl

# Cleaning Myanmar vowels without a consonant
# You might get this kind of data when you convert WinInwa to UTF8
# Ye Kyaw Thu, Visiting Researcher
# Language and Speech Science Research Lab., Waseda University, Japan
# 
# How to use: perl clean-v-without-c.pl <input-file>
# e.g. perl clean-v-without-c.pl 

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
        if ($line !~ /.*\s[\x{102B}-\x{103E}].*\s.*|^[\x{102B}-\x{103E}].*\s.*|\s[\x{102B}-\x{103E}].*$/) {
           print "$line\n";
        }
    }

}

close ($inputFILE);
