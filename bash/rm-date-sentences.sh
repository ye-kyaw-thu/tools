#!/bin/bash

# for removing sentences that started with date format YYYY-MM-DD
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# How to use: ./rm-date-sentences.sh <filename>
# e.g. ./rm-date-sentences.sh ot-5person-200k.log 
# e.g. ./rm-date-sentences.sh ot-5person-200k.log > ot-5person-200k.log.clean 

# Here -P is for Perl-compatible  regular  expression  (PCRE) and
# -v is for selecting non-matching lines

grep -Pv "[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])" $1;
