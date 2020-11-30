#!/bin/bash

# text to ASL (American Sign Language) and BSL (British Sign Language) fingerspelling image conversion
# written by Ye Kyaw Thu, LST, Thailand
# Last updated: 1 Dec 2020
#
# How to run: ./txt2ASL-BSL.sh <filename>
# e.g. ./txt2ASL-BSL.sh ./head.out
# I used two finger spelling fonts names "Fingerspelling" for ASL and
# "BSL Right Hand" for BSL
# *** Note: Both of the fonts are free for personal use and noncommercial ...

filename=$1;
n=1

while read line; do

# reading each line of the input file
   echo "txt2ASL-BSL conversion for line no. $n : $line"
   convert -pointsize 125 -font "Fingerspelling"  -define pango:justify=true pango:$line $line-asl.png
   convert -pointsize 125 -font "BSL Right Hand"  -define pango:justify=true pango:$line $line-bsl.png
   n=$((n+1))

done < $filename

# An example of tiling output images with labels
montage thumb-asl.png thumb-bsl.png index-asl.png index-bsl.png middle-asl.png middle-bsl.png \
ring-asl.png ring-bsl.png pinky-asl.png pinky-bsl.png fingernail-asl.png  fingernail-bsl.png \
knuckles-asl.png knuckles-bsl.png wrist-asl.png wrist-bsl.png palm-asl.png palm-bsl.png  \
fist-asl.png fist-bsl.png \
-border 5 -tile x10 -geometry +2+2   -pointsize 30 -set label '%f (%wx%h)' montage_asl.png
