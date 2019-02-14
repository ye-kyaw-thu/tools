#!/bin/bash

# for removing stop words
# written by Ye, LST Lab., NECTEC, Thailand
# how to run: ./rm-stopwords.sh <stopwords filename> <corpus filename>
# e.g. ./rm-stopwords.sh ./stopwords.txt ./my-text.txt

stopwordFile=$1;
corpusFile=$2;

# adding my own start and end word boundaries for both stop word and corpus files for matching exact words
# \<, \>, \b are working well for ASCII and not working for Myanmar words or unicode
# I also tried with [[:<:]],[[:>:]] and \b{w}.
# However I found following solution is the best for my case.   
sed 's/^.*$/\<\|&\|\>/' $stopwordFile | sed 's/ /\|\>&\<\|/g' > $stopwordFile.tmp;
sed 's/^.*$/\<\|&\|\>/' $corpusFile | sed 's/ /\|\>&\<\|/g' > $corpusFile.tmp;

# print out stop words removed output
# here, using ":" delimiter instead of using "/" for easier reading
# sed "s/.*/s\/&\/\/ig/"
sed -e "$(sed "s:.*:s/&//ig:" $stopwordFile.tmp)" $corpusFile.tmp | sed 's/<|\||>//g' 

# remove temp files
rm $stopwordFile.tmp;
rm $corpusFile.tmp;
