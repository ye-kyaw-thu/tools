#!/bin/bash

# ".dot" to ".png" and ".png" to ".pdf" file conversions 
# written by Ye, Visiting Professor, LST Lab., NECTEC, Thailand
# How to run: ./dot2png-pdf.sh <dot-filename>
# e.g. ./dot2png-pdf.sh ./graph.1.dot

pngFilename=$(basename $1 .dot).png;

dot -Tpng $1 > $pngFilename
convert $pngFilename $(basename $pngFilename .png).pdf;
