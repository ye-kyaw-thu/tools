#!/usr/bin/env perl

# printing common Kachin parallel sentences
# used for extracting Rawang and Myanmar sentences based on common Kachin sentences
# Ye Kyaw Thu, LST Lab., NECTEC, Thailand
#
# How to run: perl ./print-common-kachin.pl <rwkc-file> <mykc-file>
# e.g.  $ ./print-common-kachin.pl ./all.rwkc.clean ./all.mykc.clean > out

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $FILE1,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
my %pair1;

while (my $line = <$FILE1>)
{
    # lc is the function for lower case conversion
    # ဒီဟာကို သုံးခဲ့တာက kc-rw ရဲ့ကချင်စာမှာ ထိပ်ဆုံး စာလုံးတွေကို capital လုပ်ထားလို့
    chomp($line); my $lowerLine = lc $line;
    my ($left, $right) = split ("\t", $lowerLine);
    $pair1{$right}=$left;
}
close($FILE1);

# if you want to see pair1 hash ...
#while ( (my $k, my $v) = each %pair1 ) {
#    print "$k => $v\n";
#}
#print("==========");

open (my $FILE2,"<:encoding(utf8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";
my %pair2;

while (my $line = <$FILE2>)
{
    chomp($line); my $lowerLine = lc $line;
    my ($left, $right) = split ("\t", $lowerLine);
    $pair2{$right}=$left;
}
close($FILE2);

# if you want to see pair2 hash ...
#while ( (my $k, my $v) = each %pair2 ) {
#    print "$k => $v\n";
#}

foreach (keys %pair1) {
    if (exists($pair2{$_}))
    {
        print ("$_\t$pair1{$_}\t$pair2{$_}\n");
    }
}

