#!/usr/bin/perl
#use strict;

# last updated 19 Nov 2017
# ye@OPU
# for taging speaker ID

open (iFILE, $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!";

my $sentNo=1;

foreach $line(<iFILE>)
{

    chomp($line);
    print "$line (ye_$sentNo)\n";
    $sentNo = $sentNo+1;
}

close(iFILE);
