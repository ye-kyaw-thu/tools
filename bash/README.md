အောက်ပါ bash shell script ပရိုဂရမ် တစ်ခုချင်းစီရဲ့ အသုံးပြုပုံကို [example-usages.md](https://github.com/ye-kyaw-thu/tools/blob/master/bash/example-usages.md) ဖိုင်မှာ ရှင်းပြထားပါတယ်။  

# TOC of bash Scripts

1. [read-and-move.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/read-and-move.sh)  
(text ဖိုင်ထဲမှာရှိတဲ့ ဖိုင်နာမည်တွေကို တဖိုင်ချင်းဖတ်ပြီးတော့ ကိုယ်ရွှေ့ချင်တဲ့ ဖိုလ်ဒါအောက်ကို ရွှေ့ပေးဖို့ အတွက် သုံးခဲ့တယ်)  

2. [change-filenames.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/change-filenames.sh)  
(လက်ရှိရောက်နေတဲ့ path အောက်မှာ ရှိတဲ့ဖိုလ်ဒါတွေအထဲက ဖိုင်တွေကို နာမည်ပြောင်းဖို့အတွက် သုံးရန်။  
  ဖိုင်နာမည်ကို နာမည်ပြောင်းတဲ့အခါမှာ ဖိုလ်ဒါရဲ့ နာမည်ကိုပါ ယူသုံးပြထားပါတယ်။)  
  
3. [rm-date-sentences.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-date-sentences.sh)  
(log ဖိုင်ထဲကနေ YYYY-MM-DD format နဲ့ ရေးထားတဲ့ ရက်စွဲတွေ ဥပမာ 2018-10-16 လိုမျိုး ရက်စွဲတွေနဲ့ စတဲ့စာကြောင်းတွေကို ဖယ်ဖို့အတွက် သုံးခဲ့တယ်)  

4. [print-classID-prediction-result.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-classID-prediction-result.sh)  
(image classification testing လုပ်စဉ်မှာ သိမ်းထားတဲ့ log ဖိုင်ထဲကနေ၊ Class-ID အလိုက် confusion-matrix graph ဆွဲဖို့အတွက်  
မှန်မှန်ကန်ကန် classification လုပ်ပေးနိုင်တဲ့ အရေအတွက်၊ မှားပြီးတော့ classification လုပ်ထားတာတွေကို ရေတွက်ဖို့အတွက် သုံးခဲ့တယ်)  

5. [compare-img-or-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/compare-img-or-pdf.sh)  
(image ဖိုင်နှစ်ခု သို့မဟုတ် pdf ဖိုင်နှစ်ခုကို ပုံအနေနဲ့နှိုင်းယှဉ်ပြီးတော့ မတူတာကို ကြည့်ဖို့အတွက် သုံးခဲ့တယ်။ မှားရိုက်ထားတဲ့ မြန်မာစာလုံးတွေကို မှန်တာနဲ့ယှဉ်ပြဖို့အတွက် သုံးနိုင်တယ်။)  

6. [chk-sort-by-columns.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk-sort-by-columns.sh)
(input-file ရဲ့ columnအလိုက် sorting စီပေးဖို့အတွက် ရေးခဲ့တယ်။ ဥပမာ columnက ၄ ခုရှိရင် ပထမဆုံး column1 နဲ့ sorting စီပေးမယ်၊ ပြီးရင် column2 နဲ့ စီပေးမယ်၊ column3, column4 စသည်ဖြင့် အသီးသီး sorting စီပေးပြီး column တစ်ခုစီအတွက် output ဖိုင်တစ်ခုစီ ထုတ်ပေးပါလိမ့်မယ်။ sorting မစီခင်မှာ ဂဏန်းတွေကိုရိုက်ထားတဲ့ column ဖြစ်နေသလားဆိုတာကို check လုပ်ပြီး၊ ဖြစ်နေရင် numerical sorting လုပ်ပေးပါလိမ့်မယ်။)  

7. [kill-all-detached.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/kill-all-detached.sh)  
(server တစ်ခုခုကို terminal ချိတ် run ကြတဲ့အခါမှာ screen ဆိုတဲ့ command ကိုခံပြီးမှ ကိုယ်လုပ်စရာရှိတာကို လုပ်လေ့ရှိပါတယ်။ တရက်တရက် server တွေမှာ ဝင်လိုက်ထွက်လိုက် နဲ့ အလုပ်လုပ်ရင်း detached ဖြစ်နေတဲ့ screen session တွေအားလုံးကို kill လုပ်ဖို့အတွက် ရေးခဲ့တဲ့ script ပါ။ အသုံးဝင်ပါလိမ့်မယ်။)  

8. [unzip-all-with-one-passwd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/unzip-all-with-one-passwd.sh)  
(zip command နဲ့ password တစ်ခုတည်းသုံးပြီးတော့ ချုံ့ထားတဲ့ ဖိုင်တွေကို ဖြေဖို့အတွက် ရေးခဲ့ပါတယ်။)

9. [cut-filename.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/cut-filename.sh)  
(argument ကနေ pass လုပ်ပေးလိုက်တဲ့ path/filename ကနေ ဖိုင်နာမည်ကို ဆွဲထုတ်တာ၊ path ကိုပဲ ဆွဲထုတ်တာ၊ extension မပါပဲ ဖိုင်နာမည်ကိုပဲ ဆွဲထုတ်တာ၊  
extension ကိုပဲ သပ်သပ် ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့ပါတယ်။)  

