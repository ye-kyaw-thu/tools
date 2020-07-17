#!/bin/bash

# preparing 10-fold cross validation
# written by Ye Kyaw Thu, Language Understanding Lab., Pyin Oo Lwin, Myanmar
# How to use: ./mk-10cross-data.sh <corpus> <extension-for-language>

if (( $# != 3 )); then
   echo "two arguments required!";
   echo "./mk-10cross-data.sh <corpus> <source> <target>";
   echo "./mk-10cross-data.sh kc.all my kc";
   exit; 
fi

file=$1;
lang=;

count=$(wc -l < $file);
echo -e "total lines: $count\n";

shuf $file > file_shuf.txt;

split -n l/10 -a1 -d file_shuf.txt cross;

for i in {0..9}
do 

        # prepare folder
        mkdir data$i;
        cd data$i;

        # prepare test-data
	cat ../cross$i > ./test;

        # tmp file for train+dev
	find ../ -type f -name "cross*" ! -name "cross$i" -exec cat > train_dev$i {} \;
        
        # split training and development data
        tail -n  500 ./train_dev$i > dev;

         lcount=$(wc -l < ./train_dev$i)
         hline=$(echo "$lcount-500" | bc)

        echo -e "hline: $hline\n";
        head -n $hline ./train_dev$i > ./train;

        wc ./train; wc ./dev; wc ./test;
        rm ./train_dev$i;

        # splitting for source language
        cut -f1 ./train > train.$2
        cut -f1 ./dev > dev.$2
        cut -f1 ./test > test.$2
   
        # splitting for target language
        cut -f2 ./train > train.$3
        cut -f2 ./dev > dev.$3
        cut -f2 ./test > test.$3

        cd ..;

done

rm ./cross*
cp ./file_shuf.txt ./file_shuf.txt.bak


