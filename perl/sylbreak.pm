#!/usr/bin/perl

## syllable breaking perl module for Myanmar language Unicode Text
## Refer: https://github.com/ye-kyaw-thu/sylbreak
## last updated: 28 June 2020
## Author: Ye Kyaw Thu, Visiting Researcher, LST, NECTEC, Thailand
## Reference of Myanmar Unicode: http://unicode.org/charts/PDF/U1000.pdf

# ဥပမာ အနေနဲ့ ဆောက်ပြထားတဲ့ sylbreak လို့ နာမည်ပေးထားတဲ့
# perl module ကိုသုံးလို့ ရဖို့အတွက် package declaration လုပ်ထားတဲ့လိုင်းပါ
package sylbreak;

use strict;
use warnings;
use utf8;

# $otherChar နေရာမှာ ကိုယ်ထပ်ဖြည့်ချင်တဲ့ စာလုံးတွေ၊ သင်္ကေတတွေကို ထပ်ဖြည့်နိုင်ပါတယ်
my $myConsonant = "က-အ";
my $enChar = "a-zA-Z0-9";
my $otherChar = "ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-\/:-\@\[-`{-~\\s";
my $ssSymbol = "္";
my $aThat = "်";

# output: syllable breaked Myanmar sentence
# ဒီ subroutine ကတော့ input ဝင်လာတဲ့ စာကြောင်းရဲ့ နဂိုရှိနေတဲ့ word boundary ကို
# မစဉ်းစားပဲ syllable တွေအဖြစ်ပဲ ဖြတ်ပေးမှာ ဖြစ်ပါတယ်
sub syllable {
   my $line = $_[0];
   my $sep = $_[1];
   chomp $line;
   $line =~ s/ //g;

      #Regular expression pattern for Myanmar syllable breaking
      #*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
   $line =~ s/((?<!$ssSymbol)[$myConsonant](?![$aThat$ssSymbol])|[$enChar$otherChar])/$sep$1/g;
   $line =~ s/^_//;
   return $line;

}

# output: not only syllable breaking but also keeping the original word or phrase boundary Myanmar sentence
# ဒီ subroutine ကတော့ input ဝင်လာတဲ့ စာကြောင်းရဲ့ နဂိုရှိနေတဲ့ word boundary (သို့) 
# phrase boundary တွေကို မဖျက်ပဲ syllable breaking လုပ်ပေးမှာ ဖြစ်ပါတယ်
sub syllableWord {
   my $sylLine="";
   chomp $_[0]; # remove \n
   my @line = split(' ', $_[0]);
   my $sep = $_[1];

   foreach (@line) {

   # ဒီလိုင်းက syllable breaking လုပ်ပေးတဲ့ regular expression (RE) ပါ
   $_ =~ s/((?<!$ssSymbol)[$myConsonant](?![$aThat$ssSymbol])|[$enChar$otherChar])/$sep$1/g;
   # syllable break လုပ်ပြီးတော့ ရလာတဲ့ စာကြောင်း "$_" မှာက ရှေ့ဆုံးမှာလည်း
   # user ကပေးလိုက်တဲ့ syllable breaking delimiter symbol (e.g. "|", "_") တိုက ရှိနေမှာမို့
   # အဲဒီထိပ်ဆုံးက delimiter symbol ကို ဖျက်တဲ့ RE ပါ
   $_ =~ s/^_//;

   # space ခံပြီး စာလုံးတွေကို တွဲခိုင်းထားတဲ့ line ပါ
   $sylLine = $sylLine." ".$_;
   }
   # စာကြောင်းရဲ့ ရှေ့ဆုံးမှာ ရှိတဲ့ space ကို ဖျက်တဲ့ RE ပါ
   $sylLine =~ s/^ //;
   return $sylLine;
}

1;
