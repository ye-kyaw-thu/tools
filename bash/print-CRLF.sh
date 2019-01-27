#!/bin/bash

# print lines containing CRLF with line number
# How to run: print-CRLF.sh <filename> 
# Written by Ye Kyaw Thu, Waseda Univ., Tokyo

# $'\xHH' syntax for hex value
# "-n" option is for printing line number
# "-U or --binary" option treat the file(s) as binary
grep -nU $'\x0D' $1
