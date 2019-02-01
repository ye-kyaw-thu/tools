#!/bin/bash

# Split up a PDF file into two by even and odd pages
# Written by Ye Kyaw Thu, Waseda Univ., Tokyo, Japan
# You need pdftk. If you don't have: sudo apt install pdftk
# How to run: bash split-even-odd-pdf.sh <pdf-filename>
 
#Extracting no of pages from pdf file:
PAGES=`pdfinfo $1 | grep Pages | grep -o '[[:digit:]]*'`

echo "Total pages in your PDF file: $PAGES";

#Splitting pages:
pdftk $1 cat odd output odd.pdf;
echo "No. of pages of odd.pdf: " `pdfinfo odd.pdf | grep Pages | grep -o '[[:digit:]]*'`

pdftk $1 cat even output even.pdf;
echo "No. of pages of even.pdf: " `pdfinfo even.pdf | grep Pages | grep -o '[[:digit:]]*'`
