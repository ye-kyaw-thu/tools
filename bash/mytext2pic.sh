#!/bin/bash

# make "png files" for each Myanmar sentence from the input file
# written by Ye Kyaw Thu, Language Understanding Lab., Pyin Oo Lwin, Myanmar
# Note: you need "mytext.tex" latex file and your file that contained Myanmar sentences
# under the same folder with "mytext2pic.sh"
#
# Last updated: 19 June 2020 
# How to run: bash ./mytext2pic.sh <input-file>
# e.g. bash ./mytext2pic.sh ./mytxt4png.txt
# output files: line1.png, line2.png, line3.png ...

# Ref: https://tex.stackexchange.com/questions/34054/tex-to-image-over-command-line/34058#34058
# Ref: http://phyletica.org/tex-equations-on-cmd-line/

count=1;

cat $1 | while read -r line
do
   xelatex "\def\mytext{${line}}\input{mytext.tex}"
   convert -density 300 mytext.pdf -quality 90 line$count.png
   ((count++))
done

