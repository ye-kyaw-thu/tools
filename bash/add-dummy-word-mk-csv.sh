#!/bin/bash

# Adding a dummy word to a corpus, Checking the manual tagging errors of that corpus 
# and preparing a "tag and label only CSV file" for building classification models
# for my PhD student Ms. Cho Zin Oo (UTYCC)
# Written by Ye, LST, NECTEC, Thailand
# Date: 8 Dec 2020
# You need a cleaning script such as  skip-tag-err-lines.pl
# That  "skip-tag-err-lines.pl" is similar to "chk-pos-tags.pl", I just modify skipping possible tagging error lines
# How to run: ./add-dummy-word-mk-csv.sh <tagged corpus file-name>
# $ ./add-dummy-word-mk-csv.sh raw.txt

CORPUS=$1;

echo "Information of $CORPUS:";
echo "wc $CORPUS";
wc $CORPUS;
echo "head $CORPUS";
head $CORPUS;
echo

# remove double quotes
echo "Remove double quotes..."
sed "s/\"//g" $CORPUS > $CORPUS.rmquote;
echo "head $CORPUS.rmquote";
head $CORPUS.rmquote;
echo

# add dummy word for the last labels or classes
echo "Add dummy word for the last labels...";
sed "s/,/ dummy\//g" $CORPUS.rmquote > $CORPUS.rmquote.dummy;
head $CORPUS.rmquote.dummy;
echo

# remove manual tagging error sentences
echo "Remove manual tagging errors:";
perl skip-tag-err-lines.pl $CORPUS.rmquote.dummy > $CORPUS.rmquote.dummy.clean
echo "head $CORPUS.rmquote.dummy.clean":
head $CORPUS.rmquote.dummy.clean
echo

# Preparing tag only file
echo "Preparing tag only file...";
perl ./mk-wordtag.pl $CORPUS.rmquote.dummy.clean "\/" t > $CORPUS.rmquote.dummy.clean.tag;
echo "head $CORPUS.rmquote.dummy.clean.tag";
head $CORPUS.rmquote.dummy.clean.tag
echo

# Make CSV file for building classification models
echo "Make CSV file for building classification models";
sed "s/ /,/g" $CORPUS.rmquote.dummy.clean.tag > $CORPUS.rmquote.dummy.clean.tag.csv;
echo "head $CORPUS.rmquote.dummy.clean.tag.csv";
head $CORPUS.rmquote.dummy.clean.tag.csv;
echo
echo "wc $CORPUS.rmquote.dummy.clean.tag.csv;";
wc $CORPUS.rmquote.dummy.clean.tag.csv;
echo


