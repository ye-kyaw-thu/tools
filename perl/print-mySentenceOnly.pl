#!/usr/bin/env perl

# Print only Myanmar sentences (without Myanmar digits) with some symbols
# Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# usage: perl print-mySentenceOnly.pl <input-file>
# Ref: https://www.unicode.org/charts/PDF/U1000.pdf

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if ($line !~  /^\s*$/) {
        chomp($line);
 
# if you want to include English add "A-Z|0-9"
#  if you want to include Myanmar numbers replace
#  " ံ-ဿ|၊-၏" with "ံ-၏"

        if ($line !~ m/[^က-အ|ဣ-ဧ|ဩ-ဲ|ံ-ဿ|၊-၏|\p{P}|\s|\`|\$|\~]/){
           print "$line\n";
         }
    }

}

close ($inputFILE);
