#!/bin/bash

# printing most common x words
# Note: SRILM toolkit required to run this bash shell script
# Written by Ye Kyaw Thu, LST Lab., NECTEC Lab., Thailand
# How to use: ./print-most-common.sh <corpus-filename> <no-of-words>
# e.g. ./print-most-common.sh ./bookmar.zh-my.f2 100

# 1-gram counting from the input corpus $1
ngram-count -order 1 -text ./$1 -write $1.1gram.count

# select only the $2 most common words
sort -n -r -k 2 ./$1.1gram.count | head -n $2 | cut -f 1 > $1.1gram.count.top$2
