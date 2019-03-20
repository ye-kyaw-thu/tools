#!/usr/bin/env perl

# Cleaning Named Entity tags
# Written by Ye Kyaw Thu,
# Researcher, AI Lab., OPU, Japan
#
# How to run: perl rm-ne-tag.pl <filename>
# e.g. perl ./rm-ne-tag.pl ./my-ne-tag-data

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

        # replacing segmentation mark "|" with space character
        $line =~ s/\|/ /g;

        # removing Named Entity tags
        $line =~ s/(\[[A-Z\\\/]+\])//g;
         
        print "$line\n";
    }

}

close ($inputFILE);
