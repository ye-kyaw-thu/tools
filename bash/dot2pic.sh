#!/bin/bash

# to run this you have to install graphviz at first
# Reference link: https://stackoverflow.com/questions/1494492/graphviz-how-to-go-from-dot-to-a-graph
# this shell script is similar to "dot2png-pdf.sh"

# Written by Ye Kyaw Thu, NECTEC, Thailand
# How to run: ./dot2pic.sh <dot-filename>
# e.g. ./dot2pic.sh ./baseline_my-en.dot  

bname=`basename $1 .dot`;

# dot file to png file conversion
dot -Tpng $1 -o $bname.png

# dot file to eps file conversion
dot -Tps $1 -o $bname.eps

# dot file to svg file conversion
dot -Tsvg $1 -o $bname.svg

