#!/usr/bin/perl
use strict;
use warnings;
#no warnings qw ( uninitialized );

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";

# change tab separated parallel sentence to CRF column format
# last updated: 7 July 2020
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# How to run: perl ./tabpair-to-crfcol.pl <input-filename>
# e.g. 

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
open (my $errorFILE,">:encoding(utf8)", "error.log") or die "Couldn't open error output file named error.log!, $!\n";

my $line;  my $line_no = 1;

while ($line = <$inputFILE>)
{
    chomp($line); 
    # split 1st column and 2nd column as left and right strings
    my($left, $right) = split /\t/, $line;
    # push words of the left string into an array
    my @left_word = ();
    @left_word = split / /, $left; #print ("$line_no\n\@left_word: @left_word\n");
    # push words of the right string into an array
    my @right_word = ();
    @right_word = split / /, $right; #print ("\@rightt_word: @right_word\n");

    # get lenght of two arrays
    my $llength = 0; $llength = scalar(@left_word);   
    my $rlength = 0; $rlength = scalar(@right_word);

    if ($llength == $rlength) {
        #print("$llength:$rlength\n");
        no warnings; # temp solution for annoying warning messages ...
        for (my $i=0; $i <= $llength; $i++) {
            print("$left_word[$i] $right_word[$i]\n");
        }
        use warnings;
    } else {
        print("ERROR!!!\n"); exit;
        print ($errorFILE "$line_no\t$line\n");
    }
    $line_no++;
}

close($inputFILE);
close($errorFILE);

