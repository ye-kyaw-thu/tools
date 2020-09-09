#!/bin/bash

# converting a picture to color histogram
# writtten by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 10 Sept 2020
# How to run: ./pic2histogram.sh <picture-filename> <output-filename>
# e.g. ./pic2histogram.sh ./ucshinthada-present.jpg ./col_hist.png

PICTURE=$1;
OUTPUT=$2;
convert ./$PICTURE -define histogram:unique-colors=false  +write histogram:$2  NULL:
