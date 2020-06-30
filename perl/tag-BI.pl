#!/usr/bin/env perl

# Tagging BI
# Ye Kyaw Thu, AI Lab., OPU, Japan
# Note: input file must be syllable breaked with underscore "_" and word breaked with space
# e.g. $ perl ./tag-BI.pl 10line

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while(<$inputFILE>) { 
    chomp; my $outLine="";
    my @line = split(/ /, $_);
    #print("@line\n");
    
    foreach (@line) {
        if ($_ =~ /_/) {
            $_ =~ s/^([^_]+)_/$1\/B /;
            $_ =~ s/_/\/I /g;
            $outLine = $outLine.$_."/I ";
        }else {
            $outLine = $outLine." $_/B ";
        }
    }
    print ("$outLine\n");
} 
close ($inputFILE);
