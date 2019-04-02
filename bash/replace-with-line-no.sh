#!/bin/bash

# For searching old sentences with line no. and replace with edited sentences
# written by Ye, Visiting Professor, LST Lab., NECTEC, Thailand
#
# how to run: ./replace-with-line-no.sh <edited-filename> <original-filename>
# File format of edited file is as follows:
# line-number<TAB>original-sentence<TAB>edited-sentence
#  e.g. ./replace-with-line-no.sh ./4edit.txt ./ori.txt

while read line
do

   lineNo=$(echo "${line}" | awk -F$'\t' '{print $1}');
   originalText=$(echo "${line}" | awk -F$'\t' '{print $2}');
   editedText=$(echo -e "${line}" | awk -F$'\t' '{print $3}');

   echo "lineNo: $lineNo";
   echo "originalText: $originalText";
   echo "editedText: $editedText";

   sed -i "$lineNo s/$originalText/$editedText/" "$2";

done < $1
