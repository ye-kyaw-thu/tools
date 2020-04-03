#!/bin/bash

# Very basic language model building with SRILM toolkit for Myanamr students
# SRILM link: http://www.speech.sri.com/projects/srilm/
# Before running this bash shell script, you have to install SRILM on your computer
# Ref link: http://idiom.ucsd.edu/~rlevy/teaching/2015winter/lign165/lectures/lecture13/lecture13_ngrams_with_SRILM.pdf
#
# Written by Ye, LST Lab., NECTEC, Thailand
# Last updated: April 3 2020
# How to run: ./lm-building-exec.sh <corpus-filename> <test-filename>
# e.g. ./lm-building-exec.sh ./my-corpus.txt ./my-test.txt > lm-building-exec.log

# Count Ngram
echo "#count ngram, here -order 2, 2-gram ...";
/home/lar/tool/srilm/bin/i686-m64/ngram-count -text $1 -order 2 -write $1.count;

# check the count file
echo "#checking the count file ..."
cat $1.count;
echo -e "==========\n";

# LM building
# -addsmooth 0 ကို သုံးထားတာက demo run ပြတဲ့ corpus က သေးလွန်းလို့
# တကယ်တမ်းက smoothing technique နဲ့ LM က တွဲသုံးမှ အဆင်ပြေလိမ့်မယ်
echo "#language model building ...";
/home/lar/tool/srilm/bin/i686-m64/ngram-count -text $1 -order 2 -addsmooth 0 -lm $1.lm;

# Check the language model file
echo "#checking the language model file ...";
cat ./$1.lm;
echo -e "==========\n";

# Calc perplexity
echo "#calculating the model perplexity ...";
/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./$1.lm -ppl $2
echo -e "==========\n";

# Converting ARPA format into Binary
echo " Converting ARPA format into Binary ...";
/home/lar/tool/srilm/bin/i686-m64/ngram -order 2 -lm ./$1.lm -write-bin-lm ./$1.lm.bin
ls $1.lm.bin

# Calc perplexity with binary LM
echo "#calculating the binary language model perplexity ...";
/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./$1.lm.bin -ppl $2
echo -e "==========\n";

# Use debug option
# စာကြောင်း တစ်ကြောင်းချင်းစီကို perplexity တွက်ပေးနိုင်တဲ့ option ပါ
# လက်တွေ့မှာက binary LM ကို သုံးကြပေမဲ့ ARPA LM နဲ့လည်း -debug option ကို သုံးနိုင်
echo "#calculating the language model perplexity with -debug option...";
/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./$1.lm.bin -ppl $2 -debug 2

