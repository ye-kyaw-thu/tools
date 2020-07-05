#!/usr/bin/perl

# Checking source and target no. of words are equal or not
# Used for Myanmar-RomanizedMyanmar corpus building together with Ms. Wint Theingi Zaw (YTU) and Ms. Shwe Sin Moe (YTU)
# Written by Ye Kyaw Thu,
# Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to use:
# $ perl perl ./chk-src-trg-words.pl [FILE] [OPTION]
# e.g. perl ./chk-src-trg-words.pl ./SL-finaldata-15000 -all
# e.g. perl ./chk-src-trg-words.pl ./SL-finaldata-15000 -diff
# e.g. perl ./chk-src-trg-words.pl ./SL-finaldata-15000 -equal
# e.g. perl ./chk-src-trg-words.pl ./SL-finaldata-15000 -diff-sentence
# e.g. perl ./chk-src-trg-words.pl ./SL-finaldata-15000 -equal-sentence

use strict;
use warnings;
use utf8;

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";

# check no. of command line argument
if ($#ARGV + 1 != 2) {  
    print("Usage: perl ./chk-src-trg-words.pl [FILE] [OPTION]\n");
    print("Counting no. of words between source and target sentences\n\n");
    print("FILE: source<TAB>target input file\n\n");
    print("OPTION:\n");
    print("-all\tdisplay both source-target sentence and no of words comparison for the whole file\n");
    print("-diff\tdisplay only no of words comparison for different no of words between source and target sentences\n");
    print("-equal\tdisplay only no of words comparison for equal no of words between source and target sentences\n");
    print("-diff-sentence\tdisplay no of words comparison for different no of words between source and target sentences together with the original sentence\n");
    print("-equal-sentence\tdisplay no of words comparison for equal no of words between source and target sentences together with the original sentence\n");
    exit;  
}  

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
my $opt = $ARGV[1];
my $lineNo = 1;

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;

    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        my($src, $trg) = split("\t", $line);
 
       # no. of word counting for source and target
        my $wcSrc; my $wcTrg;
        ++$wcSrc while $src =~ /\S+/g;
        ++$wcTrg while $trg =~ /\S+/g;

        if ($opt eq "-all") {
            print("$lineNo\t$src\t$trg\n");
            print($lineNo, "\t", $wcSrc, "\t", $wcTrg, "\n");
        } elsif ($opt eq "-diff") {
            if ($wcSrc != $wcTrg) {
                print($lineNo, "\t", $wcSrc, "\t", $wcTrg, "\n");
            }
        } elsif ($opt eq "-equal") {
            if ($wcSrc == $wcTrg) {
                print($lineNo, "\t", $wcSrc, "\t", $wcTrg, "\n");
            }
        } elsif ($opt eq "-diff-sentence") {
            if ($wcSrc != $wcTrg) {
                print("$lineNo\t$src\t$trg\n");
                print($lineNo, "\t", $wcSrc, "\t", $wcTrg, "\n");
            }
        } elsif ($opt eq "-equal-sentence") {
            if ($wcSrc == $wcTrg) {
                print("$lineNo\t$src\t$trg\n");
                print($lineNo, "\t", $wcSrc, "\t", $wcTrg, "\n");
            }
        }
    }
    $lineNo++;
}

close($inputFILE);
