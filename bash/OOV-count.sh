#!/bin/bash

# Calculating OOV (Out-Of-Vocabulary) for test-data
# written by Ye, Visiting Professor, LST Lab., NECTEC, Thailand
# how to run: ./OOV-count.sh <corpus-filename> <test-data-filename>
# e.g. ./OOV-count.sh ./mypos-dver.1.0.word.txt ./test-data4oov
# e.g. ./OOV-count.sh ./mypos-dver.1.0.word.txt ./test-data4oov > oov.list 
# FYI: I used https://raw.githubusercontent.com/ye-kyaw-thu/myPOS/master/corpus-draft-ver-1.0/mypos-dver.1.0.word.txt as a corpus for testing

# make 1 cloumn word list, sorting and make uniq for $1 (i.e. 1st input filename)
tr " " "\n" < $1 | sort | uniq > $1.uniq

# make 1 column word list, sorting and make uniq for $2 (i.e. 2nd input filename)
# *** working on test-data
tr " " "\n" < $2 | sort | uniq > $2.uniq

# here, -23 option will show only uniq word list in the $2.uniq file (i.e. test data file)
comm -23 $2.uniq $1.uniq
