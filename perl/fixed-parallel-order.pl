#!/usr/bin/env perl

# arrange unordered up/down line numbers into ordered parallel sentences
# Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# my dirty script ... however this script was really useful for corpus cleaning
# of our Myanmar-Kayahli parallel corpus
# e.g. $ perl fixed-parallel-order.pl <input-file>

# Input file example:
#   1041	တစ်ဆယ်။	  1041	ꤏꤛꤢꤩ ꤯
#  1042	ဆယ့်တစ်။	1042	ꤏꤛꤢꤩꤒꤣ꤬ ꤯
#  1043	ဆယ့်နှစ်။	1044	ဆယ့်သုံး။
#  1044	ꤏꤛꤢꤩ꤭ꤞꤌꤣ꤭ ꤯	1045	ဆယ့်လေး။
#  1045	ꤏꤛꤢꤩꤜꤝꤟꤤ꤭ ꤯	1046	ဆယ့်ငါး။
#  1046	ꤏꤛꤢꤩꤑꤟꤢ꤭ ꤯	1047	ဆယ့်ခြောက်။
#  1047	ꤏꤛꤢꤩꤞꤌꤣ꤭ꤞꤛꤥ ꤯	  1048	ဆယ့်ခုနစ်။
#  1048	ꤏꤛꤢꤩꤔꤝꤥ ꤯	  1049	ဆယ့်ရှစ်။
#  1049	ꤏꤛꤢꤩꤜꤝꤟꤤ꤭ꤞꤛꤥ ꤯	  1050	ဆယ့်ကိုး။
#  1922	ကျွန်တော်ကလဲပြောရတာခပ်ပျင်းပျင်း၊တကယ်တော့ကျွန်တော်နဲ့လဲမဆိုင်ပါဘူး။	  1922	ꤠꤢ꤭ ꤞꤢꤧꤟꤢꤩꤔꤢꤪ ꤔꤟꤢ ꤒꤥ꤬ꤒꤥ꤬ . ꤟꤢꤩꤒꤟꤢ꤭ꤒꤟꤢ꤭꤮ ꤗꤢ꤬ ꤢ꤬ꤙꤢꤧ꤬ꤊꤛꤢ ꤔꤢ ꤠꤢ꤭ ꤒꤥ꤬ ꤯
#  1923	ခေတ်နဲ့အမီလိုက်တယ်။	  1923	ꤜꤟꤢꤦ꤬ ꤊꤌꤣ꤭ ꤖꤢꤨ ꤢ꤬ꤏꤛꤣꤋꤢꤧ꤭ ꤔꤌꤣ꤬ ꤯

# output example:
# 1041	တစ်ဆယ်။	1041	ꤏꤛꤢꤩ ꤯
# 1042	ဆယ့်တစ်။	1042	ꤏꤛꤢꤩꤒꤣ꤬ ꤯
# 1044	ဆယ့်သုံး။	1044	ꤏꤛꤢꤩ꤭ꤞꤌꤣ꤭ ꤯
# 1045	ဆယ့်လေး။	1045	ꤏꤛꤢꤩꤜꤝꤟꤤ꤭ ꤯
# 1046	ဆယ့်ငါး။	1046	ꤏꤛꤢꤩꤑꤟꤢ꤭ ꤯
# 1047	ဆယ့်ခြောက်။	1047	ꤏꤛꤢꤩꤞꤌꤣ꤭ꤞꤛꤥ ꤯
# 1048	ဆယ့်ခုနစ်။	1048	ꤏꤛꤢꤩꤔꤝꤥ ꤯
# 1049	ဆယ့်ရှစ်။	1049	ကျွန်တော်ကလဲပြောရတာခပ်ပျင်းပျင်း၊တကယ်တော့ကျွန်တော်နဲ့လဲမဆိုင်ပါဘူး။
# 1922	ကျွန်တော်ကလဲပြောရတာခပ်ပျင်းပျင်း၊တကယ်တော့ကျွန်တော်နဲ့လဲမဆိုင်ပါဘူး။	1922	ꤠꤢ꤭ ꤞꤢꤧꤟꤢꤩꤔꤢꤪ ꤔꤟꤢ ꤒꤥ꤬ꤒꤥ꤬ . ꤟꤢꤩꤒꤟꤢ꤭ꤒꤟꤢ꤭꤮ ꤗꤢ꤬ ꤢ꤬ꤙꤢꤧ꤬ꤊꤛꤢ ꤔꤢ ꤠꤢ꤭ ꤒꤥ꤬ ꤯
# 1923	ခေတ်နဲ့အမီလိုက်တယ်။	1923	ꤜꤟꤢꤦ꤬ ꤊꤌꤣ꤭ ꤖꤢꤨ ꤢ꤬ꤏꤛꤣꤋꤢꤧ꤭ ꤔꤌꤣ꤬ ꤯

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $keepNo; my $keepText;
my $alignOut;

