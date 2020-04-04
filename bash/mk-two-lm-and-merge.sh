#!/bin/bash

# for building two language models and merge or "static" interpolation
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# You need SRILM toolkit to run this shell script
# I changed original shell script name:
#  mv mk-two-lm.sh mk-two-lm-and-merge.sh

# lm building with bookmar my-zh Myanmar data
time /home/lar/tool/srilm/bin/i686-m64/ngram-count -order 3 -kndiscount -text ./bookmar.zh-my.f2 -lm ./bookmar.arpa -write_vocab bookmar.vocab -debug 2

# lm building with mypos corpus
time /home/lar/tool/srilm/bin/i686-m64/ngram-count -order 3 -kndiscount -text ./mypos.txt -lm ./mypos.arpa -write_vocab mypos.vocab -debug 2

# 10 sentences generation with bookmar.arpa language model
/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./bookmar.arpa -gen 10

# 10 sentences generation with mypos.arpa language model
/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./mypos.arpa -gen 10

# You might need to use sed for sentence generation process
# | sed "s/ //g" | sed "s/^\s//g"

# Evaluation on bookmar.arpa lm
/home/lar/tool/srilm/bin/i686-m64/ngram -ppl ./test-data.bbc.seg -lm ./bookmar.arpa -order 3 -debug 2

# Evaluation on mypos.arpa lm
/home/lar/tool/srilm/bin/i686-m64/ngram -ppl ./test-data.bbc.seg -lm ./mypos.arpa -order 3 -debug 2

# Before making interpolation you might need to do renormalize
#/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./bookmar.arpa -renorm -write-lm ./bookmar.arpa.norm
#/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./mypos.arpa -renorm -write-lm ./mypos.arpa.norm

# Interpolation
/home/lar/tool/srilm/bin/i686-m64/ngram -lm ./bookmar.arpa -mix-lm  ./mypos.arpa -lambda 0.6/0.7 -write-lm ./bookmar.mypos.arpa -debug 2

# Evaluation with merged LM
/home/lar/tool/srilm/bin/i686-m64/ngram -ppl ./test-data.bbc.seg -lm ./bookmar.mypos.arpa -order 3 -debug 2


