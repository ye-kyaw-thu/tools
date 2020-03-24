#!/usr/bin/perl
use strict;
use warnings;
use utf8;

# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# for encoding Myanmar text file as word-ID file
# sometimes you might need to encode Myanmar text file
# for using existing English NLP library e.g. Python nltk services
# How to use:
# e.g. ./encode-input.pl <input-file> <output-dictionary-file> 
# perl ./encode-input.pl ./mypos.word.txt ./dict.txt > mypos.encode
# 
# Example dictionary file:
#သူစိမ်း,8964
#လောင်ကျွမ်း,13296
#ကွင်းကွင်းကွက်ကွက်,11925
#အထူးချွန်ဆုံး,8446
#အကယ်လို့,15059
#
# Example encoded file (e.g. mypos.encode)
#2 3 4 5 6 7 8 9 10 11 12 13 14 15 12 16
#17 18 19 20 21 22 16
#23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 28 29 38 39 40 32 33 25 16


binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
 
open (iFILE, "<:encoding(UTF-8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $line; my %wordDict;
my $wordID=1;

# read the input file of $ARGV[0] line by line, splitted words by space and push them into array @words
# Then, looping the array @words and add them into the hash named "%wordDict" 
# with together with their Word-ID 
while ($line = <iFILE>)
{
    chomp($line);
    my @words=split(/ /, $line);

   foreach my $w (@words){
      if (not exists($wordDict{$w}))
      {
         $wordID = $wordID+1;
         $wordDict{$w}=$wordID;
      } 
  }

}
close(iFILE);

open (dictFILE, ">:encoding(UTF-8)", $ARGV[1]) or die "Couldn't open output file $ARGV[0]!, $!\n";

# save the prepared hash %wordDict into a file (i.e. $ARGV[1])
while ( my ($key, $value) = each %wordDict ) {
    print dictFILE "$key,$value\n";
}
close(dictFILE);

open (iFILE, "<:encoding(UTF-8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

# open the input file $ARGV[0], read line by line, splitted as word array
#  and then, encoded word by word with prepared Word-ID hash %wordDict
while ($line = <iFILE>)
{
    chomp($line);
    my @words=split(/ /, $line);
    my @sentence;
   foreach my $w (@words){
      if (exists($wordDict{$w})){
         push @sentence, $wordDict{$w};
      }
   }
   print("@sentence\n");
}
close(iFILE);