while (!eof($inputFILE)) {
     
    my $line1 = <$inputFILE>;
    chomp($line1); 
    my ($no1, $left_L1, $no2, $right_L1) = split (/\t/, $line1);
    #print("==> $no1, $left_L1, $no2, $right_L1\n");
    $no1 =~ s/^\s+|\s+$//g; $no2 =~ s/^\s+|\s+$//g;
    $left_L1 =~ s/^\s+|\s+$//g; $right_L1 =~ s/^\s+|\s+$//g;
    $left_L1 =~ s/ +/ /g; $right_L1 =~ s/ +/ /g;
    my $no3; my $left_L2; my $no4; my $right_L2;

    if (!eof($inputFILE)) {
        my $line2 = <$inputFILE>; chomp($line2);
        ($no3, $left_L2, $no4, $right_L2) = split (/\t/, $line2);
        #print("==> $no3, $left_L2, $no4, $right_L2\n");
        $no3 =~ s/^\s+|\s+$//g; $no4 =~ s/^\s+|\s+$//g;
        $left_L2 =~ s/^\s+|\s+$//g; $right_L2 =~ s/^\s+|\s+$//g;
        $left_L2 =~ s/ +/ /g; $right_L2 =~ s/ +/ /g;
    } else {
        if ($alignOut == 0) {
            print("$no1\t$left_L1\t$no2\t$right_L1\n"); exit;
        }elsif ($alignOut ==1) {
            print("$keepNo\t$keepText\t$no1\t$left_L1\n"); exit;
        }
    }

    if (($no1 == $no2) and ($no3 == $no4)) {
        print("$no1\t$left_L1\t$no2\t$right_L1\n");
        print("$no3\t$left_L2\t$no4\t$right_L2\n");
        $keepNo=0; $keepText="";
        $alignOut=0;
    } elsif ($no1 != $no2)  {
         if ($no3 == $no4) {
            if ($no1 == $keepNo) {
                print("$keepNo\t$keepText\t$no1\t$left_L2\n");
             }
            print("$no3\t$left_L2\t$no4\t$right_L2\n");
            $alignOut=0;
         }elsif (($no2 == $no3) and ($alignOut == 0)) {
            print("$no2\t$right_L1\t$no3\t$left_L2\n");
            $keepNo=$no4; $keepText=$right_L2; $alignOut=1;
        } elsif (($no2 == $no3) and ($alignOut == 1)) {
            print("$keepNo\t$keepText\t$no1\t$left_L1\n");
            print("$no2\t$right_L1\t$no3\t$left_L2\n");
            $keepNo=$no4; $keepText=$right_L2;
        } elsif ($no1 == $keepNo) {
             print("$keepNo\t$keepText\t$no1\t$left_L1\n");
             if ($no3 == $no4) {
                 print("$no3\t$left_L2\t$no4\t$right_L2\n");
              } else {
                     $keepNo=$no4; $keepText=$right_L2;
                }
        }#else {
        #print("===> $no1\t$left_L1\t$no2\t$right_L1\n");
        #print("===> $no3\t$left_L2\t$no4\t$right_L2\n");
        #}
    } elsif (($no1 == $no2) and ($no3 != $no4)) {
            print("$no1\t$left_L1\t$no2\t$right_L1\n");
            $keepNo=$no4; $keepText=$right_L2; $alignOut=1;
     }
}

close ($inputFILE);
