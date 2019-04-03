#!/usr/bin/env perl

# for checking parallel or not
# Written by Ye Kyaw Thu, Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to run: 
# e.g. for print out parallel sentences: perl ./select-en-th-my.pl ./id-en-th-my.tst.txt c
# e.g. for print out error sentences: perl ./select-en-th-my.pl ./id-en-th-my.tst.txt w

use strict;
#use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {     
   my $line = <$inputFILE>;
   if (($line ne '') & ($line !~ /^ *$/)) {
      chomp($line);

      # removing leading and trailing spaces
      $line =~ s/^\s+|\s+$//g;
      # cleaning multiple spaces (or) making one space only
      $line =~ s/ +/ /g;
         
      my ($ID, $eng, $th, $my) = split("\t", $line);
      if (($ID ne '') & ($eng ne '') & ($th ne '') & ($my ne '')) {

         # if 2nd argument is "c"
         if ($ARGV[1] eq "c") {
            print "$ID\t$eng\t$th\t$my\n";
         }
      }else {

         # if 2nd argument is "w", print the sentence that contained blank field/s
         if($ARGV[1] eq "w") {
                print "$ID\t$eng\t$th\t$my\n";
         }
      }
      
   }
}

close ($inputFILE);
