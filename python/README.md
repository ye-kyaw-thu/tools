အောက်ပါ Python shell script ပရိုဂရမ် တစ်ခုချင်းစီရဲ့ အသုံးပြုပုံကို [example-usages.md](https://github.com/ye-kyaw-thu/tools/blob/master/python/example-usages.md) ဖိုင်မှာ ရှင်းပြထားပါတယ်။ အချိန်မရလို့ ရှင်းမပြထားတဲ့ ပရိုဂရမ်တချို့လည်း ရှိပေမဲ့ coding ကို တတ်နိုင်သ၍ ရှင်းအောင်ရေးထားတာမို့ အဆင်ပြေပါလိမ့်မယ်။   

# TOC of Python scripts

1. [chk-token.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/chk-token.py)  
(parallel text ဖိုင် နှစ်ဖိုင်မှာ ရှိတဲ့ token အရေအတွက် မတူတဲ့ စာကြောင်းတွေကို ဆွဲထုတ်ဖို့အတွက် သုံးခဲ့တယ်)  

2. [numpy-array-element-compare.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/numpy-array-element-compare.py)  
(ဖိုင်နှစ်ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို numpy array အဖြစ် ပြောင်းပြီး၊ element တစ်ခုချင်းစီကို တိုက်စစ်ဖို့ရေးခဲ့တယ်။ ဖိုင်နှစ်ဖိုင်ထဲမှာရှိတဲ့ parallel စာကြောင်းတွေက၊ စာလုံးအရေအတွက်တူတဲ့အခြေအနေမျိုးဖြစ်မှ ဒီပရိုဂရမ်နဲ့ အဆင်ပြေလိမ့်မယ်)

3. [char-count-element-wise.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char-count-element-wise.py)   
(numpy array ထဲမှာရှိတဲ့ စာလုံးတွေ (i.e. element) ထဲမှာ ကိုယ်လိုချင်တဲ့ စာလုံး (i.e. char, word) ကိုရှိမရှိ ရှာဖို့အတွက် ရေးခဲ့တယ်)  

4. [char-startswith-element-wise.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char-startswith-element-wise.py)
(numpy array ထဲမှာရှိတဲ့ စာလုံးတွေ (i.e. element) ထဲမှာ ပေးလိုက်တဲ့ စာလုံးနဲ့စတဲ့ word တွေရှိသလား ဆိုတာကို ရှာဖို့အတွက် ရေးခဲ့တယ်)  

5. [fuzzy-match.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/fuzzy-match.py)  
(myG2P အဘိဓာန်ထဲက phoneme တွေကို Fuzzy matching နဲ့ ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တယ်)  

6. [hex2uni.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/hex2uni.py)  
(Python ver.2 နဲ့ ရေးထားတဲ့ code တွေက မြန်မာစာလိုမျိုး utf8 စာကြောင်းတွေကို hex value တွေနဲ့ အလုပ်လုပ်တဲ့ အခါရှိပါတယ်။ အဲဒါတွေကို ဖတ်လိုရအောင် print ထုတ်ဖို့အတွက် သုံးခဲ့တယ်)  

7. [korean-breaks.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/korean-breaks.py)  
(ကိုရီးယား စာကြောင်းတွေကို word segmentation, POS tagging လုပ်ဖို့အတွက် ရေးခဲ့တာပါ။ hangul-utils ကို သုံးထားပါတယ်။)  

8. [epitranscribe.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/epitranscribe.py)  
(မြန်မာနာမည်တွေကို IPA (International Phonetic Alphabet) လေဘယ်ထိုးဖို့ သုံးခဲ့တယ်။ original code [https://github.com/dmort27/epitran](https://github.com/dmort27/epitran) က Python 2.7 မို့လို့ Python 3 နဲ့ run လို့ရဖို့ အနည်းငယ် ပြင်ဆင်ခဲ့တယ်။)

9. [plot-unicode-char.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/plot-unicode-char.py)  
(matplotlib နဲ့ graph ပေါ်မှာ ဗမာစာလုံးတွေချဖို့အတွက် စမ်းရေးခဲ့တဲ့ python script ပါ)  

10. [en-sentence-tokenizer.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/en-sentence-tokenizer.py)  
(အင်္ဂလိပ်စာ အတွက် NLTK library ကို သုံးပြီး ရေးထားတဲ့ sentence segmenter ပါ)  

11. [en-word-tokenizer.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/en-word-tokenizer.py)  
(NLTK library ကို သုံးပြီးတော့ အင်္ဂလိပ်စာ စာကြောင်းတွေကို word tokenization လုပ်တာကို ဥပမာအနေနဲ့ ရေးပြထားတာပါ)  

12. [en-tokenization-on-punctuation.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/en-tokenization-on-punctuation.py)  
(NLTK library ကို သုံးပြီး အင်္ဂလိပ်စာကြောင်းတွေကို word tokenization လုပ်တဲ့အခါမှာ punctuation symbol တွေကို ဘယ်လို ပုံစံနဲ့ ဖြတ်မလဲ ဆိုတာနဲ့ ပတ်သက်ပြီး ရွေးချယ်လို့ ရကြောင်း ဒီမိုရေးပြထားတာပါ)  

13. [filter-en-stopwords.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/filter-en-stopwords.py)  
(အင်္ဂလိပ်စာကြောင်းတွေထဲက stopword တွေကို ဖြုတ်တာကို NLTK library သုံးပြီး လုပ်ပြထားတာပါ)  

14. [mk-QR-code.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk-QR-code.py)  
(QR-code ပုံဖိုင်တွေကို python programming နဲ့ ဘယ်လို လုပ်ယူလို့ ရသလဲဆိုတာကို ဥပမာ run ပြထားတာပါ)  

15. [wu-palmer-similarity.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/wu-palmer-similarity.py)  
(အင်္ဂလိပ်စာလုံးတွေကို Wu and Palmer Similarity တိုင်းကြည့်ထားတဲ့ ပရိုဂရမ်ပါ)  

16. [nltk-en-pos-tagger.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/nltk-en-pos-tagger.py)  
(NLTK library ကို သုံးပြီးတော့ အင်္ဂလိပ်စာအတွက် POS tagger ကို ရေးပြထားတာပါ)  

17. [folder-file-dict.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/folder-file-dict.py)  
(audio_exploration library ကို သုံးဖို့ ပြင်ခဲ့တဲ့ python script ပါ။ script ထဲမှာ assign လုပ်ထားတဲ့ path ကနေ full path ကို ဆွဲထုတ်ပြီး၊ folder path ကို Python dictionary key အဖြစ်ထားပြီး အဲဒီအောက်က filename တွေကို value list အဖြစ်ထားပေးတဲ့ dictionary creation ပရိုဂရမ်ပါ)  

18. [csv-str2mapping123.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/csv-str2mapping123.py)  
(ဗမာစာကြောင်းတွေကို string similarity တိုင်းတဲ့အခါမှာ အသံထွက်တူတဲ့စာကြောင်းတွေကိုလည်း ဆွဲထုတ်နိုင်အောင် စဉ်းစားထားတဲ့ mapping သုံးမျိုးကို proposal တင်ထားတာ ရှိပါတယ်။ အခု code က ပုံမှန် ဗမာစာကြောင်းကနေ mapping 1, 2, 3 တစ်မျိုးမျိုးကို convert လုပ်ပေးတဲ့ ပရိုဂရမ်ပါ။ စိတ်ဝင်စားသူတွေ လေ့လာနိုင်အောင်လို့ published လုပ်ခဲ့တဲ့ စာတမ်းနဲ့ပတ်သက်တဲ့ information ကိုလည်း Python code ထဲမှာ ဖော်ပြထားပါတယ်။)  

19. [str2mapping123.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/str2mapping123.py)  
(အထက်က Python code နံပါတ် 19 နဲ့ အခြေခံအားဖြင့် အတူတူပါပဲ။ ဒီပရိုဂရမ်ကတော့ ပုံမှန် text file ကို input လုပ်ပြီး သုံးဖို့အတွက် ရည်ရွယ်ပါတယ်။ အများသောအားဖြင့်က text file ကနေပဲ ပြောင်းကြမှာမို့...)  

20. [str2my-edit-distances.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/str2my-edit-distances.py)  
(အထက်က Python program နံပါတ် ၁၈၊ ၁၉ တို့နဲ့ ဆက်စပ်နေပါတယ်။ ဒီ ပရိုဂရမ်ကတော့ mapping ပြောင်းပြီး distance measure ခြောက်မျိုးကိုပါ တွက်ထုတ်ပေးဖို့အတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။)  

21. [mypos2upos.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mypos2upos.py)  
([myPOS](https://github.com/ye-kyaw-thu/myPOS) မှာ သုံးထားတဲ့ tag set ကို [Universal POS tag set](http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf) အဖြစ် ပြောင်းတဲ့အလုပ်ကို စမ်းထားတဲ့ ပရိုဂရမ်ပါ)  

22. [isolation-forest.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/isolation-forest.py)  
(ပုံမှန် မဟုတ်တဲ့ ဒေတာတွေကို Isolation Forest ML algorithm နဲ့ ဆွဲထုတ်ဖို့အတွက် စမ်းကြည့်ခဲ့တဲ့ python code)  

23. [accuracy.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/accuracy.py)  
(ကျောင်းသားတွေကို accuracy အကြောင်းကို ရှင်းပြဖို့ ရည်ရွယ်ပြီး ရေးခဲ့တဲ့ python code)  

24. [how-name-eq-main-work.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/how-name-eq-main-work.py)  
(```if __name__ == '__main__':``` ရဲ့ အလုပ်လုပ်ပုံကို နားလည်စေဖို့ ဥပမာ ရေးပြထားတဲ့ python code ပါ။ eg_module.py ကို module အနေနဲ့ ခေါ်သုံးမှာမို့ အဲဒီဖိုင်ကိုလည်း ကြည့်ပါ)  

25. [f1-score-calc.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/f1-score-calc.py)  
(F1-Score ကို micro-average နဲ့တွက်တဲ့ ပုံစံ၊ macro-average နဲ့ တွက်တဲ့ ပုံစံကို ဥပမာအနေနဲ့ ရေးပြထားတာပါ။)  

26. [multi-class-f1.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/multi-class-f1.py)  
(F1-score တွက်တာကိုပဲ multi-class classification အတွက် တွက်ပြထားတာပါ...)  

27. [language-detect.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/language-detect.py)  
(googletrans library ကို သုံးပြီး language detection လုပ်တာကို ရေးပြထားတာပါ။ ထားဝယ်၊ ကချင်၊ ရဝမ် တို့နဲ့လည်း စမ်းပြထားပါတယ်။)  

28. [python-list-eg.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/python-list-eg.py)  
(Python programming ရဲ့ list အသုံးပြုပုံကို ဒီမိုရေးပြထားတာ...)  

29. [split-train-test.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/split-train-test.py)  
(parallel data ကို Python programming နဲ့ training ဒေတာ၊ test ဒေတာ အဖြစ် ခွဲတာကို ဥပမာ အနေနဲ့ ရေးပြထားတာပါ)  

30. [split-train-valid-test.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/split-train-valid-test.py)  
(ပရိုဂရမ် 30 နဲ့ အခြေခံအားဖြင့်က တူပါတယ်။ validation ဒေတာကိုပါခွဲချင်တာမို့ train_test_split() ကို နှစ်ခါခေါ်သုံးပြီး training, validation, test ဒေတာတွေကို ခွဲပေးတဲ့ python script ပါ)  

31. [add-sign.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/add-sign.py)
(PDF ထဲက စာမျက်နှာတွေ အားလုံးရဲ့ ဘယ်ဘက်ထောင့် နေရာမှာ ကိုယ့်လက်မှတ်ပုံကို ဝင်ဖြည့်ဖို့အတွက် ရေးခဲ့။ pyMuPDF library တော့ လိုအပ်တယ်။)  

32. [add-sign-onepage-pdf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/add-sign-onepage-pdf.py)  
(အထက်က နံပါတ် 31 ရဲ့ program ကိုပဲ update လုပ်ထားတာပါ။ ဒီတစ်ခါတော့ စာမျက်နှာ တစ်မျက်နှာတည်းရှိတဲ့ PDF ဖိုင်မှာ လက်မှတ်ဝင်ထိုးတဲ့ case ပါ။)  

33. [print-img-resolution.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/print-img-resolution.py)  
(ပုံတစ်ပုံရဲ့ resolution နဲ့ channel information ကို print ထုတ်ပေးဖို့ ရေးခဲ့တယ်)  

34. [print-pixel-value.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/print-pixel-value.py)  
(ပေးလိုက်တဲ့ ပုံရဲ့ pixel တန်ဖိုးအားလုံးကို ရိုက်ထုတ်ခိုင်းတဲ့ ဥပမာ python code ပါ)  

35. [RGB2grey.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/RGB2grey.py)  
(RGB ကနေ grey ပုံအဖြစ် ပြောင်းတာကို skimage library သုံးပြီး လုပ်ကြည့်ထားတာပါ)  

36. [image2npy.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/image2npy.py)  
(class folder တစ်ခုချင်းစီအောက်မှာ ရှိနေတဲ့ image ဖိုင်တွေအားလုံးကို numpy array format နဲ့ သိမ်းထားတဲ့ feature ဖိုင်အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့)

37. [syl2freq.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2freq.py)  
(မြန်မာစာကြောင်းတွေကို syllable ဖြတ်ပြီး count လုပ်တာ သို့မဟုတ် freq တွက်တာကို sklearn library သုံးလုပ်ပြထား)  

38. [syl2tf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2tf.py)  
(မြန်မာစာကြောင်းတွေကို syllable ဖြတ်ပြီး tf-idf ရဲ့ tf အပိုင်းတွက်တာကို sklearn libary သုံး ရေးပြထားတာပါ)  

39. [syl2idf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2idf.py)  
(tf-idf ရဲ့ idf အပိုင်းတွက်တာကို sklearn library သုံးပြီး ရေးပြထားတာပါ)  

40. [syl2tf-idf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2tf-idf.py)  
(မြန်မာစာ စာကြောင်းတွေကို syllable unit အဖြစ် segmentation လုပ်ပြီးတော့ tf-idf ကို ဥပမာ အနေနဲ့ တွက်ပြထားတာပါ။ အထက်က no. 38 to no. 40 ရဲ့ အဆက်ပါပဲ။)  

41. [syl2onehot-sklearn-4teaching.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2onehot-sklearn-4teaching.py)  
(input ပေးလိုက်တဲ့ ဖိုင်ထဲက မြန်မာစာကြောင်းတွေကို syllable ဖြတ်ပြီးတော့ One-hot encoding ပြောင်းတာကို ဥပမာအနေနဲ့ ရေးပြထားတာ။ ဒီ version ကတော့ စာသင်ဖို့အတွက် ရည်ရွယ်တာမို့ တချို့ print out လုပ်ပြထားတာတွေ ပါဝင်တယ်။)  

42. [syl2onehot-sklearn.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2onehot-sklearn.py)  
(ပရိုဂရမ် နံပါတ် 41 နဲ့ အတူတူပါပဲ။ အသေးစိတ် print လုပ်တာတွေကို ဖယ်ထားလိုက်ပြီးတော့ syllable level One-hot embedding လုပ်ဖို့အတွက် tool အနေနဲ့ သုံးနိုင်ဖို့ ရည်ရွယ်ပါတယ်။)  

43. [zawgyi2unicode.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/zawgyi2unicode.py)  
(Zawgyi encoding နဲ့ သိမ်းထားတဲ့ မြန်မာစာဖိုင်ကို Unicode encoding အဖြစ် ပြောင်းတာကို PyICU library ကိုသုံးပြီး လုပ်ပြထားတာပါ)  

44. [zawgyi2unicode-syl.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/zawgyi2unicode-syl.py)  
(အထက်က Python code no. 43 ကိုပဲ update လုပ်ထားတာပါ။ ဒီတစ်ခါတော့ Zawgyi ကနေ Unicode ကို ပြောင်းပြီးတော့ တစ်ခါတည်း print ရိုက်ထုတ်တာ မဟုတ်ပဲနဲ့ syllable unit အဖြစ် ဖြတ်ပြီးမှ print ရိုက်ထုတ်တာပါ)  

45. [word2vec.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/word2vec.py)  
(word2vec မော်ဒယ်ကို gensim library သုံးပြီး ဆောက်ပြထားတာပါ)  

46. [make-edit-error.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/make-edit-error.py)  
(Producing spelling mistake words based on the edit-distance and print out as parallel data)  

47. [8eval.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/8eval.py)  
(Machine translation နဲ့ တခြား NLP Task တွေအတွက် evaluation ကို metirc ၈မျိုးနဲ့ လုပ်ဖို့အတွက် ရေးခဲ့တယ်။)

48. [soundex-metaphone.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/soundex-metaphone.py)  
(dictionary ဖိုင်ထဲကနေ Soundex နဲ့ Metaphone code တွေအဖြစ် ပြောင်းပေးတဲ့ script)  

49. [7sim.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/7sim.py)  
(input အဖြစ် ပေးလိုက်တဲ့ စာကြောင်း နှစ်ကြောင်း သို့မဟုတ် ဖိုင် နှစ်ဖိုင်ထဲက စာကြောင်းတွေကို Levenshtein, Jaro Winkler, Cosine, Dices Coefficient, jaccard, LCS ratio, Sorensen Dice Coefficient တွေ တွက်ပေးတဲ့ Python script ပါ)  

50. [abugida.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/abugida.py)  
(Abugida ဘာသာစကား အုပ်စုထဲမှာ ပါဝင်တဲ့ language တွေမှာ သုံးတဲ့ ဗျည်း၊ သရ၊ နံပါတ်တွေကို ဥပမာအနေနဲ့ ရိုက်ထုတ်ပြပေးတဲ့ python script ပါ။ Writing system က အခြေခံအားဖြင့် တူတာကို ကျောင်းသားတွေ လေ့လာနိုင်ဖို့ ရည်ရွယ်ပါတယ်။)  

51. [tex-spellcheck.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/tex-spellcheck.py)  
(Latex file အပါအဝင် text ဖိုင်တွေကို စာလုံးပေါင်းအမှားတွေ ဆွဲထုတ်နိုင်ဖို့ ရေးခဲ့တယ်။)  

52. [video_augment.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/video_augment.py)  
(ကမ္ဘောဒီးယားက ITC တက္ကသိုလ်က undergrad internship ကျောင်းသားတွေအတွက် ရေးခဲ့တာ။ Video ဒေတာကို augment method လေးမျိုးနဲ့ လုပ်ထားတဲ့ demo code ပါ။)  

53. [mk-video-class.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk-video-class.py)  
(Augmented video ဖိုင်တွေကို class folder တွေအသီးသီး ဆောက်ပြီး သိမ်းဖို့ ရေးခဲ့တဲ့ script ပါ။)

54. [mk-video-class-for-sentence.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk-video-class-for-sentence.py)  
(mk-video-class.py နဲ့ အတူတူပါပဲ၊ အဓိက ကွဲသွားတာက ဖိုင်နာမည်တွေမှာ (1), (2), (3), (4) တွေ ပါလာပြီး ရှေ့ပိုင်းဖိုင်နာမည်က တူရင် class တစ်ခုတည်း ထားဖို့အတွက် ပြင်ရေးထားတာ။)

55. [m4v_to_mp4.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/m4v_to_mp4.py)  
(m4v encoding က Apple OS စက်တွေမှာ သုံးတာပါ။ လက်တွေ့ ဗီဒီယိုဖိုင်တွေနဲ့ အလုပ်လုပ်တဲ့အခါမှာ ရောပါလာတတ်တယ်။ ဒီ script က m4v ကနေ mp4 ကို ပြောင်းပေးတာပါ။)

56. [mov_to_mp4.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mov_to_mp4.py)  
(အထက်က m4v_to_mp4.py နဲ့ အတူတူပါပဲ။ ဒီ ပရိုဂရမ်ကတော့ mov encoding ကနေ mp4 ကို ပြောင်းဖို့အတွက် သုံးခဲ့တယ်။)

57. [jiwer_wer_mer_wil.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/jiwer_wer_mer_wil.py)  
(ijwer ဆိုတဲ့ Python library ကို သုံးပြီးတော့ WER, MER, WIL သုံးမျိုးကို တွက်ဖို့အတွက် ရေးခဲ့တယ်။ ASR evaluation အတွက် အသုံးဝင်လိမ့်မယ်။)

58. [passphrase_generator.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/passphrase_generator.py)  
(passphrase generation ကို မြန်မာစာလုံးတွေနဲ့ လက်တွေ့စမ်းကြည့်ဖို့ ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။)

59. [rule_based_password_gen.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/rule_based_password_gen.py)  
(Rule-based password generation ကို မြန်မာစာ အတွက် စမ်းကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။)

60. [MOS_eval.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/MOS_eval.py)  
(TTS model တွေကို Mean Opinion Score evaluation လုပ်ဖို့အတွက် ရေးခဲ့တယ်။)

61. [spacy_pos_ner.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/spacy_pos_ner.py)  
(Spacy Library ကို သုံးပြီး အင်္ဂလိပ်စာကြောင်းတွေကို POS/NER tagging လုပ်ဖို့အတွက် ရေးခဲ့တယ်။)

62. [spacy_pos_dep_jp.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/spacy_pos_dep_jp.py)  
(Spacy Library ကို သုံးပြီး ဂျပန်စာကြောင်းတွေကို POS tagging နဲ့ Dependency parsing လုပ်ကြည့်ထားတာပါ။)

63. [spacy_pos_ner_dep_zh.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/spacy_pos_ner_dep_zh.py)  
(အထက်က ပရိုဂရမ် နှစ်ပုဒ်တဲ့ အတူတူပါပဲ။ ဒီတစ်ခါတော့ တရုပ်စာကြောင်းတွေကို tagging လုပ်ဖို့အတွက် ရေးခဲ့တာပါ။ POS/NER/Dependency သုံးမျိုးစလုံးအတွက် ရတယ်။)

64. [nltk-lm.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/nltk-lm.py)  
(NLTK library ကို သုံးပြီးတော့ language model ဆောက်တာကို ဥပမာ လုပ်ပြထားတဲ့ ပရိုဂရမ်ပါ။)  

65. [nltk-lm-predict.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/nltk-lm-predict.py)  
(အထက်က nltk-lm.py နဲ့ ဆောက်ထားခဲ့တဲ့ language model ကို သုံးပြီးတော့ interactive next word prediction ကို ဒီမိုလုပ်ပြထားတာပါ။)

66. [format_conversion.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/format_conversion.py)  
(left-to-right ကနေ top-down format ထိုနည်းလည်းကောင်း top-down ကနေ left-to-right ကို ပြောင်းဖို့အတွက် ရေးခဲ့တယ်။)

67. [format_conversion_with_error_check.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/format_conversion_with_error_check.py)  
(ဒီတစ်ခါတော့ ပရိုဂရမ် နံပါတ် ၆၆ ကို corpus error checking ထပ်ဖြည့်ထားတာပါ။ format conversion မလုပ်ခင်မှာ corpus ထဲက အမှားတချို့ကို ရှာပေးပါလိမ့်မယ်။)

68. [cut_columns.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/cut_columns.py)  
(Linux OS ရဲ့ cut command လို အလုပ်ကို Python နဲ့ ရေးကြည့်ထားတာပါ။)


69. [bidirectional_maximum_matching.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/bidirectional_maximum_matching.py)   
(Maximum Matching နဲ့ Bidirectional Maximum Matching algorithm ကိုသုံးပြီး မြန်မာစာ စာလုံးတွေကို word segmentation NLP task အတွက် စမ်းထားတာ။ Segmentation unit ကို character level နဲ့ရော မြန်မာစာအတွက် အရေးပါတဲ့ syllable unit နဲ့ရော နှစ်မျိုးလုံးသုံးပြီး စမ်းထားတယ်။)

70. [extract_filename_parts.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/extract_filename_parts.py)  
(Filename က my_9762_1798008689.wav ဆိုတဲ့ ပုံစံမျိုး ရှိနေတာမို့၊ underscore ကို delimiter အဖြစ်ထားပြီးတော့ ကော်လံအလိုက် unique count လုပ်ဖို့အတွက် ရေးခဲ့တယ်။)

71. [sort_openslr_transcript.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/sort_openslr_transcript.py)  
(OpenSLR, 80 ရဲ့ မြန်မာစာဒေတာ index ဖိုင်က randomized ဖြစ်နေတာကြောင့်၊ sorting စီဖို့အတွက် ရေးခဲ့တယ်။)   

72. [speech_corpus_info.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/speech_corpus_info.py)  
(ASR, TTS အတွက် speech corpus တွေကို သိမ်းထားတဲ့ format က အမျိုးမျိုးမို့လို့ လူသိများ၊ လူသုံးများတဲ့ format နဲ့ ပတ်သက်ပြီး information ပေးဖို့ ရည်ရွယ်တယ်။ update လုပ်ရဦးမယ်)    

73. [dKNN.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/dKNN.py)  
(KNN မော်ဒယ်ကိုပဲ Neural Network နဲ့ ပေါင်းပြီး experiment တချို့ လုပ်ထားတာ။)

74. [dKNN-ver2.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/dKNN-ver2.py)  
(အဓိက Function က အပေါ်က dKNN.py နဲ့ အတူတူပါပဲ၊ Graphviz ကို သုံးပြီး deepKNN နဲ့ diffKNN ရဲ့ အလုပ်လုပ်ပုံကို diagram ဆွဲပေးတဲ့ function နှစ်ခုတိုးပေးထားတာပါ။ Graphviz ကတော့ ကိုယ့်စက်ထဲမှာ မရှိသေးရင် installation လုပ်ဖို့ လိုအပ်လိမ်မယ်။)

75. [change_sampling_rate.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/change_sampling_rate.py)  
(ASR, TTS မော်ဒယ် ဆောက်တဲ့အခါမျိုးမှာ သုံးတဲ့ framework ပေါ်မူတည်ပြီးတော့ အသံဖိုင်တွေကို သတ်မှတ်ထားတဲ့ sampling rate ကို ပြောင်းပေးဖို့ လိုအပ်ပါတယ်။ ဒီ python script က အဲဒီအလုပ်အတွက် ရေးခဲ့တာ။)

76. [check_silence.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/check_silence.py)  
(TTS model ကိုသုံးပြီးတော့ testing လုပ်တဲ့အခါမှာ အကြောင်းအမျိုးမျိုးကြောင့် output ထွက်လာတဲ့ wave ဖိုင်တွေက silence ဖြစ်နေတာမျိုး ကြုံရတတ်တယ်။ အဲဒီအတွက် silence ဖြစ်နေသလား ဆိုတာကို စစ်ဆေးဖို့အတွက် ရေးခဲ့တာ။)

77. [graph_lm_spellchek.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/graph_lm_spellchek.py)  
(graph+LM based spelling checking, just testing ...)

78. [detect_language_ver1.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/detect_language_ver1.py)  
(ဖိုင်ထဲက စာကြောင်းတွေကို တစ်ကြောင်းချင်း ဖတ်ပြီး ဘယ်ဘာသာလဲ ဆိုတာကို ဆုံးဖြတ်ပြီး၊ တစ်ဖိုင်လုံးမှာ ဘယ်ဘာသာနဲ့ ရေးထားတဲ့ စာကြောင်းက ရာခိုင်နှုန်း ဘယ်လောက် ဆိုတာကို တွက်ပေးတဲ့ ပရိုဂရမ် version 1.0 ပါ။ ဒီပရိုဂရမ်နဲ့က မြန်မာစာတို့ ခမာစာတို့ဆိုရင် Unknown အနေနဲ့ပဲ ပြပေးပါလိမ့်မယ်။)

79. [detect_language_ver2.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/detect_language_ver2.py)  
(ဒီ version 2 မှာတော့ Unknown ဖြစ်နေတဲ့ စာကြောင်းတွေကို Unicode page no. အလိုက် ခွဲလိုက်ပြီး ဖြစ်နိုင်တဲ့ ဘာသာစကားကို ခန့်မှန်းပေးတာ ဖြစ်ပါတယ်။ မှားတဲ့ case တွေလည်း ရှိမှာ ဖြစ်ပေမဲ့ အတိုင်းအတာ တစ်ခုအထိ အသုံးဝင်ပါလိမ့်မယ်။)

80. [embedder.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/embedder.py)  
(tf-idf, word2vec နဲ့ fasttext ဆိုတဲ့ ထင်ရှားတဲ့ word embedding မော်ဒယ် သုံးမျိုးကို ဗမာစာနဲ့ ဆောက်ဖို့အတွက် ရေးခဲ့တယ်။)

81. [test_embedding.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/test_embedding.py)  
(အထက်က embedder.py ပရိုဂရမ်နဲ့ ဆောက်ထားခဲ့တဲ့ tf-idf, word2vec, fasttext မော်ဒယ်တွေကနေ similar words တွေကို ဆွဲထုတ်ယူဖို့အတွက် ရေးခဲ့။)

82. [convert_to_conllu.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/convert_to_conllu.py)   
(myPOS corpus လိုမျိုး left-to-right Tagged data ကို CONLLU column type format အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တယ်။)

83. [convert_to_spacyNER_json.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/convert_to_spacyNER_json.py)  
(Spacy library က လက်ခံတဲ့ NER corpus ပုံစံကို ပြောင်းဖို့အတွက် ရေးခဲ့တယ်။)

84. [split_parallel_data.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/split_parallel_data.py)  
(Machine translation မလုပ်ခင်မှာ TAB သို့မဟုတ် ||| နဲ့ ခြားထားတဲ့ parallel corpus ကနေ ဘာသာစကား တစ်ခုခြင်းစီအတွက် source file, target file ခွဲတဲ့ အလုပ်ကို လုပ်ရပါတယ်။ အဲဒီအတွက် ရေးထားတဲ့ python script တစ်ပုဒ်ပါ။)

85. [clean_text.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/clean_text.py)  
(စာလုံး တစ်လုံးနဲ့ တစ်လုံး အကြားမှာ အပိုပါနေတဲ့ space တွေ၊ စာကြောင်းရဲ့ ရှေ့ပိုင်းမှာ နောက်ဆုံး အပိုင်းမှာ ရှိနေတဲ့ heading, trailing space တွေနဲ့ မျက်စိနဲ့ မမြင်ရတဲ့ ZWSP စာလုံးကို ရှင်းပစ်ဖို့အတွက် ရေးထားခဲ့တဲ့ python code ပါ။)  

86. [extract_emoji.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/extract_emoji.py)  
(Input file ထဲမှာ ပါတဲ့ emoji စာလုံးတွေကို ဆွဲထုတ်ပြီး unique list လုပ်ပြလိမ့်မယ်။)

87. [compare_characters.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/compare_characters.py)  
(character ဖြတ်ထားတဲ့ ဖိုင်နှစ်ဖိုင်အကြားကို နှိုးယှဉ်ကြည့်ဖို့အတွက်)

88. [word_length_analysis.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/word_length_analysis.py)  
(NMT မလုပ်ခင်မှာ ကိုယ့် corpus ဖိုင်ထဲက စာကြောင်းတွေထဲမှာ ပါဝင်တဲ့ စာလုံးရေ အရေအတွက် min, max number of words ကို သိထားရင် ကောင်းပါတယ်။ အဲဒီအတွက်)

89. [comma2tab_label2digit.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/comma2tab_label2digit.py)  
(CSV file ကနေ TSV format ကို ပြောင်းဖို့နဲ့ text label နှစ်မျိုးကို digit အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့)

90. [conv_delimiter_label2digit.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/conv_delimiter_label2digit.py)  
(အထက်က program no. 89 ကို extension လုပ်ထားတဲ့ ဗားရှင်းပါ။ ဒီ တစ်ခါတော့ delimiter တွေကို --from, --to ဆိုတဲ့ option နှစ်ခုနဲ့ သတ်မှတ်ပေးလို့ ရပါတယ်။ ပြီးတော့ text label တွေကိုလည်း ပရိုဂရမ်က input file ကနေ auto count လုပ်ပြီး digit label အဖြစ် ပြောင်းပေးပါလိမ့်မယ်။)    

91. [padsint_detection.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/padsint_detection.py)  
(ပါဌ်ဆင့် သို့မဟုတ် ဆင့်ထားတဲ့ ဗျည်းတွေကို detect လုပ်ဖို့အတွက် ရေးခဲ့တယ်။)  

92. [replace_pipe_with_space.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/replace_pipe_with_space.py)   
(Input ဖိုင်ထဲက pipe (|) ကို space နဲ့ အစားထိုးဖို့အတွက် ရေးခဲ့တယ်။)  

93. [pos_pattern_checker.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/pos_pattern_checker.py)  
(မြန်မာစာရဲ့ POS pattern combination တွေအမျိုးမျိုး ရှိနေတဲ့အထဲကနေ ကိုယ်ဆွဲထုတ်ကြည့်ချင်တဲ့ pattern ကို ကြည့်လို့ ရဖို့အတွက် ရေးခဲ့တယ်။ DSL library ကိုလည်း သုံးထားတယ်။)

94. [sort_ngram.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/sort_ngram.py)  
(ngram ဖိုင်တွေကို စာသားနဲ့ သို့မဟုတ် ngram value နဲ့ sorting စီပေးဖို့အတွက် ရေးခဲ့တဲ့ python code ပါ။)

95. [analyze_NER_corpus.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/analyze_NER_corpus.py)  
(NER corpus မှာ တပ်ထားတဲ့ tag အရေအတွက်နဲ့ ပတ်သက်ပြီး စစ်ဆေးဖို့အတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။)

96. [compare_sentence_tag_distributions.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/compare_sentence_tag_distributions.py)  
(GPT-2 LLM ကနေ testig လုပ်ပြီး ထွက်လာတဲ့ hatespeech စာကြောင်းတွေကို manual tagging ပြန်လုပ်ပြီးတော့ ဘယ်လို hatespeech တွေထုတ်ပေးသလဲ ဆိုတာကို graph ထုတ်ပြီး လေ့လာဖို့ ရေးခဲ့တဲ့ python script ပါ။)  

97. [compare_word_tag_distributions.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/compare_word_tag_distributions.py)  
(အထက်က no. 96 ပရိုဂရမ်ကို word/phrase level tag distribution လုပ်ဖို့အတွက် ပြင်ရေးခဲ့တဲ့ python script ပါ။)  

98. [print_codepoint.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/print_codepoint.py)  
(Extension of print_codepoint.pl for Python language. Added some more command line arguments. Enjoy!)

99. [syl_ngram_mi.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl_ngram_mi.py)  
(Mutual information ကို တွက်ပြီးတော့ syllable pair n-gram တွေကို ဆွဲထုတ်ဖို့ ရေးခဲ့တယ်။)

100. [txt_dl.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/txt_dl.py)  
(ကိုယ်ရှာဖွေချင်တဲ့ keyword နဲ့ website link ကို ပေးပြီး အဲဒီ keyword ပါဝင်နေတဲ့ မြန်မာစာကြောင်းတွေကို ဆွဲထုတ်ယူဖို့အတွက် ရေးခဲ့တယ်။)

101. [markov_txt_gen.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/markov_txt_gen.py)  
(Markov Chain နဲ့ မြန်မာစာကြောင်းတွေကို generate လုပ်ဖို့အတွက် ရေးခဲ့တယ်။)  

102. [tesseract_ocr.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/tesseract_ocr.py)
(Google ရဲ့ pytesseract module ကို သုံးပြီး မြန်မာစာ OCR အကြမ်းစမ်းကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ code ပါ။)

103. [NER_23to9_conv.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/NER_23to9_conv.py)  
(လက်ရှိ LU Lab. မှာက NER corpus ကို 23 tagsets နဲ့ 9 tagsets ဆိုပြီး နှစ်မျိုး develop လုပ်နေတာမို့လို့ အရင်ရှိပြီးသား 23 tagsets နဲ့ tag လုပ်ထားတဲ့ စာကြောင်းတွေကို 9 tagsets အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တယ်။)  

104. [tf_event2txt.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/tf_event2txt.py)  
(tensorflow framework ကိုသုံးပြီး မော်ဒယ်တခုခု ဆောက်ရင် event log ဖိုင်ရလာလိမ့်မယ်။ အဲဒီဖိုင်က ပုံမှန်အားဖြင့်က tensorboard နဲ့ ကြည့်ရတာ။ သို့သော် တခါတလေမှာ command line မှာပဲ အကြမ်းဖတ်ကြည့်ချင်တဲ့ အခါမျိုး ရှိတတ်ပါတယ်။ အဲဒီလိုအခါအတွက် text ဖိုင် format အဖြစ်ပြောင်းပေးတဲ့ python code ပါ။)  

105. [hangul_syl_generator.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/hangul_syl_generator.py)  
(for printing all Korean syllables)

106. [ngram_segmentation.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/ngram_segmentation.py)  
(word segmentation simulation for Burmese)  

107. [long_sentence_wrapper.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/long_sentence_wrapper.py)  
(to wrap long sentences)  

108. [mm_proverb_parser.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mm_proverb_parser.py)  
(Json file extraction for Burmese proverbs)  

109. [grapheme_tokenizer.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/grapheme_tokenizer.py)  
(Grapheme tokenizer)  

110. [icu_collation.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/icu_collation.py)  
(string collation based on ICU library)  

111. [icu_transliteration.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/icu_transliteration.py)  
(Transliteration, Reverse transliteration example program based on ICU library)  

112. [my_transliteration.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/my_transliteration.py)  
(Experiment code for Burmese transliteration with two transliteration systems: ALA-LC and Sawada)  

113. [kana2roman.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/kana2roman.py)  
(Hiragana, Katakana to Romanization)  

114. [prefix_suffix_extract.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/prefix_suffix_extract.py)  
(Prefix, Suffix တွေကို အဘိဓာန်ဖိုင်နဲ့ corpus ဖိုင်နှစ်ဖိုင်သုံးပြီး ဆွဲထုတ်ကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ code ပါ။ )  

115. [mk_only_my.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk_only_my.py)  
(ဖိုင်ထဲမှာ ရှိတဲ့စာကြောင်းတွေထဲက အင်္ဂလိပ်စာလုံးတို့ တရုတ်စာလုံးစတာတွေအားလုံးကို ဖယ်လိုက်ပြီး မြန်မာစာလုံးတွေပဲ ရှိစေဖို့အတွက် ရေးထားတဲ့ Python code ပါ။ မြန်မစာ NLP အလုပ်တွေအတွက် မရှိမဖြစ်တဲ့ ပရိုဂရမ်တစ်ပုဒ်လို့ ပြောလို့ ရပါတယ်။)  

116. [rm_my_two_symbols.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/rm_my_two_symbols.py)  
(ကိုယ်လုပ်ချင်တဲ့ NLP task အပေါ်ကို မူတည်ပြီးတော့ ပုဒ်ထီး၊ ပုဒ်မ တွေကို ဖြုတ်ဖို့လိုအပ်တဲ့အခါတွေရှိပါတယ်။ အဲဒီအတွက် ရေးထားခဲ့တဲ့ python script ပါ။)  

117. [char_segmentation.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char_segmentation.py)  
(ဒီ code က character segmentation လုပ်ပေးလိမ့်မယ်။)  

118. [fasttext_format_converter.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/fasttext_format_converter.py)  
(FastText ကိုသုံးပြီး classification experiment ဘာညာ လုပ်တော့မယ်ဆိုရင် ဒေတာကို format ပြောင်းပေးဖို့ လိုအပ်ပါတယ်။ အဲဒီအတွက် ရေးခဲ့တဲ့ Python code ပါ။)  

119. [run_sylbreak.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/run_sylbreak.py)  
(Machine translation မလုပ်ခင်မှာ source langauge အတွက်ကော၊ target language အတွက်ကော syllable breaking လုပ်တာမျိုး လုပ်လေ့ရှိပါတယ်။ အဲဒီအလုပ်အတွက် သုံးခဲ့တဲ့ Python code ပါ။)  

120. [rm_zwnj_zwsp_hsp.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/rm_zwnj_zwsp_hsp.py)  
(မမြင်ရတဲ့ ZWNJ, ZWSP, HSP character တွေကို ဖယ်ဖို့ ရေးခဲ့တဲ့ python code ပါ။)  

121. [clean_non_burmese.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/clean_non_burmese.py)  
(မမြင်ရတဲ့ ZWNJ, ZWSP တို့ကိုလည်းဖယ်မယ်။ ဗမာစာလုံး မဟုတ်တဲ့ နိုင်ငံခြားဘာသာစကားတွေကိုလည်း ဖယ်ချင်တယ်၊ ပြီးတော့ သင်္ကေတာတွေလည်း ဖယ်ဖို့အတွက် ရေးခဲ့တယ်။ ဒီ script က ဗမာစာ NLP အတွက်က မရှိမဖြစ် ပါပဲ)  

122. [eval_ngram_lm.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/eval_ngram_lm.py)  
(for Ngram language model evaluation with test-data)  

123. [parquet_extractor.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/parquet_extractor.py)  
(Big Data ecosystem တွေဖြစ်တဲ့ Apache Hadoop, Apache Spark နဲ့ Apache Arrow တို့မှာ ဖိုင်တွေကို သိမ်းတဲ့အခါမှာ .parquet ဆိုတဲ့ format နဲ့ သိမ်းလေ့ရှိတယ်။ အဲဒီဖိုင်ကို ဖြေဖို့အတွက် ရေးခဲ့တဲ့ python code ပါ)  

124. [g2p-compare.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/g2p-compare.py)  
(word level g2p model ထွက်လာတဲ့ original phoneme tagging ဖိုင်နဲ့ manual checked လုပ်ထားတဲ့ phoneme tagging ဖိုင်နှစ်ခုအကြားကို compare လုပ်ကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ code)

125. [extract-ReMeDi.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/extract-ReMeDi.py)  
(ReMeDi Chinese corpus က json ဖိုင်၊ အဲဒီဖိုင်ထဲကနေ ကိုယ်လိုချင်တဲ့ field သုံးခုကို ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တဲ့ python code ပါ။)   

126. [split-sentences-by-pipe.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/split-sentences-by-pipe.py)   
(စာကြောင်းတွေကို pipe နဲ့ခြားထားတဲ့ တစ်လိုင်းထဲ ဖြစ်နေတဲ့ Harry Porter data ဖိုင်ထဲက စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ ဆွဲထုတ်ဖို့ ရေးခဲ့တဲ့ code)  

127. [https://github.com/ye-kyaw-thu/tools/blob/master/python/format-conv.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/format-conv.py)  
(Spelling corpus ကို သတ်မှတ်ထားတဲ့ format တစ်ခုနဲ့ ကျောင်းသားတွေကို ပြင်ဆင်ခိုင်းခဲ့တယ်။ အဲဒီ corpus ဖိုင်ကနေ အမှားစာကြောင်း၊ spelling error type စာကြောင်းနဲ့ အမှန်ပြင်ထားတဲ့ စာကြောင်းတွေကို သပ်သပ်စီဆွဲထုတ်ပြီး၊ ဖိုင် တစ်ဖိုင်စီမှာ ခွဲသိမ်းဖို့ ရေးခဲ့တဲ့ python code ပါ)    

 
