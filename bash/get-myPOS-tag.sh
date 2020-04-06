#!/bin/bash

# extracting myPOS tags
# myPOS link: https://github.com/ye-kyaw-thu/myPOS
# head -2 ./mypos.txt 
#ယခု/n လ/n တွင်/ppm ပျားရည်/n နှင့်/conj ပျားဖယောင်း/n များ/part ကို/ppm စုဆောင်း/v ကြ/part သည်/ppm ဟု/part ခန့်မှန်း/v နိုင်/part သည်/ppm ။/punc
#အခန်းခ/n ထဲ/ppm မှာ/ppm ထည့်/v လိုက်/part ပါ/part ။/punc

# Written by Ye, LST Lab., NECTEC, Thailand
# How to run: ./get-myPOS-tag.sh

cat ./mypos.txt | sed "s/ /\n/g" | cut -f2 -d "/" | sort | uniq -c | sort -k1 -nr > ./tag-freq
rev ./tag-freq | cut -f1 -d" " | rev > tag


