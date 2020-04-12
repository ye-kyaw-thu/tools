#!/bin/bash

# for checking blank fields
# Written by Ye Kyaw Thu, LST Lab, NECTEC, Thailand
# I assumed the input file that contained 3 fields or columns
# used this script for checking Myanmar<TAB>Rakhine<TAB>Dawei parallel corpus

# How to run: chk-blank-fields.sh <input-filename>
# ./chk-blank-fields.sh ./rk-dw.txt.shuf > out 

# Here, -F"\t" means TAB delimiter
# $1 ~ /^[[:space:]]*$/ means if field-1 matches 0, 1 or more occurrences of "space"
# Note: $1, $2, $3 inside single quotes ' ' is relating to awk command (i.e. field-1) and 
# $1 outside of ' ' is relating to bash shell (i.e. command line argument filename)
awk -F"\t" '{if(NF == 3 && $1 ~ /^[[:space:]]*$/ || $2 ~ /^[[:space:]]*$/ || $3 ~ /^[[:space:]]*$/)print NR": "$0}' $1

