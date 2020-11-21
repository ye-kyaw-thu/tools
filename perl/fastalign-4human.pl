#!/usr/bin/env perl

# converting alignment output file of fastalign to human readable text
# Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 20 Nov 2020
#
# Example input file formats for your reference:
# 1) <aligned-fastaling-output-filename>
# $ head -3 train.myrk.fast_align 
# 0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8 9-9 10-10 11-11 12-12 13-13
# 0-0 1-1 5-3 6-6 7-7 8-8 9-10 10-9 11-11
# 0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8 9-9 10-10
#
# 2) <input-source-target-parallel-filename>
# $ head -3 train.myrk
# မင်း အဲ့ ဒါ ကို အ ခြား တစ် ခု နဲ့ မ ချိတ် ဘူး လား ။ ||| မင်း ယင်း ချင့် ကို အ ခြား တစ် ခု နန့် မ ချိတ် ပါ လား ။
# သူ မ ဘယ် သူ့ ကို မှ မ မှတ် မိ တော့ ဘူး ။ ||| ထို မ ချေ တစ် ယောက် လေ့ မ မှတ် မိ ပါ ယာ ။
# အဲ့ ဒါ ကျွန် တော် တို့ အ တွက် ခက် ခဲ တယ် ။ ||| ယင်း ချင့် ကျွန် တော် ရို့ အ တွက် ခက် ခ ရေ ။
#
# How to run:
# $ perl fastalign-4human.pl <aligned-fastaling-output-filename> <input-source-target-parallel-filename>
# e.g. $ perl ./fastalign-4human.pl ./train.myrk.fast_align ./train.myrk

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $alignmentFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
open (my $parallelFILE,"<:encoding(utf8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";
#my $lineAlign; my $lineParallel;

# ဒီ while loop နေရာမှာ defined မထည့်ရင် perl version အဟောင်းတွေမှာ အောက်ပါလိုမျိုး error ပေးတယ်
# Value of <HANDLE> construct can be "0"; test with defined() at ./fastalign-4human.pl line 34.
# ဖတ်တဲ့ စာကြောင်းထဲမှာ zero ပါနေရင် while loop က ရပ်သွားနိုင်လို့ warning ပေးတာ
# reference: http://computer-programming-forum.com/53-perl/2ee49a64d5f4cce7.htm
while( defined(my $lineAlign = <$alignmentFILE>) and defined(my $lineParallel = <$parallelFILE>)){

   # for debugging
   #print("line align: $lineAlign"); print("line parallel: $lineParallel\n");
   # split aligned line by space and put into an array
   my @alignedPair = split(" ", $lineAlign); #print("Aligned Pair: @alignedPair\n");
   # split parallel line by the delimiter "<space>|||<space>" and put into $sourceLine and $targetLine variables
   my ($sourceLine, $targetLine) = split(/ \|\|\| /, $lineParallel); #print("$sourceLine:$targetLine\n");
   # split word by word from $sourceLine and $targetLine and put into arrays
   my @src = split(" ", $sourceLine); my @trg = split(" ", $targetLine); #print("source: @src\n"); print("target: @trg\n");
   my $printLine = "";

   foreach (@alignedPair) {
      my ($sourceWord, $targetWord) = split("-", $_);
      $printLine = $printLine.$src[$sourceWord]."-".$trg[$targetWord]." ";
   } 
   $printLine =~ s/\s$//;
   print($printLine."\n");
}

close ($alignmentFILE);

