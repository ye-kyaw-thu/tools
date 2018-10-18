#!/bin/bash

# comparing two images or pdf files
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# last updated: 19 Oct 2018

show_help() {
    echo "Usage: compare-img-or-pdf.sh <input-filename> <input-filename> <output-filename> [ no-background | color-name]"
    echo "You can compare between image files such as .jpg, .png, .bmp and also pdf"
    echo "" 
    echo "e.g.1: ./compare-img-or-pdf.sh ./errors-from-aru-corpus-white-bg.png  ./errors-from-aru-corpus-edited-white-bg.png diff1.png"
    echo "e.g.2: ./compare-img-or-pdf.sh ./errors-from-aru-corpus.pdf  ./errors-from-aru-corpus-edited.pdf diff2.png"
    echo "e.g.3: ./compare-img-or-pdf.sh ./errors-from-aru-corpus.pdf  ./errors-from-aru-corpus-edited.pdf diff3.png no-background"
    echo "e.g.4: ./compare-img-or-pdf.sh ./errors-from-aru-corpus.pdf  ./errors-from-aru-corpus-edited.pdf diff4.png green"
    exit 1
}

# $# variable tells the number of input arguments the script was passed
if [[ "$#" < "3" ]]; then

   show_help;
   exit 1;

elif [[ "$#" == "3" ]]; then
   
   # with lightened background first-input-file
   compare $1 $2 $3;

elif [[ "$#" == "4" ]] && [[ "$4" == "no-background" ]]; then

   # with transparency layer
   compare $1 $2 -compose src $3;

elif [[ "$#" == "4" ]] && [[ "$4" != "no-background" ]]; then

   # differences with user defined (i.e. $4) color
   compare $1 $2 -highlight-color $4 $3;
   #compare $1 $2 -compose src -highlight-color $4 $3;

fi

display $3;
