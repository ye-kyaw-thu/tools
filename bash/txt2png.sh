#!/bin/bash

# converting Myanmar text from the input file into PNG file
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# How to run: txt2png.sh <input-filename> <font-name>
# e.g. ./txt2png.sh ./input.txt Myanmar3
# ./txt2png.sh ./input.txt Padauk
# ./txt2png.sh ./input.txt Pyidaungsu

FILENAME=$1;
FONT=$2;
convert -font $FONT -pointsize 36 -encoding Unicode "pango:@$FILENAME" output.png

