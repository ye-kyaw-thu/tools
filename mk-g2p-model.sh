#!/bin/bash

# Building g2p model with Phonetisaurus
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# Last updated: 17 Jan 2020
# Used for ASR Winter School at CU Banmaw

# How to run: bash ./mk-g2p-model.sh <dict-file> <test-file>
# e.g. 

echo -e ">>> Corpus building ...\n";
phonetisaurus-align --input=$1 --ofile=./$1.corpus --seq1_del=false

echo -e ">>> Create symbol file ...\n";
ngramsymbols < ./$1.corpus > $1.syms

echo -e ">>> Preparing far file ...\n";
farcompilestrings --symbols=$1.syms --keep_symbols=1 ./$1.corpus > $1.far

echo -e ">>> running ngramcount ...\n";
ngramcount --order=8 $1.far > $1.cnts

echo ">>> running ngrammake ...";
ngrammake --v=2 --bins=3 --method=kneser_ney ./$1.cnts > $1.mod

echo -e ">>> Converting to ARPA file format ...\n";
ngramprint --ARPA ./$1.mod > $1.arpa

# FST Model Building
echo -e ">>> FST model building ...\n";
phonetisaurus-arpa2wfst --lm=$1.arpa > $1.fst

echo -e ">>> Finished FST model building ...\n";

# Testing ... 
echo -e ">>> Start testing with filename=$2\n";
phonetisaurus-g2pfst --model=$1.fst --wordlist=./$2  | perl -e'while(<>){s/\|/ /g; print $_;}' > $2.out

