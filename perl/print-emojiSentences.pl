#!/usr/bin/env perl

# printing sentences that contain emoji character
# with -r option, the program will print sentences that do not contain emoji character
# Ye Kyaw Thu, NICT, Kyoto, Japan
#
# last updated: 25 April 2015
# usage: perl print-emojiSentences.pl <input-file>
# e.g. perl ./print-emojiSentences.pl ./tst-emoji 
# e.g. perl ./print-emojiSentences.pl ./tst-emoji r

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

if (! defined $ARGV[1]){
 
   while (!eof($inputFILE)) {
     
      my $line = <$inputFILE>;
      if (($line ne '') & ($line !~ /^ *$/) & ($line =~ /(\p{Emoticons})/g)) {
         chomp($line);
         
        print "$line\n";
       }

    }
  
}
elsif ($ARGV[1] eq "r"){

   while (!eof($inputFILE)) {
     
      my $line = <$inputFILE>;
      if (($line ne '') & ($line !~ /^ *$/) & ($line !~ /(\p{Emoticons})/g)) {
         chomp($line);
         
        print "$line\n";
       }

    }


}


close ($inputFILE);
