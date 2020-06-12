#!/bin/bash

# drawing waveform from .wav files
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Note: you need ffmpeg command to run this bash shell script
# Last updated: 12 June 2020
# Reference: https://trac.ffmpeg.org/wiki/Waveform
#
# How to run: bash ./wav2wavform.sh <foldername>
# e.g. bash ./wav2wavform.sh ./wave4trim/

for wavfile in $1/*.wav
do
   echo "drawing waveform for $wavfile";
   trimwav=$(basename "$wavfile" .wav);
   ffmpeg -i $wavfile -filter_complex "showwavespic=s=640x120" -frames:v 1 $1/$trimwav.png
done
