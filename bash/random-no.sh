#!/bin/bash

# random number generation with bash
# written by Ye Kyaw Thu, NECTEC, Thailand
# 22 Oct 2021
# Reference: https://www.baeldung.com/linux/random-numbers
#
# How to use: ./random-no.sh <min> <max> <no-of-iter>
# e.g. ./random-no.sh 1 6 10 

min=$1;
max=$2;
iter=$3;

for ((i=1; i<=$iter; i++))
do
   expr $min + $RANDOM % $max
done
