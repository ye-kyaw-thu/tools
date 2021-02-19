#!/bin/bash

# find all text files under current path, pass them to zenity and editing each file
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# last updated: 19 Feb 2021
# how to run: bash ./find-edit-gui.sh

reply=1;
while [ $reply -eq 1 ]; do

   filePath=$(find  .  -name  '*.txt' | tr ' ' '\n' | zenity --list --title "Search Results" --text "Finding all header files.." --column "Files");

   if [ "$filePath" != "" ]
   then
      data=$(cat "$filePath");
      newData=$(echo -n "$data" | zenity --text-info --editable --width 650 --height 400)
      savePath=$(echo -n "$(zenity --file-selection --filename="$filePath" --save --confirm-overwrite)")
      echo -n "$newData" > $savePath;
   fi
      answer=$(zenity --info --title 'User Confirmation' \
         --text 'Continue or not?' \
         --ok-label 'Quit' \
         --extra-button 'Editor');

   reply=$?;
done

