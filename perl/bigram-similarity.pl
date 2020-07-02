#!/usr/bin/perl

# Dice Coefficient or Bigram String Similarity Calculation
# Written by Ye Kyaw Thu,
# Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to use:
# $ perl bigram-similarity.pl <string1> <string2>
# e.g. perl ./bigram-similarity.pl ကိုကို ကိုကြီး 

use strict;
use warnings;
use utf8;

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";

sub bigram {
   my $str = shift; my @charBigram=();
   my $strLength = length($str)-1;
      for (my $i=0; $i<$strLength; $i++){
         push @charBigram, substr($str, $i, 2);
        }
   return @charBigram;
}

sub uniqArray {
  my %uniq;
  return grep { !$uniq{$_}++ } @_;
}

sub calc_similarity {
   my $inputStr1 = shift;
   my @str1 = bigram($inputStr1);
   #print("str1: @str1\n");

   my $inputStr2 = shift;
   my @str2 = bigram($inputStr2);
   #print("str2: @str2\n");

#   my (%union,@union);
#   foreach my $item ((@str1,@str2)) {
#      $union{$item} = 1;
#   }
#   @union = keys %union;

   my (%isect, @isect);
   foreach my $item (@str1) {
      $isect{$item}++ if grep {  $item eq $_ } @str2;
   }
   @isect = keys %isect;
   #print("\@isect: @isect\n");
   my @uniqStr1 = uniqArray(@str1);
   my @uniqStr2 = uniqArray(@str2);
   #print("@uniqStr1\n");
   #print("length \@uniqStr1: ", scalar(@uniqStr1), "\n");
   #print("@uniqStr2\n");
   #print("length \@uniqStr2: ", scalar(@uniqStr2), "\n");

   my $similarityValue = (2.0 * scalar(@isect))/(scalar(uniqArray(@str1)) + scalar(uniqArray(@str2)));
   print("Similarity Value:\t$similarityValue\n");
}

calc_similarity($ARGV[0], $ARGV[1]);
