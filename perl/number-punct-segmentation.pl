#!/usr/bin/env perl

# for number and punctuation segmentation
# used for cleaning Myanmar name Romanization corpus
# Written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
#
# usage: perl ./number-punct-segmentation.pl <input-file>
# e.g. perl ./number-punct-segmentation.pl ./number-punct.eg.txt 

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if ($line !~  /^\s*$/) {

        # remove \n
        chomp($line);
       # add <SPACE>number<SPACE>
        $line =~ s/([၀-၉0-9[:punct:]])/ $1 /g;
        # clean heading and trailing spaces
        $line =~ s/^\s+|\s+$//g;
        # remove multiple spaces
        $line =~ s/ +/ /g;

        print("$line\n");
    }
}

close ($inputFILE);
