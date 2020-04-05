#!/bin/bash

# LM building with classes
# Note: SRILM toolkit required to use this bash script
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# How to run:
# ./mk-class-lm.sh <corpus> <no-of-classes> <test-data> <debug-level>
# e.g.  ./mk-class-lm.sh ./bookmar.zh-my.f2 2000 ./test-data/test-data.bbc 1
# e.g. ./mk-class-lm.sh ./bookmar.zh-my.f2 5000 ./test-data/10lines 2

# getting 1st character of $2 argument
classNo=${2:0:1};

# 1-gram count
echo "1-gram counting ...";
ngram-count -order 1 -text ./$1 -write $1.1gram.count;

# select only the 5000 most common words
echo "sorting with freq and taking the top 5k words ...";
sort -n -r -k 2 ./$1.1gram.count | head -n $2 | cut -f 1 > $1.1gram.count.top.${classNo}k;

# make class file,
# here, bookmar.class-counts file is the class n-gram count file
# which can then be read by ngram-count to estimate a class language model
# bookmar.classes: the class definitions (i.e. each word and its probability within the class) file
echo "making classes ...";
ngram-class -vocab ./$1.1gram.count.top.${classNo}k \
            -text ./$1 \
            -numclasses $2 \
            -class-counts $1.class-counts \
            -classes $1.classes;

# building a 3gram language model using the classes generated in the previous step:
echo "builing 3grm language model using the classes ...";
ngram-count -order 3 \
            -read $1.class-counts \
            -write $1.ngrams;
ngram-count -order 3  \
            -read $1.ngrams \
            -lm  $1.class.3gram.lm;

# evaluaiton with ppl
# I have two ngram program and thus, I assigned SRILM ngram path
echo "Evaluation with ppl, test-data filename:$3, debug level: $4";
/home/lar/tool/srilm/bin/i686-m64/ngram -lm $1.class.3gram.lm -classes $1.classes -ppl $3 -debug $4
