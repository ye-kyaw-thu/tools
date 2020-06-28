#!/usr/bin/perl

# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Example usage of sylbreak perl module
# How to run:
# e.g. cat ./bbc-article-27june2020.5sent.txt | perl ./test.sylbreak.pm.pl 

use lib './';
use sylbreak;
# perl module ကို ခေါ်သုံးတဲ့ အခါမှာ use နဲ့ မဟုတ်ပဲ require နဲ့လည်း သုံးနိုင်ပါတယ်
#require sylbreak; 

use strict;
use warnings;
use utf8;
binmode STDIN, ":encoding(UTF-8)";
binmode STDOUT, ":encoding(UTF-8)";

while (my $line = <STDIN>)
{
   print (sylbreak::syllable("$line", "_"), "\n");
   print (sylbreak::syllableWord("$line", "_"), "\n");
}
