#!/bin/bash -v

# the example bash script for KidBright video Burmese transcription
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 12 Dec 2020

# Extract English audio only and saved as 2.mp3
ffmpeg -i '[ENG] KidBright #2 Basic Coding.mp4' 2.mp3;

# Remove audio from no caption video and saved as 2.mp4
ffmpeg -i '02 การเขียน code เบื้องต้น.mp4' -vcodec copy -an 2.mp4;

# Combining mp4  (no caption without audio) and mp3 (English audio)
ffmpeg -i 2.mp4 -i 2.mp3 -shortest ./eng-nocaption2.mp4;

# Manual Burmese transcription with ELAN
# မြန်မာလို ဘာသာပြန်ပြီး video ကို transcription လုပ်တာကတော့ ELAN software ကို သုံးပြီး လက်နဲ့ပဲ လုပ်ခဲ့ပါတယ်။
#
# If using ELAN software is your first time, see references
# Export As ===> Subtitle Text လုပ်ရင် .srt ဖိုင် ရလာလိမ့်မယ်

# Convert .srt annotation file into .ass format
 ffmpeg -i eng-voice-burmese-caption2.srt eng-voice-burmese-caption2.ass

sed  -i "s/Arial,16/Myanmar3,24/" ./eng-voice-burmese-caption2.ass
#open .ass file and find "Arial,16"
#[V4+ Styles] 
#Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
#Style: Default,Arial,16,&Hffffff,&Hffffff,&H0,&H0,0,0,0,0,100,100,0,0,1,1,0,2,10,10,10,0
#
#
# add Myanmar font filename and font size
#Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
#Style: Default,Myanmar3,24,&Hffffff,&Hffffff,&H0,&H0,0,0,0,0,100,100,0,0,1,1,0,2,10,10,10,0

# Combining video and transcription
#(base) ye@ykt-pro:/media/ye/Transcend/burmese-tran$ time ffmpeg -i ./eng-nocaption1.mp4 -vf "ass=eng-voice-burmese-caption1.ass" ./eng-caption1.mp4
time ffmpeg -i ./eng-nocaption2.mp4 -vf "ass=eng-voice-burmese-caption2.ass" ./eng-caption2.mp4;

### Reference ###

# ELAN download link: https://archive.mpi.nl/tla/elan
# Video Tutorial (Praat 1/4 - Basic overview and importing media - VILA VIDEO TUTORIALS):
# https://www.youtube.com/watch?v=GBGN_DslzrE
# Video Tutorial (Praat 2/4 - Selecting and zooming and extracting audio selctions - VILA VIDEO TUTORIALS):
# https://www.youtube.com/watch?v=wLFIjqQUSWA&t=49s
# Video Tutorial (ELAN 3/7 - Types and tiers - VILA VIDEO TUTORIALS):
# https://www.youtube.com/watch?v=whVc0yYZbwE&t=1s
# Video Tutorial (ELAN 4/7 - Annotation, Segmentation and Transcription - VILA VIDEO TUTORIALS): 
# https://www.youtube.com/watch?v=fLeUHb3KWlg&t=337s

# https://stackoverflow.com/questions/48246828/ffmpeg-utf-8-subtitles-not-properly-displayed-in-mp4-file
# http://sub.wordnerd.de/linux-subs.html

