#!/usr/bin/env perl

# for removing symbols, Myanmar vowels and Independent vowels only sentences
# Note: Although this program is working well for my cleaning case,
# you might need to update the RE syntax based on your requirements
# Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# usage: perl ./rm-symbol-and-myVowel-only-sentences.pl <input-filename>
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

        if ($line !~ /^[ဣ|ဤ|ဧ|ဩ|ါ-ဲ|ံ-ဿ|၊|။|\p{P}|\s|\`|\$|\~|\.]+$/){
           print "$line\n";
         }
    }

}

close ($inputFILE);
