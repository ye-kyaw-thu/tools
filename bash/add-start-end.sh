#!/bin/bash

# for labeling the start "<s>" and end "<\s>" of the sentence
# this labeling task is required for some NLP preprocessing such as language model building
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# How to use: ./add-start-end.sh <filename>
# e.g.: ./add-start-end.sh ./my-text.txt

cat $1 | while read -r line
do

   printf "<s> $line <\s>\n"
   
done

