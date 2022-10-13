#!/bin/bash

## Written by Ye Kyaw Thu, Affiliate Professor, CADT, Cambodia
## Checking end-mark tags
## Last updated: 13 Oct 2022
## How to run: bash ./check-end-mark.sh <input-file> <output-file>

cat $1 | grep -o '[^/]*$' \
	| nl -s: | sed 's/^ *//g' | grep "N\|O" > $2 
