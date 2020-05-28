#!/bin/perl

# print union, intersection and difference of two files based on the segmented units
# column information: line-from-filename1|||line-from-filename2|||union-array|||intersection-array|||difference-array
#
# Written by Ye Kyaw Thu,
# Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to use:
# $ perl print-union-isect-diff.pl <filename1> <filename2>
# e.g. perl ./print-union-isect-diff.pl

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

   my @isect = my @diff = my @union = ();
   my %count; my $e;
   foreach $e (@l1, @l2) { $count{$e}++ }

   foreach $e (keys %count) {
      push(@union, $e);
      push @{ $count{$e} == 2 ? \@isect : \@diff }, $e;
}

print("@l1|||@l2|||@union|||@isect|||@diff\n");

}

close ($FILE1);
close ($FILE2);
