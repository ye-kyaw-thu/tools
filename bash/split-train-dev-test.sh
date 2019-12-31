#!/bin/bash

# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# practical bash shell script of preparing training, development and test data
# for running SMT
# I wrote this bash shell script for one of the SMT experiments
# with my Ph.D. Student Ms. Honey Htun (YTU)
#
# How to run:
# ./split-train-dev-test.sh

# change following three variable based on your experiment and the data size
train_percent=80;
dev_percent=10;
test_percent=10;

echo "train %: $train_percent";
echo "dev %: $dev_percent";
echo "test%: $test_percent";
echo "==========";

#for no in {10,20}; # testing ...
for no in {10,20,30,40,50,60,70,80,90,100};
do

   echo -e "\nstart working for multiple translation $no ...\n";
   mkdir smt-$no;

   total=$(wc -l < ./1to1.out$no)
   echo "total sentence: $total";
   shuf 1to1.out$no > all.shuf.tmp;

# for training data
   percent=$(bc -l<<<"scale=2;$train_percent /100 * $total");
   train_sentence=$(printf '%.0f' "$percent");

   head -n $train_sentence all.shuf.tmp > ./smt-$no/train.par

# for development data
   percent=$(bc -l<<<"scale=2; $dev_percent /100 * $total")
   dev_sentence=$(printf '%.0f' "$percent")
   train_dev=$(( dev_sentence + train_sentence ))

   head -n $train_dev all.shuf.tmp | tail -n $dev_sentence > ./smt-$no/dev.par

# for testing (open-test) data
	percent=$(bc -l<<<"scale=2; $test_percent /100 * $total")
	test_sentence=$(printf '%.0f' "$percent")

   tail -n $test_sentence all.shuf.tmp > ./smt-$no/test.par

   cd ./smt-$no/;
#   echo "folder info:";
#   wc -l *;

# splitting for source and target language pair
   cut -f1  -d "|" ./train.par > train.en;
   cut -f2  -d "|" ./train.par > train.my;
 
   cut -f1  -d "|" ./dev.par > dev.en;
   cut -f2  -d "|" ./dev.par > dev.my;

   cut -f1  -d "|" ./test.par > test.en;
   cut -f2  -d "|" ./test.par > test.my;
   
   # removing .par files
   rm -f *.par;

   # print out train, dev and test data of source and target languages
   # for human confirmation
   echo "prepared for English ...:";
   wc -l *.en;
   echo "prepared for Myanmar...:";
    wc -l *.my;
   cd ..;
   echo "==========";
done

