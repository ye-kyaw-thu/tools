#!/bin/bash

# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# for searching x-letter word (e.g. 1 letter words, 2 letter words, 3 letter words ...)
# here, you need word segmented input file.
# of course, if you input syllable segmented input file,
# it will works for searching 1 letter syllables, 2 letter syllables, 3 letter syllables etc.
# no of letter is given by no of dots as command line argument no. 3,
# How to run: ./x-letter-word.sh <input-file> <no-of-letters> <option>
# two options; -show for "showing matched words",
# -count for "just counting" and it is also a default option
#
# e.g. input file named syl.txt as follows:
# စာ ရေး ရဲ ရင် ရေး ကြည့်
# ကျော် ကြား ရဲ ကျော် ကြား ကြည့်
# အ ခု လို လွတ် လပ် မှာ မ ဟုတ် ဘူး

# demo running:
# lar@lar-air:/media/lar/Transcend/to-code/morph$ ./x-letter-word.sh ./syl.txt ...
# 7
# lar@lar-air:/media/lar/Transcend/to-code/morph$ ./x-letter-word.sh ./syl.txt ... -show
# ရေး
# ရင်
# ရေး
# လို
# လပ်
# မှာ
#ဘူး

if [ "$3" == "-show" ]; then 
   tr ' ' '\n' < $1 | grep -o '^'$2'$';
elif [ "$3" == "-count" ] || [ "$3" == "" ]; then
   tr ' ' '\n' < $1 | grep -c '^'$2'$';
fi

