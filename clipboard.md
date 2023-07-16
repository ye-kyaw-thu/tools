
- General ပြောဖို့တော့ ကြိုးစားမယ်​
- သို့သော် AI အကြောင်းကို ပြောမှာဖြစ်လို့ မဖြစ်မနေ ပါဝင်မှာက technical jargon တွေ ​
- Computer Science, IT, ICT ကျောင်းသားတွေ ဆိုရင်တော့ တော်တော်များများ နားလည်လိမ့်မယ်လို့ ယူဆတယ်​
- လက်တွေ့ပိုင်း Coding တချို့  run ပြတာ လုပ်မယ်​
- အနည်းဆုံးတော့ မြန်မာ NLP/AI researcher တစ်ယောက်အနေနဲ့ ဘာတွေလုပ်နေသလဲ ဆိုတာကိုတော့ မြင်သွားပါလိမ့်မယ်​
- ကိုယ်တိုင်လည်း စိတ်ဝင်စားရင် ဘာတွေ လုပ်လို့ ရမလဲ ဆိုတာတော့ သိသွားပါလိမ့်မယ်​
- Slide တွေက အင်္ဂလိပ်လိုများပေမဲ့၊ ဗမာလိုပဲ ပြောမယ်

- Turing Test နဲ့ ပတ်သက်ပြီးတော့ ဝေဖန်တာတွေ လည်း ရှိပါတယ်
- ဘာကြောင့်လဲ ဆိုတော့ လူတွေလိုမျိုး စကားအပြန်အလှန် ပြောနိုင်ဖို့က အဲဒီ စကားကို နားမလည်ရင်တောင်မှ တုပလို့ ရတာမို့ပါ
- နောက်ပြီးတော့ ဒီ Testing မှာက အသိဉာဏ် ဆိုတာနဲ့ ပတ်သက်ပြီး (စက်ရဲ့ အသိဉာဏ်ပိုင်း) ထဲထဲဝင်ဝင် ထည့်သွင်းစဉ်းစားထားတာ မရှိလို့ပါ
- ဘယ်လိုပဲ ဖြစ်ဖြစ်ပါ personal အမြင်ကတော့ ဒီ Turing Test က AI ရဲ့ သမိုင်းမှာ အရေးပါတဲ့ အခန်းကဏ္ဍ တစ်ခုပါပဲ၊ လက်ရှိ အချိန်အထိလည်း အမျာကြီး လွှမ်းမိုးမှု ရှိနေပါတယ်

------

န တဲတၢ်ကတိၤ န့ၣ် ယ ဒိကနၣ် လီၤ .	မင်း ပြောစကား ကို ကိုယ် နားထောင် ပါတယ်   
တၢ်ဝဲအံၤ န့ၣ် ကိးမုၢ်နံၤဒဲး ယ တၢ်မၤ လီၤ .	ဒါ ဟာ ကျွန်တော့် ရဲ့ နေ့စဉ် အလုပ် ပါ   
အဝဲသ့ၣ်န့ၣ် ဆီၣ်နၢၤ အဝဲ ဒ်သိး ကဆီဟံၣ်ဆီဃီ လီၤ .	သူတို့က သူ့ကို အိမ်ထောင်ပြု ဖို့ ဖိအားပေး နေတယ်   
ယမ့ၢ် ထိၣ်သတြီၤ ဒီး နၤန့ၣ် ယ လာ်အၢ လီၤ .	မင်း နဲ့ ယှဉ်လိုက်ရင် ငါ က ရုပ်ဆိုး တယ်   
န မၤစၢၤ ယၤ အဃိ ယ သးခု လီၤ .	ခင်ဗျား ကျွန်တော့်ကို ကူညီခဲ့တဲ့ အတွက်ကြောင့် ကျွန်တော် ဝမ်းသာ တယ် 
  
မ့မ့ၢ် ဖီသၣ်န့ၣ် ကဂ့ၤလီၤ .	ပန်းသီး ဆိုရင် ကောင်းမယ်   

The BLEU score is given by the formula:

$$
\text{{BLEU}} = BP \cdot \exp\left(\sum_{{n=1}}^{N}\frac{1}{N} \log p_n\right)
$$

