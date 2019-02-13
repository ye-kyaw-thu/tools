#!/bin/bash

# for printing even line or odd line
# Ye, LST Lab., NECTEC, Thailand
# Ref: https://unix.stackexchange.com/questions/26723/print-odd-numbered-lines-print-even-numbered-lines

if [ "$#" -lt 2 ]; then

   echo "Two command line argument is required!"
   echo "even-odd.sh <filename> <even|odd>";

elif [ $2 = "even" ]; then

   sed -n 'n;p' $1;

elif [ $2 = "odd" ]; then

   sed -n 'p;n' $1;

fi


