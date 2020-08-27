#!/bin/bash

# for continuous recording with rec command
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Press ctrl+c to stop the reording
# How to run ./rec-recorder.sh

i=1;
while :
do

   read -p "Press enter when you're ready to record:" startREC
   if [ -z $startREC ]; then
     rec --channels=1 --bits=16 --rate=16000 audio$i.wav
   fi

   ((i=i+1));

done
