#!/bin/bash

# for removing stop words
# written by Ye, LST Lab., NECTEC, Thailand
# how to run: ./rm-stopwords.sh <stopwords filename> <corpus filename>
# e.g. ./rm-stopwords.sh ./stopwords.txt ./my-text.txt

stopwordFile=$1;
corpusFile=$2;

sed 's/^.*$/\<\|&\|\>/' $stopwordFile | sed 's/ /\|\>&\<\|/g' > $stopwordFile.tmp;
sed 's/^.*$/\<\|&\|\>/' $corpusFile | sed 's/ /\|\>&\<\|/g' > $corpusFile.tmp;

# print out stop words removed output
# here, using ":" delimiter instead of using "/" for easier reading
# sed "s/.*/s\/&\/\/ig/"
sed -e "$(sed "s:.*:s/&//ig:" $stopwordFile.tmp)" $corpusFile.tmp | sed 's/<|\||>//g' 

# remove temp files
rm $stopwordFile.tmp;
rm $corpusFile.tmp;
