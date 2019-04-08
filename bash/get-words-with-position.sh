#!/bin/bash

# retrieving words of a sentence with start and end positions
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# How to use: ./get-words-with-position.sh <filename> <position_of_start_word> <position_of_end_word>
# e.g.1: ./get-words-with-position.sh ./my-text.txt 1 1
# e.g.2: ./get-words-with-position.sh ./my-text.txt 3 2 

start_word=$2;
end_word=$3;

cat $1 | while read -r line
do

   # -   Assign any remaining arguments to the positional parameters.
   #     The -x and -v options are turned off. 
   set -- $line

   # accessing elements of the array "$@" with start and end indexes
   echo ${@:$start_word:$end_word}
   
done

