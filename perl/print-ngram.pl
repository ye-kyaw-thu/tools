#!/usr/bin/env perl

# printing bi-gram, tri-gram, ngram
# Written by Ye Kyaw Thu, Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to run: perl print-ngram.pl <input-file> <n-gram value>
# e.g. for 2 gram: perl ./print-ngram.pl ./input.txt 2
# e.g. for 3 gram: perl ./print-ngram.pl ./input.txt 3
 

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# assign ngram value
my $n = $ARGV[1]-1; 

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
   my $line = <$inputFILE>;
   if (($line ne '') & ($line !~ /^ *$/)) {

       chomp($line);

       # split the sentence with space and assign into array
       my @tokens = split(' ', $line);
  
   for(my $i=0;$i<=$#tokens-$n;$i++){
      print "@tokens[$i .. $i+$n]\n";
      }
 
    }

}

close ($inputFILE);
