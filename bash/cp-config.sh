#!/bin/bash

# for preparing config.baseline and run-baseline.pl files for 10-fold-cross validation MT experiments
# Written by Ye Kyaw Thu,
# Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to run: bash ./cp-config.sh

for f in {dw-my,my-bk,dw-bk}
do
   # /home/ye/exp/dw-bk-my/data/dw-bk/1
   str="myrk-data = /home/ye/exp/dw-bk-my/data/$f/"
   p1="my @configs = \`find /home/ye/exp/dw-bk-my/data/$f/"
   p2="/ -name \"config.baseline*\" \`;"

   for i in {1..10}
   do
      sed -i "46 s|.*|${str}${i}|" ./config.baseline;
      echo "Added following line to line no. 45 of \"./config.baseline\" file ...";
      sed -n 46p ./config.baseline;
      echo
      echo "Copying ./config.baseline to ./$f/$i/ ...";
      cp ./config.baseline ./$f/$i/;

      sed -i "27 s|.*|my \$smtpath = \"/home/ye/exp/dw-bk-my/data/${f}/${i}/\";|" ./generate_configs.pl;
      echo
      echo "Added following line to line no. 27 of \"./generate_configs.pl\" file ...";
      sed -n 27p ./generate_configs.pl;

      sed -i "41 s|.*|foreach my \$trainFile ( </home/ye/exp/dw-bk-my/data/${f}/${i}/train.[a-z][a-z]>)|" ./generate_configs.pl;
      echo "Added following line to line no. 41 of \"./generate_configs.pl\" file ...";
      sed -n 41p ./generate_configs.pl;
      echo
      echo "Copying ./generate_configs.pl to ./$f/$i/ ...";
      cp ./generate_configs.pl ./$f/$i/;
      echo
      sed -i "28 s|.*|${p1}${i}${p2}|" ./run-baseline.pl
      echo "Added following line to line no. 28 of \"./run-baseline.pl\" file ...";
      sed -n 28p ./run-baseline.pl;
      echo
      echo "Copying ./run-baseline.pl to ./$f/$i/ ...";
      cp ./run-baseline.pl ./$f/$i/;
      echo "ls ./$f/$i/";
      ls ./$f/$i/;
      echo "==========";
      echo
   done
done
