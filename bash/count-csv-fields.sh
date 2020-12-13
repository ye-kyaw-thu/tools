#!/bin/bash

#for counting fields of CSV file
# Written by Ye, LST, NECTEC Lab
# How to run: bash ./count-csv-fields.sh <csv-filename>

head -n 1 $1 | sed 's/[^,]//g' | wc -c
