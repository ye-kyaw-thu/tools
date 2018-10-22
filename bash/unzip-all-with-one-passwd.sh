#!/bin/bash

# unziping many zip files with a password
# here I assumed all zip files are zipped with the same password and used "zip" command
# written by Ye Kyaw Thu, Visiting Researcher, Waseda Univ., Japan
# last updated: 22 Oct 2018 
# usage: ./unzip-all-with-one-passwd.sh *.zip 

# Read user's password
echo -n Password: 
read -s usrPassword

#$1 is the 1st argument
$zipfile=$1;

for zipfile in *.zip;
do

   # unzipping *.zip files
   unzip -P $usrPassword $zipfile;

done
