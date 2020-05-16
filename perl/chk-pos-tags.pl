#!/usr/bin/perl
#use warnings;
use utf8;

# for checking POS tag errors based on myPOS POS tag-set
#
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# Last updated: 16 May 2020
# How to run: perl ./chk-pos-tags.pl <manual-POStagged-filename>
# e.g. ./chk-pos-tags.pl ./myanmar.pos.rmpipe.txt | wc

binmode STDIN,  ":utf8";
binmode STDOUT, ":utf8";

open(my $inputFILE, '<:encoding(UTF-8)', $ARGV[0])
  or die "Could not open file '$inputFILE' $!";

my $lineNo=1;

while($line = <$inputFILE>) {

   if ($line!~/^$/) {
      chomp ($line);
      $line =~ s/^\s+|\s+$//g;
      $line =~ s/ +/ /g;
      my @token = split('\s', $line);
      #print ("\@tokens:\n"."@token\n");
      foreach $one_token(@token) {
         #print "one_token: $one_token\n";
         if (my ($text, $tag) = split(/\//, $one_token)) {
            #print ("$text: $tag\n");
            if ($tag !~ /abb|adj|adv|conj|fw|int|n|num|part|ppm|pron|punc|sb|tn|v/) {
               #print ("$lineNo\t$line\n"); last;
               print("Tag ERROR! Line no ($lineNo): $line\n");
               print ("$text:$tag\n"); last;
            }
         } else {
            print ("Other ERROR! Line no ($lineNo): $line\n"); last;
         }
      }
   }
   $lineNo = $lineNo+1;
}

close($inputFILE);
