#!/bin/bash

# for getting average number of one column input file
# written by Ye Kyaw Thu
# How to use: ./calc-avg.sh <filename>

total=`cat $1 | wc -l`;
cat $1 | tr '\n' '+' | sed 's/.$//' | xargs -i echo "scale=2; ((({})/$total)*10)/100" | bc
