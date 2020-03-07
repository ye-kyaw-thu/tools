#!/bin/bash

# splitting my_sentence|beik_sentence|dawei_sentence and
# preparing 10-fold cross validation of
# training, development and test data for Beik and Dawei language pair
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
#
# How to run: bash ./prepare-10fold-smt-pair.sh <inputFile> <no-of-lines-per-file>
# e.g. ./prepare-10fold-smt-pair.sh ./out 670 
# Note: you have to adjust <no-of-lines-per-file> based on your size of <inputFile>

#split -n 10 -d $1; # you will get an error on splitted files,  NEL line terminators
split -l $2 -d $1; # use -l option instead of -n option

fd=1;
for skipFile in {x00,x01,x02,x03,x04,x05,x06,x07,x08,x09}
do
   mkdir $fd;
   echo "Start working for $fd/ ...";
   find . -maxdepth 1 -iname 'x*' -not -name $skipFile -exec cat {} +> ./$fd/train-dev;
   cp $skipFile ./$fd/test;

   linecount=`cat ./$fd/train-dev | wc -l`;
   trainCount=$[linecount-500];
   
   # prepare training and development file
   head  -n $trainCount ./$fd/train-dev > ./$fd/train;
   tail -n 500 ./$fd/train-dev > ./$fd/dev;
   
   # split bk and dw
   cut -f2 ./$fd/train -d '|' > ./$fd/train.bk;
   cut -f3 ./$fd/train -d '|' > ./$fd/train.dw;
 
   cut -f2 ./$fd/dev -d '|' > ./$fd/dev.bk;
   cut -f3 ./$fd/dev -d '|' > ./$fd/dev.dw;

   cut -f2 ./$fd/test -d '|' > ./$fd/test.bk;
   cut -f3 ./$fd/test -d '|' > ./$fd/test.dw;

   mkdir ./$fd/original;
   mv ./$fd/train-dev ./$fd/original/;
   mv ./$fd/train ./$fd/original/;
   mv ./$fd/dev ./$fd/original/;
   mv ./$fd/test ./$fd/original/;

   echo "tree structure of folder ./$fd/";
   tree ./$fd/
   echo ""
   echo "wc of train dev test:";
   wc ./$fd/train.*;
   wc ./$fd/dev.*;
   wc ./$fd/test.*;
   echo "";

   echo "head of train dev test:";
   echo "./$fd/train.bk"; head ./$fd/train.bk;
   echo "./$fd/train.dw"; head ./$fd/train.dw;
   echo "./$fd/dev.bk"; head ./$fd/dev.bk;
   echo "./$fd/dev.dw"; head ./$fd/dev.dw;
   echo "./$fd/test.bk"; head ./$fd/test.bk;
   echo "./$fd/test.dw"; head ./$fd/test.dw;
   echo "==========";
   echo "file type checking:";
   file ./$fd/*;
   echo "==========";
   echo "";

   fd=$[fd+1];
done

# removing splitte files
rm {x00,x01,x02,x03,x04,x05,x06,x07,x08,x09};

