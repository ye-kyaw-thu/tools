#!/usr/bin/env perl

# word wraping
# Ye Kyaw Thu, Visiting Professor, LST Lab., NECTEC
# 14 Mar 2019 
# 
# How to run: perl wc.pl <input-file> <no-of-words>
# e.g. ./wordwrap.pl ./input-file 8
# e.g. ./wordwrap.pl ./input-file 3 

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

my $no_of_word = $ARGV[1];

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
   my $line = <$inputFILE>;
   chomp($line);
   my @word = split(' ', $line);
   my $wc = scalar(@word);
   my $loop_value = int($wc/$no_of_word);
   #print "loop value: $loop_value\n";
   if ($wc > $no_of_word) {
      my $start = 0;
      my $end = $no_of_word -1 ;

      for (my $i=0; $i<=$loop_value; $i++) { 
         if ($end < $wc) {
            #print "loop value: $loop_value, i: $i, wc: $wc, start: $start, end: $end\n";
            print "@word[$start..$end]\n";
            $start = $end + 1;
            $end = $end + $no_of_word;
         } elsif ($start < $wc){
              #print "loop value: $loop_value, i: $i, wc: $wc, start: $start, end: $end, \$#word: $#word\n";
              print "@word[$start..$#word]\n";
         }
      }

   } else {
     print "$line\n";
     }
}

close ($inputFILE);
