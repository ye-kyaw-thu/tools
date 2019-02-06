#!/usr/bin/env perl

# Remove space(s) between Myanmar numbers
# Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# usage: perl .pl <input-file>
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

   # remove space(s) between Myanmar numbers
   $line =~ s/([၀-၉])[  ]+([၀-၉])/$1$2/g; 
   print $line."\n";
    }

}

close ($inputFILE);
