#!/bin/bash

# espeak + zenity textbox demo
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand.
# Note: You have to install espeak in advanced.
# How to run ./espeak-and-zenity.sh

reply=1;

while [ $reply -eq 1 ]; do

   # command နှစ်ခုကို semicolon နဲ့ ခြားထားတာကို သတိပြုပါ။  
   # ပထမ command မှာတော့ zenity textbox မှာ user က ရိုက်ထည့်ပေးလိုက်တဲ့ စာကြောင်းကို text ဆိုတဲ့ variable ထဲမှာ သိမ်းပါလိမ့်မယ်။  
   # ဒုတိယ command ဖြစ်တဲ့ espeak ကို အဲဒီ သိမ်းထားတဲ့ $text ကို pass လုပ်ပြီး run ခိုင်းရင် ရိုက်ထားတဲ့ စာကြောင်းကို အင်္ဂလိပ်လို အသံထွက်ပေးပါလိမ့်မယ်။  
   bash -c 'text=$(zenity --text-info --editable --title "Text-to-Speech" --width 500 --height 100);
   espeak "$text";'

   # ဒီ နေရာမှာတအာ့ Quit တို့ espeak စတဲ့ button ရဲ့ label တန်ဖိုးတွေကို answer နဲ့ လက်ခံထားပေမဲ့ သုံးမထားပါဘူး။ လိုရမယ်ရ သုံးပြထားတာသာ ဖြစ်ပါတယ်။  
   # တကယ်တမ်း while loop ကို control လုပ်နေတာက reply ဆိုတဲ့ variable နဲ့ပါ  
   answer=$(zenity --info --title 'User Confirmation' \
      --text 'Continue or not?' \
      --ok-label 'Quit' \
      --extra-button 'espeak');
      
   reply=$?;
done
