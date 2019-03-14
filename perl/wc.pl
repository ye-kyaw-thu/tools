#!/usr/bin/env perl

# word counting for each line
# Ye Kyaw Thu, Visiting Professor, LST Lab., NECTEC
# 14 Mar 2019 
# 
# e.g. $ perl wc.pl <input-file>

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
   my @word = split(' ', $line);

   print "@word ".scalar(@word)."\n";

}

close ($inputFILE);
