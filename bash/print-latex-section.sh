#!/bin/bash

# for extracting section, subsection and subsubsection from latex file
# written by Ye Kyaw Thu
# date: 29 Nov 2018
# how to use: print-latex-section.sh <tex-filename>

cat ./$1 | grep "subsection{\|section{" | \
sed "s/^%//" | \
sed "s/^\\\section{//" | \
sed "s/^\\\subsection{/|--/" | \
sed "s/^\\\subsubsection{/    |----/" | \
sed "s/}//" 

