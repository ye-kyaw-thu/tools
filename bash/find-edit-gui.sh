#!/bin/bash

# find all text files under current path, pass them to zenity and editing each file
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# last updated: 19 Feb 2021
# how to run: bash ./find-edit-gui.sh

reply=1;

# $reply variable က 1 ဖြစ်နေသ၍ ဒီ while loop ထဲကို ဝင်နေမှာ ဖြစ်တယ်
while [ $reply -eq 1 ]; do

   # find command နဲ့ *.txt ဖိုင်တွေကို ရှာပြီး tr command ကို လက်ဆက်ကမ်းမယ်  
   # tr command က ရှာလို့တွေတဲ့ ဖိုင်နာမည်တစ်ခုစီကို စာကြောင်းတစ်ကြောင်းစီ ဖြစ်သွားအောင် space နေရာမှာ \n (newline) နဲ့ အစားထိုးတဲ့ အလုပ်ကို လုပ်တယ်  
   # ပြီးမှ zenity command ဆီကို လက်ဆင့်ကမ်းတယ်။ zenity ရဲ့ listbox ထဲမှာ ရှာလို့တွေ့တဲ့ text ဖိုင်တွေက တန်းစီပြီး ပေါ်လာအောင် လုပ်ခိုင်းထားတယ်။  
   filePath=$(find  .  -name  '*.txt' | tr ' ' '\n' | zenity --list --title "Search Results" --text "Finding all header files.." --column "Files");

   if [ "$filePath" != "" ]
   then
      # ဒီအောက်က လေးကြောင်းကတော့ zenity နဲ့ simple text editor လိုမျိုး သုံးလို့ ရအောင် ရေးထားတဲ့အပိုင်းဖြစ်ပါတယ်။
      # $filePath ထဲမှာ ရှိနေတဲ့ ဖိုင် ကို cat နဲ့ တစ်ကြောင်းခြင်းစီ ရိုက်ထုတ်ပြီးတော့ data variable ထဲကို ထည့်သိမ်းထားပါတယ်။
      data=$(cat "$filePath");
      # user ကိုတော့ အဲဒီဖိုင်ကို zenity --text-info နဲ့ ဖွင့်ပြပါတယ်။ ပြီးတော့ ပြင်ဆင်မှုတွေလုပ်နိုင်အောင်လို့ --editable ဆိုတဲ့ option ကိုပေးထားပါတယ်။
      newData=$(echo -n "$data" | zenity --text-info --editable --width 650 --height 400)
      # 
      savePath=$(echo -n "$(zenity --file-selection --filename="$filePath" --save --confirm-overwrite)")
      echo -n "$newData" > $savePath;
   fi
      # confirmation box ကို info dialogue အနေနဲ့ပဲ အလွယ်လုပ်ထားပါတယ်။ တခြား Yes/No box ဘာညာနဲ့ ပြောင်းရေးကြည့်လို့ ရပါတယ်။
      # ပုံမှန်အားဖြင့် info dialogue box မှာက OK button တစ်ခုပဲ ပါတာပါ။ ဒီနေရာမှာတော့ အဲဒီ button ကို "Quit" ဆိုပြီး ပေါ်အောင် ပြောင်းထားပါတယ်။
      # ပြီးတော့ --extra-button ဆိုတဲ့ option နဲ့ button အသစ် တစ်ခုကို တိုးယူထားပြီးတော့ "Editor" ဆိုတဲ့ label ကို ထိုးထားတာကို တွေ့ရပါလိမ့်မယ်။
      # Info box မှာ OK button ကို နှိပ်ရင် "0" ဆိုပြီး reply ပြန်မှာ ဖြစ်ပါတယ်။
      # ထပ်တိုးထားတဲ့ button ကို နှိပ်ရင်တော့ reply variable မှာက "1" ဆိုပြီး ဝင်မှာ ဖြစ်ပါတယ်။
      answer=$(zenity --info --title 'User Confirmation' \
         --text 'Continue or not?' \
         --ok-label 'Quit' \
         --extra-button 'Editor');

   reply=$?;
done

