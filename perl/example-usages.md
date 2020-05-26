# Example usages of perl programs

မှတ်ချက်။ ။ perl ပရိုဂရမ်တွေရဲ့ အသုံးပြုနည်းကို ဥပမာအဖြစ် စမ်းသုံးပြထားသော test-data ဖိုင်အများစုက အင်တာနက်ပေါ်က စာကြောင်းတွေကို တိုက်ရိုက်ယူသုံးထားသောကြောင့် စာလုံးပေါင်းမှားတာမျိုး၊ စာကြောင်းတွေက နားလည်ရခက်တာမျိုးလည်း ရှိနိုင်တာကို နားလည်ပေးကြပါ။  

## 1.[clean-space.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-space.pl)

```bash
lar@lar-air:~/tool/perl$ cat ./tst-input 
This is  a car.
  This is       a cat.


cat is a cat.     

Blue

B l     u           e    


lar@lar-air:~/tool/perl$ perl ./clean-space.pl ./tst-input 
This is a car.
This is a cat.
cat is a cat.
Blue
B l u e
lar@lar-air:~/tool/perl$
```

## 2.[rm-EnglishSentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-EnglishSentences.pl)

```bash
lar@lar-air:~/tool/perl$ cat tst-input2
မြန်မာစာ နဲ့ English
မြန်မာစာ နဲ့ အင်္ဂလိပ်စာ
ကခဂ နဲ့ abc
ကခဂ နဲ့ အေဘီစီ
Do you speak English?
အင်္ဂလိပ်စကား ပြောနိုင်လား။

ဘာလုပ်နေတာလဲ။ thinking လုပ်နေတာလား။
က a ခ b ဂ c
a b c d e f g

lar@lar-air:~/tool/perl$ perl ./rm-EnglishSentences.pl ./tst-input2 
မြန်မာစာ နဲ့ အင်္ဂလိပ်စာ
ကခဂ နဲ့ အေဘီစီ
အင်္ဂလိပ်စကား ပြောနိုင်လား။
```
## 3.[word-analysis.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/word-analysis.pl)

```bash
lar@lar-air:~/tool/perl$ ./word-analysis.pl ./10-lines 
4 word(s) sentence(s) : 
	10 : ၇ နာရီ ပါ ။
total: 1

6 word(s) sentence(s) : 
	3 : ညစာ က ဘယ် အချိန် လဲ ။
total: 1

9 word(s) sentence(s) : 
	9 : ဥပမာ ရောန်ဂွန်း ကို ရန်ကုန် ဟု အစားထိုး ခဲ့ သည် ။
total: 1

11 word(s) sentence(s) : 
	7 : မျူနီစီပယ် ရပ်ကွက် ၃၈ ၊ အိမ်ခြေ ပေါင်း ၃၅ဝဝဝ ခန့် ရှိ ၏ ။
total: 1

19 word(s) sentence(s) : 
	8 : အမည်ရင်း ကိုလှ ဖြစ် ပြီး ၂၆ စက်တင်ဘာ ၁၉၁၇ တွင် ပုစွန်တောင် ရေကျော်ရပ် ၌ ဦးဖိုးထင် ဒေါ်သင်းမြိုင် တို့ က ဖွားမြင် ခဲ့ သည် ။
total: 1

21 word(s) sentence(s) : 
	2 : ဗိုင်ဩလိုဂျီ သည် သက်ရှိ အရာ သို့မဟုတ် သဇီဝ တို့ နှင့် ပတ်သက် သော အကြောင်း အကျိုး တို့ ကို လေ့လာ သော သိပ္ပံ ပညာရပ် ဖြစ် သည် ။
total: 1

27 word(s) sentence(s) : 
	5 : GOS တွက်ချက် ရန် စုစုပေါင်း ထုတ်လုပ် မှု စရိတ် မှ ကုန်ကျငွေ တစ်စိတ်တစ်ပိုင်း ကို သာ နုတ်ယူ တွက်ချက် ထား ခြင်း ဖြစ် သော်လည်း သာမန် အားဖြင့် အမြတ်စွန်း ရရှိ သည့် ငွေ ဖြစ် သည် ။
total: 1

32 word(s) sentence(s) : 
	6 : တွေ့ဆုံ ရာတွင် ဗိုလ်ချုပ် အောင်ဆန်း သည် မိမိ ကိုယ် မိမိ မြန်မာ နိုင်ငံ ယာယီ အစိုးရ ၏ ကိုယ်စားလှယ် အဖြစ် မိတ်ဆက် ပြီး ၊ မဟာမိတ် စစ် ဦးစီး တစ် ဦး အဖြစ် အသိအမှတ်ပြု ရန် ရဲရဲတင်းတင်း တောင်းဆို လိုက် ပါ သည် ။
total: 1

34 word(s) sentence(s) : 
	1 : စိုက်ပျိုး ရေး သည် နိုင်ငံ ၏ အဓိက လုပ်ငန်း ဖြစ် သော်လည်း များပြား သော လူဦးရေ ၏ စား ဝတ် နေ ရေး ဖူလုံ စေရန် အိန္ဒိယ နိုင်ငံ သည် စက်မှု နိုင်ငံ အဖြစ် သို့ အရှိန် ကောင်းကောင်း ဖြင့် ချီတက် လျက် ရှိ သည် ။
total: 1

35 word(s) sentence(s) : 
	4 : အစော ဆုံး ခိုင်မာ သည့် သမိုင်း အထောက်အထား မှာ ၁၅၈၆ ၁၅၈၈ အတွင်း မြန်မာ နိုင်ငံ သို့ ရောက် ရှိ လာ ခဲ့ သည့် အင်္ဂလိပ် လူမျိုး ခရီးသွား RalphFitch ၏ မှတ်တမ်း ဖြစ် ပြီး ၎င်း က Cosmin မြို့ ဟု မှတ်သား ခဲ့ သည် ။
total: 1

Average words per line : 19.80

lar@lar-air:~/tool/perl$ ./word-analysis.pl ./10-lines longest-shortest
Longest sentence : 35 words
	4 : အစော ဆုံး ခိုင်မာ သည့် သမိုင်း အထောက်အထား မှာ ၁၅၈၆ ၁၅၈၈ အတွင်း မြန်မာ နိုင်ငံ သို့ ရောက် ရှိ လာ ခဲ့ သည့် အင်္ဂလိပ် လူမျိုး ခရီးသွား RalphFitch ၏ မှတ်တမ်း ဖြစ် ပြီး ၎င်း က Cosmin မြို့ ဟု မှတ်သား ခဲ့ သည် ။
total : 1


Shortest sentence : 4 word(s)
	10 : ၇ နာရီ ပါ ။
total : 1

Average words per line : 19.80

lar@lar-air:~/tool/perl$ ./word-analysis.pl ./10-lines count
4 word(s) : 1 sentence(s)
6 word(s) : 1 sentence(s)
9 word(s) : 1 sentence(s)
11 word(s) : 1 sentence(s)
19 word(s) : 1 sentence(s)
21 word(s) : 1 sentence(s)
27 word(s) : 1 sentence(s)
32 word(s) : 1 sentence(s)
34 word(s) : 1 sentence(s)
35 word(s) : 1 sentence(s)
Average words per line : 19.80
```  
## 4.[print-emojiSentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-emojiSentences.pl)   

```bash

lar@lar-air:~/tool/perl$ perl ./print-emojiSentences.pl ./tst-emoji 
သူက ဆေးမမှီတော့ဘူးရူးနေတာသိရဲ့လား ရူးတာမှရိုးရိုးအရူးမဟုတ်ဘူး လင်တရူး... 😂😂😂
😂😂😂😂
စိတ်ဝင်စားတယ်😝
သာဓုပါတော်😜😜😜
ဘေရှိလဲ ဖတ်မရဘူး 😏😏😏
ဖြေးဖြေးဆဲကြနော်😂😂😂😂😂
ဆေးလာမထိုးနဲ့ 😒
လက်ညောင်းတယ် 😆😆😆
ကွန်မန့်ကိုပဲ ဖတ်တော့ သတင်းပြည့်စုံတာပေါ့ 😎
မီယမ်မာပြည်ကြီးကို မကောင်းဘူးထင်တဲ့လူတေသိပလား😂😂😂
😁😁😁
ပင်နယ်ဒို ပါဆို 😂
ပြည်တွင်းမှာဆန်ဈေးကျတာပေါ့😁
😂😆
😃😃😃😃😃😃
ငါတို့ အရှေ့တောင်အာရှကိုလဲ အလှည့်ပေးဦးလေ 😁😁😁
ရန်ကုန် ဒလ မြစ်ကူးတံတားကြီး အမြန်ဆောက်ပါ စေ 🙏🙏🙏
ခင်လှိုင်လဲငါ့လိုပဲ ရွာပြင်ရောက်တော့ မယ်🙈🙈🙊😃

lar@lar-air:~/tool/perl$ perl ./print-emojiSentences.pl ./tst-emoji r
မြန်မြန်သွား
ဘယ်သူက ပြောတာလဲ
တရားနဲ့သာ ဖြေပါ။
မသိသလိုပဲ နေနေတယ်။
ကျေးဇူးတင်ပါတယ်။
နေမကောင်းဘူးလား
ဖုန်းဆက်ကွာ
စစ်ကားတွေကို ငယ်ငယ်တုန်းက ကြိုက်ခဲ့တယ်။ အခုတော့ ကြည့်ချင်စိတ်ကို မရှိတော့ပါဘူး။
မရတော့ပါဘူး။
ဝမ်းသာတယ်
အမြဲတမ်း သူတို့ပဲ နိုင်နေတာပဲကွာ
ပျော်ပျော်နေကြပါ

lar@lar-air:~/tool/perl$ perl ./print-emojiSentences.pl ./tst-emoji c
မြန်မြန်သွား
သူက ဆေးမမှီတော့ဘူးရူးနေတာသိရဲ့လား ရူးတာမှရိုးရိုးအရူးမဟုတ်ဘူး လင်တရူး... 
ဘယ်သူက ပြောတာလဲ
စိတ်ဝင်စားတယ်
သာဓုပါတော်
တရားနဲ့သာ ဖြေပါ။
ဘေရှိလဲ ဖတ်မရဘူး 
မသိသလိုပဲ နေနေတယ်။
ကျေးဇူးတင်ပါတယ်။
ဖြေးဖြေးဆဲကြနော်
နေမကောင်းဘူးလား
ဆေးလာမထိုးနဲ့ 
ဖုန်းဆက်ကွာ
လက်ညောင်းတယ် 
ကွန်မန့်ကိုပဲ ဖတ်တော့ သတင်းပြည့်စုံတာပေါ့ 
စစ်ကားတွေကို ငယ်ငယ်တုန်းက ကြိုက်ခဲ့တယ်။ အခုတော့ ကြည့်ချင်စိတ်ကို မရှိတော့ပါဘူး။
မီယမ်မာပြည်ကြီးကို မကောင်းဘူးထင်တဲ့လူတေသိပလား
မရတော့ပါဘူး။
ပင်နယ်ဒို ပါဆို 
ပြည်တွင်းမှာဆန်ဈေးကျတာပေါ့
ဝမ်းသာတယ်
အမြဲတမ်း သူတို့ပဲ နိုင်နေတာပဲကွာ
ငါတို့ အရှေ့တောင်အာရှကိုလဲ အလှည့်ပေးဦးလေ 
ပျော်ပျော်နေကြပါ
ရန်ကုန် ဒလ မြစ်ကူးတံတားကြီး အမြန်ဆောက်ပါ စေ 
ခင်လှိုင်လဲငါ့လိုပဲ ရွာပြင်ရောက်တော့ မယ်

```

## 5.[dq-multilines.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/dq-multilines.pl)

```bash

lar@lar-air:~/tool/perl$ cat ./dq-tst 
"Hello
Who
are
you?"
abc
def
"abc
def"
This is a car
"This
is
a
cat."

lar@lar-air:~/tool/perl$ perl ./dq-multilines.pl ./dq-tst -raw
"Hello
Who
are
you?"
"abc
def"
"This
is
a
cat."

lar@lar-air:~/tool/perl$ perl ./dq-multilines.pl ./dq-tst -single
"Hello Who are you?"
"abc def"
"This is a cat."

lar@lar-air:~/tool/perl$ perl ./dq-multilines.pl ./dq-tst -remove
abc
def
This is a car


```

## 6.[mk-abstract-para.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-abstract-para.pl)

```bash
lar@lar-air:~/tool/perl$ cat ./NAACL-HLT-2016-abstract.txt 
This paper presents an study of the use of in-
terlocking phrases in phrase-based statistical
machine translation. We examine the effect on
translation quality when the translation units
used in the translation hypotheses are allowed
to overlap on the source side, on the target side
and on both sides. A large-scale evaluation
on 380 language pairs was conducted. Our
results show that overall the use of overlap-
ping phrases improved translation quality by
0.3 BLEU points on average. Further analysis
revealed that language pairs requiring a larger
amount of re-ordering benefited the most from
our approach. When the evaluation was re-
stricted to such pairs, the average improve-
ment increased to up to 0.75 BLEU points
with over 97% of the pairs improving. Our
approach requires only a simple modification
to the decoding algorithm and we believe it
should be generally applicable to improve the
performance of phrase-based decoders.

lar@lar-air:~/tool/perl$ perl ./mk-abstract-para.pl ./NAACL-HLT-2016-abstract.txt 
This paper presents an study of the use of interlocking phrases in phrase-based statistical machine translation. We examine the effect on translation quality when the translation units used in the translation hypotheses are allowed to overlap on the source side, on the target side and on both sides. A large-scale evaluation on 380 language pairs was conducted. Our results show that overall the use of overlapping phrases improved translation quality by 0.3 BLEU points on average. Further analysis revealed that language pairs requiring a larger amount of re-ordering benefited the most from our approach. When the evaluation was restricted to such pairs, the average improvement increased to up to 0.75 BLEU points with over 97% of the pairs improving. Our approach requires only a simple modification to the decoding algorithm and we believe it should be generally applicable to improve the performance of phrase-based decoders.

```

## 7.[print-mySentenceOnly.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-mySentenceOnly.pl)

