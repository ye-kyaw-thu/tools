#!/bin/bash

# for converting Myanmar text file into PDF file
# written by Ye Kyaw Thu (Researcher, Waseda Univ., Tokyo, Japan)
# How to run: mytxt2pdf.sh <text filename> <output PDF filename>
# e.g. mytxt2pdf.sh input.txt output.pdf
 

pandoc --variable mainfont="Myanmar3" --latex-engine=xelatex $1 -o $2
