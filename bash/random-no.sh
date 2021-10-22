#!/bin/bash

# random number generation with bash
# written by Ye Kyaw Thu, NECTEC, Thailand
# 22 Oct 2021
#
# How to use: ./random-no.sh <min> <max> <no-of-iter>
# e.g. ./random-no.sh 1 6 10 

min=$1;
max=$2;
iter=$3;

for ((i=0; i<=$iter; i++))
do
   shuf -i $min-$max -n 1
done

