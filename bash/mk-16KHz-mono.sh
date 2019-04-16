#!/bin/bash

# Changing wave files into 16khz and mono
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan

for fd in */ ; do

   cd ./$fd;
   
   for file in *; do
      filename_only="${file%.*}"
      sox ./$file -b 16 -r 16k -c 1 ./$filename_only.16khz.mono.wav;
      soxi ./$filename_only.16khz.mono.wav;
   done
   
   cd ..;

done

