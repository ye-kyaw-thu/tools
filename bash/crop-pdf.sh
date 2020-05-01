#!/bin/bash

# shell script for cropping PDF file (i.e. remove empty margin of the input PDF file)
# useful for extraction of graphics/figures also
# Ref: https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
# Ref: http://manpages.ubuntu.com/manpages/precise/man1/pdfcrop.1.html
# Written by Ye, LST Lab., NECTEC, Thailand
# How to run: crop-pdf.sh <pdf-filename>
# e.g. crop-pdf.sh ./example-crop.pdf

#Extracting no of pages from pdf file:
PAGES=`pdfinfo $1 | grep Pages | grep -o '[[:digit:]]*'`
START=1;

# cropping all pages
# Note: looping with "for i in {$START..$PAGES};" is not working ...
for (( i=$START; i<=$PAGES; i++ ))
do
   pdftk ./$1 cat $i output ./pg$i.pdf;
   pdfcrop --margins "3 3 3 3" ./pg$i.pdf pg$i-crop.pdf;
   evince ./pg$i-crop.pdf;
done

