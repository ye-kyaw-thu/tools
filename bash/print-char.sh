#!/bin/bash

# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# for printing character by character
# How to run: ./print-char.sh <input-filename>

inputFile=$1;

while read -n1 char;
do
   echo $char;
done < $inputFile
