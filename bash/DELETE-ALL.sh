#!/bin/bash

# code for deleting SMT baseline folder for 10-fold corss validation experiments for dw-my, my-bk and dw-bk language pairs
# Note: this script is relating to https://github.com/ye-kyaw-thu/tools/blob/master/bash/cp-config.sh
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# How to run: time bash ./DELETE-ALL.sh 


for f in {dw-my,my-bk,dw-bk}
do
   cd ./$f/; echo "Current path: $PWD";
   for i in {1..10}
   do
    cd ./$i/; echo "Current path: $PWD";
      echo "Deleting the folder $i ...";
      rm -r ./baseline;
      cd ../; 
   done
   cd ../;
done
