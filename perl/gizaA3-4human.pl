#!/usr/bin/env perl

# converting alignment output file of GIZA++ to human readable text
# Ye Kyaw Thu, Multilingual Transltion Lab., Kyoto, Japan
#
# e.g. $ perl gizaA3-4human.pl <alignment-filename>

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $alignmentFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($alignmentFILE)) {     

    # reading 3 continuous lines, here we don't need header line and thus just read it
    my $header = <$alignmentFILE>;     my $source = <$alignmentFILE>;     my $target = <$alignmentFILE>;
    my @src = split(" ", $source); my @trg = split(" ", $target);
    my $printString = "";

    # looping target words array
    foreach (@trg) {
        if (($_ ne "({") and ($_ ne "})")) { # if read element is not equal to "({" and "})"
            if ($_ !~ /\d+/) { # if not digit
                 # preparing for target words
                 $printString = $printString." ".$_;
            } else {
                   # -1 have to do because perl array index starting from no. ZERO
                   my $index = $_ - 1;
                   # printing aligned source word(s)
                   $printString = $printString."(".$src[$index].") ";
            }
       }
    }
        # replacing ") (" with ","
        $printString=~ s/\) \(/,/g;
        # removing heading and trailing spaces
        $printString=~ s/^\s+|\s+$//g; 
        # now we can print a sentence for an annoying human being :)
        print "$printString\n";
}
close ($alignmentFILE);

