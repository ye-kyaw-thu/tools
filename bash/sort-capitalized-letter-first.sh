#!/bin/bash

# Written by Ye, LST Lab., NECTEC, Thailand
# Written for sorting capitalized letter first and then small letter 
# Used for mdpi Journal latex template, \abbreviations{Abbreviations}
# Last updated: 7 Feb 2022
# How to run:
# $ ./sort-capitalized-letter-first.sh <input-filename>
#
# Ref: https://unix.stackexchange.com/questions/162084/sort-and-ls-why-arent-capitalized-letters-sorted-first/162086

cat $1 | LC_COLLATE=C sort;
