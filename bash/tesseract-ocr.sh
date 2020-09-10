#!/bin/bash

# Doing OCR with freely available Google Tesseract OCR Engine (perparing the baseline)
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 10 Sept 2020
#
# Note: At first, you have to install tesseract OCR engine on your computer
# How to run: tesseract-ocr.sh <language> <input-png-filename> <outputbase>
#e.g. ./tesseract-ocr.sh mya ./input.png myanmar-output
#e.g. ./tesseract-ocr.sh eng ./eng-monospace.png eng-monospace
#e.g. ./tesseract-ocr.sh jpn ./jpn.png japanese

LANG=$1;
PNG=$2;
OUTPUTBASE=$3;

tesseract -l $LANG $PNG $OUTPUTBASE;
cat $OUTPUTBASE.txt;
