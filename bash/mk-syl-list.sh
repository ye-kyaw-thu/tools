#!/bin/bash

# Written by Ye, LST Lab., NECTEC, Thailand
# syllable breaking and making uniq syllable list for maw maw data
# A good example of a shell script calling other perl programs for cleaning Myanmar data
#How to run: ./mk-syl-list.sh

# Note: This program will required other perl programs
# print-mySentenceOnly.pl, sylbreak.pl, clean-space.pl

cut -f1 -d"," ./data-categorized-uni-sent-drY.csv > f1
perl print-mySentenceOnly.pl ./f1 > f1.my
cat ./f1.my | tr -d " " > ./f1.my.nospace
perl ./sylbreak.pl -i ./f1.my.nospace -s " " > f1.my.nospace.syl
perl ./clean-space.pl ./f1.my.nospace.syl > f1.my.nospace.syl.clean
cat ./f1.my.nospace.syl.clean | tr " " "\n" | sort | uniq > ./f1.my.nospace.syl.clean.uniq

echo "output file: f1.my.nospace.syl.clean.uniq";

