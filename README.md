# Preprocessing and postediting tools especially for NLP

Natural Language Processing သုတေသန လုပ်ကြတော့မယ်ဆိုရင် အရင်ဆုံး text file တွေကို cleaning လုပ်တာ၊ encoding ပြောင်းတာ၊
ရှိနေတဲ့ format ကို ကိုယ်လိုချင်တဲ့ ပုံစံဖြစ်အောင် ပြောင်းရတာ၊ လိုချင်တဲ့ စာလုံးတွေ၊ စာကြောင်းတွေကိုပဲ ဆွဲထုတ်ယူတာ စသည်ဖြင့် လုပ်ရတဲ့ အလုပ်တွေက အများကြီးပါပဲ။
Experiment တွေကို လုပ်ဖို့အတွက်က နေ့စဉ်လိုလို shell, perl (အခုနောက်ပိုင်းမှာတော့ python language) နဲ့ ပရိုဂရမ်တွေကို ရေးကြရပါတယ်။ တစ်ခါတလေမှာ format တစ်ခုကနေ နောက်တခြား format တစ်ခုကို ပြောင်းဖို့အတွက် ပရိုဂရမ်တပုဒ်ကို တရက်လုံးအချိန်ပေးပြီး ရေးလိုက်ရတာမျိုးလည်း ရှိပါတယ်။ အဲဒါကြောင့် အသုံးဝင်နိုင်မယ့် bash, perl, python ပရိုဂရမ်တွေကို ကျွန်တော် အချိန်ရရင်ရသလို တင်ပေးသွားပါမယ်။ တစ်ခုမှာချင်တာက ကျွန်တော်တင်ပေးထားတဲ့ ပရိုဂရမ်တွေကို အခြေခံပြီးတော့ shell, perl scripts တွေကို ကိုယ်တိုင်ရေးနိုင်အောင် ကြိုးစားကြပါ။ 

သုံးပုံသုံးနည်း အသေးစိတ်ကိုတော့ သက်ဆိုင်ရာ ဖိုလ်ဒါအသီးသီးမှာ ရှိတဲ့ **example-usages.md** ([for bash](https://github.com/ye-kyaw-thu/tools/blob/master/bash/example-usages.md), [for perl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/example-usages.md), for python) ဖိုင်တွေကို မှီငြမ်းပါ။   

ရဲကျော်သူ

# bash

1. [read-and-move.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/read-and-move.sh)  
2. [change-filenames.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/change-filenames.sh)  
3. [rm-date-sentences.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-date-sentences.sh)  
4. [print-classID-prediction-result.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-classID-prediction-result.sh)
5. [compare-img-or-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/compare-img-or-pdf.sh)  
6. [chk-sort-by-columns.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk-sort-by-columns.sh)  
7. [kill-all-detached.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/kill-all-detached.sh)  
8. [unzip-all-with-one-passwd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/unzip-all-with-one-passwd.sh)  
9. [cut-filename.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/cut-filename.sh)  
10. [calc-avg.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-avg.sh)  
11. [print-latex-section.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-latex-section.sh)  
12. [list-mistake-5-suggestion.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/list-mistake-5-suggestion.sh)  
13. [mytxt2pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytxt2pdf.sh)  
14. [prepare-open-test-data.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/prepare-open-test-data.sh)  
15. [print-CRLF.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-CRLF.sh)  
16. [group-files.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-files.sh)  
17. [segmentation.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/segmentation.sh)  
18. [split-even-odd-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/split-even-odd-pdf.sh)  
19. [even-odd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/even-odd.sh)  
20. [rm-stopwords.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-stopwords.sh)  
21. [rm-spaces-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-spaces-lineno.sh)  
22. [blowfish.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/blowfish.sh)  


# perl

1. [clean-space.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-space.pl)
2. [rm-EnglishSentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-EnglishSentences.pl)
3. [word-analysis.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/word-analysis.pl)
4. [print-emojiSentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-emojiSentences.pl)
5. [dq-multilines.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/dq-multilines.pl)  
6. [mk-abstract-para.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-abstract-para.pl)  
7. [print-mySentenceOnly.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-mySentenceOnly.pl)  
8. [rm-symbol-and-myVowel-only-sentences.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-symbol-and-myVowel-only-sentences.pl)  
9. [rm-space-btw-numbers.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-space-btw-numbers.pl)  
10. [print-ngram.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-ngram.pl)  
11. [print-codepoint.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-codepoint.pl)  
12. [wc.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/wc.pl)  
13. [wordlimit.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/wordlimit.pl)  


# python

1. [chk-token.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/chk-token.py)  
