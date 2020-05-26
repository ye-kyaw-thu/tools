#!/bin/perl

# print differences of two files based on the "word" or "syllable"
# or "sub-word" segmented units separated by spaces
# Written by Ye Kyaw Thu,
# Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to use:
# $ perl print-diff-word.pl <filename1> <filename2>
# e.g. perl ./print-diff-word.pl ./file1 ./file2

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $FILE1,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
open (my $FILE2,"<:encoding(utf8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";

my $line1; my $line2;
while(defined($line1 = <$FILE1>) and defined($line2 = <$FILE2>)){
   chomp($line1);
   chomp($line2);

   my @l1 = split(/\s/, $line1);
   my @l2 = split(/\s/, $line2);
   #print("@l1\n"); print("@l2\n"); # for debugging
   #print ("==========\n");
 
   my @array1=(); my @array2=(); my $i;
   if (scalar(@l1) == scalar(@l2)) {
      @array1 = @l1; @array2 = @l2;
      $i = scalar(@array1);
   } elsif (scalar(@l1) > scalar(@l2)) {
         @array1 = @l1; @array2 = @l2;
         $i = scalar(@array1);
   } else {
         @array1 = @l2; @array2 = @l1;
         $i = scalar(@array1);
   }    

   my $checkLength = scalar(@array2);  #print("checkLength=$checkLength, i=$i\n");
   for(my $j=0; $j<$i; $j++){
         if ($checkLength != $j) {
            # if two array elements are not equal, print that two elements
            if ($array1[$j] ne $array2[$j]){
               print("$array1[$j]|$array2[$j]\t");
            }
         } else {
         # for the last two elements,
         #considering length of the array1 might greather than the length of the array2
                  print("@array1[$j..$#array1]| Null"); last;
            }
      }
      print("\n");
}

close($FILE1);
close($FILE2);
