#!/bin/bash

# syllable breaking for 10 fold-cross SMT with moses
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# How to run: ./sylbreak-10fold-smt.sh <source-language-extension> < target-language-extension>
# e.g. for Dawei, Beik language pair: bash ./sylbreak-10fold-smt.sh dw bk

SRC=$1;
TRG=$2;

for i in {1..10}
do
   echo "cd $i";
   cd $i;

   # filename changing for source langauge
   mv train.$SRC train.$SRC.word;
   mv dev.$SRC dev.$SRC.word;
   mv test.$SRC test.$SRC.word;

   # filename changing for target language
   mv train.$TRG train.$TRG.word;
   mv dev.$TRG dev.$TRG.word;
   mv test.$TRG test.$TRG.word;

   #space removing (preprocess for syllable breaking ...)
   for EXT in {$SRC,$TRG}
   do
      sed 's/ //g' ./train.$EXT.word > ./train.$EXT.word.nospace;
      sed 's/ //g' ./dev.$EXT.word > ./dev.$EXT.word.nospace;
      sed 's/ //g' ./test.$EXT.word > ./test.$EXT.word.nospace;
   done

   # syllable segmentation and cleaning heading, training and double spaces for both source and target
   for EXT in {$SRC,$TRG}
   do
      perl ../sylbreak.pl -i ./train.$EXT.word.nospace -s " " > ./train.$EXT.word.nospace.syl;
      perl ../clean-space.pl ./train.$EXT.word.nospace.syl > ./train.$EXT;
      # printing some information for user
      echo "head  ./train.$EXT";
      head  ./train.$EXT;

      perl ../sylbreak.pl -i ./dev.$EXT.word.nospace -s " " > ./dev.$EXT.word.nospace.syl;
      perl ../clean-space.pl ./dev.$EXT.word.nospace.syl > ./dev.$EXT;
      echo "head ./dev.$EXT";
      head ./dev.$EXT;

      perl ../sylbreak.pl -i ./test.$EXT.word.nospace -s " " > ./test.$EXT.word.nospace.syl;
      perl ../clean-space.pl ./test.$EXT.word.nospace.syl > ./test.$EXT;
      echo "head ./test.$EXT";
      head ./test.$EXT;
      echo "==========";

   done

   # backup original word segmented data
   mkdir word_data;
   mv *.*.word* word_data;

   cd ..;
done
