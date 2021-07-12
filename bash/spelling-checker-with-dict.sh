#!/bin/bash

# spelling checking for English with a dictionary
# written by Ye Kyaw Thu
# How to run: bash ./spelling-checker-with-dict.sh ./testfile.txt

# Eample dictionary preparation:
# Ref: https://github.com/jeremy-rifkin/Wordlist
# cat master.txt  | tr A-Z a-z | sort > ./dictionary.txt

cat $1 | tr A-Z a-z | tr -c a-z '\n' | sort | uniq | comm -13 dictionary.txt -
