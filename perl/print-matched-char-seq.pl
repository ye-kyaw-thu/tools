# Printing matched character sequence
# Ye Kyaw Thu, Language Understanding Lab., Myanmar
# Last updated: 29 July 2019
#
# Used for preparation for Myanmar-Kachin parallel corpus
# e.g. $ perl ./print-matched-char-seq.pl <input-file>
# e.g. $ perl ./print-matched-char-seq.pl ./kc-input

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);

      # finding Kachin sentence ending marks and 
      # assigning all matched characters into matchedCharArray variable
      my (@matchedCharArray) = $line =~ /([\.\?\!])/g;

      print ("input: $line\n");
      print ("Matched Char Sequence: @matchedCharArray\n");

   }

}

close ($inputFILE);
