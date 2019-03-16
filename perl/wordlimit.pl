#!/usr/bin/env perl

# word wraping
# Ye Kyaw Thu, Visiting Professor, LST Lab., NECTEC
# 14 Mar 2019 
# 
# How to run: perl wc.pl <input-file> <no-of-words>
# e.g. ./wordlimit.pl ./input-file ">8"
# e.g. ./wordlimit.pl ./input-file "<7" 

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

my $operator_word = $ARGV[1];

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
   my $line = <$inputFILE>;
   chomp($line);
   my @word = split(' ', $line);
   my $wc = scalar(@word);

   if (eval($wc. $operator_word)) {
      print "@word\n";
   }

}

close ($inputFILE);
