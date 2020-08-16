#!/bin/bash

# converting .mp4 video file to audio only .wav file
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# How to run: ./mp4-to-wav.sh <video-filename-with-mp4>
# e.g. 

audioFilename="${1%.*}"
#ffmpeg -i ./dawsu-election-1.mp4 -q:a 0 -map a dawsu-election-1.mp3
ffmpeg -i $1 -q:a 0 -map a $audioFilename.mp3

#ffmpeg -i ./dawsu-election-1.mp3 ./dawsu-election-1.wav
ffmpeg -i $audioFilename.mp3 $audioFilename.wav

