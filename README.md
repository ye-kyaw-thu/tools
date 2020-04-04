# Preprocessing and postediting tools especially for NLP

Natural Language Processing သုတေသန လုပ်ကြတော့မယ်ဆိုရင် အရင်ဆုံး text file တွေကို cleaning လုပ်တာ၊ encoding ပြောင်းတာ၊
ရှိနေတဲ့ format ကို ကိုယ်လိုချင်တဲ့ ပုံစံဖြစ်အောင် ပြောင်းရတာ၊ လိုချင်တဲ့ စာလုံးတွေ၊ စာကြောင်းတွေကိုပဲ ဆွဲထုတ်ယူတာ စသည်ဖြင့် လုပ်ရတဲ့ အလုပ်တွေက အများကြီးပါပဲ။
Experiment တွေကို လုပ်ဖို့အတွက်က နေ့စဉ်လိုလို shell, perl (အခုနောက်ပိုင်းမှာတော့ python language) နဲ့ ပရိုဂရမ်တွေကို ရေးကြရပါတယ်။ တစ်ခါတလေမှာ format တစ်ခုကနေ နောက်တခြား format တစ်ခုကို ပြောင်းဖို့အတွက် ပရိုဂရမ်တပုဒ်ကို တရက်လုံးအချိန်ပေးပြီး ရေးလိုက်ရတာမျိုးလည်း ရှိပါတယ်။ အဲဒါကြောင့် အသုံးဝင်နိုင်မယ့် bash, perl, python ပရိုဂရမ်တွေကို ကျွန်တော် အချိန်ရရင်ရသလို တင်ပေးသွားပါမယ်။ တစ်ခုမှာချင်တာက ကျွန်တော်တင်ပေးထားတဲ့ ပရိုဂရမ်တွေကို အခြေခံပြီးတော့ shell, perl scripts တွေကို ကိုယ်တိုင်ရေးနိုင်အောင် ကြိုးစားကြပါ။ 

သုံးပုံသုံးနည်း အသေးစိတ်ကိုတော့ သက်ဆိုင်ရာ ဖိုလ်ဒါအသီးသီးမှာ ရှိတဲ့ **example-usages.md** ([for bash](https://github.com/ye-kyaw-thu/tools/blob/master/bash/example-usages.md), [for perl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/example-usages.md), [for python](https://github.com/ye-kyaw-thu/tools/blob/master/python/example-usages.md)) ဖိုင်တွေကို မှီငြမ်းပါ။   

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
23. [replace-with-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno.sh)  
24. [replace-with-lineno2.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno2.sh) 
25. [OOV-count.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/OOV-count.sh)  
26. [find-blank-lines.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/find-blank-lines.sh)  
27. [dot2png-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2png-pdf.sh)  
28. [add-start-end.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/add-start-end.sh)  
29. [get-words-with-position.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/get-words-with-position.sh)  
30. [count-string-length.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/count-string-length.sh)  
31. [strip-substring.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/strip-substring.sh)  
32. [chk_total_duration.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk_total_duration.sh)  
33. [print-sentenceID-count.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-sentenceID-count.sh)  
34. [mk-16KHz-mono.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-16KHz-mono.sh)  
35. [mk-spectrogram.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-spectrogram.sh)  
36. [group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-UCF11.sh)  
37. [group-within-group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-within-group-UCF11.sh) 
38. [dot2pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2pic.sh)  
39. [2mono-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/2mono-pdf.sh)  
40. [calc-bleu-all.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-bleu-all.sh)  
41. [calc-ribes-all.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-ribes-all.sh)  
42. [print-matched-x.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-matched-x.sh)  
43. [split-train-dev-test.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/split-train-dev-test.sh)  
44. [clean-space-all.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/clean-space-all.sh)  
45. [mk-g2p-model.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-g2p-model.sh)  
46. [mk-syl-list.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-syl-list.sh)  
47. [rm-200b-200d.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-200b-200d.sh)  
48. [print-char.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-char.sh)    
49. [prepare-10fold-smt-pair.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/prepare-10fold-smt-pair.sh)  
50. [rm-ctrl-m.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-ctrl-m.sh)  
51. [x-letter-word.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/x-letter-word.sh)  
52. [paste-column.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/paste-column.sh)  
53. [lm-building-exec.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/lm-building-exec.sh)  
54. [print-most-common.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-most-common.sh)  


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
14. [wordwrap.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/wordwrap.pl)  
15. [get-syl-potma.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/get-syl-potma.pl)  
16. [my-linebreak.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/my-linebreak.pl)  
17. [rm-ne-tag.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-ne-tag.pl)  
18. [clean-v-without-c.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-v-without-c.pl)  
19. [x-x-to-x-comma-x-with-brackets.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/x-x-to-x-comma-x-with-brackets.pl)  
20. [select-en-th-my.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/select-en-th-my.pl)  
21. [mk-speakers-json.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-speakers-json.pl)  
22. [string-distance.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/string-distance.pl)  
23. [print-matched-char-seq.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/print-matched-char-seq.pl)  
24. [search-common.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/search-common.pl) 
25. [fixed-parallel-order.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/fixed-parallel-order.pl)  
26. [encode-input.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/encode-input.pl)  
27. [decode.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/decode.pl)  
28. [mk-one2one-freq.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-one2one-freq.pl)  
29. [mk-one-syl-confusion.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/mk-one-syl-confusion.pl)  
30. [rm-onechar-line.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/rm-onechar-line.pl)  


# python

1. [chk-token.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/chk-token.py)  
2. [numpy-array-element-compare.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/numpy-array-element-compare.py)  
3. [char-count-element-wise.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char-count-element-wise.py) 
4. [char-startswith-element-wise.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char-startswith-element-wise.py) 
5. [fuzzy-match.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/fuzzy-match.py)  
6. [hex2uni.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/hex2uni.py)  