```
$ cat ./tst4mySentenceOnly.txt 
မောင်မောင်ကို အင်္ဂလိပ်လို Mg Mg လို့ရေးတယ်။
မောင်မောင် ကို ဂျပန်လို ကော ဘယ်လိုရေးသလဲ။
မောင်မောင် ကို ဂျပန်လို マウン・マウン လို့ရေးတယ်။
ရဲကိုကော ဂျပန်လို ဘယ်လို+လဲ။
ရဲကိုတော့ ဂျပန်လိုイェလိုပေါင်းတယ်။
မင်္ဂလာပါကို ထိုင်းလိုဆိုရင် ဘယ်လို ရေးသလဲ။
မင်္ဂလာပါ ကိုထိုင်းလိုက สวัสดี လို့ရေးတယ်။
မင်္ဂလာပါကို တရုပ်လို ဘယ်လိုရေးသလဲ။
မင်္ဂလာပါကို တရုပ်လိုတော့ 你好 လို့ရေးတယ်။
မင်္ဂလာပါကို ဟင်ဒီလိုဘယ်လို ရေးသလဲ။
မင်္ဂလာပါကို ဟင်ဒီလိုက नमस्ते ရေးပါတယ် ။
ဟေး!!!
နေကောင်းလား?
"ကျန်းမာပါတယ်" ကွာ
`ကြားရတာ ဝမ်းသာတယ်` ဗျို့
Mg Mg ကို မြန်မာလို မောင်မောင်လို့ရေးကြတယ်။
$ ဈေးတွေက တက်နေတယ်ဆို။
ဟေး~!
 (၁၀၀ ကျပ်) လို့ရေးထားတယ်
မဟုတ်ပါဘူးကွာ [၁၀၀၀ ကျပ်] လို့ရေးထားတယ်
ဒုံး . . ဒုံး . . . ဒုံး . .
သာ ဓု . . . သာ ဓု . . . သာ ဓု
မွေး နေ့ မှ သည် - - - - - - နောင် နှစ် ပေါင်း များ စွာ
~ အ စိုး ရ ဝန် ထမ်း
( ၂ ) ဘဏ် စာ ရင်း ရှင်း တမ်း
အောင် မြင် ပါ စေ "
ချို သဲ 🤭🤭🤭🤭🤭🤭
မ ဂၤ လာ ပါ
အား ပေး နေ ပါ တယ် . .💪💪💪
ချစ် စ ရာ လေး : - * : - * 
👍
၂၃၄၅ ၈၉၀ ၉၉၉၉ ၀၀၀၀၂
( ဂ ) အ ကန့် အ သတ် ရှိ
[ ဂ ] အ ကန့် အ သတ် မ ရှိ
" " "ပြဿနာ" " "
၎င်း က လည်း သက်သေပါပဲ
ညီမလေး 👋
☑ အမှတ်ပေး လိုက်ပါတယ်
အများကြီး လှူနိုင်ပါစေ ☺️☺️☺️
မန္တလေးမှာ နေပါတယ်
မြန်မြန်, သွားမှ ဖြစ်မယ်
အားးးးးး
မ လာ နဲ႔
မဂၤႅာပါ

$ perl ./print-mySentenceOnly.pl ./tst4mySentenceOnly.txt 
မောင်မောင် ကို ဂျပန်လို ကော ဘယ်လိုရေးသလဲ။
မင်္ဂလာပါကို ထိုင်းလိုဆိုရင် ဘယ်လို ရေးသလဲ။
မင်္ဂလာပါကို တရုပ်လို ဘယ်လိုရေးသလဲ။
မင်္ဂလာပါကို ဟင်ဒီလိုဘယ်လို ရေးသလဲ။
ဟေး!!!
နေကောင်းလား?
"ကျန်းမာပါတယ်" ကွာ
`ကြားရတာ ဝမ်းသာတယ်` ဗျို့
$ ဈေးတွေက တက်နေတယ်ဆို။
ဟေး~!
ဒုံး . . ဒုံး . . . ဒုံး . .
သာ ဓု . . . သာ ဓု . . . သာ ဓု
မွေး နေ့ မှ သည် - - - - - - နောင် နှစ် ပေါင်း များ စွာ
~ အ စိုး ရ ဝန် ထမ်း
အောင် မြင် ပါ စေ "
ချစ် စ ရာ လေး : - * : - * 
( ဂ ) အ ကန့် အ သတ် ရှိ
[ ဂ ] အ ကန့် အ သတ် မ ရှိ
" " "ပြဿနာ" " "
၎င်း က လည်း သက်သေပါပဲ
မန္တလေးမှာ နေပါတယ်
မြန်မြန်, သွားမှ ဖြစ်မယ်
အားးးးးး
```

## 8.[rm-symbol-and-myVowel-only-sentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-symbol-and-myVowel-only-sentences.pl)  

see the test file: [symbols-test-data.txt](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/symbols-test-data.txt)  
ဒီဖိုင်က အွန်လိုင်းကနေဆွဲယူထားတဲ့ မြန်မာစာ raw data ဖိုင်ကို cleaning လုပ်စဉ်က  
ကျွန်တော်ရှင်းထုတ်ချင်တဲ့ စာကြောင်းတွေနဲ့ program testing အတွက်ပြင်ဆင်ခဲ့တဲ့ test ဖိုင်ဖြစ်ပါတယ်။   

```
$ perl ../rm-symbol-and-myVowel-only-sentences.pl ../symbols-test-data.txt
ဘေ
က
ပုံမှန် စာကြောင်း
ငါကလည်း ပုံမှန် စာကြောင်း နော် !!!
I love all languages!
```

## 9.[rm-space-btw-numbers.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-space-btw-numbers.pl)  

[my-no.txt](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/my-no.txt) ဖိုင်ထဲမှာ အောက်ပါအတိုင်း မြန်မာဂဏန်းတွေလည်း ပါဝင်နေပါတယ်။  

```bash
$ cat my-no.txt
ဖုန်းနံပါတ်က ၃၂၇ ၁၁၀ ပါ။
အဲဒါက အိမ်ဖုန်းပါနော်။
မိုဘိုင်းဖုန်းနံပါတ်ကကော။
မိုဘိုင်းဖုန်းနံပါတ်ကတော့ ၀၉၀ ၈၅၆၄   ၈၁၇၇ ပါ။
ကောင်းပါပြီဗျာ။
```

မြန်မာဂဏန်းတွေရဲ့အကြားမှာ ရှိနေတဲ့ space တွေကို ဖြုတ်မယ်ဆိုရင် rm-space-btw-numbers.pl ကို အောက်ပါအတိုင်း run ပါတယ်။  

```bash
$ perl ./rm-space-btw-numbers.pl ./my-no.txt
ဖုန်းနံပါတ်က ၃၂၇၁၁၀ ပါ။
အဲဒါက အိမ်ဖုန်းပါနော်။
မိုဘိုင်းဖုန်းနံပါတ်ကကော။
မိုဘိုင်းဖုန်းနံပါတ်ကတော့ ၀၉၀၈၅၆၄၈၁၇၇ ပါ။
ကောင်းပါပြီဗျာ။
```
မှတ်ချက်။ ။ အထက်ပါ ကိစ္စမျိုးကို sed ကို သုံးပြီး လုပ်မယ်ဆိုရင် ခက်ခဲပါတယ်။ မြန်မာစာ စာလုံးတွေအတွက်ဆိုရင် hex value နဲ့ pass လုပ်ပေးရတာမျိုး လုပ်ရပါတယ်။ ဘယ်စာလုံးကနေ ဘယ်စာလုံးကြားဆိုတဲ့ (range) ကိစ္စမှာလည်း ကိုယ်လိုချင်တဲ့ ပုံစံအတိုင်း အလုပ် လုပ်မပေးတာတွေကို တွေ့ရပါလိမ့်မယ်။ ဒီလိုနေရာမှာတော့ perl နဲ့ ရေးရတာက ပိုအဆင်ပြေပါတယ်။  

## 10.[print-ngram.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-ngram.pl)  

ဖိုင်ထဲမှာ ရှိတဲ့ စာလုံးဖြတ်ထားတဲ့ စာကြောင်းတွေကို ကိုယ်လိုချင်တဲ့ ngram အတွဲတွေအဖြစ် print ထုတ်ဖို့ ရေးခဲ့တယ်။
input.txt ဖိုင်ထဲမှာ အောက်ပါအတိုင်း စာကြောင်း ၅ကြောင်း ရှိပါတယ်။  

```
$ cat input.txt 
This is a cat .
Who are you ?
My name is Ko Gyi .
I don't know who you are .
Beer Chang Beer Chang ... Beer Chang Beer Chang .
```

2-grams စာလုံးအတွဲတွေအဖြစ် print ထုတ်စေချင်ရင် command line argument ကို 2 ပေးပြီး run ပါတယ်။  

```
$ perl ./print-ngram.pl ./input.txt 2
This is
is a
a cat
cat .
Who are
are you
you ?
My name
name is
is Ko
Ko Gyi
Gyi .
I don't
don't know
know who
who you
you are
are .
Beer Chang
Chang Beer
Beer Chang
Chang ...
... Beer
Beer Chang
Chang Beer
Beer Chang
Chang .
```

3-grams စာလုံးအတွဲတွေအဖြစ် print ထုတ်စေချင်ရင် command line argument ကို 3 ပေးပြီး run ပါတယ်။ 

```
$ perl ./print-ngram.pl ./input.txt 3
This is a
is a cat
a cat .
Who are you
are you ?
My name is
name is Ko
is Ko Gyi
Ko Gyi .
I don't know
don't know who
know who you
who you are
you are .
Beer Chang Beer
Chang Beer Chang
Beer Chang ...
Chang ... Beer
... Beer Chang
Beer Chang Beer
Chang Beer Chang
Beer Chang .
```
## 11. [print-codepoint.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-codepoint.pl)  

[pair.txt](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/pair.txt) ဖိုင်ထဲမှာ စာလုံးပေါင်းမှားတဲ့စာလုံး (သို့) ပုံမှန်အရေးအသားမဟုတ်တဲ့စာလုံးတွေနဲ့ မှန်ကန်တဲ့ မြန်မာစာလုံးတွေကို အပေါ်အောက်ဆင့်ရေးထားပါတယ်။ တကယ်က အဲဒီစာလုံးတွေမှာ ကျွန်တော်တို့ မျက်စိနဲ့ မမြင်နိုင်တဲ့ non printable character တွေပါဝင်နေပါတယ်။   

```bash
$ cat pair.txt
ဇွတ်​ကြီးပါဟယ်​လ်​
ဇွတ်​ကြီးပါဟယ်​
ယောက်​ျား​တွေပါဟယ်​လ်​
ယောက်​ျား​တွေပါဟယ်​​
အသိခဲ့ဘူး
မသိခဲ့ဘူး
စနီး​မောင်​နှံ
ဇနီး​မောင်​နှံ
ပြင်​စဉ်
ပြင်​ဆင်
```

စာလုံးတစ်လုံးချင်းစီရဲ့ character code point တွေကို ရိုက်ထုတ်ပေးဖို့အတွက် print-codepoint.pl ပရိုဂရမ်ကို ရေးခဲ့ပါတယ်။ run မယ်ဆိုရင် ကိုယ်စစ်ချင်တဲ့ ဖိုင်နာမည်ကို command line argument အနေနဲ့ ပေးရပါမယ်။ အထက်ပါ pair.txt ဖိုင်ကို ရိုက်ထုတ်ခိုင်းကြည့်ရအောင်။  

```bash
$ perl ./print-codepoint.pl ./pair.txt 
ဇွတ်​ကြီးပါဟယ်​လ်​
ဇ (4103, U1007) ွ (4157, U103d) တ (4112, U1010) ် (4154, U103a) ​ (8203, U200b) က (4096, U1000) ြ (4156, U103c) ီ (4142, U102e) း (4152, U1038) ပ (4117, U1015) ါ (4139, U102b) ဟ (4127, U101f) ယ (4122, U101a) ် (4154, U103a) ​ (8203, U200b) လ (4124, U101c) ် (4154, U103a) ​ (8203, U200b) , no. of char = 18
ဇွတ်​ကြီးပါဟယ်​
ဇ (4103, U1007) ွ (4157, U103d) တ (4112, U1010) ် (4154, U103a) ​ (8203, U200b) က (4096, U1000) ြ (4156, U103c) ီ (4142, U102e) း (4152, U1038) ပ (4117, U1015) ါ (4139, U102b) ဟ (4127, U101f) ယ (4122, U101a) ် (4154, U103a) ​ (8203, U200b) , no. of char = 15
ယောက်​ျား​တွေပါဟယ်​လ်​
ယ (4122, U101a) ေ (4145, U1031) ာ (4140, U102c) က (4096, U1000) ် (4154, U103a) ​ (8203, U200b) ျ (4155, U103b) ာ (4140, U102c) း (4152, U1038) ​ (8203, U200b) တ (4112, U1010) ွ (4157, U103d) ေ (4145, U1031) ပ (4117, U1015) ါ (4139, U102b) ဟ (4127, U101f) ယ (4122, U101a) ် (4154, U103a) ​ (8203, U200b) လ (4124, U101c) ် (4154, U103a) ​ (8203, U200b) , no. of char = 22
ယောက်​ျား​တွေပါဟယ်​​
ယ (4122, U101a) ေ (4145, U1031) ာ (4140, U102c) က (4096, U1000) ် (4154, U103a) ​ (8203, U200b) ျ (4155, U103b) ာ (4140, U102c) း (4152, U1038) ​ (8203, U200b) တ (4112, U1010) ွ (4157, U103d) ေ (4145, U1031) ပ (4117, U1015) ါ (4139, U102b) ဟ (4127, U101f) ယ (4122, U101a) ် (4154, U103a) ​ (8203, U200b) ​ (8203, U200b) , no. of char = 20
အသိခဲ့ဘူး
အ (4129, U1021) သ (4126, U101e) ိ (4141, U102d) ခ (4097, U1001) ဲ (4146, U1032) ့ (4151, U1037) ဘ (4120, U1018) ူ (4144, U1030) း (4152, U1038) , no. of char = 9
မသိခဲ့ဘူး
မ (4121, U1019) သ (4126, U101e) ိ (4141, U102d) ခ (4097, U1001) ဲ (4146, U1032) ့ (4151, U1037) ဘ (4120, U1018) ူ (4144, U1030) း (4152, U1038) , no. of char = 9
စနီး​မောင်​နှံ
စ (4101, U1005) န (4116, U1014) ီ (4142, U102e) း (4152, U1038) ​ (8203, U200b) မ (4121, U1019) ေ (4145, U1031) ာ (4140, U102c) င (4100, U1004) ် (4154, U103a) ​ (8203, U200b) န (4116, U1014) ှ (4158, U103e) ံ (4150, U1036) , no. of char = 14
ဇနီး​မောင်​နှံ
ဇ (4103, U1007) န (4116, U1014) ီ (4142, U102e) း (4152, U1038) ​ (8203, U200b) မ (4121, U1019) ေ (4145, U1031) ာ (4140, U102c) င (4100, U1004) ် (4154, U103a) ​ (8203, U200b) န (4116, U1014) ှ (4158, U103e) ံ (4150, U1036) , no. of char = 14
ပြင်​စဉ်
ပ (4117, U1015) ြ (4156, U103c) င (4100, U1004) ် (4154, U103a) ​ (8203, U200b) စ (4101, U1005) ဉ (4105, U1009) ် (4154, U103a) , no. of char = 8
ပြင်​ဆင်
ပ (4117, U1015) ြ (4156, U103c) င (4100, U1004) ် (4154, U103a) ​ (8203, U200b) ဆ (4102, U1006) င (4100, U1004) ် (4154, U103a) , no. of char = 8
```

