#!/bin/bash -v

# alignment training with mgiza
# written by Ye, LST, NECTEC, Thailand
# Date: 7 Dec 2020
# Note: You have to install mgiza before you use this shell script
# Note: You also have to prepare parallel data and configuration file
#
# How to run: ./mgiza-align.sh <source> <target> <configfile>
# e.g. time ./mgiza-align.sh train.my train.rk config.template


# updating the SOURCE and TARGET filenames of configfile
find ./$3 -type f -exec sed "s|train.SRC|${1}|g;s|train.TRG|${2}|g" {} \; > config.update
cat config.update;

# mgiza bin path
BIN_DIR=/home/ye/tool/giza-pp/mgiza/mgizapp/bin/

# class building for HMM
$BIN_DIR/mkcls -n10 -p$1 -V$1.vcb.classes
$BIN_DIR/mkcls -n10 -p$2 -V$2.vcb.classes

$BIN_DIR/plain2snt $1 $2
$BIN_DIR/snt2cooc $1\_$2.cooc $1.vcb $2.vcb $1\_$2.snt

$BIN_DIR/mgiza config.update

wc *.A3.final.part*
