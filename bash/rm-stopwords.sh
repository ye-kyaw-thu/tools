#!/bin/bash

# for removing stop words
# written by Ye, LST Lab., NECTEC, Thailand

stopwordFile=$1;
corpusFile=$2;

# same with following line. using ":" delimiter instead of using "/" for easier reading 
# sed -e "$(sed 's/.*/s\/& \/\/ig/' $stopwordFile)" $corpusFile;
# Note space character after &

sed -e "$(sed 's:.*:s/^& //ig:' $stopwordFile)" $corpusFile | sed -e "$(sed 's:.*:s/& //ig:' $stopwordFile)" ;
