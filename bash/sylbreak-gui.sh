#!/bin/sh

## An example of using "zenity" GUI
## Here, accept Burmese text with zenity text entry dialog box and parse it to perl one liner for syllable breaking
## Usage: bash ./sylbreak-gui.sh
## Written by Ye Kyaw Thu, LST, NECTEC, Thailand
## Reference for the syllable breaking Regular Expression: https://github.com/ye-kyaw-thu/sylbreak
##
## Reference for the zenity GUI:
## https://www.howtogeek.com/107537/how-to-make-simple-graphical-shell-scripts-with-zenity-on-linux/
## https://linuxconfig.org/how-to-use-graphical-widgets-in-bash-scripts-with-zenity
## https://www.tecmint.com/zenity-creates-graphical-gtk-dialog-boxes-in-command-line-and-shell-scripts/
## https://www.geeksforgeeks.org/using-zenity-with-python/

# unset variables and parameters other than the special parameters ‘@’ or ‘*’
set -u
# a variable for the syllable delimiter
sepOption="|";

# variables for Burmese characters
myConsonant="က-အ"
enChar="a-zA-Z0-9"
eChar="abcdefg"
otherChar="ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-\/:-\@\[-\`{-~\\s"
ssSymbol="္"
aThat="်"

inputStr=$(zenity --entry \
   --title="Add new profile" \
   --text="Enter name of new profile:" \
   --entry-text "NewProfile");
if [ ! -z "$inputStr" ]
then
   echo $inputStr | sed "s/ //g;" | perl -CSDA -Mutf8 -e ' while(<STDIN>){$_ =~ s/($ARGV[0])/$ARGV[1]$1/g; print $_;}' "((?<!$ssSymbol)[$myConsonant](?![$aThat$ssSymbol])|[$enChar$otherChar])" $sepOption
   else echo "No text entered"
fi
