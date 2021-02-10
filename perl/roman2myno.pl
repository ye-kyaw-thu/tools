#!/usr/bin/env perl

# converting Roman numbers to Burmese numbers
# Ye Kyaw Thu, LST, NECTEC, Thailand
#
# I code this perl script for my stress release ...
# e.g. $ perl ./roman2myno.pl < roman.txt
# or
# e.g. $ echo -e "I\nII\nMMXXI" | perl ./roman2myno.pl
# Ref: https://en.wikipedia.org/wiki/Roman_numerals

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# တိုက်စစ်ရမယ့် အစီအစဉ်အတိုင်း တန်ဖိုး ကြီးစဉ်ငယ်လိုက် စီထားတယ်
my @roman = ("M:1000", "CM:900", 
   "D:500", "CD:400",
   "C:100", "XC:90",
   "L:50", "XL:40",
   "X:10", "IX:9",
   "V:5", "IV:4", "I:1");
   	           
# <STDIN> ကို သုံးထားတာမို့ input data ကို ဖိုင်ကနေလည်း ဖတ်ခိုင်းလို့ ရသလို standard input အနေနဲ့လည်း (ဥပမာ pipe နဲ့ လက်ဆင့်ကမ်းတာမျိုး) pass လုပ်ပေးလို့ ရပါတယ်။  
foreach my $line ( <STDIN> ) {
   chomp($line); my $inputRo = $line;
   my $bamarNo=0;

   # $line က space တွေပဲ ရှိတာမျိုး မဟုတ်မှ (i.e. not empty line) 
   if ($line !~ /^\s*$/) {
   
      foreach my $roPair (@roman) {
         my ($ro, $value) = split(":", $roPair);
         #roman array ထဲမှာရှိတဲ့ အစီအစဉ်အတိုင်းပဲ RE နဲ့ တိုက်စစ်ပါတယ် (i.e. M, CM, D, CD...)
         # $line =~ s/^$ro//i; ဆိုပြီး ^ ကိုသုံးထားတာကြောင့် ဖိုင် (သို့) STDIN က 
         # ဝင်လာတဲ့ စာကြောင်းရဲ့ ထိပ်ဆုံးပိုင်းကနေ $ro နဲ့ (e.g. M?, CM?, CM?) တူသလားလို့ စစ်ပြီး တူရင် အဲဒီတူတဲ့ အပိုင်းကို $line မှာဖျက်ပစ်မယ်။
         # တူတဲ့ key ရဲ့ value (i.e. 1000, 900, 500 etc.) ကို $bamarNo မှာ ဝင်ပေါင်းမယ်
         # RE မှာ နောက်ဆုံးက i က စာလုံး အကြီးအသေးကို ဂရုမစိုက်ဖူး (i.e. case-insensitive) လို့ သတ်မှတ်ပေးထားတာ
         $bamarNo += $value while $line =~ s/^$ro//i;
      }
      # convert English numbers to Burmese numbers
      # tr ကို သုံးပြထားပါတယ်။ 0 ကို ၀ နဲ့အစားထိုး။ 1 ကို ၁ နဲ့အစားထိုး စသည်ဖြင့်...
      $bamarNo =~ tr/0123456789/၀၁၂၃၄၅၆၇၈၉/;
   
      # ဥပမာအနေနဲ့ ရေးပြထားတာမို့ နားလည်ရလွယ်အောင် input လုပ်ပေးလိုက်တဲ့ Roman number တွေနဲ့အတူတွဲပြမယ်
      print "$inputRo = $bamarNo\n";
   }
}


