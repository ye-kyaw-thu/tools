#!/bin/bash

# "f1.uniq" file contained English sentences
# "one_many_data.unique" file is a parallel corpus that contained
# several translated Myanmar sentences of the same English sentence
#
# this bash shell script will print out translated Myanmar sentences together with 
# parallel English sentence according to your $3 parameter (e.g. 1 or 2 or 100)
#
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# Last updated: 31 December 2019
# How to run:
# e.g. ./print-matched-x.sh ./f1.uniq ./one_many_data.unique 1 > 1to1.out1
# ./print-matched-x.sh ./f1.uniq ./one_many_data.unique 2 > 1to1.out2


#search sentence of this file
sentenceFile=$1;

#search inside this file
searchFile=$2;

#print only a count of matching lines
noOfMatch=$3;

xargs -a $sentenceFile -d \n |\
 xargs -I '{}' fgrep -w '{}' $searchFile \
-m $noOfMatch | sort | uniq;
