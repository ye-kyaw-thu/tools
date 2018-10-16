#!/bin/bash

# printing "ClassID" and "predicted results" from testing-log file
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# Last updated: 16 Oct 2018 
# How to use: ./print-classID-prediction-result.sh <log-filename>
# e.g. ./print-classID-prediction-result.sh ./ot-5person-200k.log | less -r
# e.g. ./print-classID-prediction-result.sh ./ot-5person-200k.log > classification-result

# grep: grep sentences that contained classID and predicted probability values
# sed: print the very frist line and print every 5th line from STDIN 
# cut: cut field no. 1, here -d" " is for delimiter "space" 
# split: print 36 lines per STDIN 
grep -P "^[0-9]{1,2} [0-9]\." $1 \
| sed -n -e '1~5p' \
| cut -f1 -d" " \
| split --numeric-suffixes=1 -l 36

COUNT=1;

for i in x*;do
   echo -e "Classification Result for Class-$COUNT:\n";

   # sort: make sorting in numerical order,
   # uniq: make unique and print the number of occurrences,
   # sed: remove leading spaces
   # awk: swaping column-1 and column-2 and print column-1 together with prefix "Class-"
   sort -n $i | uniq -c | sed 's/^ *//g' | awk '{printf("Class-%s\t%s\n", $2, $1)}';
   echo "";
   ((COUNT++))
done

# for removing splitted output files of input file (i.e. $1) such as x01, x02, x03 ... 
# if you want to see classification results for each class, comment out the following line
rm x*;