ကွင်းစကွင်းပိတ်ထဲမှာ ပထမဂဏန်းက သက်ဆိုင်ရာစာလုံးတစ်လုံးချင်းစီရဲ့ decimal code point ဖြစ်ပြီးတော့ "U" နဲ့တွဲရိုက်ပြထားတဲ့ ဒုတိယဂဏန်းကတော့ unicode code point ဖြစ်ပါတယ်။ သတိထားပြီးကြည့်ရင် ကျွန်တော်တို့ စကရင်မှာမမြင်ရတဲ့ (non printable character) စာလုံးတွေ ဥပမာ U200b (zero width space) လို စာလုံးမျိုးတွေလည်း ပါနေတာကို တွေ့ရပါလိမ့်မယ်။ ဒီနေရာမှာ စာလုံးတွေကို ရိုက်ထုတ်မပြခင်မှာ လိုင်းခြားပေးတဲ့ "\n" ကိုတော့ ဖြုတ်ထားပါတယ်။ စာလုံးတွေကိုပဲ နှိုင်းယှဉ်ကြည့်ချင်လို့ပါ။ လက်ရှိ ဥပမာ ပြထားတဲ့ ဖိုင်က စာလုံးတွေပဲဆိုပေမယ့်၊ ကိုယ်ပေးလိုက်တဲ့ ဖိုင်ထဲမှာ စာကြောင်းတွေရှိရင် စာကြောင်းတွေကိုလည်း အထက်ပါအတိုင်း code point တွေကို ရိုက်ထုတ်ပေးပါလိမ့်မယ်။ ပြီးတော့ စာကြောင်း တစ်ကြောင်း ပြီးသွားတိုင်းမှာ အဲဒီ စာကြောင်းထဲမှာ စာလုံးရေအရေအတွက် စုစုပေါင်းဘယ်လောက်ရှိတယ်ဆိုတာကိုလည်း "no. of char = X" ဆိုတဲ့ ပုံစံနဲ့ ရိုက်ထုတ်ပေးပါလိမ့်မယ်။ 

မြန်မာစာနဲ့ ပတ်သက်တဲ့ NLP အလုပ်တွေကို လုပ်ပြီ၊ သို့မဟုတ် Unicode text ဖိုင်တွေနဲ့ အလုပ်လုပ်ပြီဆိုရင် ဒီပရိုဂရမ်က အသုံးဝင်ပါလိမ့်မယ်။ ဥပမာအနေနဲ့ မြန်မာစာလုံး နှစ်လုံး သို့မဟုတ် စာကြောင်း နှစ်ကြောင်းကို ဘယ်လောက်တူသလဲ၊ နီးစပ်သလဲ ဆိုတာကို သိဖို့အတွက် similarity တိုင်းတာတဲ့အခါမှာ မမြင်ရတဲ့ စာလုံးတွေကလည်း similarity score ကို သက်ရောက်မှုရှိလို့ပါ။  

## 12. [wc.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/wc.pl)  
စာကြောင်းတစ်ကြောင်းချင်းစီရဲ့ စာလုံးအရေအတွက်ကို ရေတွက်ပြီး print ထုတ်ပြဖို့ ရေးခဲ့တယ်။  

[input-file](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/input-file) ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို အရင်ဆုံး ရိုက်ကြည့်ရအောင်  

```bash
$ cat ./input-file
How are you?
Who are you?
My name is blue papaya.
1 2 3 4 5 6 7 8 9 10
a b c d e f g h i j k
1 2 3
1 2 3 4 5
1 2 3 4 5 6 
```
wc.pl ကို run ကြည့်ရအောင်။ အဲဒါဆိုရင် input-file ထဲမှာရှိတဲ့ စာကြောင်း တစ်ကြောင်းချင်းစီကို ရိုက်ပြပြီး အဲဒီနောက်မှာ space ခြားပြီးတော့ စာလုံးအရေအတွက်ကို ရိုက်ပြပေးပါလိမ့်မယ်။ ဒီနေရာမှာ word အရေအတွက်လို့ ပြောနေပေမယ့် input လုပ်တဲ့ဖိုင်က syllable break လုပ်ထားရင် syllable အရေအတွက်ဖြစ်သွားပြီး၊ character break လုပ်ထားရင် character အရေအတွက် ဖြစ်သွားပါလိမ့်မယ်။ Count လုပ်ပေးမယ့် Unit က input လုပ်တဲ့ ဖိုင်အပေါ်ကို မူတည်ပါလိမ့်မယ်။  

```bash
$ ./wc.pl ./input-file 
How are you? 3
Who are you? 3
My name is blue papaya. 5
1 2 3 4 5 6 7 8 9 10 10
a b c d e f g h i j k 11
1 2 3 3
1 2 3 4 5 5
1 2 3 4 5 6 6
```

## 13. [wordlimit.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/wordlimit.pl)  
Machine translation နဲ့ ပတ်သက်တဲ့ မော်ဒယ်တွေကို မဆောက်ခင်မှာ preprocessing အလုပ်တော်တော်များများ လုပ်ရပါတယ်။ အဲဒီအထဲက တစ်ခုကတော့ language-pair      တစ်ခုစီအတွက် စာကြောင်းတစ်ကြောင်းချင်းစီကို စာလုံးရေအရေအတွက် ဘယ်လောက်အထိဆိုတာကို သတ်မှတ်တာမျိုး လုပ်ရတဲ့ ကိစ္စပါ။ အင်္ဂလိပ်လိုပြောရရင်တော့ word wrapping လုပ်တယ်လို့      ခေါ်ပါတယ်။ သုံးပုံသုံးနည်း က အောက်ပါအတိုင်းပါ။ အထက်က perl program နံပါတ် ၁၂ မှာ ဥပမာပေးခဲ့တဲ့ [input-file](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/input-file) ကိုပဲ သုံးထားပါတယ်။   

စာလုံး ၅လုံးထက်နည်းတဲ့ စာကြောင်းတွေကိုပဲ ရိုက်ထုတ်ပြခိုင်းရအောင်  

```bash
$ ./wordlimit.pl ./input-file "<5"
How are you? 
Who are you? 
1 2 3 
```

စာကြောင်းတစ်ကြောင်းမှာ စာလုံးအရေအတွက် ၇လုံးထက်များတာကိုပဲ ရိုက်ထုတ်ခိုင်းကြည့်ရအောင်   

```bash
$ ./wordlimit.pl ./input-file ">7"
1 2 3 4 5 6 7 8 9 10 
a b c d e f g h i j k 
```

## 14. [wordwrap.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/wordwrap.pl)  

[english-input](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/english-input) ဖိုင်ထဲမှာ ရှိတဲ့စာကြောင်းတွေက အောက်ပါအတိုင်းပါ။  

```
$ cat english-input 
Who are you?
How are you?
My name is blue papaya.
1 2 3 4 5 6 7 8 9 10
a b c d e f g h i j k
I love you, you love me.
for your refreshment
Kachin Kayar Kayin Chin Mon Bamar Rakhine Shan
Towards Sufficiency Economy with Science and Technology, NAC2006
Pascal, C, C++, Visual Basic, Microsoft Access, MySQL, Bash, Perl, Python etc.
one two three four five six seven eight nine ten
```

အထက်ပါစာကြောင်းတွေကို စာလုံး ၅လုံးကျော်တာနဲ့ နောက်တလိုင်းကိုဆင်းပေးခိုင်းစေချင်ရင် အောက်ပါအတိုင်း run ပါ။ command line argument အနေနဲ့က ဖိုင်နာမည်နဲ့ စာလုံးရေအရေအတွက်ကို perl program နာမည်ရဲ့ နောက်မှာ ရိုက်ထည့်ပေးယုံပါပဲ။  

```
lar@lar-air:~/tool/perl/word-wrap$ perl ./wordwrap.pl ./english-input 5
Who are you?
How are you?
My name is blue papaya.
1 2 3 4 5
6 7 8 9 10
a b c d e
f g h i j
k
I love you, you love
me.
for your refreshment
Kachin Kayar Kayin Chin Mon
Bamar Rakhine Shan
Towards Sufficiency Economy with Science
and Technology, NAC2006
Pascal, C, C++, Visual Basic,
Microsoft Access, MySQL, Bash, Perl,
Python etc.
one two three four five
six seven eight nine ten
```

နောက်ထပ် ဥပမာအနေနဲ့ စာလုံးရေအရေအတွက်ကို ၃လုံးထားပြီး run ရင်အောက်ပါအတိုင်း ရိုက်ထုတ်ပေးပါလိမ့်မယ်။  

```
$ perl ./wordwrap.pl ./english-input 3
Who are you?
How are you?
My name is
blue papaya.
1 2 3
4 5 6
7 8 9
10
a b c
d e f
g h i
j k
I love you,
you love me.
for your refreshment
Kachin Kayar Kayin
Chin Mon Bamar
Rakhine Shan
Towards Sufficiency Economy
with Science and
Technology, NAC2006
Pascal, C, C++,
Visual Basic, Microsoft
Access, MySQL, Bash,
Perl, Python etc.
one two three
four five six
seven eight nine
ten
```

## 15. [get-syl-potma.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/get-syl-potma.pl)  

အရင်ဆုံး [my-tst.txt](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/my-tst.txt) ဖိုင်ထဲမှာ ဘယ်လို မြန်မာစာကြောင်းတွေရှိသလဲ ဆိုတာကို ကြည့်ကြရအောင်။  

```
$cat ./my-tst.txt
မင်္ဂ လာ ပါ ခင် ဗျား ။ ( ၀ ၂ ) ၃ ၁ ၆ ၉ ၇ ၊ ၃ ၅ ၀ ၁ ၃ ၊ ၃ ၄ ၂ ၆ ၃ ၊ ၃ ၅ ၄ ၃ ၀ ဖြစ် ပါ တယ် ။
အား ပေး နေ တယ် နော်
ခွက် ထဲ မှာ အ ခ န့် သား . . . ။
အ ကု သိုလ် များ နေ ပြီ ။ လုံး လိုက် ချပ် ပြား ဖြစ် နေ
ဟုတ် ကဲ့ ပါ ခင် ဗျာ ။
```

ပုဒ်မရှေ့မှာ ရှိနေတဲ့ syllable တစ်လုံးတည်းကိုပဲ ဆွဲထုတ်ချင်ရင် နောက်ဆုံး command line argument ကို 1 ပေးပြီး run ပါ။ အောက်ပါအတိုင်း ဆွဲထုတ်ပေးပါလိမ့်မယ်။ ဒီနေရာမှာ ကျွန်တော်က မြန်မာsyllable တွေကို စိတ်ဝင်စားလို့ ပရိုဂရမ်နာမည်ကို syl ဆိုပြီးယူထားပေမယ့် ရေးထားတဲ့ code ကို ဝင်ကြည့်ရင်မြင်ရတဲ့အတိုင်း space နဲ့ ဖြတ်ပြီးဆွဲထုတ်ထားတာမို့ unit  က ခင်ဗျား input လုပ်တဲ့ဖိုင် (သို့) segmentation ကို ဘယ်လိုဖြတ်ထားသလဲ ဆိုတဲ့အပေါ်ကို မူတည်ပါလိမ့်မယ်။    

```
$ perl ./get-syl-potma.pl ./my-tst.txt 1
ဗျား ။
. ။
ပြီ ။
ဗျာ ။
```

ပုဒ်မ ရှေ့မှာ ရှိနေတဲ့ syllable နှစ်လုံးကို ဆွဲထုတ်ချင်ရင်တော့ နောက်ဆုံး command line argument ကို 2 ပေးပြီး run ပါ။  

```
$ perl ./get-syl-potma.pl ./my-tst.txt 2
ခင် ဗျား ။
. . ။
နေ ပြီ ။
ခင် ဗျာ ။
```

ပုဒ်မ ရှေ့မှာ ရှိနေတဲ့ syllable သုံးလုံးကို ဆွဲထုတ်ချင်ရင်တော့ နောက်ဆုံး command line argument ကို 3 ပေးပြီး run ပါ။ 

```
$ perl ./get-syl-potma.pl ./my-tst.txt 3
ပါ ခင် ဗျား ။
. . . ။
များ နေ ပြီ ။
ပါ ခင် ဗျာ ။
```

## 16.[my-linebreak.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/my-linebreak.pl)  
မြန်မာစာကြောင်းတွေကို web ကနေ mining လုပ်ပြီးသုံးဖို့ပြင်တဲ့အခါမှာ စာပိုဒ်တွေလည်း ပါလာပါလိမ့်မယ်။ လိုချင်တာတွေကော၊ မလိုချင်တဲ့ XML tag တွေရော မျိုးစုံပါပဲ။ အဲဒီဒေတာတွေကို ကိုယ်က သုံးလို့ရဖို့အတွက်က အများကြီး preprocessing လုပ်ကြရပါတယ်။ အဲဒီအထဲက တစ်ခုကတော့ စာကြောင်းတစ်ကြောင်းချင်းစီ ဖြတ်ပြီးတော့ သိမ်းချင်တဲ့ အလုပ်ပါ။ အင်္ဂလိပ်လိုတော့ sentence breaking သို့မဟုတ် line breaking လို့ခေါ်ပါတယ်။ အဲဒီအလုပ်ကလည်း လက်တွေ့မှာ သိပ်လွယ်ကူတဲ့ အလုပ်မဟုတ်ပါဘူး။ ဒီနေရာမှာတော့ တခြား သဒ္ဒါတွေကြည့်ဖြတ်တာ၊ POS tag တွေနဲ့ ဆုံးဖြတ်ပြီးမှသွားတဲ့ အထိမလုပ်ပဲ၊ အကြမ်းမျဉ်း ပုဒ်မ တွေကိုပဲ တည်ပြီး ဖြတ်တဲ့နည်းကို ကျွန်တော် လုပ်ပြထားပါတယ်။   

