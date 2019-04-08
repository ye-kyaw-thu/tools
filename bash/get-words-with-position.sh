#!/bin/bash

# retrieving words of a sentence with start and end positions
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# How to use: ./get-words-with-position.sh <filename> <position_of_start_word> <number_of_words>
# e.g.1: ./get-words-with-position.sh ./my-text.txt 1 1
# e.g.2: ./get-words-with-position.sh ./my-text.txt 3 2 

start_word=$2;
no_of_words=$3;

cat $1 | while read -r line
do

   # -   Assign any remaining arguments to the positional parameters.
   #     The -x and -v options are turned off. 
   set -- $line

   # accessing elements of the array "$@" with start and end indexes
   echo ${@:$start_word:$no_of_words}
   
done

