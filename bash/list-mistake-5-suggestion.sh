#!/bin/bash

# for listing spelling mistakes and 5 spelling suggestion words
# written by Ye Kyaw Thu
# How to use: ./list-mistake-5-suggestion.sh <filename>
# e.g. ./list-mistake-5-suggestion.sh ./mistakes.txt

cat ./$1 | aspell -a \
| grep -v '*\|@' \
| sed '/^$/d' \
| sed 's/& //' \
| sed 's/\w /|||/' \
| sed 's/: /|||/' \
| cut -f1-5 -d','
