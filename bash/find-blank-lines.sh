#!/bin/bash

# for printout filename and lineno of blank lines 
# written by Ye, NECTEC, Thailand
# How to run: ./find-blank-lines.sh <filename or regular expression>
# e.g. ./find-blank-lines.sh train.my
# e.g. ./find-blank-lines.sh 't*.*' 
# Note: when you want to pass special characters such as *, you should use single quote!!!

#find . -name "$1"  | xargs grep -E --line-number --with-filename '^$';
find . -wholename "$1"  | xargs grep -E --line-number --with-filename '^$';