ဆိုပါစို့ ခင်ဗျားက Wikipedia ကနေ မြန်မာစာဒေတာကို ဆွဲယူလာပြီး၊ XML tag တွေလည်း ဖြုတ်ပြီးပြီ ဆိုတဲ့ အနေအထားကနေပဲ စဉ်းစားကြရအောင်။ လုပ်လို့ရတဲ့နည်းတစ်ခုက အဲဒီ စာကြောင်းတွေကို ကျွန်တော် တင်ပေးထားတဲ့ sylbreak ပရိုဂရမ်နဲ့ syllable breaking လုပ်ပြီးတော့ ပုဒ်မ နဲ့ ပုဒ်မရဲ့ ရှေ့မှာရှိတဲ့ syllable တွဲတွေကို ဆွဲထုတ်၊ အတွဲတွေက corpus တစ်ခုလုံးမှာ ဘယ်နှစ်ခါပါနေသလဲ ဆိုတာကို frequency တွက်ပြီးတော့၊ frequency များတဲ့ကောင်တွေကို ဖိုင်တစ်ဖိုင်မှာသိမ်းပြီး manual cleaning လုပ်ပြီး သွားရင်၊ အဲဒီဖိုင်ကို dictionary အနေနဲ့ သုံးပြီးတော့ raw corpus ထဲက စာကြောင်းတွေကို စာကြောင်းတစ်ကြောင်းချင်းစီ ဖြတ်ထုတ်လို့ရပါတယ်။ သေချာတာက ခင်ဗျားစုထားတဲ့ raw data အတွက်က အလုပ်ကောင်းကောင်း လုပ်ပေးမှာပါပဲ။ အခု ကျွန်တော် ရှင်းပြထားတာကို လက်တွေ့လုပ်ဆောင်နိုင်ဖို့ အတွက် 2-gram dictionary ကိုလည်း တင်ပေးထားပြီးတော့၊ အဲဒီ dictionary ကိုသုံးပြီးတော့ ဖြတ်ဖို့အတွက် ရေးထားတဲ့ perl program ကိုလည်း တင်ပေးထားပါတယ်။ ကျွန်တော်တို့ လက်ရှိ မြန်မာစာ NLP သုတေသနအတွက် အတိုင်းအတာတစ်ခုအထိတော့ အသုံးဝင်ပါလိမ့်မယ်။  

အရင်ဆုံး တင်ပေးထားတဲ့ dictionary ဖိုင်ဖြစ်တဲ့ [1syl.potma.dict](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/4linebreak/1syl.potma.dict) ကို head command ပေးပြီး ထိပ်ဆုံး ၁၀ကြောင်းကိုပဲ peekလုပ်ကြည့်ရင်တော့ အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
$ head -n 20 ./1gram.potma.dict
သည် ။
တယ် ။
ပါ ။
ဗျာ ။
လား ။
ဘူး ။
လဲ ။
မယ် ။
၂ ။
စေ ။
ပဲ ။
မည် ။
ပြီ ။
ရှင် ။
၏ ။
တာ ။
နော် ။
ဗျ ။
ပေါ့ ။
လေ ။
```

တင်ပေးထားတဲ့ [test-data](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/4linebreak/test-data) ကို cat လုပ်ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
$ cat ./test-data
မင်္ဂ လာ ပါ ခင် ဗျား ။ ( ၀ ၂ ) ၃ ၁ ၆ ၉ ၇ ၊ ၃ ၅ ၀ ၁ ၃ ၊ ၃ ၄ ၂ ၆ ၃ ၊ ၃ ၅ ၄ ၃ ၀ ဖြစ် ပါ တယ် ။
အ ကု သိုလ် များ နေ ပြီ ။ လုံး လိုက် ချပ် ပြား ဖြစ် နေ
* ၂ ၀ ၁ ၁   ခု နှစ်   ။   ။   နို ဝင် ဘာ တွင်   မြန် မာ နိုင် ငံ ဆိုင် ရာ   အ ထူး ကိုယ် စား လှယ်   မစ် ချယ် သည်   သက် တမ်း နှစ် လ   မ ပြ ည့် သေး သ ည့်   အ ချိန် တွင်   တ တိ ယ အ ကြိမ် မြောက် ခ ရီး စဉ် အ ဖြစ်   မြန် မာ နိုင် ငံ သို့ သွား ရောက် ပြီး   မြန် မာ အ စိုး ရ ခေါင်း ဆောင် များ အ ပါ အ ဝင်   ဒေါ် အောင်   ဆန်း စု ကြည် နှ င့် ပါ   တွေ့ ဆုံ သည် ။ 
  မြန် မာ နိုင် ငံ မှ   နောက် ထပ် ဖြစ် ပေါ် လာ မ ည့်   အ ပြု သ ဘော ဆောင် သော   အ ပြောင်း   အ လဲ   များ နှ င့် အ တူ   အ မေ ရိ ကန် အ စိုး ရ က လည်း   အ ပြန် အ လှန် ဆောင် ရွက် သွား မည် ဟု   အ မေ ရိ ကန် အ စိုး ရ က   ထုတ် ပြန် ကြေ ညာ   သည် ။
ဆုံ နေ ကြ ပါ
ဟုတ် ကဲ့ ပါ ခင် ဗျာ ။ မင်္ဂ လာ ရှိ သော နေ့ လေး ဖြစ် ပါ စေ ခင် ဗျာ ။
ကမ္ဘာ လော က မှ လူ အ များ သည် ကမ္ဘာ ဦး ကာ လ မှ စ ၍ ရော ဂါ အ သွယ် သွယ် အန္တ ရာယ် အ မျိုး မျိုး ဘေး ဆိုး ကပ် ဆိုး အ တန် တန် တို့ ကို ရင် ဆိုင် တွေ့ ကြုံ ခံ စား ခဲ့ ကြ ရ သည် ။ ယ ခု ရင် ဆိုင် နေ ကြ ရ ၍ နောင် လည်း ရင် ဆိုင် နေ ကြ ရ ဦး မည် ဖြစ် သည် ။ ထို ရော ဂါ အ သွယ် သွယ် အန္တ ရာယ် အ မျိုး မျိုး ဘေး ဆိုး ကပ် ဆိုး အ တန် တန် တို့ ကို တွေ့ ကြုံ ကြ ရ သော အ ခါ ဘေး အန္တ ရာယ် တို့ မှ ကာ ကွယ် စော င့် ရှောက် နိုင် မ ည့် ပုဂ္ဂိုလ် ကို မျှော် လ င့် ခဲ့ ကြ သည် ။ ရှာ ဖွေ ခဲ့ ကြ သည် ။ ကိုး ကွယ် ရာ အ ဖြစ် အ သိ အ မှတ် ပြု လို ခဲ့ ကြ သည် ။ ယင်း သို့ ဖြ င့် မြစ် များ ၊ ချောင်း များ ၊ သစ် ပင် တော တောင် များ သည် လူ တို့ ၏ ကိုး ကွယ် ရာ အ ဖြစ် သို့ ရောက် ခဲ့ ကြ ရ သည် ။ အ သိ ဉာဏ် မ ဖွံ့ ဖြိုး သေး သော ကမ္ဘာ ဦး ကာ လ လူ သား များ သည် မြစ် ကို နတ် ဘု ရား အ ဖြစ် ထင် မှတ် ခဲ့ ကြ သည် ။ မြစ် သည် သောက် စ ရာ ရေ ကို လည်း ပေး သည် ။ သစ် ပင် သီး နှံ ကို လည်း ဖြစ် ထွန်း စေ သည် ။ ရေ ထဲ မှ စား စ ရာ သား ငါး ကို လည်း ရ သည် ။ ဤ သို့ လူ တို့ ၏ အ ကျိုး စီး ပွား ဖြစ် ထွန်း စေ သ လို တစ် ခါ တ ရံ တွင် မြစ် ရေ များ လျှံ တက် ၍ လူ တို့ စိုက် ပျိုး ထား သော သီး နှံ ပင် များ ၊ လယ် ယာ စိုက် ခင်း များ ၊ ကျွဲ နွား တိ ရစ္ဆာန် များ ကို ဖျက် ဆီး ပစ် တတ် သည် ။ လူ တို့ ၏ အ သက် စည်း စိမ် ချမ်း သာ များ ကို ချေ မှုန်း ပစ် တတ် သည် ။ လူ တို့ အား အ ကျိုး ပြု ခြင်း ၊ ဖျက် ဆီး ခြင်း နှစ် မျိုး ကို ပြု တတ် သော ကြော င့် မြစ် ကို ပင် ဖန် ဆင်း ရှင် အ ဖြစ် ထင် မှတ် လာ ခဲ့ ကြ သည် ။ ထို မြစ် ၌ မျက် စိ နှ င့် မ မြင် နိုင် သော တန် ခိုး ရှင် နတ် ဘု ရား ရှိ မည် ဟု ယုံ ကြည် လာ ကြ တော့ သည် ။
ဒ ဂုန်   တာ ရာ ၏   စာ ပေ သစ် ၊   ပ ဒေ သာ   ( ဩ ဂုတ်   ၁ ၉ ၄ ၉ ) ။ 
သိ ထား ဖို့ တော့ လို တယ်   ။   စာ လေး   ပေ လေး   ဖတ် ကြ အုံး   ။   ရ ဟန်း ရှင် လူ
" ၁ ။   အ သား ဟင်း   ၁   မျိုး ၊   အ ရွက် ကြော်   ၁   ၊   အ သုတ်   ၁   ၊   ဟင်း ချို   ၁ ၊
```

အထက်ပါ ဖိုင်ကို sentence breaking သို့မဟုတ် line breaking လုပ်ကြည့်ရအောင်။  

```
$ perl ./my-linebreak.pl ./1syl.potma.dict ./test-data
မင်္ဂ လာ ပါ ခင် ဗျား ။ 
( ၀ ၂ ) ၃ ၁ ၆ ၉ ၇ ၊ ၃ ၅ ၀ ၁ ၃ ၊ ၃ ၄ ၂ ၆ ၃ ၊ ၃ ၅ ၄ ၃ ၀ ဖြစ် ပါ တယ် ။
အ ကု သိုလ် များ နေ ပြီ ။ 
လုံး လိုက် ချပ် ပြား ဖြစ် နေ
* ၂ ၀ ၁ ၁ ခု နှစ် ။ 
။ နို ဝင် ဘာ တွင် မြန် မာ နိုင် ငံ ဆိုင် ရာ အ ထူး ကိုယ် စား လှယ် မစ် ချယ် သည် သက် တမ်း နှစ် လ မ ပြ ည့် သေး သ ည့် အ ချိန် တွင် တ တိ ယ အ ကြိမ် မြောက် ခ ရီး စဉ် အ ဖြစ် မြန် မာ နိုင် ငံ သို့ သွား ရောက် ပြီး မြန် မာ အ စိုး ရ ခေါင်း ဆောင် များ အ ပါ အ ဝင် ဒေါ် အောင် ဆန်း စု ကြည် နှ င့် ပါ တွေ့ ဆုံ သည် ။
မြန် မာ နိုင် ငံ မှ နောက် ထပ် ဖြစ် ပေါ် လာ မ ည့် အ ပြု သ ဘော ဆောင် သော အ ပြောင်း အ လဲ များ နှ င့် အ တူ အ မေ ရိ ကန် အ စိုး ရ က လည်း အ ပြန် အ လှန် ဆောင် ရွက် သွား မည် ဟု အ မေ ရိ ကန် အ စိုး ရ က ထုတ် ပြန် ကြေ ညာ သည် ။
ဆုံ နေ ကြ ပါ
ဟုတ် ကဲ့ ပါ ခင် ဗျာ ။ 
မင်္ဂ လာ ရှိ သော နေ့ လေး ဖြစ် ပါ စေ ခင် ဗျာ ။
ကမ္ဘာ လော က မှ လူ အ များ သည် ကမ္ဘာ ဦး ကာ လ မှ စ ၍ ရော ဂါ အ သွယ် သွယ် အန္တ ရာယ် အ မျိုး မျိုး ဘေး ဆိုး ကပ် ဆိုး အ တန် တန် တို့ ကို ရင် ဆိုင် တွေ့ ကြုံ ခံ စား ခဲ့ ကြ ရ သည် ။ 
ယ ခု ရင် ဆိုင် နေ ကြ ရ ၍ နောင် လည်း ရင် ဆိုင် နေ ကြ ရ ဦး မည် ဖြစ် သည် ။ 
ထို ရော ဂါ အ သွယ် သွယ် အန္တ ရာယ် အ မျိုး မျိုး ဘေး ဆိုး ကပ် ဆိုး အ တန် တန် တို့ ကို တွေ့ ကြုံ ကြ ရ သော အ ခါ ဘေး အန္တ ရာယ် တို့ မှ ကာ ကွယ် စော င့် ရှောက် နိုင် မ ည့် ပုဂ္ဂိုလ် ကို မျှော် လ င့် ခဲ့ ကြ သည် ။ 
ရှာ ဖွေ ခဲ့ ကြ သည် ။ 
ကိုး ကွယ် ရာ အ ဖြစ် အ သိ အ မှတ် ပြု လို ခဲ့ ကြ သည် ။ 
ယင်း သို့ ဖြ င့် မြစ် များ ၊ ချောင်း များ ၊ သစ် ပင် တော တောင် များ သည် လူ တို့ ၏ ကိုး ကွယ် ရာ အ ဖြစ် သို့ ရောက် ခဲ့ ကြ ရ သည် ။ 
အ သိ ဉာဏ် မ ဖွံ့ ဖြိုး သေး သော ကမ္ဘာ ဦး ကာ လ လူ သား များ သည် မြစ် ကို နတ် ဘု ရား အ ဖြစ် ထင် မှတ် ခဲ့ ကြ သည် ။ 
မြစ် သည် သောက် စ ရာ ရေ ကို လည်း ပေး သည် ။ 
သစ် ပင် သီး နှံ ကို လည်း ဖြစ် ထွန်း စေ သည် ။ 
ရေ ထဲ မှ စား စ ရာ သား ငါး ကို လည်း ရ သည် ။ 
ဤ သို့ လူ တို့ ၏ အ ကျိုး စီး ပွား ဖြစ် ထွန်း စေ သ လို တစ် ခါ တ ရံ တွင် မြစ် ရေ များ လျှံ တက် ၍ လူ တို့ စိုက် ပျိုး ထား သော သီး နှံ ပင် များ ၊ လယ် ယာ စိုက် ခင်း များ ၊ ကျွဲ နွား တိ ရစ္ဆာန် များ ကို ဖျက် ဆီး ပစ် တတ် သည် ။ 
လူ တို့ ၏ အ သက် စည်း စိမ် ချမ်း သာ များ ကို ချေ မှုန်း ပစ် တတ် သည် ။ 
လူ တို့ အား အ ကျိုး ပြု ခြင်း ၊ ဖျက် ဆီး ခြင်း နှစ် မျိုး ကို ပြု တတ် သော ကြော င့် မြစ် ကို ပင် ဖန် ဆင်း ရှင် အ ဖြစ် ထင် မှတ် လာ ခဲ့ ကြ သည် ။ 
ထို မြစ် ၌ မျက် စိ နှ င့် မ မြင် နိုင် သော တန် ခိုး ရှင် နတ် ဘု ရား ရှိ မည် ဟု ယုံ ကြည် လာ ကြ တော့ သည် ။
ဒ ဂုန် တာ ရာ ၏ စာ ပေ သစ် ၊ ပ ဒေ သာ ( ဩ ဂုတ် ၁ ၉ ၄ ၉ ) ။
သိ ထား ဖို့ တော့ လို တယ် ။ 
စာ လေး ပေ လေး ဖတ် ကြ အုံး ။ 
ရ ဟန်း ရှင် လူ
" ၁ ။ 
အ သား ဟင်း ၁ မျိုး ၊ အ ရွက် ကြော် ၁ ၊ အ သုတ် ၁ ၊ ဟင်း ချို ၁ ၊
```
ကျွန်တော် 3-gram, 4-gram ... တွေနဲ့လည်း စမ်းဖြစ်ပါတယ်။ gram များလာတာနဲ့အမျှ dictionary ရဲ့ size ကလည်း ကြီးလာပါတယ်။ ကိုယ်သုံးမယ့် raw-data အတွက်က အထက်မှာ ကျွန်တော်လုပ်ပြထားသလို 1-gram လို dictionary နဲလည်း ကောင်းကောင်း အလုပ်လုပ်ပေးလို့ အိုက်ဒီယာရအောင် ရှဲလုပ်ပေးလိုက်တာပါ။  

