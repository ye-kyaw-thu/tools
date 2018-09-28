#!/usr/bin/env perl

# printing sentences that contained emoji character
# Ye Kyaw Thu, NICT, Kyoto, Japan
#
# last updated: 25 April 2015
# usage: perl print-emojiSentences.pl <input-file>
# e.g. perl ./print-emojiSentences.pl ./tst-emoji 

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/) & ($line =~ /(\p{Emoticons})/g)) {
        chomp($line);
         
        print "$line\n";
    }

}

close ($inputFILE);
