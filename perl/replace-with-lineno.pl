#!/usr/bin/env perl

# replacing the whole sentence with specified line number
# Ye Kyaw Thu, LST, NECTEC, Thailand
#
# e.g. $ perl replace-with-lineno.pl <lineno-tab-sentence-filename> <input-filename>
# e.g. perl ./replace-with-lineno.pl ./correction.txt ./myanmar.pos.rmpipe.txt  > ./myanmar.pos.rmpipe.txt.corrected

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE1,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
my %correction=();

while (!eof($inputFILE1)) {

   my $line = <$inputFILE1>;
   chomp($line);

   # prepare a hash with line number keys
   (my $key, my $correctSentence) = split /\t/, $line;
   #print ("$key: $correctSentence\n");
   $correction{$key} = $correctSentence;
}

# numerical sort with hash key and this is for just debugging/print out the whole hash
#foreach my $key (sort { $a <=> $b } (keys(%correction))) {
#   print "$key: $correction{$key}\n";
#}
#exit();

open (my $inputFILE2,"<:encoding(utf8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";

# line number counting variable;
my $lineNo = 1;

while (!eof($inputFILE2)) {
     
   my $line = <$inputFILE2>;
   chomp($line);
   # check the hash key exist or not with the line number and 
   # if found print the value of a hash key "$lineNo"
   # if not found print the current line from the $inputFILE2
   if (exists ($correction{$lineNo})) {
      print ("$correction{$lineNo}\n");
   } else {
      print ("$line\n");
   }
  $lineNo = $lineNo+1;
}
 
close ($inputFILE1);
close ($inputFILE2);