## 17. [rm-ne-tag.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-ne-tag.pl)  

ကျွန်တော်တို့မှာ name entity tag တွေပါတဲ့ ဒေတာဖိုင် [my-ne-tag-data](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/my-ne-tag-data) က အောက်ပါအတိုင်းရှိနေတယ် ဆိုကြပါစို့။ ဒီနေရာမှာ "|" သင်္ကေတကတော့ word boundary ကိုပြထားတာဖြစ်ပါတယ်။  

```
$ cat ./my-ne-tag-data
ကျွန်တော်|[LOC]မြန်မာ[\LOC]|စစ်တုရင်|ကစားရတာ|ကြိုက်တယ်|။|
[FOOD]ဘိန်းမုန့်[\FOOD]|နှစ်ခု|လောက်|။| 
[TRA]မန္တလေး ဘူတာရုံ[\TRA]|က|ဘယ်နေရာမှာလဲ|။|
[PER][TITLE]ဒေါက်တာ[\TITLE]|ရူပ[\PER]|ရဲ့|သုတေသန|ရုံးခန်း|ကပါ|။|
[DTM]လေးနှစ်[\DTM]|လောက်|ရှိပြီ|။|
```

[rm-ne-tag.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-ne-tag.pl) ပရိုဂရမ်နဲ့ tag တွေကို ဖြုတ်ပြီးသွားတဲ့အခါမှာတော့ အေက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။ Regualr Expression ကို ဘယ်လိုသုံးသွားသလဲ ဆိုတာကိုတော့ code ကို ဝင်လေ့လာပါ။  

```
$ perl ./rm-ne-tag.pl ./my-ne-tag-data
ကျွန်တော် မြန်မာ စစ်တုရင် ကစားရတာ ကြိုက်တယ် ။ 
ဘိန်းမုန့် နှစ်ခု လောက် ။  
မန္တလေး ဘူတာရုံ က ဘယ်နေရာမှာလဲ ။ 
ဒေါက်တာ ရူပ ရဲ့ သုတေသန ရုံးခန်း ကပါ ။ 
လေးနှစ် လောက် ရှိပြီ ။
```

## 18.[clean-v-without-c.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-v-without-c.pl)  

အရင်ဆုံး [v-no-c.testdata](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/v-no-c.testdata) ဖိုင်ထဲမှာ ရှိနေတဲ့ ဗျည်းမရှိပဲ သရတွေပဲဖြစ်နေတဲ့ စာလုံးတွေကို လေ့လာကြည့်ကြရအောင်။   

```
$ cat ./v-no-c.testdata 
တရားကေို စာင့သ
 သ
 သွငး် ယူခသ
 ဲ
ဖိတေ် ခါ်ပြိုင်ပွဲ အုပစ် ပု စွဲ ဉ်များ ထွကေ် ပါ်
ရန်ကုန	
ဆောက်လပု ေ် ရးတာဝန်ခံ ဦးစည်သြူ ဖို းဝေ
လှိုင်သာယာကျန်စစ်မင်းအိမ်ရာ တည်ဆောက်ခြင်းစီမံကိန်းပြီးစီးသောအပိုင်းမှ တိုက်ခန်းများကို ရောင်းချပေးလျက်ရှိ
 နိ း် ၉၀ ဝန်းကျငက
]] တည်ဆောက်မျှု ႈပြီးစီးတဲ့ ၇၀

သောကြာ၊ မတ် ၁၅၊ ၂၀၁၉
ဒီ ေ ရလှု ိ င ် း ကာ ပြုလု ပ ် ေ နမှု တ ိ ု ့ က ိ ု
 ဂိးု ထပ်မသ
ဖရူဆြို မိုန့ ယ်နငှ ့် ဒီးမော့ဆြို မိုန့ ယ်အတွငး် ရှိ ကျောင်းသား ကျောင်းသူများ၏ ဇီဝဗေဒ
အပိငု း် (၁)၊ အပိငု း် (၂)ကို ဆောက်လပု ေ် ရး
```

အထက်ပါအမှားတွေထဲက တော်တော်များများ ကို clean-v-without-c.pl ပရိုဂရမ်က ရှင်းပေးပါလိမ့်မယ်။ run ကြည့်ပြီး ထွက်လာတဲ့ output စာကြောင်းတွေကို out ဆိုတဲ့ ဖိုင်နာမည်ပေးပြီး သိမ်းမယ်။ ပြီးတော့ အဲဒီ out ဆိုတဲ့ဖိုင်ကို cat command နဲ့ ရိုက်ထုတ်ကြည်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
$ perl ./clean-v-without-c.pl ./v-no-c.testdata > out
lar@lar-air:/media/lar/Transcend/paper/next-paper/LRL2019/data/4seg/newspaper-tst/tst-clean$ cat out
တရားကေို စာင့သ
ဖိတေ် ခါ်ပြိုင်ပွဲ အုပစ် ပု စွဲ ဉ်များ ထွကေ် ပါ်
လှိုင်သာယာကျန်စစ်မင်းအိမ်ရာ တည်ဆောက်ခြင်းစီမံကိန်းပြီးစီးသောအပိုင်းမှ တိုက်ခန်းများကို ရောင်းချပေးလျက်ရှိ
]] တည်ဆောက်မျှု ႈပြီးစီးတဲ့ ၇၀

သောကြာ၊ မတ် ၁၅၊ ၂၀၁၉
```

အထက်ပါ မြင်ရတဲ့အတိုင်း clean-v-without-c.pl က မရှင်းပေးနိုင်သေးတာက တခြား မြန်မာစာလုံးတွေနဲ့တွဲကပ်နေတဲ့ အမှားတွေဖြစ်ပါတယ်။ အဲဒီအတွက်က syllable level ဖြတ်ပြီး checking လုပ်တာမျိုးနဲ့ clean လုပ်နိုင်ပါတယ်။ လောလောဆယ် နဂိုကရှိနေတဲ့ လိုင်းအရေအတွက်နဲ့ clean လုပ်ပြီးသားမှာ လျော့သွားတဲ့ လိုင်းတွေကို နှိုင်းယှဉ်ကြည့်ရင် အောက်ပါအတိုင်းဖြစ်ပါလိမ့်မယ်။  

```
$ wc v-no-c.testdata 
  15   85 1349 v-no-c.testdata
  
$ wc out
  5  22 619 out
```

clean-v-without-c.pl ကို သုံးပြီးတော့ မြန်မာ့အလင်း သတင်းစာဖိုင်ကို ရှင်းကြည့်တဲ့အခါမှာ အမှားတွေပါတဲ့ လိုင်းတွေကို တော်တော်လေးရှင်းပေးသွားတာကို အောက်ပါအတိုင်း တွေ့ရပါလိမ့်မယ်။ ကျွန်တော် သင်ပေးချင်တာက consonant မပါပဲ Myanmar vowel တွေပဲ ဖြစ်နေတဲ့ အမှားစာကြောင်းတွေကို clean လုပ်ချင်တဲ့အခါမှာ အခုလိုမျိုး Regular Expression ကို သုံးပြီးတော့ perl script ကို လွယ်လွယ်ကူကူနဲ့ ရေးပြီး ရှင်းနိုင်တယ်ဆိုတာကိုပါ။ ဖိုင်တွေအများကြီးကို ကိုင်တွယ် အလုပ်လုပ်တဲ့အခါမှာ manual checking တွေချည်းပဲ မလုပ်ပဲ၊ နိုင်တဲ့အပိုင်းတွေကို ပရိုဂရမ်ရေးပြီး ဖြေရှင်းကြဖို့ပါ။  

```
$ wc ./mal_15.3.19.utf8.txt 
  8466  28050 786257 ./mal_15.3.19.utf8.txt
$ perl ./clean-v-without-c.pl ./mal_15.3.19.utf8.txt > out
$ wc out
  5202  15062 565372 out
