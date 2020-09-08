#!/bin/bash

# converting mp4 movie file into animated GIF image
# Ye, LST Lab., NECTEC, Thailand
#reference: https://askubuntu.com/questions/648603/how-to-create-an-animated-gif-from-mp4-video-via-command-line
# movie file link: https://www.youtube.com/watch?v=XUXFCm2h2zk
# (used download mp4 file from YouTube)
# How to run: mp42gif.sh <mp4-filename>
# e.g. $ ./mp42gif.sh ./AlbertEinsteinInHisOfficeAtPrincetonUniversity.mp4 


FILE=$1;
# တစ်ခု သတိထားရမှာက example ပြထားတာက filename.ext လိုမျိုးဖိုင်နာမည်နဲ့ပါ
# တကယ်လို့ extension က နှစ်ခု ပါရင် ဥပမာ filename.ext1.ext2 ဆိုရင် ${FILE%%.*} လုပ်ရပါလိမ့်မယ်
filename=${FILE%.*};

# make a dractory named "frames"
mkdir -p ./frames

# extracting frames from mp4 video
# "-r" option က FPS value အတွက်ပါ
# quality ကောင်းကောင်းလိုချင်ရင်တော့ နံပါတ်ကိုကြီးကြီးပေးရလိမ့်မယ်
# တစ်ခုရှိတာက နံပါတ်ကြီးကြီးပေးရင် frame ပုံတွေလည်း အများကြီးထွက်လာမှာ ဖြစ်တယ်
ffmpeg -i $1 -r 5 'frames/frame-%03d.jpg'

cd ./frames

# jpg ဖိုင်တွေကိုအားလုံးကိုတွဲပြီးတော့ gif ဖိုင်အဖြစ် ပြောင်းဖို့အတွက် conert command ကို သုံးလိုရတယ်
# -delay option က ffmpeg command ရဲ့ -r option နဲ့ ညှိဖို့ လိုအပ်တယ်
# -delay 10 ထားရင် 10 frames per second ပါ၊ -delay 20 ထားရင် 5 frames per second
# -delay 25 ထားရင် 4 fps, -delay 50 ထားရင် 2fps, -delay 100 ထားရင် 1 fps ဖြစ်ပြီးတော့
# အကြမ်းမျဉ်း ပြောရရင် 100/delay = fps
convert -delay 10 -loop 0 *.jpg $filename.gif

# viewing the output gif image with eog (Eye of Gnome) command
eog $filename.gif

# စိတ်ဝင်စားမယ့် သူများအတွက် bonus shell code ပါ
# gif ကနေ original picture တွေ ကို ပြန်ဆွဲထုတ်ချင်တယ်ဆိုရင်လည်း လွယ်ပါတယ်
# convert command ရဲ့ -coalesce option ကို သုံးပြီးတော့ အောက်ပါ ဥပမာအတိုင်း run ပါ။
# convert -verbose -coalesce ./AlbertEinsteinInHisOfficeAtPrincetonUniversity.gif eg-out.png

