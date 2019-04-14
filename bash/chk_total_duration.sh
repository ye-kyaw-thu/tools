#!/bin/bash

# check total duration of the recorded wave files
# written by Ye Kyaw Thu, NECTEC, Thailand
# how to run: chk_total_duration.sh

# Note: Don't use space for folder names

# find all wave files under current folders
find . -name "*.wav" > wavefiles.txt

# read wave filenames and pass them to "soxi" command
# for calculating the duration (in seconds) for each file
cat ./wavefiles.txt | while read -r filename
#head ./wavefiles.txt | while read -r filename # for checking quickly ...
do
   soxi -D $filename

done > secondsfile # duration seconds of each wavefile will be save


sec2hr_min_sec() {
 hr=$(bc <<< "${1}/3600")
 min=$(bc <<< "(${1}%3600)/60")
 sec=$(bc <<< "${1}%60")
 printf "%02d:%02d:%05.2f\n" $hr $min $sec
}

# if you have jq command, you can also use it as follows
#total_seconds=$(cat ./secondsfile | jq -s 'add' )

# 
total_seconds=$(cat ./secondsfile | paste -s -d+ - | bc)
echo $(sec2hr_min_sec $total_seconds)
