#!/bin/bash

# if "1st column of file1" is equal to "1st column of file2",
# print out some fields from both file1 and file2
# written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
#
# How to run: ./print-same-col1.sh <file1> <file2>
#e.g. ./print-same-col1.sh final.common.my-dw.sort final.common.my-rk.sort > rk-dw
# output example:
#ကစားနေတဲ့ခွေးတွေ။	ကစားနေ တဲ့ ခွေ းတွေ ။	ကဇတ် နီ ရေ ခွီး တိ ။	ကစားနေ ဟှို ခွီး လေ ။
#ကစားမယ်စိတ်ကူးနေတာ။	ကစား မယ် စိတ်ကူး နေတာ ။	ကဇတ် ဖို့  စိတ်ကူး နီစွာ ။	ကစား ဟှို့ စိကူး နေဇာ ။
#ကတိပေးဖို့ဝန်လေးနေလား။	ကတိ ပေး ဖို့ ဝန်လေး နေလား ။	ကတိ  ပီး ဖို့ ဝန်လေး   နီလား ။	ကတိ ပေး ဟှို ဝန်လေး ဇလား ။

# assign field-1 of file 1 into file1col1, assign field-3 into dw
# if field1 of file2 equal to field-1 of file1, print the whole sentence of file 2 and follow by dw[$1]
awk -F'\t' 'NR==FNR{file1col1[$1]=$1;dw[$1]=$3;next}; ($1==file1col1[$1]){print $0"\t"dw[$1]}' $1 $2

