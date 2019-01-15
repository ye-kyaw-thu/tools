#!/bin/bash

# for preparing open-test data
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan

for fd in */ ; do
   
   # cutting last character of folder name (i.e. "/")
   classID="${fd::-1}"

   # list all files, shuffle and only get 31 files for test-set
   # you can change no. of files as you like
   mkdir -p /home/ka2pluskha2/exp/tl/flower-recognition/dataset/test/$classID 
   for file in $(find ./$fd -type f | shuf -n 31); do

      # echo running command
      echo "mv ./$file /home/ka2pluskha2/exp/tl/flower-recognition/dataset/test/$classID/";

      # move 31 files to test folder
      mv ./$file /home/ka2pluskha2/exp/tl/flower-recognition/dataset/test/$classID/ ;
   done
   
done
