#!/bin/bash

# Written by Ye Kyaw Thu, Language Understanding Lab., Myanmar
# Word alignment with GIZA++
# Last updated: 29 July 2020
# ./align.sh <source> <target> <output-folder>
# ./align.sh train.en train.th align2

GIZA_PATH="/home/ye/tool/giza-pp/GIZA++-v2";

# check for output folder
if [ ! -d "$3" ]; then
   mkdir $3;
fi
# making .vcb and .snt files
echo "making .vcb and .snt files";
echo "$GIZA_PATH/plain2snt.out $1 $2";
$GIZA_PATH/plain2snt.out $1 $2;
echo "##########";

echo "head $1.vcb";
head $1.vcb;
echo "head $2.vcb";
head $2.vcb;
echo "##########";

echo "head $1_$2.snt";
head $1_$2.snt;
echo "##########";

echo "head $2_$1.snt";
head $2_$1.snt;
echo "##########";

# making word classes for source
#/home/lar/tool/giza-pp/mkcls-v2/mkcls -c80 -n10 -p./train-dev.ky.char -V./train-dev.ky.char.classes opt;
$GIZA_PATH/mkcls -c80 -n10 -p$1 -V$1.classes opt;
echo "##########";

# check source classes
echo "ls *.classes";
ls *.classes
echo "##########";

echo "head $1.classes";
head $1.classes
echo "##########";

# making word classes for unicode
#/home/lar/tool/giza-pp/mkcls-v2/mkcls -c80 -n10 -p./train-dev.un.char -V./train-dev.un.char.classes opt;
$GIZA_PATH/mkcls -c80 -n10 -p$2 -V$2.classes opt;

# check target classes
echo "head $2.classes";
head $2.classes;
echo "##########";

echo "ls *.cats";
echo "##########";

# check two .snt file
echo "diff $1_$2.snt $2_$1.snt";
diff  ../$1_$2.snt $2_$1.snt;
echo "##########";

# making cooccurrence file
echo "making co-occurrence file ...";
#/home/lar/tool/giza-pp/GIZA++-v2/snt2cooc.out ./train-dev.ky.char.vcb ./train-dev.un.char.vcb ./train-dev.ky.char_train-dev.un.char.snt  > train-dev.ky_un.char.cooc;
$GIZA_PATH/snt2cooc.out $1.vcb $2.vcb $1_$2.snt > $1_$2.char.cooc;
echo "##########";

# making alignment
echo "making alignment ...";
#/home/lar/tool/giza-pp/GIZA++-v2/GIZA++ -s ./train-dev.ky.char.vcb -t ./train-dev.un.char.vcb -c ./train-dev.ky.char_train-dev.un.char.snt -CoocurrenceFile ./train-dev.ky_un.char.cooc -o Result -outputpath $1| tee align-ky-un.char.log;
$GIZA_PATH/GIZA++ -s $1.vcb -t $2.vcb -c $1_$2.snt -CoocurrenceFile ./$1_$2.char.cooc -o Result -outputpath $3| tee align-$1_$2.log;
echo "##########";

# list files
echo "finished ...";
echo "ls ./$3/*.final";
ls ./$3/*.final
echo "##########";

echo "Note by Ye ...";
echo "output folder name: $3";
echo "GIZA++ learns the translation tables of IBM Model 4, but we are only interested in \".A3.final\"";
