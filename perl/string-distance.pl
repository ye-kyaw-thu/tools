#!/usr/bin/env perl

# check two strings similarity, here I did left-to-right character by character matching
# *** Note: This is really roughly checking and this approach is different with Edit Distance measurement
# *** Just for Perl coding and measuring string similarity exercise for my students
#
# Ye Kyaw Thu, LST Lab., NECTEC, Thailand
#
# How to run: $perl string-distance.pl <string1> <string2>
# e.g.  $ perl ./string-distance.pl "တက္ကသိုလ်" "တက္ကသိုလ"
#11.1111111111111


use strict;
use warnings;
use utf8;
use Encode;

binmode(STDIN, ":encoding(UTF-8)");
binmode(STDOUT, ":encoding(UTF-8)");
binmode(STDERR, ":encoding(UTF-8)");

my $str1 = decode('UTF-8', $ARGV[0]);
my $str2 = decode('UTF-8', $ARGV[1]);

# Based on two strings, prepare two arrays
# and get the length of that two arrays
my @chars1 = split //, $str1;
my @chars2 = split //, $str2;

# for Unicode character debugging
#print "@chars1\n";
#print "@chars2\n";

my $length1 = scalar(@chars1);
my $length2 = scalar(@chars2);

# a variable for comparing two arrays length
my $lengthDiff = 0;

# a variable for keeping maximum length of array
my $maxLength = $length1;

# get the string length difference and make equal length for both of the arrays
if ($length1 > $length2) {
   $lengthDiff = $length1 - $length2;
   for (my $i=0; $i < $lengthDiff; $i++) {
      push @chars2, "";
   }
} elsif ($length2 > $length1) {
   $maxLength = $length2;
   $lengthDiff = $length2 - $length1;
   for (my $i=0; $i < $lengthDiff; $i++) {
      push @chars1, "";
   }
}

# define differenceValue as ZERO
my $differenceValue = 0;

for(my $i=0; $i<=$#chars1; $i++){
   if ($chars1[$i] ne $chars2[$i]) {
       #print "$chars1[$i] : $chars2[$i]\n";
       $differenceValue++;
       #print "$differenceValue\n";
   }
}

# for debugging
# print "differenceValue: $differenceValue\n";

# calculating similarity score
my $distance  = (100 * $differenceValue/ $maxLength);
print "$distance\n";