Where:

- $\text{{BLEU}}$ is the score for the evaluated machine translation. It ranges from 0 to 1. A score of 1 means a perfect match with the reference translation.
- $BP$ is the brevity penalty. It penalizes shorter machine translations. If the length of the machine translation is less than the reference translation, then $BP = e^{1 - r/c}$, otherwise $BP = 1$. Here, $r$ is the effective reference corpus length and $c$ is the length of the machine translation.
- $p_n$ is the precision for n-gram comparisons. It is the ratio of the number of n-grams in both the machine translation and the reference translation to the number of n-grams in the machine translation.
- $N$ is the maximum order of n-grams used in the calculation. Usually, $N = 4$ is used, meaning unigrams, bigrams, trigrams, and 4-grams are considered.
- The $\exp(\cdot)$ and $\log(\cdot)$ functions are the exponential and natural logarithm functions, respectively. The logarithm function is used to convert the product of precisions to a sum in the logarithmic space.

-----------

ဒီ Dartmouth Conference က AI သမိုင်းမှာ အရေးပါတယ်​  
- တစ်ခု သိထားသင့်တာက အဲဒီ conference အပြီး 1956 နောက်ပိုင်း မှာ ဆက်လုပ်ခဲ့ကြတဲ့ AI R&D ရဲ့ တိုးတက်မှုက အရမ်းကို နှေးပါတယ်​  
- လူရဲ့ အသိဉာဏ်ကို တုပဖို့ စက်ကို သင်ကြားပေးနိုင်ဖို့၊ လူပြောတဲ့ စကားကို နားလည်နိုင်ဖို့ ကိစ္စတွေဟာ အရမ်း ရှုပ်ထွေးတဲ့ problem တွေပါလား ဆိုတာကို တဖြည်းဖြည်းနဲ့ ပိုနားလည်လာကြတယ်​  

---------


- ခုချိန်ထိ 1943 ကနေ 1956 အထိ ပြောပြီးသွားပြီ
- 1960 ကနေ 2000 အထိ တိုးတက်ပြောင်းလဲလာတဲ့ AI History ကို လေ့လာကြည့်ရင် အုပ်စု သုံးခုအဖြစ် အကြမ်းဖျဉ်းခွဲလို့ ရတယ်
- အဲဒါတွေကတော့ Rule-based, Machine Learning (ML) နဲ့ Neural Network ကို အခြေခံပြီး တိုးတက်လာတဲ့ Deep Learning ဆိုပြီးတော့
- ကွန်ပျူတာ ကျောင်းသားတွေ၊ programming အခြေခံသိတဲ့သူတွေအတွက် အဓိက ရည်ရွယ်ပြီး လက်တွေ့ ပြဿနာတစ်ခုကို တည်ပြီး၊ အဲဒီ ပြဿနာကိုပဲ Rule-based, ML (SVC), Deep learning (LSTM, Transformer) ဆိုတဲ့ approach သုံးမျိုးနဲ့ coding လုပ်၊ လက်တွေ့ run တာကို လုပ်ပြပြီး မိတ်ဆက်ပေးသွားမယ်
- အချိန်ရရင် 2010 ကနေ ခုချိန်ထိ  Transformer မော်ဒယ်ကို အခြေခံပြီး ဖြစ်လာတဲ့ AI modeling တချို့ကို ပြောမယ်။ ChatGPT 4 ကိုလည်း လက်တွေ့ သုံးပြမယ်လို့ စိတ်ကူးထားတယ်

​---------

- ဗမာစာ၊ တိုင်းရင်းသားစာ တွေအတွက် လုပ်ဖြစ်နေတဲ့ NLP R&D project တွေက အမျိုးမျိုးပါပဲ။
- တချို့ ပရောဂျက်တွေဆိုရင် ၆နှစ် ၇နှစ် မကပါဘူး။ ဥပမာ myPOS project ဆိုရင် 2015, 2016 လောက်ကတည်းက စပြီး 2017 နှစ်မှာ Github မှာ release လုပ်ပေးနိုင်တာပါ။ မနှစ်ကအထိ ဆက်လုပ်ဖြစ်နေခဲ့ပါတယ်။

​


​

​
