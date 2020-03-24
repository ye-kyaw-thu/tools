#!/usr/bin/perl
use strict;
use warnings;
use utf8;

# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# decoding the encoded file with "encode-input.pl" perl script
# How to use: perl ./decode.pl <dictionary-file> <encoded-file>
# e.g. perl ./decode.pl ./dict.txt ./mypos.encode > ./mypos.decode
# e.g. perl ./decode.pl ./dict.txt ./1718.txt > ./1718.txt.decode
# e.g. perl ./decode.pl ./dict.txt ./4370.txt > ./4370.txt.decode

# Example encoded file: 4370.txt (i.e. extracted concodance of the word ID 4370)
#368 1713 68 539 4369 21 539 16 227 25 4370 4371 109 333 359 4372 33 75 1644 313 
#188 157 53 8 274 5056 603 401 514 169 4370 33 12 16 419 126 50 87 455 2856 145 9
#2 649 4 9669 15 169 391 1820 7832 8 9 4370 246 13 186 12 16 545 152 552 441 8315
#63 151 59 8 274 26 50 9 1166 1324 169 4370 4040 40 68 12 19 552 4847 846 9 623 1
#908 766 15 194 12 16 5103 4 59 50 315 4370 358 1490 68 34 59 5372 29 11317 11318

# Example decoded file:
#၁၃ ရှည် ရ တာ အားကျ လိုက် တာ ။ အစိုးရ ၏ ဖိတ်ခေါ် ကမ်းလှမ်း ချက် အရ လက်နက် ချအပ် ခဲ့ သော ပြောက်ကျား သူပုန်
#အာဏာ ၍ ကျောင်းသား များ အား ဩဝါဒ စကား ပြောကြား ပေး ရန် ဖိတ်ခေါ် ခဲ့ သည် ။ အများ က နိုင်ငံ ရေး သတ္တဝါ ပကတိ အဖြစ် ကို
#ယခု နေ့ တွင် သတင်းယူ နိုင် ရန် အတွက် နိုင်ငံခြား သတင်းထောက် များ ကို ဖိတ်ခေါ် မည် ဟု ကြေညာ သည် ။ နောက်ဆုံး ၌ “ ဗိုလ် လရောင်
#၃၀၀၀၀၀ တို့ ဂျပန် များ အား မြန်မာ နိုင်ငံ ကို ဝင်ရောက် သိမ်းပိုက် ရန် ဖိတ်ခေါ် သကဲ့သို့ ဖြစ် ရ သည် မှာ “ ဖက်ဆစ် စနစ် ကို လိုလား
#လေ့လာ သိရှိ နိုင် ပေ သည် ။ များမကြာမီ တွင် ဂျပန် နိုင်ငံ သို့ ဖိတ်ခေါ် ခြင်း ခံ ရ ပြီး ဂျပန် ဧကရာဇ် မှ တက်နေဝန်း ဂုဏ်ထူးဆောင်

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
 
open (dictFILE, "<:encoding(UTF-8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $line; my %wordDict;

# open dictionary file and keep as hash %wordDict
while ($line = <dictFILE>)
{
    chomp($line);
  my ($key, $val) = split (/,/, $line);
        $wordDict{$key}=$val;
}

close(dictFILE);

# for print out hash for checking ...
#while ( my ($key, $value) = each %wordDict ) {
#    print "$key,$value\n";
#}

my %revWordDict = reverse %wordDict;

open (iFILE, "<:encoding(UTF-8)", $ARGV[1]) or die "Couldn't open input file $ARGV[1]!, $!\n";

# read encoded input file of $ARGV[1] line by line and push into array @words
# encode all elements of the array @words by using the hash %wordDict and push into new array @sentence
# after that, print out that array @sentence
while ($line = <iFILE>)
{
    chomp($line);
    my @words=split(/ /, $line);
    my @sentence;
   foreach my $w (@words){
      if (exists($revWordDict{$w})){
         push @sentence, $revWordDict{$w};
      }
   }
   print("@sentence\n");
}
close(iFILE);
