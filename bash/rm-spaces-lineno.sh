#!/bin/bash

# for removing several spaces and line no of code
# How to run: ./rm-spaces-lineno.sh <filename>
# Written by Ye Kyaw Thu, Waseda Univ., Tokyo 

sed -E 's/^\s+[0-9]+\s//g' $1
