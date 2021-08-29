#!/bin/bash

# Chopping audio file by silence
# written by Ye Kyaw Thu
# How to run: bash ./chop-by-silence.sh <input-audio-filename>
# e.g. $ bash ./chop-by-silence.sh ./TheGuest-mono.wav

sox $1 split_num.wav silence 1 0.1 1% 1 0.1 1% : newfile : restart

