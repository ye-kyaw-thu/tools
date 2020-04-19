#!/bin/bash

# calculating length of string for field1, field2 and field3
# Written by Ye, LST Lab., NECTEC, Thailand
#
# How to run. ./chk-field-length.sh <3column-input-file> <option -avg >
# ./chk-field-length.sh ./en-th-my -avg
# ./chk-field-length.sh ./en-th-my

filename=$1;

if [ "$#" -ne 2 ] then
   awk -F "\t" ' { col1=length($1); col2=length($2); col3=length($3); len1+=col1; len2+=col2; len3+=col3; avg1=len1/NR; avg2=len2/NR; avg3=len3/NR; printf("%-5s\t%d, %d, %d\n", NR, col1, col2, col3);}' $filename
elif [ $2 == '-avg' ] then
   awk -F "\t" ' { col1=length($1); col2=length($2); col3=length($3); len1+=col1; len2+=col2; len3+=col3; avg1=len1/NR; avg2=len2/NR; avg3=len3/NR;}
END {printf("%-5s\t%d, %d, %d\n", NR, avg1, avg2, avg3);} ' $filename
fi

