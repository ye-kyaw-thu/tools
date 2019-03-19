#!/usr/bin/env perl

# retrieving syllables and potma
# Ye Kyaw Thu, AI Lab., OPU, Japan
#
# How to run: perl get-syl-potma.pl <input-file> <no-of-syllable>
# e.g. 1: perl ./get-syl-potma.pl ./my-tst.txt 1
# e.g. 2: perl ./get-syl-potma.pl ./my-tst.txt 3

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $no = $ARGV[1];

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        if ($no == 1) {
             if ($line =~ /([^\s]* ။)/) {
                print "$1\n";
            }
         }
        elsif ($no == 2) {
           if ($line =~ /([^\s]* [^\s]* ။)/) {
              print "$1\n";
            }
       }
       elsif ($no == 3) {
           if ($line =~ /([^\s]* [^\s]* [^\s]* ။)/) {
              print "$1\n";
            }
       }
    }

}

close ($inputFILE);
