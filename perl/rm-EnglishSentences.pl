#!/usr/bin/env perl

# Remove sentences that contain English character or word
# Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# usage: perl rm-EnglishSentences.pl <input-file>

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
        chomp($line);

        #  if you used "$line !~ /\W/", the program will printout one word sentences 
        if ($line !~ /[a-zA-z0-9]/ ) {
           print "$line\n";
         }
    }

}

close ($inputFILE);

