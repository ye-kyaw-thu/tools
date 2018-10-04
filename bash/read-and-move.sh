#!/bin/bash

# read filenames from a file and then move them to a folder
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# Date: 4 Oct 2018 
# How to use: ./read-and-move.sh <input-file> <folder-name>
# e.g. ./read-and-move.sh ./filename.txt ./tmp/ 

cat $1 | while read -r filename
do
   printf "moving $filename to $2\n"
   mv $filename ./$2/
   
done
