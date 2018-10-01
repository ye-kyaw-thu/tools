#!/usr/bin/env perl

# Making multi-lines paper abstract into one paragraph abstract 
# Ye Kyaw Thu, AI Lab., OPU, Japan
#
# usage: perl mk-abstract-para.pl <input-file> 
# e.g. $ perl mk-abstract-para.pl ./NAACL-HLT-2016-abstract.txt 

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
my $abstract = "";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        
        $line =~ s/\-$/\|/g;
        chomp($line);
 
        $abstract = $abstract." $line";
    }

}

$abstract =~ s/\| //g;
$abstract =~ s/^\s//;

print $abstract."\n";

close ($inputFILE);
