#!/bin/bash

# for rename files based on folder names
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# How to use: ./change-filenames.sh

# looping all folders under current directory
for fd in */ ; do

   #initialize count value
   counter=0;

   cd ./$fd;
   echo -e "Rename files under folder $fd\n";
   
   # cutting last character of folder name (i.e. "/")
   classID="${fd::-1}" 
   for file in *; do

      counter=$[$counter +1]

      # filename changing: Here $classID is a foldername
      # spk2 is just prefix of the filename and you can update as you like
      echo "mv ./$file ./spk2-$classID-$counter.wav";
      mv ./$file ./spk2-$classID-$counter.wav;
   done
   
   cd ..;

done
