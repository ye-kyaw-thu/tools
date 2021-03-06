#!/bin/bash

# for building phrase table by using fast_align aligned output
# Note: For running this script, you need moses toolkit
# Update moses path before you run this script
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 25 Nov 2020
# ref: https://github.com/bitextor/bicleaner/issues/17
# ref: https://moses-support.mit.narkive.com/x2BdfPvc/reusing-alignments-for-10-9-fr-en-and-using-fast-align
# ref: https://gist.github.com/noisychannel/302c2f58f57b92290f2f
# ref: http://www.statmt.org/moses/
# ref: https://github.com/clab/fast_align
#
# How to run: ./build-fastalign-pt.sh <source-extension> <target-extension>
# for Myanmar-Rakhine
# ./build-fastalign-pt.sh my rk
# for Rakhine-Myanmar
# ./build-fastalign-pt.sh rk my

SRC=$1
TRG=$2

# (4) generate lexical translation table
perl /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/ems/support/symmetrize-fast-align.perl ./train.$SRC$TRG.pipe.forward.align ./train.$SRC$TRG.pipe.reverse.align ./train.$SRC ./train.$TRG aligned grow-diag-final-and /home/ye/tool/moses-bin/ubuntu-17.04/moses/bin/symal
# FYI:
# Saved: /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-bk-fastalign/tmp/lex.f2e and /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-bk-fastalign/tmp/lex.e2f

# (5) extract phrases & (6) score phrases
perl /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/training/train-model.perl -first-step 4 -last-step 6 -f $SRC -e $TRG -alignment grow-diag-final-and -score-options '--GoodTuring' -lexical-file lex -alignment-file aligned -alignment-stem aligned -corpus train

# gunzip
gunzip ./model/extract.inv.sorted.gz
gunzip ./model/extract.sorted.gz
gunzip ./model/phrase-table.gz

# confirmation
echo "head ./model/extract.inv.sorted...";
head ./model/extract.inv.sorted;

echo "head ./model/extract.sorted...";
head ./model/extract.sorted;

echo "head ./model/phrase-table...";
head ./model/phrase-table;

