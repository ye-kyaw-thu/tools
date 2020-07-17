#!/bin/bash

# for removing heading tab, space and line no 
# How to run: ./rm-heading-tab-lineno.sh <filename>
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand 


# using perl one liner
perl -p -e 's/^[ *|\t][0-9]*\s*//g' $1

# adjust based on your data format
#perl -p -e 's/^[ |\t]*[0-9]+[ |\t]*//g' $1
