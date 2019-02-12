# Example usages of perl programs

မှတ်ချက်။ ။ perl ပရိုဂရမ်တွေရဲ့ အသုံးပြုနည်းကို ဥပမာအဖြစ် စမ်းသုံးပြထားသော test-data ဖိုင်အများစုက အင်တာနက်ပေါ်က စာကြောင်းတွေကို တိုက်ရိုက်ယူသုံးထားသောကြောင့် စာလုံးပေါင်းမှားတာမျိုး၊ စာကြောင်းတွေက နားလည်ရခက်တာမျိုးလည်း ရှိနိုင်တာကို နားလည်ပေးကြပါ။  

## [clean-space.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-space.pl)

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

## [rm-EnglishSentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-EnglishSentences.pl)

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
## [word-analysis.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/word-analysis.pl)

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
## [print-emojiSentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-emojiSentences.pl)   

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

## [dq-multilines.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/dq-multilines.pl)

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

## [mk-abstract-para.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-abstract-para.pl)

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

## [print-mySentenceOnly.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-mySentenceOnly.pl)

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

## [rm-symbol-and-myVowel-only-sentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-symbol-and-myVowel-only-sentences.pl)  

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

## [rm-space-btw-numbers.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-space-btw-numbers.pl)  

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

## 10. [print-ngram.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-ngram.pl)  

ဖိုင်ထဲမှာ ရှိတဲ့ စာလုံးဖြတ်ထားတဲ့ စာကြောင်းတွေကို ကိုယ်လိုချင်တဲ့ ngram အတွဲတွေအဖြစ် print ထုတ်ဖို့ ရေးခဲ့တယ်။
input.txt ဖိုင်ထဲမှာ အောက်ပါအတိုင်း စာကြောင်း ၅ကြောင်း ရှိပါတယ်။  

```bash
$ cat input.txt 
This is a cat .
Who are you ?
My name is Ko Gyi .
I don't know who you are .
Beer Chang Beer Chang ... Beer Chang Beer Chang .
```

2gram စာလုံးအတွဲတွေအဖြစ် print ထုတ်စေချင်ရင် command line argument ကို 2 ပေးပြီး run ပါတယ်။  

```bash
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

3gram စာလုံးအတွဲတွေအဖြစ် print ထုတ်စေချင်ရင် command line argument ကို 3 ပေးပြီး run ပါတယ်။ 

```bash
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