```

## 19. [x-x-to-x-comma-x-with-brackets.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/x-x-to-x-comma-x-with-brackets.pl)  

Parallel text ဒေတာကနေ alignment algorithm တစ်ခုခုကိုသုံးပြီးတော့ alignment လုပ်ပြီးရလာတဲ့ဖိုင်ပုံစံက Pharaoh format လို့ခေါ်တဲ့ အောက်ပါပုံစံအတိုင်း ရှိပါတယ်။  

```
$ cat ./align
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8
0-0 1-1 2-2 3-3 4-4
0-0 1-1 1-2 2-3 3-4 3-5 4-6
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4 5-4
0-0 1-1 2-2 3-3 3-4 4-4 4-5 5-6
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 2-3 3-4
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8 9-9 10-9
0-0 1-1 2-2 3-2 3-3 4-3 5-4 6-5 7-6 8-7 9-7
```

အဲဒါကို တခြားအလုပ်တစ်ခုအတွက် ကျွန်တော်သုံးတဲ့ python program က alignment word နှစ်ခုကြားမှာ ကော်မှာနဲ့ခံရေးပြီး ကွင်းစကွင်းပိတ် ခတ်ရေးတဲ့ ပုံစံကိုလက်ခံလို့ format ပြောင်းဖို့အတွက် [x-x-to-x-comma-x-with-brackets.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/x-x-to-x-comma-x-with-brackets.pl) ပရိုဂရမ်ကို ရေးခဲ့ပါတယ်။ run တဲ့ပုံစံကတော့ အောက်ပါအတိုင်းပါ။  

```
$ ./x-x-to-x-comma-x-with-brackets.pl ./align 
(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), 
(0,0), (1,1), (2,2), (3,3), (4,4), 
(0,0), (1,1), (1,2), (2,3), (3,4), (3,5), (4,6), 
(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), 
(0,0), (1,1), (2,2), (3,3), (4,4), (5,4), 
(0,0), (1,1), (2,2), (3,3), (3,4), (4,4), (4,5), (5,6), 
(0,0), (1,1), (2,2), (3,3), (4,4), 
(0,0), (1,1), (2,2), (2,3), (3,4), 
(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,9), 
(0,0), (1,1), (2,2), (3,2), (3,3), (4,3), (5,4), (6,5), (7,6), (8,7), (9,7),
```

အထက်ပါ output format မှာ စာကြောင်းရဲ့ နောက်ဆုံးပိုင်းမှာ ပါနေတဲ့ comma နဲ့ space ကို ဖျက်ဖို့ကလည်း x-x-to-x-comma-x-with-brackets.pl ပရိုဂရမ်မှာ print မထုတ်ခင် if နဲ့ စစ်ပြီးမှ print ရိုက်ထုတ်တာမျိုးကို လုပ်လို့ရပါတယ်။ ဒီနေရမှာတော့ perl one liner ကို သုံးပြီး လုပ်ပြပါမယ်။ ဥပမာ အထက်ပါ output ကို ကျွန်တော်တို့က align.b ဆိုတဲ့ နာမည်နဲ့ သိမ်းထားတယ်ဆိုရင် အောက်ပါအတိုင်း perl နဲ့ Regular Expression ကို သုံးပြီးတော့ အလွယ်တကူ ရှင်းလို့ရပါတယ်။  

```
$ perl -p -e "s/\, $//g" ./align.b 
(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)
(0,0), (1,1), (2,2), (3,3), (4,4)
(0,0), (1,1), (1,2), (2,3), (3,4), (3,5), (4,6)
(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)
(0,0), (1,1), (2,2), (3,3), (4,4), (5,4)
(0,0), (1,1), (2,2), (3,3), (3,4), (4,4), (4,5), (5,6)
(0,0), (1,1), (2,2), (3,3), (4,4)
(0,0), (1,1), (2,2), (2,3), (3,4)
(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,9)
(0,0), (1,1), (2,2), (3,2), (3,3), (4,3), (5,4), (6,5), (7,6), (8,7), (9,7)
```

## 20.[select-en-th-my.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/select-en-th-my.pl)  

[id-en-th-my.tst.txt](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/id-en-th-my.tst.txt) ဆိုတဲ့ ဖိုင်က အောက်ပါအတိုင်း sentence ID ရယ်၊ အင်္ဂလိပ်စာ စာကြောင်းရယ်၊ ထိုင်းစာကြောင်းရယ်နဲ့ မြန်မာစာ စာကြောင်းတွေကို \<TAB\> နဲ့ခြားပြီး သိမ်းထားတဲ့ parallel data ဖိုင်လို့ဆိုပါစို့။ သို့သော် မြင်ရတဲ့အတိုင်းပါပဲ တချို့ field တွေမှာ စာရိုက်ထားတာ မရှိပါဘူး။ အဲဒါမျိုးက NLP အလုပ်တွေမှာ ကြုံရတတ်ပါတယ်။ ဘာကြောင့်လည်းဆိုတော့ အခုဥပမာဖိုင်လို ၄ကြောင်း ၅ကြောင်း ဖိုင်မဟုတ်ပဲ လက်တွေ့မှာက စာကြောင်းရေက သောင်းနဲ့ချီပြီး ရှိတဲ့အခါမျိုးမှာ ဘာသာစကားတစ်ခုစီရဲ့ စာကြောင်းတွေကို ပရိုဂရမ်တွေနဲ့ တွဲတာမျိုး လုပ်လို့ ထွက်တဲ့ error တွေလည်း ရှိသလို၊ အင်္ဂလိပ်စာကနေ မြန်မာစာကို ပြန်တာက တစ်ယောက်၊ အင်္ဂလိပ်စာကနေ ထိုင်းစာကို ဘာသာပြန်တာက တစ်ယောက်စီ ဖြစ်ပြီးတော့၊ ပြန်လို့ မတတ်တဲ့ စာကြောင်းတွေကို ချန်ထားတာမျိုးလည်း ရှိတတ်တာကြောင့်မို့ပါ။  
	
```
$ cat ./id-en-th-my.tst.txt 
1	Hello!	สวัสดี ครับ/ค่ะ	မင်္ဂလာ ပါ ။
2	How are you?	สบายดีไหม ครับ/ค่ะ	
3		คุณชื่ออะไร ครับ/คะ	မင်း နာမည် ဘယ်လို ခေါ် လဲ ။
4	Where are you from?	คุณมาจากไหน ครับ/คะ	မင်း က ဘယ် က လာ တာ လဲ ။
5	What is your job?	คุณทำงานอะไร ครับ/คะ	မင်း ဘာ အလုပ် လုပ် တာ လဲ ။
```

select-en-th-my.pl ပရိုဂရမ်ကိုသုံးပြီးတော့ field အားလုံးမှာ စာရှိနေတဲ့ စာကြောင်းတွေကိုပဲ (parallel ဖြစ်တဲ့စာကြောင်းတွေကိုပဲ) ဆွဲထုတ်မယ် ဆိုရင် ဖိုင်နာမည် argument ရဲ့ နောက်မှာ "c" ကိုရိုက်ထည့်ပြီး run ပါ။  

```
$ perl ./select-en-th-my.pl ./id-en-th-my.tst.txt c
1	Hello!	สวัสดี ครับ/ค่ะ	မင်္ဂလာ ပါ ။
4	Where are you from?	คุณมาจากไหน ครับ/คะ	မင်း က ဘယ် က လာ တာ လဲ ။
5	What is your job?	คุณทำงานอะไร ครับ/คะ	မင်း ဘာ အလုပ် လုပ် တာ လဲ ။
```

တကယ်လို့ parallel မဖြစ်တဲ့ စာကြောင်းတွေကိုပဲ ဆွဲထုတ်ချင်တယ်ဆိုရင်တော့ "w" command line argument ပေးပါ။ အောက်ပါအတိုင်း မြန်မာလိုဘာသာမပြန်ရသေးတဲ့ စာကြောင်းတွေ၊ အင်္ဂလိပ်စာက မရှိတဲ့ စာကြောင်းတွေကိုပဲ ရိုက်ထုတ်ပြပါလိမ့်မယ်။  

```
$ perl ./select-en-th-my.pl ./id-en-th-my.tst.txt w
2	How are you?	สบายดีไหม ครับ/ค่ะ	
3		คุณชื่ออะไร ครับ/คะ	မင်း နာမည် ဘယ်လို ခေါ် လဲ ။
```

## 21.[mk-speakers-json.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-speakers-json.pl)  

ဆိုကြပါစို့ ASR model ဆောက်ဖို့အတွက် speaker အမျိုးမျိုးနဲ့ အသံသွင်းထားတဲ့ wave ဖိုင်တွေ ကျွန်တော့်မှာ ရှိပါတယ်။ အဲဒီ wave ဖိုင်တွေကို speaker တစ်ယောက်ချင်းစီရဲ့ speaker-ID အနေနဲ့ပေးထားတဲ့ဖိုလ်ဒါအောက်ထဲမှာ သိမ်းထားပါတယ်။ အရင်ဆုံး အဲဒီ folder-path နဲ့ တကွ ရှိသမျှ wave ဖိုင်တွေကို find command နဲ့ပဲဖြစ်ဖြစ် list လုပ်ပြီး ဖိုင်တစ်ဖိုင်ထဲမှာ သိမ်းထားပါတယ်။ အဲဒီ ဖိုင်က [100-wave-filenames2.txt](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/json-output/100-wave-filenames2.txt) လိုမျိုးဖိုင်ပါ။ ဖိုင်ထဲမှာ ပါနေတဲ့ ဖိုင်နာမည်တွေရဲ့ ပုံစံက အောက်ပါအတိုင်းပါ။  

```
/Spk1/Univ1-HninHnin-F-25-burmese-2637.wav
/Spk2/Univ1-AungAung-M-20-burmese-1025.wav
/Spk3/Univ1-Sabai-F-29-burmese-1403.wav
/Spk4/Univ1-HtetHtet-M-20-burmese-1025.wav
/Spk5/Univ1-HlaHla-F-20-burmese-1403.wav
```

နားလည်မယ်လို့ထင်ပါတယ်။ ဖိုင်နာမည်မှာလည်း အဖွဲ့အစည်းနာမည်၊ speaker ရဲ့ နာမည်၊ female/male အချက်အလက်၊ မိခင်ဘာသာစကား နဲ့ ဖတ်ထားတဲ့ စာကြောင်းနံပါတ် တွေပါနေပါတယ်။ [mk-speakers-json.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-speakers-json.pl) က အဲဒီဖိုလ်ဒါနာမည်၊ ဖိုင်နာမည်ကနေ အချက်အလက်တွေကို ဆွဲထုတ်ယူပြီးတော့ json ဖိုင် format အနေနဲ့ စကရင်မှာ ရိုက်ထုတ်ပေးမှာ ဖြစ်ပါတယ်။  

run မယ်ဆိုရင် perl ./mk-speakers-json.pl <filename> ဆိုတဲ့ ပုံစံနဲ့ အောက်ပါအတိုင်း run ပါတယ်။  

```
perl ./mk-speakers-json.pl ./100-wave-filenames2.txt 
```

ထွက်လာတဲ့ json ဖိုင်ကိုလည်း လေ့လာလို့ ရအောင် တင်ပေးထားပါတယ်။ [speakers-info.json](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/json-output/speakers-info.json) ဖိုင်ကို ဖွင့်ကြည့်ပါ။  

ပုံမှန်အားဖြင့်က json ဖိုင်တွေက အချက်အလက်တွေကို serial အလိုက် တောက်လျှောက်သိမ်းသွားတာမို့၊ လူတွေအနေနဲ့က ဖတ်ရခက်ပါတယ်။ အဲဒီအတွက် Linux terminal မှာတော့ "jq" command လို json ဖိုင်တွေကို handle ကောင်းကောင်းလုပ်ပေးတဲ့ command line ပရိုဂရမ်တွေကို သုံးပြီး ကိုယ်လိုချင်တဲ့ အချက်အလက်တွေကို ဆွဲထုတ်ကြည့်လို့ ရပါတယ်။  

ဥပမာ json ဖိုင်ကို လူ့မျက်လုံးနဲ့ ဖတ်ရလွယ်တဲ့ ပုံစံအနေနဲ့ printout လုပ်ပေးစေချင်ရင် အောက်ပါအတိုင်း command ပေးကြည့်နိုင်ပါတယ်။ record တွေက အများကြီးမို့လို့ အိုက်ဒီယာရရှိအောင် record တချို့ကိုပဲ print လုပ်ပြထားပါတယ်။   

```bash
$ jq '.' ./speakers-info.json
{
  "Spk40": {
    "organization": "Univ2",
    "name": "SarU",
    "native_language": "burmese",
    "gender": "F",
    "age": "46",
    "recorded_sentence": "1975,2408"
  },
  "Spk36": {
    "organization": "Univ1",
    "age": "23",
    "native_language": "burmese",
    "gender": "F",
    "name": "TheThe",
    "recorded_sentence": "1175"
  },
  "Spk43": {
    "native_language": "Kayin",
    "name": "SawGyi",
    "gender": "M",
    "age": "23",
    "recorded_sentence": "12671,1949",
    "organization": "Univ1"
  },
  "Spk15": {
    "organization": "Univ1",
    "age": "22",
    "name": "HtweHtwe",
    "native_language": "burmese",
    "gender": "M",
    "recorded_sentence": "4,12,12"
  },
  "Spk45": {
    "organization": "Univ1",
    "native_language": "burmese",
    "gender": "M",
    "name": "MyoAung",
    "age": "28",
    "recorded_sentence": "10001"
  },
  "Spk17": {
    "organization": "Univ1",
    "recorded_sentence": "223,9527",
    "age": "33",
    "name": "SuSu",
    "native_language": "burmese",
    "gender": "F"
  },
  ...
  ...
  ...
```

ဥပမာ json ဖိုင်ကနေ နာမည်၊ ကျား/မ၊ အသံသွင်းထားပြီးဖြစ်တဲ့ စာကြောင်းနံပါတ် တွေကိုပဲ ဆွဲထုတ်ကြည့်ချင်တယ်ဆိုရင် အောက်ပါအတိုင်း command ပေးပြီး ကြည့်ရှုနိုင်ပါတယ်။  

```
$ jq '.[]|[.name, .gender, .recorded_sentence]|join(",")' ./speakers-info.json 
"SarU,F,1975,2408"
"TheThe,F,1175"
"SawGyi,M,12671,1949"
"HtweHtwe,M,4,12,12"
"MyoAung,M,10001"
"SuSu,F,223,9527"
"MyatMon,F,1975"
"NayKyar,F,2018"
"MyintMyint,F,25,6776,6889,1739"
"KyawMoe,M,1975"
"OoOo,F,1975,1975,5404,2018,5404"
"HlaHla,F,1403"
"YeKyaw,M,2975,6338,5404"
"Thiha,M,2975,2408"
"KoKo,M,1975,12671"
"MuMu,F,223"
"DoeLone,M,2664,12671"
"HtetHtet,M,1025,223,6776,1975,1022,693,6338,10031,1949"
"PhyoPhyo,M,210,12,92"
"ZweKaung,M,1222,1975"
"Sandar,F,25,172,127,154"
"SoeMoe,M,1039,154"
"ZinWaine,M,6776"
"Ei,F,2540"
"WuLin,M,506"
"Kaung,M,1005,1006"
"SeinSein,F,4,2107,1175,2975,2530"
"HninHnin,F,2637,2637"
"MinMin,M,1739"
"MoeMoe,F,6776,5975,1792,9587,1739,6338"
"YinYinMyint,F,1022"
"NyeinNyein,M,2324,2408,2107"
"HtooHtoo,M,2018"
"ChawChaw,F,4039"
"NayOo,M,2975"
"MyatMyat,F,127,5063,1975"
"YiYi,F,25"
"Sabai,F,1403,1430"
"WinWin,F,1975,5975"
"Shwe,F,1975,1792,12671"
"ZayYar,M,1175"
"MaGyi,F,154"
"KhineKhine,F,127,2107,2018,1739,2049"
"AungAung,M,1025"
"GanDaMar,F,2018"
```

## 22. [string-distance.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/string-distance.pl)  

string နှစ်ခု (မြန်မာလိုဆိုရင်တော့ စာကြောင်းနှစ်ကြောင်း) မှာ ရှိနေတဲ့ စာလုံး တစ်လုံးချင်းစီကို ဘယ်ကနေညာတိုက်စစ်သွားပြီး၊ မတူရင် တန်ဖိုးကို 1+ တိုးတိုးသွားပြီးတော့ ရလာတဲ့ တန်ဖိုးကို 100 နဲ့ မြှောက်ပြီး၊ string length နဲ့ စားရင် string နှစ်ခုက ဘယ်လောက်တူသလဲ ဆိုတာကို အကြမ်းမျဉ်းတော့ တိုင်းကြည့်လို့ရပါတယ်။ perl code နဲ့ရေးရင်တော့ အောက်ပါအတိုင်းဖြစ်ပါလိမ့်မယ်။  

```perl
# calculating similarity score
my $distance  = (100 * $differenceValue/ $maxLength);
```

string similarity တိုင်းတာတဲ့ကိစ္စကို ရှင်းပြဖို့နဲ့ perl script ရေးတဲ့ လေ့ကျင့်ခန်းအနေနဲ့ ကျောင်းသားတွေကို စာသင်တဲ့နေရာမှာ သုံးဖို့ ဥပမာအနေနဲ့ ရေးပြထားတာဖြစ်ပါတယ်။   

```
$ perl ./string-distance.pl "ကျောင်းသား" "ကျောင်းသူ"
20

$ perl ./string-distance.pl "Who are you?" "Who am I?"
58.3333333333333

$ perl ./string-distance.pl "ပါပါ ပြန်လာပြီ" "ပပ ပြန်လာပြီ"
92.8571428571429

```

## 23. [print-matched-char-seq.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-matched-char-seq.pl)  
   (RE နဲ့ ကိုယ်ရှာဖွေချင်တဲ့ character တွေကို string တစ်ခုစီမှာ တိုက်စစ်ပြီး၊ matched ဖြစ်တဲ့ character sequence ကို ရိုက်ထုတ်ကြည့်ဖို့အတွက် သုံးခဲ့တယ်) 
   
မြန်မာ-ကချင် parallel corpus ကို ပြင်ဆင်တဲ့အခါမှာ သုံးခဲ့တဲ့ script တစ်ခုပါ။  
ဘာသာပြန်ပြီး ရလာတဲ့ အခါမှာ ကြုံရတာက မြန်မာစာဘက် အခြမ်းမှာလည်း စာကြောင်း တစ်ကြောင်းထက်ပိုတယ်။ ကချင်စာဘက် အခြမ်းမှာလည်း စာကြောင်း တစ်ကြောင်းထက်ပိုတယ် ဆိုတဲ့ အခြေအနေမှာ။ ပုံမှန် လုပ်တဲ့ Machine Translation အတွက်က အဲဒီ စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ parallel ပြန်တွဲပေးဖို့ လိုအပ်ပါတယ်။ အဲဒီအတွက်က အရင်ဆုံး မြန်မာစာဘက် အခြမ်းမှာ၊ ကချင်စာဘက်အခြမ်းမှာ စာကြောင်းရေ စုစုပေါင်းဘယ်လောက်ပါသလဲ ဆိုတာကို သိဖို့လိုအပ်ပါတယ်။ အဲဒီအတွက်က ကချင်စာရဲ့ စာကြောင်း အဆုံးသတ်မှာ သုံးကြတဲ့ sentence ending marker သုံးမျိုးဖြစ်တဲ့ (.?!) နဲ့ ဖြတ်ထုတ်လို့ ရပါတယ်။ ဥပမာ အောက်ပါ RE နဲ့ ဖြတ်ထုတ်တာမျိုးပါ။  

```perl
 my @kachinSentArray = split(/[\.|\?|\!]/, $kachinSent);
```

အထက်ပါအတိုင်း split function ကိုသုံးပြီး ဖြတ်ထုတ်လိုက်ရင် ရတဲ့ array ထဲမှာက sentence ending marker တွေက ပြုတ်ကျန်ခဲ့ပါလိမ့်မယ်။
အဲဒီလိုပဲ မြန်မာစာဘက် အခြမ်းက စာကြောင်းတွေကိုလည်း တစ်ကြောင်းစီ ဖြတ်ထုတ်ပြီး၊ မြန်မာ-ကချင် parallel sentence လုပ်ချင်တဲ့အခါမှာ အခက်အခဲက ပြန်တွဲတဲ့အခါမှာ sentence ending marker တွေကို ပြန်ထည့်ဖို့အတွက် ဘယ်ကချင်စာကြောင်းက ဘယ် sentence ending နဲ့ ဆုံးတာလဲ ဆိုတာကို မှတ်ထားဖို့လိုအပ်ပါတယ်။ အခု တင်ပေးထားတဲ့ print-matched-char-seq.pl က မဖြတ်ခင်မှာ input လုပ်ပေးလိုက်တဲ့ ကချင်စာကြောင်းထဲမှာ ပါဝင်တဲ့ sentence ending marker sequence တွေကို သိမ်းထားဖို့အတွက် စမ်းရေးကြည့်ခဲ့တဲ့ perl script ပါ။ အသုံးဝင်ပါလိမ့်မယ်။  

အသုံးပြုပုံ ဥပမာကတော့ ဆိုကြပါစို့ ကျွန်တော်တို့မှာ အောက်ပါအတိုင်း multi-sentence ကချင် စာကြောင်းတွေရှိတဲ့ ဖိုင် kc-input (https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/kc-input) တစ်ဖိုင်ရှိနေတယ်။

```
lar@lar-air:/media/lar/Transcend/yLab/intern-1/kc-my-team/original/25-july-2019/script$ cat ./kc-input 
Nga chyu one .
Two tea .
Tea i ? Coeffe i ? Lapai lahkra i ? Nest i ?
N gup mi ram sha nga ai .
U , Ka tsu , Jahkan , Shat ka-ngau boi lahkawng . Nang gaw . Hpa sha na rai ?
A shan n bang ai . La sha ma hte nam sha ma hpa sha mayu ai rai ? Htet u le .
```

အဲဒီ kc-input ဖိုင်ထဲမှာရှိနေတဲ့ ကချင် စာကြောင်း တစ်ကြောင်းချင်းစီရဲ့ sentence ending marker တွေကို print ထုတ်ကြည့်ချင်ရင် အောက်ပါအတိုင်း run ပါ။  

```
lar@lar-air:/media/lar/Transcend/yLab/intern-1/kc-my-team/original/25-july-2019/script$ perl ./print-matched-char-seq.pl ./kc-input 
input: Nga chyu one .
Matched Char Sequence: .
input: Two tea .
Matched Char Sequence: .
input: Tea i ? Coeffe i ? Lapai lahkra i ? Nest i ?
Matched Char Sequence: ? ? ? ?
input: N gup mi ram sha nga ai .
Matched Char Sequence: .
input: U , Ka tsu , Jahkan , Shat ka-ngau boi lahkawng . Nang gaw . Hpa sha na rai ?
Matched Char Sequence: . . ?
input: A shan n bang ai . La sha ma hte nam sha ma hpa sha mayu ai rai ? Htet u le .
Matched Char Sequence: . ? .
```

## 31. [replace-with-lineno.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/replace-with-lineno.pl)  

အတို ရှင်းပြရရင် POS tagged corpus တစ်ခုကို developing လုပ်နေကြတယ် ဆိုပါစို့။ ထုံးစံအတိုင်းပဲ အဲဒီ corpus ထဲမှာ manual tagging အလုပ်မို့လို့ typing error တွေ၊ tag ရဲ့ symbol က slash "/" ဆိုပြီး သတ်မှတ်ထားတယ်ဆိုရင်လည်း slash ခြားဖို့ မေ့သွားတာမျိုးတွေ ဖြစ်တတ်ပါတယ်။ အဲဒီလိုင်းတွေကို လိုင်နံပါတ်နဲ့တကွ ဆွဲထုတ်ပြီးတော့ manual tagging လုပ်နေတဲ့သူဆီကို အကြောင်းကြားပြီးတော့ စာကြောင်းတွေကို ပြန်စစ်ပေးဖို့၊ POS tag တွေကို ပြန်ပြင်ပေးဖို့ ပြောရပါတယ်။ ပြန်ပြင်ပေးပြီး ရောက်လာတဲ့ အခါမှာတော့ အဲဒီ လိုင်းနံပါတ်တပ်ထားတဲ့ ပြင်ထားတဲ့ စာကြောင်းတွေသိမ်းထားတဲ့ ဖိုင်ကို ကိုင်ပြီး အော်ရဂျင်နယ် POS tagged corpus ကို ဝင် update လုပ်ပေးဖို့ လိုအပ်ပါတယ်။ ဒီ perl script က အဲဒီ အလုပ်အတွက် ရေးခဲ့တာ ဖြစ်ပါတယ်။ ဥပမာအနေနဲ့ စာကြောင်းအနည်းငယ်ကိုပဲ မြင်သာအောင် ပြပြီး ရှင်းမှာ ဖြစ်ပေမဲ့ လက်တွေမှာ ပြင်ရမယ့်စာကြောင်းတွေက corpus ကြီးရင်ကြီးသလို အများကြီးမို့၊ အခုလိုမျိုး script ရှိရင် အများကြီးအဆင်ပြေပါလိမ့်မယ်။  

correction.txt ဆိုတဲ့ ဖိုင်ထဲမှာ line_number<TAB>Checked_POS_Tagged_Sentence ဆိုတဲ့ format နဲ့ အောက်ပါအတိုင်း ရှိနေပါတယ်။  
	
```
$ head correction.txt
70 တစ်/tn လ/n လောက်/part ပါ/part ပဲ/part ။/punc
114 မနက်/n ခုနှစ်/tn နာရီ/n မှာ/ppm နှိုး/v ပေး/part ပါ/part ။/punc
133 အခု/n အလုပ်/n လုပ်/v နေ/part ပါ/part တယ်/ppm ။/punc
145 ဟုတ်ကဲ့/part ။/punc ရှိ/v ပါ/part တယ်/ppm ။/punc
173 ပန်းသီး/n ၁/num လုံး/part ကို/ppm ဘယ်လောက်/adj လဲ/part ။/punc
188 ဒီ/adj သစ်တော်သီး/n အချို/n လား/part အချဉ်/n လား/part ။/punc
192 ဟုတ်ကဲ့/part ။/punc ထည့်/v ပေး/part ပါ/part မယ်/ppm ။/punc
194 ဟင့်အင်း/part ။/punc မ/part ရောင်း/v ပါ/part ဘူး/part ။/punc
204 ဘယ်/adj ဟာ/pron က/ppm ပို/adj ကြီး/v လဲ/part ။/punc
218 မြန်မာ/n သည်/ppm ကျွန်တော်/pron တို့/part နိုင်ငံ/n နှင့်/conj သံတမန်/n ရေးရာ/n စာချုပ်/n နှစ်/n ပေါင်း/n ၄၀/num ကျော်/adj ရှိ/v သော်လည်း/conj ကျွန်တော်/pron တို့/part နှင့်/conj အခု/n ထိ/ppm ဝေးကွာ/v သော/part စိမ်း/v သော/part နိုင်ငံ/n ဖြစ်/v နေ/part ပါ/part တယ်/ppm ။/punc
```

POS tagged corpus ကြီးထဲကနေ မှားနေတဲ့ စာကြောင်းတွေ (သို့) အထက်ပါ လိုင်းနံပါတ်နဲ့ ဝင်ပြင်ချင်တဲ့ စာကြောင်းတွေကိုပဲ sed command နဲ့ ဆွဲထုတ်ပြရရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  ဒီနေရာမှာ -n က option က sed command ကို လိုင်းတိုင်းကို print မလုပ်ပါနဲ့ silent mode နဲ့ အလုပ်လုပ်ပေးပါ၊ သို့မဟုတ် အင်္ဂလိပ်လိုတော့ suppress automatic printing of pattern space လုပ်ပေးပါလို့ ဆိုလိုပါတယ်။ 70p ဆိုတာက လိုင်းနံပါတ် ၇၀ ကို print လုပ်ပေးပါလို့ condition ပေးထားတာ ဖြစ်ပါတယ်။  

```
$ sed -n '70p;114p;133p;145p;173p;188p;192p;194p;204p;218p' ./myanmar.pos.rmpipe.txt
တ/tn လ/n လောက်/part ပါပဲ ။/punc
မနက်/n ခုနှစ်/tn နာရီ/n /မှာ/ppm နှိုး/v ပေး/part ပါ/part ။/punc
အခု/n အလုပ်/n လုပ် နေ ပါ/part တယ်/ppm ။/punc
ဟုတ်ကဲ့/part ။/punc ရှိ ပါ/part တယ်/ppm ။/punc
ပန်းသီး/n ၁/num လုံး/p ကို/ppm ဘယ်လောက်/adj လဲ/part ။/punc
ဒီ/adj သစ်တော်/n သီး/n အချို/n လား/part အချဉ်/n လား/ ။/punc
ဟုတ်ကဲ့/part ။/punc ထည့်/ ပေး/part ပါ/part မယ်/ppm ။/punc
ဟင့်အင်း/part ။/punc မ ရောင်း ပါ/part ဘူး/part ။/punc
ဘယ်/adj ဟာ/pron က/ ပို/adj ကြီး/v လဲ/part ။/punc
မြန်မာ/n သည်ppm ကျွန်တော်/pron တို့/part နိုင်ငံ/n နှင့်/conj သံတမန်/n ရေးရာ/n စာချုပ်/n နှစ်/n ပေါင်း/n ၄၀/num ကျော်/adj ရှိ/v သော်လည်း/conj ကျွန်တော်/pron တို့/part နှင့်/conj အခု/n ထိ/ppm ဝေးကွာသော/adj စိမ်းသော/adj နိုင်ငံ/n ဖြစ်/v နေ/part ပါ/part တယ်/ppm ။/punc
```

run တဲ့ပုံစံကတော့ အထက်ပါ ဖိုင်နှစ်ဖိုင်ကို command line argument အနေနဲ့ ပေးပြီးတော့ အောက်ပါအတိုင်း perl script ကို run ယုံပါပဲ။  

```
perl ./replace-with-lineno.pl ./correction.txt ./myanmar.pos.rmpipe.txt  > ./myanmar.pos.rmpipe.txt.corrected
```

## 32. [chk-pos-tags.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/chk-pos-tags.pl)  

မြန်မာစာ NLP R&D တိုးတက်ဖွံ့ဖြိုးဖို့အတွက် ကျွန်တော်ဦးဆောင် လုပ်နေတဲ့ myPOS corpus ကို extension လုပ်ဖို့ စာကြောင်းတွေကို manual corpus တပ်ကြတဲ့အခါမှာ ထုံးစံအတိုင်းပဲ လူက လုပ်ရတဲ့ အလုပ်မို့လို့ အမှားမကင်းပါဘူး။ အများသောအားဖြင့် typing error ဖြစ်တာမျိုး၊ tag delimeter (e.g. /) ကိုပဲ ရိုက်ပြီး POS tag name ကို ရိုက်ထည့်ဖို့ မေ့သွားတာမျိုးတွေ ဖြစ်တတ်ပါတယ်။ အဲဒီအမှားတွေကို သတ်မှတ်ထားတဲ့ myPOS POS tag-set ၁၅ခုထဲမှာ ပါသလား၊ မပါသလား ဆိုတာကို တိုက်စစ်ဖို့အတွက် အကြမ်းရေးထားတဲ့ perl script ပါ။  

command line argument အဖြစ်ပေးမဲ့ POS tagged corpus ဖိုင်ကို မြင်သာအောင် head command နဲ့ ပထမဆုံး စာကြောင်း ၁၀ကြောင်းကို ရိုက်ထုတ်ကြည့်ရအောင်။  

```
$ head ./myanmar.pos.rmpipe.txt
မင်္ဂလာ/n ပါ/part ။/punc
မင်္ဂလာ/n ပါ/part ။/punc
မင်္ဂလာ/n ပါ/part ။/punc
ကျေးဇူးတင်/v ပါ/part တယ်/ppm ။/punc
ရ/v ပါ/part တယ်/ppm/part ။/punc
ကျေးဇူးတင်/v စရာ/part မ/part လို/v ပါ/part ဘူး/part ။/punc
စိတ်မကောင်း/v ပါ/part ဘူး/part ။/punc
ခွင့်လွှတ်/v ပါ/part ။/punc
ရ/v ပါ/part တယ်/ppm ။/punc
ဟုတ်/v လား/part ။/punc
```

chk-pos-tags.pl ဖိုင်ကို run တဲ့အခါမှာ အောက်ပါအတိုင်း မှားတဲ့စာကြောင်း ရဲ့လိုင်းနံပါတ်ရော၊ စာကြောင်းရော ရိုက်ထုတ်ပြပါလိမ့်မယ်။  
ပြီးတော့ ပထမဆုံး မှားတဲ့ စာလုံးအပိုင်းကိုလည်း ရိုက်ထုတ်ပြမှာဖြစ်ပါတယ်။ တစ်ခုရှိတာက တစ်ခုထက်မက ပိုတဲ့ အမှားတွေက စာကြောင်းတစ်ကြောင်းထဲမှာလည်း ရှိနေနိုင်ပါတယ်။ အဲဒါကြောင့် ပြန်စစ်ဆေးတဲ့ အခါမှာတော့ စာကြောင်းတစ်ကြောင်းလုံးကို ဂရုစိုက် စစ်ဆေးစေချင်ပါတယ်။ POS tagging ရဲ့ သဘောသဘာဝအရ စာလုံး တစ်လုံးကို tag မလုပ်ခင်မှာလည်း ရှေ့နောက် စာလုံးတွေကို တွဲကြည့်ရမှာ ဖြစ်ပါတယ်။  

```
OS)/smt-with-pos/my-pos-tagging/err-chk-github$ ./chk-pos-tags.pl ./myanmar.pos.rmpipe.txt | head -n 20
Tag ERROR! Line no (70): တ/tn လ/n လောက်/part ပါပဲ ။/punc
ပါပဲ:
Tag ERROR! Line no (114): မနက်/n ခုနှစ်/tn နာရီ/n /မှာ/ppm နှိုး/v ပေး/part ပါ/part ။/punc
:မှာ
Tag ERROR! Line no (133): အခု/n အလုပ်/n လုပ် နေ ပါ/part တယ်/ppm ။/punc
လုပ်:
Tag ERROR! Line no (145): ဟုတ်ကဲ့/part ။/punc ရှိ ပါ/part တယ်/ppm ။/punc
ရှိ:
Tag ERROR! Line no (173): ပန်းသီး/n ၁/num လုံး/p ကို/ppm ဘယ်လောက်/adj လဲ/part ။/punc
လုံး:p
Tag ERROR! Line no (188): ဒီ/adj သစ်တော်/n သီး/n အချို/n လား/part အချဉ်/n လား/ ။/punc
လား:
Tag ERROR! Line no (192): ဟုတ်ကဲ့/part ။/punc ထည့်/ ပေး/part ပါ/part မယ်/ppm ။/punc
ထည့်:
Tag ERROR! Line no (194): ဟင့်အင်း/part ။/punc မ ရောင်း ပါ/part ဘူး/part ။/punc
မ:
Tag ERROR! Line no (204): ဘယ်/adj ဟာ/pron က/ ပို/adj ကြီး/v လဲ/part ။/punc
က:
Tag ERROR! Line no (218): မြန်မာ/n သည်ppm ကျွန်တော်/pron တို့/part နိုင်ငံ/n နှင့်/conj သံတမန်/n ရေးရာ/n စာချုပ်/n နှစ်/n ပေါင်း/n ၄၀/num ကျော်/adj ရှိ/v သော်လည်း/conj ကျွန်တော်/pron တို့/part နှင့်/conj အခု/n ထိ/ppm ဝေးကွာသော/adj စိမ်းသော/adj နိုင်ငံ/n ဖြစ်/v နေ/part ပါ/part တယ်/ppm ။/punc
သည်ppm:
```

## 33. [count-string-length.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/count-string-length.pl)  

ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်း တစ်ကြောင်းခြင်းစီရဲ့ စာလုံး (character including spaces) အရေအတွက်ကို၊ လိုင်းနံပါတ်နဲ့တကွ ရိုက်ထုတ်ဖို့အတွက် ရေးခဲ့ပါတယ်။ run လိုက်ရင် အောက်ပါအတိုင်း screen မှာ print ရိုက်ပေးပါလိမ့်မယ်။ ပထမဆုံး ကော်လံက လိုင်းနံပါတ်ပါ၊ ဒုတိယကော်လံက စာကြောင်းဖြစ်ပြီးတော့၊ တတိယကော်လံက သက်ဆိုင်ရာ စာကြောင်းရဲ့ စာလုံးအရေအတွက်ပါ။ ကော်လံ တစ်ခုနဲ့ တစ်ခုကိုတော့ \<TAB\> ကီးနဲ့ ခြားပေးထားပါတယ်။   

ဒီ script ကို ထိုင်နိုင်ငံးမှာ သုံးဖို့အတွက် COVID-19 ဗိုင်းရပ်စ် စောင့်ကြည့်ရေး app ကိုပြင်ဆင်တဲ့နေရာမှာ မြန်မာစာကို ထည့်ဖို့အတွက် UI နဲ့ ရှင်းလင်းချက်တွေကို မြန်မာလိုဘာသာပြန်တဲ့အခါမှာ မြန်မာစာကြောင်းတွေက ရှည်နေတဲ့အတွက် စာလုံးအရေအတွက်နဲ့ကန့်သတ်ပြီး ဘာသာပြန်ဖို့အတွက်၊ စာလုံးတွေကို ရေတွက်တဲ့ နေရာမှာ သုံးခဲ့ပါတယ်။  

```
perl ./count-string-length.pl ./ui.shuf.my.head 
1	အန္တရာယ် အမျိုးအစားများ	23
3	ကျေးဇူးပြုပြီးတော့ ထိုင်း ID ကဒ်နံပါတ် သို့မဟုတ် နိုင်ငံကူးလက်မှတ် နံပါတ် ကို မှန်မှန်ကန်ကန် ဖြည့်ပါ။	101
4	ကျေးဇူးပြုပြီးတော့ ထိုင်း ID ကဒ်နံပါတ် သို့မဟုတ် နိုင်ငံကူးလက်မှတ် နံပါတ် ကို ဖြည့်ပါ။	86
5	OTP ကုဒ်နံပါတ်ကို နောက်တစ်ခု ထပ်တောင်းပါ။	41
6	မဟုတ်ဘူး	8
7	မဟုတ်ဘူး	8
8	အဆက်အသွယ် ရပ်ဆိုင်းသွားပါတယ်။ ကျေးဇူးပြုပြီးတော့ လော့ဂ်အင် ပြန်ဝင်ပါ။	69
9	နေ့စဉ် ကိုယ်တိုင် စစ်ဆေးရေးမှတ်တမ်း စာမျက်နှာ	45
10	ဆက်သွယ်ရန် ဖုန်းနံပါတ် ဖြည့်စွက် စာမျက်နှာ	42
```

## 34. [print-diff-word.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-diff-word.pl)  

လိုင်းအရေအတွက်တူတဲ့ ဖိုင်နှစ်ဖိုင်ထဲက စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ နှိုင်းယှဉ်ကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ perl script ပါ။ ဒီနေရာမှာ စိတ်ဝင်စားတာက မတူတဲ့ စာလုံးတွေကိုပါပဲ။  

code ကို တိုက်ရိုက်ကြည့်တာထက် run ပြပြီးတော့ output တွေကို ကြည့်လိုက်ရင် ပိုမြင်သာမှာမို့ ပထမဆုံးအနေနဲ့ word segmentation ဖြတ်ထားတဲ့ဖိုင်နှစ်ဖိုင်ကို cat command နဲ့ ရိုက်ပြပါမယ်။ error.txt.word ဆိုတဲ့ ဖိုင်က စာလုံးပေါင်းမှားနေတဲ့ မြန်မာစာကြောင်း ခြောက်ကြောင်းကို သိမ်းထားတဲ့ဖိုင်ပါ။  

```
$ cat ./error.txt.word
သိခြင် လိုက် တာ
လှ လိုက် ဝာာ
🎼 ညနေခင်း ရဲႉ လေပြေ ထဲ မာ . . . 🎼 🎧
ပြည်တော််ပြန် တွေ ကို ကြိုဆို ဖို့ ၊ လိုအပ် တဲ့ ကျန်းမာရေး လုပ်ငန်း တွေ ကို ကျန်းမာရေးဝန်ကြီးဌာန နဲ့ ပူးပေါင်း ဆောင်ရွက် ဖို့ ၊ သက်ဆိုင် ရာ တိုင်း ၊ ပြည်နယ် တွေ ကို ခရီးဆက် နိုင်ရေး စီစဉ် ဖို့ တာဝန် တွေ က ကရင်ပြည််နယ်အစိုးရ ပေါ် မှာ အများဆုံး ကျ ပါတယ် ။
သိဒယ် သိဒယ် အဘ 😁 😁
မင်း ဂ ဘျင် ကြီး လား ကွာ နည်းနည်း တော့ များ ဒေ
```

correct.txt.word ဆိုတဲ့ ဖိုင်က စာလုံးပေါင်း အမှားတွေကို ပြင်ထားတဲ့ဖိုင်ပါ။  

```
$ cat ./correct.txt.word
သိချင် လိုက် တာ
လှ လိုက် တာ
🎼 ညနေခင်း ရဲႉ လေပြေ ထဲ မှာ . . . 🎼 🎧
ပြည်တော်ပြန် တွေ ကို ကြိုဆို ဖို့ ၊ လိုအပ် တဲ့ ကျန်းမာရေး လုပ်ငန်း တွေ ကို ကျန်းမာရေးဝန်ကြီးဌာန နဲ့ ပူးပေါင်း ဆောင်ရွက် ဖို့ ၊ သက်ဆိုင် ရာ တိုင်း ၊ ပြည်နယ် တွေ ကို ခရီးဆက် နိုင်ရေး စီစဉ် ဖို့ တာဝန် တွေ က ကရင်ပြည်နယ်အစိုးရ ပေါ် မှာ အများဆုံး ကျ ပါတယ် ။
သိတယ် သိတယ် အဘ 😁 😁
မင်း က ဘုရင် ကြီး လား ကွာ နည်းနည်း တော့ များ တယ်
```

./error.txt.word ဖိုင်နဲ့ ./correct.txt.word ဖိုင်ကို argument အနေနဲ့ ပေးပြီး run ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
$ perl ./print-diff-word.pl ./error.txt.word ./correct.txt.word
သိခြင်|သိချင်
ဝာာ|တာ
မာ|မှာ
ပြည်တော််ပြန်|ပြည်တော်ပြန် ကရင်ပြည််နယ်အစိုးရ|ကရင်ပြည်နယ်အစိုးရ
သိဒယ်|သိတယ် သိဒယ်|သိတယ်
ဂ|က ဘျင်|ဘုရင် ဒေ|တယ်
```
ဒီနေရာမှာ "တာ" ဆိုတဲ့ စာလုံးရယ်၊ "ပြည်တော်ပြန်" စာလုံးနဲ့ "ကရင်ပြည်နယ်အစိုးရ" ဆိုတဲ့ စာလုံးသုံးလုံး က ဘာတွေက မှားနေတာလဲ ဆိုတာကို ကျွန်တော် အခုသုံးနေတဲ့ Chrome browser မှာတော့ မသိသာပါဘူး။ အဲဒါကြောင့် အဲဒီ စာလုံးတွေကို gedit text editor မှာ ကော်ပီကူးပြီးတော့ screen capture လုပ်ထားတဲ့ ပုံဖိုင်ကို အောက်ပါအတိုင်း တင်ပေးထားပါတယ်။ သေချာ ဂရုစိုက်ကြည့်ရင် မြင်ရပါလိမ့်မယ်။ "သုည ရေးချ ရေးချ" ကို "တာ" အဖြစ် ရိုက်ထားတာ နဲ့ အသတ်တွေကို ထပ်ပြီး ရိုက်ထားတာတွေကို။  

