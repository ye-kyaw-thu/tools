#!/bin/bash

# Cleaning heading, trailing and double spaces
# Written by Ye Kyaw Thu, LSt Lab., NECTEC, Thailand
# Used for cleaning data of Ms. Honey Htun (YTU) before running SMT
# Last updated: 31 December 2019

# Note: you should prepare "clean-space.pl" file 
# under the same folder with this bash shell script
# Link: https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-space.pl

for folder in */ ;
do

    echo "Start working for $folder ...";

   # change directory to the working folder
   cd $folder;
   for file in ./*.{en,my};
   do
   
      echo "Space cleaning for $file ...";
      echo -e "head $file\n";
      head $file;
      echo "";

     # cleaning spaces
      perl ../clean-space.pl $file > $file.clean;

      echo -e "head $file.clean\n";
      head $file.clean;
      echo -e "==========\n";
      rm $file;
      mv $file.clean $file;
   done
   cd ..;

done
