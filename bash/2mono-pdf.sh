#!/bin/bash

#ref: https://superuser.com/questions/104656/convert-a-pdf-to-greyscale-on-the-command-line-in-floss

# Refer above link and added two lines for extracting only filename
# By Ye, LST Lab., NECTEC, Thailand
#How to run: ./2mono-pdf.sh ./color.pdf
#e.g. ./2mono-pdf.sh ./csjkaldisp2016oct.pdf 


basefilename=$(basename -- $1)
filename="${basefilename%.*}"

gs \
 -sOutputFile=$filename.mono.pdf \
 -sDEVICE=pdfwrite \
 -sColorConversionStrategy=Gray \
 -dProcessColorModel=/DeviceGray \
 -dCompatibilityLevel=1.4 \
 -dNOPAUSE \
 -dBATCH \
 $1
