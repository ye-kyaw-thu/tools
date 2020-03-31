#!/usr/bin/env perl

# for printing one syllable confusion pairs
# real confusion pair ထဲကနေမှ မြန်မာ syllable တစ်လုံးပဲ ပါတဲ့ confusion pair ကိုပဲ ဆွဲထုတ်ရန်
# Coded by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
#
# How to run: $ perl mk-one-syl-confusion.pl <syllable-segmented-confusion-pair-file>
# e.g. perl ./mk-one-syl-confusion.pl ./confusion.txt.syl
# e.g. input and running output:
# $ cat tst1
# ဆ်ု | ဆို
# ပီး | ပြီး
# ကိူ | ကို
# ပီး | ပြီး
# မန်း လေး | မန္တ လေး
# သ ဘက် ခါ | သန် ဘက် ခါ
# ဘိုလ် | ဘယ် လို
#$ perl ./mk-one-syl-confusion.pl ./tst1
#1:ဆ်ု|ဆို
#2:ပီး|ပြီး
#3:ကိူ|ကို
#4:ပီး|ပြီး
#7:ဘိုလ်|ဘယ် လို

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $confuFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
chomp(my @confuPair = <$confuFILE>);
close($confuFILE);
my $count=0;

foreach my $pair (@confuPair) {
   $count++;
   my ($wrong, $correct) = split (/\|/, $pair);

   # removing heading and trailing spaces
   $wrong =~ s/^\s+|\s+$//g; $correct =~ s/^\s+|\s+$//g;
   #print("$wrong, $correct\n");

   # if $wrong that does not contained space
   if ($wrong !~ /\s/) {
      print("$count:$wrong|$correct\n");
   }
}

