#!/bin/bash

# for checking unsegmented sentences 
# written by Ye, NECTEC, Thailand
# How to run: ./segmentation.sh <filename that contained segmented and unsegmented sentences>
# e.g. ./segmentation.sh ./thai.txt

# read from $1 and make line array
readarray -t lines < $1;

for line in "${lines[@]}"; do

    # check the line contained "|" character
    if [[ $line == *"|"* ]]
    then
       echo "$line";
    else
       #echo ">> $line";
       # pass unsegmented $line to word segmentation program of Thai
       echo $line | python ./wordcut-test.py       
    fi

done
