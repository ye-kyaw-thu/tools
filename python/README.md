အောက်ပါ Python shell script ပရိုဂရမ် တစ်ခုချင်းစီရဲ့ အသုံးပြုပုံကို [example-usages.md](https://github.com/ye-kyaw-thu/tools/blob/master/python/example-usages.md) ဖိုင်မှာ ရှင်းပြထားပါတယ်။  

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

54. [m4v_to_mp4.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/m4v_to_mp4.py)
(m4v encoding က Apple OS စက်တွေမှာ သုံးတာပါ။ လက်တွေ့ ဗီဒီယိုဖိုင်တွေနဲ့ အလုပ်လုပ်တဲ့အခါမှာ ရောပါလာတတ်တယ်။ ဒီ script က m4v ကနေ mp4 ကို ပြောင်းပေးတာပါ။)  
