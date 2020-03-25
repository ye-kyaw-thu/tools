#!/usr/bin/perl
use strict;
use warnings;
use utf8;

# for conversion of "one-to-many" Romanized file to 
# "one-to-one" Romanized file based on the highest frequency of Romanized syllable
#
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# Last updated: 26 Mar 2020
# How to run: perl ./mk-one2one-freq.pl <Myanmar-Romanized-file> <Myanmar> 
# Note: Both Myanmar and Romanized sentences are syllable segmented.
# e.g. perl ./mk-one2one-freq.pl ./one-to-many ./one-to-many.f1.uniq > out

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
 
open (iFILE1, "<:encoding(UTF-8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $line; my %sylDict; my %romanDict;
my @lsyl=(); my @rsyl=();
while ($line = <iFILE1>)
{
   chomp($line);
   my ($left, $right) = split(/\t/, $line);
   @lsyl = split(/ /, $left); @rsyl = split(/ /, $right);
   my @pair;
   if (scalar(@lsyl) eq scalar(@rsyl)) {
      for (my $i=0; $i<@lsyl; $i++) {
         push(@pair, $lsyl[$i]."/".$rsyl[$i]);
      }
   }
   #print ("@pair\n");
   foreach my $sylPair (@pair){
      if (exists($sylDict{$sylPair}))
      {
         $sylDict{$sylPair}++;
      } else {
         $sylDict{$sylPair}=1;
      }
  }
}
close(iFILE1);

open (dictFILE1, ">:encoding(UTF-8)", "sylDict.sort.txt") or die "Couldn't open output file sylDict.sort.txt!, $!\n";

# sort by key and print the sylDict hash
# Note: all possible romanizations are containing
foreach my $key (sort keys %sylDict){
   print dictFILE1 "$key, $sylDict{$key}\n";
}
close(dictFILE1);

# loop %sylDict hash and 
# create a new hash only contained the highest freq romanization
my %highestFreq;
while ( my ($key, $value) = each %sylDict ) {
  my($mySyl, $Roman) = split("/", $key);
   if (exists($highestFreq{$mySyl}))
   {
      my ($roman, $freq) = split(/_/, $highestFreq{$mySyl});
      if($value > $freq){
         $highestFreq{$mySyl}=$Roman."_".$value;
      }
   } else {
      $highestFreq{$mySyl}=$Roman."_".$value;
   }
}

open (dictFILE2, ">:encoding(UTF-8)", "sylDict.sort.freq.txt") or die "Couldn't open output file sylDict.sort.freq.txt!, $!\n";

#write the syllable and the highest frequency romanized syllable dictionary to a file
foreach my $key (sort keys %highestFreq){
   print dictFILE2 "$key, $highestFreq{$key}\n";
}
close(dictFILE2);

open (iFILE2, "<:encoding(UTF-8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";

while ($line = <iFILE2>)
{
    chomp($line);
    my @syllables=split(/ /, $line);
    my @sentence;
   foreach my $s (@syllables){
      if (exists($highestFreq{$s})){
         my ($ro, $frq) = split(/_/, $highestFreq{$s});
         push @sentence, $ro;
      }
   }
   print("@sentence\n");
}
close(iFILE2);
