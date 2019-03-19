#!/usr/bin/env perl

# Myanmar sentence breaking based on syllable+potema list
# (i.e. only prefix syllable and potema 2gram) data
# Written by Ye Kyaw Thu,
# Visiting Professor,
# Language Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to use:
# $ perl print-error-sent.pl <syl-potma-list-filename> <corpus-filename>
# e.g. perl ./my-linebreak.pl ./1gram.potma.dict ./test-data > out

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# reading the input file of collected syllable and potema
open (my $errFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
our @errorSyl;

while (!eof($errFILE)) {

   my $line = <$errFILE>;
   if (($line ne '') & ($line !~ /^ *$/)) {

      chomp($line);
      push @errorSyl, $line;

   }
}
    
close ($errFILE);

#prepare regular expression
my $errorSylRegEx = join "[^\n]|", @errorSyl;

open (my $corpusFILE,"<:encoding(utf8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";
while (!eof($corpusFILE)) {

   my $line = <$corpusFILE>;
   if (($line ne '') & ($line !~ /^ *$/)) {

      chomp($line);

      # removing spaces and tabs from the beginning and from the end of a string
      $line =~ s/^\s+|\s+$//g;

      # this line will make only one space between words
      # if you want to keep potema with more than one spaces as original
      # (i.e. don't want to make line break), comment out the following line
      $line =~ s/ +/ /g; 

      # if collected "syllable<space>potema" found,
      # added space character after the matched string   
      $line =~ s/($errorSylRegEx)/$1\n/g;
      print $line."\n";

     }
}

close ($corpusFILE);
