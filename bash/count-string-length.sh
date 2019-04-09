#!/bin/bash

# measuring string length or counting characters
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
#
# How to use: ./count-string-length.sh <filename>
# e.g. ./count-string-length.sh ./my-text2.txt

cat $1 | while read -r line
do

   echo ${#line};

done
