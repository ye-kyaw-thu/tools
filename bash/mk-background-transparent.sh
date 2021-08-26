#!/bin/bash

# for making an image background transparent...
# I used this script for preparing a transparent background signature image.
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# last updated: 13 May 2021

# Reference Link:
# https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=32090
# https://legacy.imagemagick.org/discourse-server/viewtopic.php?f=1&t=36208
# https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=18196
# https://stackoverflow.com/questions/28136471/image-enhancement-solution
# https://en.wikipedia.org/wiki/SRGB

# if you want to keep foreground colour, following one command is OK
# convert ./akm-sign.png -transparent white bg-transparent-fg-color.png

imageFILE=$1;

# convert to gray scale image
convert $imageFILE -colorspace Gray -auto-level ./gray.png;

# get background color information
bgColor=`convert ./gray.png -format "%[pixel:u.p{0,0}]" info:`;

# fill background color with white color
convert ./gray.png -fuzz 50% -fill 'srgb(255,255,255)' -opaque $bgColor ./gray-white.png;

# make transparent background
convert ./gray-white.png -transparent 'srgb(255,255,255)' -fuzz 30% ./bg-transparent.png;

# check the output
display $imageFILE & display ./bg-transparent.png;

# clean temp files
rm ./gray.png ./gray-white.png;
