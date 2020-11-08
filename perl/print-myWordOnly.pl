#!/usr/bin/env perl

# Print Myanmar words (including Myanmar digits and Myanmar punctuation pot htee and pot ma) only
# Ye Kyaw Thu, LST, NECTEC, Thailand
#
# usage: perl print-myWordOnly.pl <input-file>
# Ref: https://www.unicode.org/charts/PDF/U1000.pdf

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
        $line =~ s/[^က-အ|ဣ-ဧ|ဩ-ဲ|ံ-ဿ|၀-၉|၊-၏|\s]//g;
        $line =~ s/^\s+|\s+$//g;
        $line =~ s/\s+/ /g;
        print "$line\n";
    }
}

close ($inputFILE);
