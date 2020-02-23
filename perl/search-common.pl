#!/usr/bin/env perl

# searching common lines
# used for extracting common Dawei and Beik sentences based on Myanmar sentences
# Ye Kyaw Thu, LST Lab., NECTEC, Thailand
#
# How to run: perl ./search-common.pl <pattern-file> <input-file>
# e.g. perl ./search-common.pl ./common.all.my ./bk-my/all.mynospace.my-bk > final.common.my-bk
# perl ./search-common.pl ./common.all.my ./dw-my/all.mynospace.my-dw > final.common.my-dw

use strict;
use warnings;
use utf8;
#use experimental 'smartmatch';

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $patternFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my @pattern=<$patternFILE>;
close ($patternFILE);
#print "@pattern";
#exit();
open (my $inputFILE,"<:encoding(utf8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        my ($col1, $col2, $col3) = split("\t", $line); 
        #print ("column 1: $col1, column 2: $col2, column 3: $col3\n");
        #if ( $col1 ~~ @pattern ) {  
        if ( grep( /^$col1$/, @pattern ) ) {
           print "$line\n";
         }         
#exit();
    }

}

close ($inputFILE);

