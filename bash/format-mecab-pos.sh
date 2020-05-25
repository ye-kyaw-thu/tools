#!/bin/bash
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# Written for changing output of mecab
# Last updated: 25 May 2020
# How to run: ./format-mecab-pos.sh <-pos|-subpos> <Japanese-text-filename>
# ./format-mecab-pos.sh subpos ./jp.test.txt
# ./format-mecab-pos.sh pos ./jp.test.txt

if [[ $1 == "-subpos" ]]; then
   cat $2 |\
   mecab |\
   cut -f1,2 -d"," |\
   sed 's/\t/\//; s/,/_/;' |\
   perl -pe 's/\n/ /g; s/EOS/\n/g;' |\
   awk '!/^\s*$/ {print NR, $0}' |\
   sed 's/ \+/ /g; s/^ $//;';
elif [[ $1 == "-pos" ]]; then
   cat $2 |\
   mecab |\
   cut -f1 -d"," |\
   sed 's/\t/\//' |\
   perl -pe 's/\n/ /g; s/EOS/\n/g;' |\
   awk '!/^\s*$/ {print NR, $0}' |\
   sed 's/ \+/ /g; s/^ $//;';
fi
