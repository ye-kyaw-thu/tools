#!/usr/bin/env perl

# Syntax Tree to sentence conversion
# Input: (S The/DT first/JJ keepresentations/NNS must/MD (VP (V be/VB)) (VP (V included/VBN)) (P by/IN) minders/NNS ./.)
# Output: We want to express our thanks on the good , the party 's fair .
#
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 6 April 2021
# One of the scripts for preparing "WAT2021 Myanmar-English Share Task" participation
# e.g. $ perl bracket-tree2sentence.pl <input-file>

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    # blank line, space ပဲ ပါတဲ့ စာကြောင်းတွေ မဟုတ်မှ...
    if (($line ne '') & ($line !~ /^ *$/)) {
        # \n ကို ဖြုတ်တယ်။ 
        chomp($line);
        my $sentence="";
        
        # ဝင်လာတဲ့ စာကြောင်းကို space နဲ့ segmentation ဖြတ်ချပြီး word ဆိုတဲ့ array ထဲကို ထည့်သိမ်းတယ်
        my @word = split(" ", $line);
        #print("@word\n");
        
        # word array တစ်ခုလုံးကို looping ပတ်ပြီး၊ array element တစ်ခုချင်းစီကို token ဆိုတဲ့ variable ထဲကို ထည့်သိမ်းပြီး အဲဒီ စာလုံး တစ်လုံးချင်းစီကို ကိုယ်လိုချင်တဲ့ ပုံစံပြောင်းမှာ...
        foreach my $token (@word) {
            # token variable ရဲ့ string မှာ / (slash) ပါတဲ့ စာလုံးတွေဖြစ်မှပဲ if condition အထဲကို ဝင်လိမ့်မယ်၊ ဆက် အလုပ်လုပ်မယ်...
            if ($token =~ /\//) {
                # forward slash ပါတဲ့ token ကိုမှ split function နဲ့ နှစ်ပိုင်းခွဲမယ်
                # slash ရဲ့ ဘယ်ဘက်က အပိုင်းက sub_token1 variable ထဲမှာ သိမ်းမယ်။ slash ရဲ့ ညာဘက်က အပိုင်းကို sub_token2 variabler ထဲမှာ သိမ်းမယ်။
                my($sub_token1, $sub_token2) = split("/", $token);
                # sub_token1 စာလုံးတွေ (i.e. normal English word) ကိုပဲ space ခြားပြီး sentence variable ထဲကို ပေါင်းထည့်ပြီး စာကြောင်းအဖြစ်နဲ့ သိမ်းမယ်။
                $sentence=$sentence." ".$sub_token1;
            }
        }
        # print မထုတ်ခင်မှာ စာကြောင်းရဲ့ ရှေ့ဆုံးမှာ၊ နောက်ဆုံးမှာ မလိုအပ်ပဲ ရှိနေနိုင်တဲ့ space တွေကို RE နဲ့ cleaning လုပ်တာ...
        $sentence=~ s/^\s+|\s+$//g;
        print "$sentence\n";
    }
}

close ($inputFILE);

