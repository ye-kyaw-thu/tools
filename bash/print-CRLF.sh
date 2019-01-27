#!/bin/bash

# print lines containing CRLF with line number
# How to run: print-CRLF.sh <filename> 
# Written by Ye Kyaw Thu, Waseda Univ., Tokyo

grep -nU $'\x0D' $1
