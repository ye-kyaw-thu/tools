#!/bin/bash

# substitute string on specified line number
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# How to run: ./replace-with-lineno.sh <lineno-tab-string filename> <old filename>
# e.g. ./replace-with-lineno.sh ./patchfile ./oldfile

# Note: if your line contained "/" character, you will get an error!
# စာကြောင်းတွေမှာ "/" ကို သုံးထားရင် ဒီ shell script က အလုပ်လုပ်မှာ မဟုတ်ဘူး ။ အောက်ပါ ဥပမာလို စာကြောင်းမျိုး ...
# 70	တစ်/tn လ/n လောက်/part ပါ/part ပဲ/part ။/punc
# 114	မနက်/n ခုနှစ်/tn နာရီ/n မှာ/ppm နှိုး/v ပေး/part ပါ/part ။/punc
# Reason: s/x/x/ pattern

file=$1;

while IFS= read -r line
do

   line_no=${line%$'\t'*};
   string=${line#*$'\t'};
   #echo "line_no: $line_no";
   #echo "string: $string";

   sed -i "${line_no} s/.*/${string}/" $2;

done < $file;

