#!/bin/bash

# for counting sentenceID and no of occurrence
# Wave filename format e.g: /Univ1-HninHnin-F-25-burmese-2637.wav
# Here, OrganizationName-SpeakerName-Sex-Age-NativeLanguage-SentenceID.wav
# 
# how to run: ./print-sentenceID-count.sh ./100-wave-filenames.txt 

cat $1 | grep -oE "[0-9]+.wav$" | sed 's/.wav//' \
| sort | uniq -c | awk '{print $2, $1}' | sort -n

