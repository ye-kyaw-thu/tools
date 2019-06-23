#!/bin/bash

# 2nd time Grouping .mpg and .xgtf files of UCF YouTube Action Data Set
# *** This script should run after running "group-UCF11.sh".

# Written by Ye, Language Understanding Lab., Pyin Oo Lwin, Myanmar
# How to run: group-within-group-UCF11.sh ./UCF11/ 

#Example filenames of UCF-11 folder:
#v_walk_dog_25_04.mpg
#v_walk_dog_25_04.xgtf

cd $1;

for folder in biking diving golf juggle jumping riding shooting spiking swing tennis walk_dog;
#for folder in */; 
do
   cd $folder;
   pwd;
      for group in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25;
      do
         mkdir $group;
         for file in v_$folder\_$group\_*
         do
            echo "$file ./$group/";
            mv $file ./$group/;
         done
      done
   cd ..;
done

cd ..;

