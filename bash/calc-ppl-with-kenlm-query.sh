#!/bin/bash

# Calculating perplexity with KenLM command "query"
# Note: KenLM is required to use this bash shell script
# Coded by Ye, LST Lab., NECTEC, Thailand
# How to run: ./calc-ppl-with-kenlm-query.sh <kenlm-model> <test-data> <summary|sentence|word>
# e.g. ./calc-ppl-with-kenlm-query.sh ./bookmar.zh-my.f2.klm ./10lines word

# e.g. path of the query command
# /home/lar/tool/kenlm/build/bin/query
query -v $3 ./$1 < ./$2
