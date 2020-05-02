#!/bin/bash

# Converting Excel file (i.e. xlsx) to CSV (comma-separated values) files and count fields of each CSV file
# If the input Excel file have 3 sheets, you will get 3 CSV files under the folder that you specified with $2 argument 
# Written by Ye, LST Lab., NECTEC, Thailand

# Before you run this shell script, you need to install xlsx2csv python program
# Ref: https://github.com/dilshod/xlsx2csv
# Ref: https://stackoverflow.com/questions/10557360/convert-xlsx-to-csv-in-linux-with-command-line
# How to run: ./execl2csv-chk-fields.sh <Excel-filename or .xlsx file> <output-folder-name>
# e.g. ./excel2csv-chk-fields.sh ./COVID-19_Languages.xlsx output

xlsxFile=$1;
outputFolder=$2;

echo "Converting xlsx file to csv ...";
python ~/tool/xlsx2csv/xlsx2csv.py --all $xlsxFile $outputFolder;
echo "Finished conversion!";
echo "==========";
echo

for i in ./$outputFolder/*.csv;
do
   echo $i;
   printf "no. of field: ";
   head -n 1 "$i" | awk -F, '{print NF}'
done


