#!/bin/bash

# demo code of syllable breaking of several Myanmar utf8 text files ...
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# how to run:
# e.g. ./syllable-break-multi-files.sh newg1 newg2 newg3

for FILE in $*;
do
   echo "Syllable breaking of $FILE...";
   perl ./sylbreak.pl -i $FILE -s " " > $FILE.syl
   perl ./clean-space.pl ./$FILE.syl > $FILE.syl.clean
   echo "head $FILE.syl.clean";
   head $FILE.syl.clean
   echo "=====";

done
