#!/bin/bash

# espeak + zenity textbox demo
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand.
# Note: You have to install espeak in advanced.
# How to run ./espeak-and-zenity.sh

reply=1;

while [ $reply -eq 1 ]; do

   bash -c 'text=$(zenity --text-info --editable --title "Text-to-Speech" --width 500 --height 100);
   espeak "$text";'

   answer=$(zenity --info --title 'User Confirmation' \
      --text 'Continue or not?' \
      --ok-label 'Quit' \
      --extra-button 'espeak');
      
   reply=$?;
done
