#!/bin/bash

# substitute string on specified line number
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# How to run: ./replace-with-lineno.sh <lineno-tab-string filename> <old filename>
# e.g. ./replace-with-lineno.sh ./patchfile ./oldfile

file=$1;

while IFS= read -r line
do

   line_no=${line%$'\t'*};
   string=${line#*$'\t'};
   #echo "line_no: $line_no";
   #echo "string: $string";

   sed -i "${line_no} s/.*/${string}/" $2;

done < $file;

