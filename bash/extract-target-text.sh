#!/bin/bash
# for extracting translated output only from the moses MT engine osm output
# written by Ye, LST, NECTEC  Thailand
# Date: 8 Sept 2020
# How to run: ./extract-target-text.sh <filename>
# e.g. 

# အရင်ဆုံး sed command နဲ့ "|||" တွေကို "/" နဲ့ အစားထိုးတယ်
# field no. 2 ကို delimiter "/" ထားဆွဲထုတ်ယူ
# ပြီးတော့မှ sed နဲ့ပဲ "|" နဲ့စ သူ့နောက်မှာ digit တစ်လုံးနဲ့အထက်, dash, digit တစ်လုံးနဲ့အထက်, "|" နဲ့ ဆုံးတာကို ဖျက်တယ် 
sed 's/|||/\//g' ./$1 \
| cut -f2 -d"/" \
| sed 's/|[[:digit:]]\+-[[:digit:]]\+|//g'
