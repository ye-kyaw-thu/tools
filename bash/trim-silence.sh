#!/bin/bash

# for trimming silence from beginning and end of wavefile
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
#
# If you don't have "sox" command, install with "sudo apt-get install sox"
#Reference: man page for the silence filter
#Reference: https://digitalcardboard.com/blog/2009/08/25/the-sox-of-silence/#comment-111698
#Reference: https://stackoverflow.com/questions/41273701/stripping-silence-with-sox/49826050
#
# How to run: bash ./trim-silence.sh <foldername>
# e.g. bash ./trim-silence.sh ./wave4trim/

for wavfile in $1/*.wav
do
   echo "trim silence for $wavfile";
   # Here 1 = silence parameter, 0.1 = duration, 1% = 1% volume
   # And thus, trim silence (anything less than 1% volume) until we encounter sound lasting more than 0.1
   sox $wavfile $1/temp.wav silence 1 0.1 1% reverse;

   # removed ".wav" file extension
   trimwav=$(basename "$wavfile" .wav);

   echo "trimmed filename: $trimwav.trim.wav";
   # "temp.wav" ဖိုင်က အစပိုင်းမှာရှိနေတဲ့ silence တွေကို ဖြတ်ထုတ်ထားပြီးတော့ reverse လုပ်ထားတဲ့ output file ပါ။
   # အောက်ပါ command ကတော့ အစပိုင်း silence တွေကို ဖြတ်ထုတ်ပြီးတော့ ပြန် reverse လုပ်ပေးမယ်
   # (တကယ်က အော်ရဂျင်နယ်ဖိုင်ရဲ့ နောက်ဆုံးမှာ ရှိနေတဲ့ silence part ပါ 
   # အထက်က command မှာ reverse လုပ်ခဲ့လို့သာ ရှေ့ပိုင်းကို ရောက်နေတာပါ) 
   sox $1/temp.wav $1/$trimwav.trim.wav silence 1 0.1 1% reverse;
done

# temp သုံးထားတဲ့ ဖိုင်ကို ဖျက်တာ
rm $1/temp.wav;

