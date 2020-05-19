#!/bin/bash

# for changing format of POS tagged Korean sentences
# Written by Ye, LST Lab., NECTEC, Thailand
# input: ['학생|NNG', '시절|NNG', '을|JKO', '돌아보|VV', '다|EF', '.|SF']
# output: 학생|NNG 시절|NNG 을|JKO 돌아보|VV 다|EF .|SF

# How to run: cat <input-filename> | ./change-format.sh
# or
# ./change-format.sh < input-filename>
#
# e.g. cat ./eg.ko.pos.txt | ./change-format.sh
# e.g. ./change-format.sh < ./eg.ko.pos.txt


cat - | sed "s/[][',]//g"
