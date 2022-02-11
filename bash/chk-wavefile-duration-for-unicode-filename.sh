#!/bin/bash

#!/bin/bash

# check total duration of the recorded wave files
# written by Ye Kyaw Thu, NECTEC, Thailand
# Based on the previous program (https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk_total_duration.sh)
# Last updated: 11 Feb 2022
# how to run: ./chk-wavefile-duration-for-unicode-filename.sh

# Reference
# https://askubuntu.com/questions/343727/filenames-with-spaces-breaking-for-loop-find-command
# https://stackoverflow.com/questions/3001177/how-do-i-grep-for-all-non-ascii-characters
# https://www.baeldung.com/linux/find-non-ascii-chars
# perl -ne 'print if /[^[:ascii:]]/' text-file.txt

# removing existing wavefiles.txt
rm wavefiles.txt;

# internal field separator
IFS=$'\n';

#for FILE in `find . -name *.wav`; do

# get only filenames with Myanmar name
for FILE in `find . -name *.wav | perl -ne 'print if /[^[:ascii:]]/'`; do
    echo $FILE >> wavefiles.txt
    soxi -D $FILE 
done > secondsfile

# function for converting seconds to hour, minute and second
sec2hr_min_sec() {
 hr=$(bc <<< "${1}/3600")
 min=$(bc <<< "(${1}%3600)/60")
 sec=$(bc <<< "${1}%60")
 printf "%02d:%02d:%05.2f\n" $hr $min $sec
}

# if you have jq command, you can also use it as follows
#total_seconds=$(cat ./secondsfile | jq -s 'add' )

# read secondsfile line by line and connect with "+" sign and pass to "bc" command
total_seconds=$(cat ./secondsfile | paste -s -d+ - | bc)
echo $(sec2hr_min_sec $total_seconds)
