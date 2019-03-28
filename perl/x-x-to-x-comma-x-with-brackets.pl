#!/usr/bin/env perl

# format changing from: 0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8
# to: (0,0) (1,1) (2,2) (3,3) (4,4) (5,5) (6,6) (7,7) (8,8)
# 
# Written by Ye Kyaw Thu, Visiting Professor, LST Lab., NECTEC
# How to run: $ perl ./x-x-to-x-comma-x-with-brackets.pl <alignment-output-filename>
# e.g. perl ./x-x-to-x-comma-x-with-brackets.pl ./align 

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
   my @pair = split(' ', $line);
   
   foreach (@pair) { 
    my ($left, $right) = split('-', $_);
    print "($left,$right), ";
   }

   print "\n";


}

close($inputFILE);
