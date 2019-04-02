#!/bin/bash

# For searching old sentences with line no. and replace with edited sentences
# written by Ye, Visiting Professor, LST Lab., NECTEC, Thailand
#
# how to run: ./replace-with-line-no.sh <edited-filename> <original-filename>
# File format of edited file is as follows:
# line-number<TAB>original-sentence<TAB>edited-sentence
#  e.g. ./replace-with-line-no2.sh ./4edit.txt ./ori.txt

while read line
do

   # getting line no only and assigned to the variable lineNo
   lineNo=$(echo "${line}" | awk -F$'\t' '{print $1}');
   
   # getting original sentence and assigned to the variable originalText 
   originalText=$(echo "${line}" | awk -F$'\t' '{print $2}');
   
   # getting edited sentence and assigned to the variable editedText
   editedText=$(echo -e "${line}" | awk -F$'\t' '{print $3}');

   echo "lineNo: $lineNo";
   echo "originalText: $originalText";
   echo "editedText: $editedText";

   # sed command for search and replace with line number
   sed -i "$lineNo s/$originalText/$editedText/" "$2";

done < $1
