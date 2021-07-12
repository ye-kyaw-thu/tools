#!/bin/bash

# spelling checking for English with a dictionary
# written by Ye Kyaw Thu
# How to run: bash ./spelling-checker-with-dict.sh <input-filename>
# e.g. bash ./spelling-checker-with-dict.sh ./my.testfile

# Eample dictionary preparation:
# Ref: https://github.com/jeremy-rifkin/Wordlist
# $ cat master.txt  | tr A-Z a-z | sort > ./dictionary.txt

# Example dictionary preparation for Myanmar language
# $ wget https://raw.githubusercontent.com/ye-kyaw-thu/myG2P/master/ver2/myg2p.ver2.0.txt
# $ cut -f2 ./myg2p.ver2.0.txt > myg2p.ver2.0.txt.f2
# $ sort ./myg2p.ver2.0.txt.f2 > my.dictionary.txt

#cat $1 | tr A-Z a-z | tr -c a-z '\n' | sort | uniq | comm -13 dictionary.txt -
cat $1 | tr A-Z a-z | tr ' ' '\n' | sort | uniq | comm -13 my.dictionary.txt -