![invisible-spelling-error-example](https://github.com/ye-kyaw-thu/tools/blob/master/perl/test-data/invisible-spelling-error1.png)  


input လုပ်တဲ့ ဖိုင်တွေထဲမှာ တကယ်လို့ syllable segmentation ဖြတ်ထားရင် syllable level comparison အဖြစ် အလုပ်လုပ်သွားပါလိမ့်မယ်။ ./error.txt.word.syl.clean ဖိုင်ကတော့ ./error.txt.word ဖိုင်ကို syllable ဖြတ်ထားပြီးတော့ ပိုနေတဲ့ space တွေကို clean လုပ်ထားတဲ့ ဖိုင်ဖြစ်ပါတယ်။  

```
$ cat ./error.txt.word.syl.clean
သိ ခြင် လိုက် တာ
လှ လိုက် ဝာာ
🎼 ည နေ ခင်း ရဲႉ လေ ပြေ ထဲ မာ . . . 🎼 🎧
ပြည် တော်် ပြန် တွေ ကို ကြို ဆို ဖို့ ၊ လို အပ် တဲ့ ကျန်း မာ ရေး လုပ် ငန်း တွေ ကို ကျန်း မာ ရေး ဝန် ကြီး ဌာ န နဲ့ ပူး ပေါင်း ဆောင် ရွက် ဖို့ ၊ သက် ဆိုင် ရာ တိုင်း ၊ ပြည် နယ် တွေ ကို ခ ရီး ဆက် နိုင် ရေး စီ စဉ် ဖို့ တာ ဝန် တွေ က က ရင် ပြည်် နယ် အ စိုး ရ ပေါ် မှာ အ များ ဆုံး ကျ ပါ တယ် ။
သိ ဒယ် သိ ဒယ် အ ဘ 😁 😁
မင်း ဂ ဘျင် ကြီး လား ကွာ နည်း နည်း တော့ များ ဒေ
```

./correct.txt.word.syl.clean ဖိုင်ကတော့ ./correct.txt.word ဖိုင်ကို syllable ဖြတ်ထားပြီးတော့ ပိုနေတဲ့ space တွေကို clean လုပ်ထားတဲ့ ဖိုင်ဖြစ်ပါတယ်။  

```
$ cat ./correct.txt.word.syl.clean
သိ ချင် လိုက် တာ
လှ လိုက် တာ
🎼 ည နေ ခင်း ရဲႉ လေ ပြေ ထဲ မှာ . . . 🎼 🎧
ပြည် တော် ပြန် တွေ ကို ကြို ဆို ဖို့ ၊ လို အပ် တဲ့ ကျန်း မာ ရေး လုပ် ငန်း တွေ ကို ကျန်း မာ ရေး ဝန် ကြီး ဌာ န နဲ့ ပူး ပေါင်း ဆောင် ရွက် ဖို့ ၊ သက် ဆိုင် ရာ တိုင်း ၊ ပြည် နယ် တွေ ကို ခ ရီး ဆက် နိုင် ရေး စီ စဉ် ဖို့ တာ ဝန် တွေ က က ရင် ပြည် နယ် အ စိုး ရ ပေါ် မှာ အ များ ဆုံး ကျ ပါ တယ် ။
သိ တယ် သိ တယ် အ ဘ 😁 😁
မင်း က ဘု ရင် ကြီး လား ကွာ နည်း နည်း တော့ များ တယ်
```

syllable level အနေနဲ့ ဖိုင်နှစ်ဖိုင်ထဲမှာ ရှိနေတဲ့ စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ နှိုင်းယှဉ်ကြည့်ကြရအောင်။  

```
$ perl ./print-diff-word.pl ./error.txt.word.syl.clean ./correct.txt.word.syl.clean
ခြင်|ချင်
ဝာာ|တာ
မာ|မှာ
တော််|တော် ပြည််|ပြည်
ဒယ်|တယ် ဒယ်|တယ်
က|ဂ ဘု|ဘျင် ရင်|ကြီး ကြီး|လား လား|ကွာ ကွာ|နည်း နည်း|တော့ တော့|များ များ|ဒေ တယ်| Null
```

