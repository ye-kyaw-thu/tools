#!/usr/bin/env perl

# Print only sentences that contained Myanmar numbers
# Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# usage: perl print-my-numeric-sentence.pl <input-file>
# Ref: https://www.unicode.org/charts/PDF/U1000.pdf

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $count=1;
while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if ($line !~  /^\s*$/) {
        chomp($line);
        if ($line =~ m/[၀-၉]/){
           print "$count\t$line\n";
         }
    }
    $count++;
}

close ($inputFILE);
