#!/bin/bash

# character segmentation
# Written by Ye, LST Lab., NECTEC, Thailand
# How to run: char-segmentation.sh <input-filename>
# e.g. ./char-segmentation.sh tmp.char 

sed 's/\(.\)/\1 /g' $1 | sed 's/ \+/ /g';

