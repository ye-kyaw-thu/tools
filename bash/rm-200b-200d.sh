#!/bin/bash

# for removing "\u200b" and "\u200d" characters from a Myanmar syllable list
# after removing "\u200b" and "\u200d" characters, change to column layout for easier checking "\u200b" and "\u200d"
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand

# How to run: ./rm-200b-200d.sh <input-file>
# e.g. ./rm-200b-200d.sh ./all.manual.uniq

sed -i -e "s/$(echo -ne '\u200b')//g; s/$(echo -ne '\u200d')//g;" $1; 
column ./all.manual.uniq > ./all.manual.uniq.column
vi ./all.manual.uniq.column

