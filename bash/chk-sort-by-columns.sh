#!/bin/bash

# sorting based on columns 
# written by Ye Kyaw Thu, Researcher, Multilingual Translation Lab., NICT, Kyoto, Japan
# Date: 3 Feb 2013 
# How to use: ./chk-sort-by-columns.sh <input-file>
# e.g. ./chk-sort-by-columns.sh myg2p.ver1.txt.shuf.1k 

inputFile=$1;

# counting how many columns
column=$(head -n 1 $inputFile | awk -F"\t" '{print NF}');

# read the first line
firstLine=$(head -n 1 $inputFile);

echo "No. of columns: $column";

# checking the column value, I assumed all rows have equal data type
function chkIntegerOrFloat()
{
   #echo "inside: ${1}";
   if [[ ${1} =~ ^[+-]?[0-9]*$ ]] || [[ ${1} =~ ^[+-]?[0-9]+\.?[0-9]*$ ]];then
      #an integer or a float number case
      return 1;
   else
      #NOT an integer or a float number case
      return 0;
   fi
}

# looping based on number of columns
for i in $(seq 1 $column);
do

   field=$(echo "$firstLine" | cut -f$i -d $'\t');
   #echo $field; # for debugging 
   chkIntegerOrFloat $field;

   # getting return value of previous function
   # Here, $? is the exit status of the most recently executed foreground pipeline
   if [[ $? == 0 ]]; then
      sort -t$'\t' -k$i $inputFile > $inputFile.sorted-by-col$i;
   else
      # sorting with -n option (i.e. for integer or float values)
      sort -t$'\t' -k$i -n $inputFile > $inputFile.sorted-by-col$i;
   fi

   # confirmation by print out first 10 lines of outputfile
   echo -e "\nhead $inputFile.sorted-by-col$i:\n";
   head $inputFile.sorted-by-col$i;
   echo "==========";

done

