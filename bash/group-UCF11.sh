#!/bin/bash

# Grouping .mpg and .xgtf files based on action categories of UCF YouTube Action Data Set
# Written by Ye, Language Understanding Lab., Pyin Oo Lwin, Myanmar
# How to run: ./group-UCF11.sh ./UCF11/

#Example filenames of UCF-11 folder:
#v_walk_dog_25_04.mpg
#v_walk_dog_25_04.xgtf

cd $1;

for class in biking diving golf juggle jumping riding shooting spiking swing tennis walk_dog;
do
   mkdir $class;
   for file in *$class*;
   do
      echo "moving $file into class $class ...";
      mv $file ./$class/;
   done   
done

cd ..;
