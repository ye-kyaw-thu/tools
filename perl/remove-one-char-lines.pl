use strict;
use warnings;
use utf8;

# Written by Prof. Ye Kyaw Thu, IDRI, CADT, Cambodia
# Removing one character lines from the dictionary
# Last updated: 21 Oct 2022
# How to run:
# perl ./remove-one-char-lines.pl <input-file>

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {

    my $line = <$inputFILE>;
    if ($line !~  /^\s*$/) {
        chomp($line);

        # print lines that length >1
        if (length($line) > 1) {
           print "$line\n";
         }
    }

}

close ($inputFILE);
