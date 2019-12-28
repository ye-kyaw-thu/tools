#!/bin/bash

# Written by Ye, LST Lab., NECTEC, Thailand
# Written for calculating RIBES score (machine translation performance measuring matrix)
# Used for Thazin Myanmar-Rakhine SMT 10-fold cross validation SMT
# Last updated: 26 Dec 2019

# How to run:
# ./calc-ribes-all.sh 2>&1 | tee ribes-score.txt

for i in {1,3,6,7,8,9};
do
   echo "### sRakhine$i ###";
   echo "Baseline: my-rk";
   python /home/lar/tool/RIBES-1.03.1/RIBES.py -z -r ./sRakhine$i/my-rk/smt1/baseline/my-rk/evaluation/test.reference.txt.1 ./sRakhine$i/my-rk/smt1/baseline/my-rk/evaluation/test.cleaned.1
   echo "";

   echo "Baseline: rk-my";
   python /home/lar/tool/RIBES-1.03.1/RIBES.py -z -r ./sRakhine$i/my-rk/smt1/baseline/rk-my/evaluation/test.reference.txt.1 ./sRakhine$i/my-rk/smt1/baseline/rk-my/evaluation/test.cleaned.1
   echo "";

   echo "Hiero: my-rk";
   python /home/lar/tool/RIBES-1.03.1/RIBES.py -z -r ./sRakhine$i/my-rk/smt1/hiero/my-rk/evaluation/test.reference.txt.1 ./sRakhine$i/my-rk/smt1/hiero/my-rk/evaluation/test.output.1
   echo "";

   echo "Hiero: rk-my";
   python /home/lar/tool/RIBES-1.03.1/RIBES.py -z -r ./sRakhine$i/my-rk/smt1/hiero/rk-my/evaluation/test.reference.txt.1 ./sRakhine$i/my-rk/smt1/hiero/rk-my/evaluation/test.output.1
   echo "";

   echo "OSM: my-rk";
   python /home/lar/tool/RIBES-1.03.1/RIBES.py -z -r ./sRakhine$i/my-rk/smt1/osm/my-rk/evaluation/test.reference.txt.1 ./sRakhine$i/my-rk/smt1/osm/my-rk/evaluation/test.cleaned.1
   echo "";

   echo "OSM: rk-my";
   python /home/lar/tool/RIBES-1.03.1/RIBES.py -z -r ./sRakhine$i/my-rk/smt1/osm/rk-my/evaluation/test.reference.txt.1 ./sRakhine$i/my-rk/smt1/osm/rk-my/evaluation/test.cleaned.1
   echo -e "====================\n";

done;
