အောက်ပါ bash shell script ပရိုဂရမ် တစ်ချို့ရဲ့ အသုံးပြုပုံကို [example-usages.md](https://github.com/ye-kyaw-thu/tools/blob/master/bash/example-usages.md) ဖိုင်မှာ ရှင်းပြထားပါတယ်။  

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
(argument ကနေ pass လုပ်ပေးလိုက်တဲ့ path/filename.ext ကနေ ဖိုင်နာမည်ကို ဆွဲထုတ်တာ "i.e. filename.ext", path/ ကိုပဲ ဆွဲထုတ်တာ၊ extension မပါပဲ ဖိုင်နာမည်ကိုပဲ "i.e. filename" ဆွဲထုတ်တာ၊ extension ကိုပဲ သပ်သပ် ဆွဲထုတ်ဖို့အတွက် "i.e. ext" ရေးခဲ့ပါတယ်။)  

10. [calc-avg.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-avg.sh)  
(ဖိုင်တစ်ဖိုင်ထဲမှာ ကော်လံတစ်ခုအနေနဲ့ သိမ်းထားတဲ့ ဂဏန်းတွေအားလုံးကို ပေါင်းပြီးတော့ ပျှမ်းမျှ တွက်ထုတ်ပေးဖို့အတွက် ရေးထားတဲ့ bash shell script ပါ။ ဒဿမ နှစ်လုံးနဲ့ပဲ ရိုက်ပြအောင် setting လုပ်ထားပါတယ်။)  

11. [print-latex-section.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-latex-section.sh)  
(latex source ဖိုင်ထဲကနေ \section{}, \subsection{}, \subsubsection{} တွေနဲ့ ရေးထားတဲ့ စာကြောင်းတွေကို ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တယ်။)  

12. [list-mistake-5-suggestion.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/list-mistake-5-suggestion.sh)  
(input-file ထဲက အင်္ဂလိပ်စာ spelling mistake တွေနဲ့ ဖြစ်နိုင်တဲ့ စာလုံးအမှန် ၅လုံးကို list လုပ်ပေးတဲ့ ပရိုဂရမ်ပါ။ aspell ဆိုတဲ့ spelling checking program ကို သုံးထားပါတယ်။)  

13. [mytxt2pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytxt2pdf.sh)  
(မြန်မာစာ စာကြောင်းတွေ ပါနေတဲ့ text ဖိုင်ကို PDF ဖိုင်အဖြစ် ပြောင်းဖို့အတွက် pandoc ကို သုံးပြထားတဲ့ shell script ပါ)  

14. [prepare-open-test-data.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/prepare-open-test-data.sh)  
(ရှိနေတဲ့ ဒေတာဖိုလ်ဒါထဲကနေ class ရှိသလောက်ကို open-test data အဖြစ် သပ်သပ်ခွဲထုတ်ချင်တဲ့အခါ အသုံးပြုနိုင်ပါတယ်)  

15. [print-CRLF.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-CRLF.sh)  
(Windows OS ရဲ့ စာကြောင်းအဆုံးသင်္ကေတဖြစ်တဲ့ CRLF ပါနေတဲ့ စာကြောင်းတွေကို ဆွဲထုတ်ဖို့အတွက် သုံးခဲ့တယ်)  

16. [group-files.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-files.sh)
(ဖိုင်တွေအများကြီးကို n-file စီခွဲပြီး သိမ်းဖို့အတွက် ရေးခဲ့တယ်)  

17. [segmentation.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/segmentation.sh)  
(စာလုံးမဖြတ်ထားရသေးတဲ့ စာကြောင်း "|" မပါတဲ့ စာကြောင်းတွေကို၊ word segmentation program ကို pass လုပ်တဲ့ shell script)  

18. [split-even-odd-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/split-even-odd-pdf.sh)  
(PDF ဖိုင်တစ်ဖိုင်ကို စုံဂဏန်း စာမျက်နှာတွေကို တစ်ဖိုင်၊ မဂဏန်း စာမျက်နှာတွေကို တစ်ဖိုင်စီ သပ်သပ်ခွဲသိမ်းဖို့အတွက် ရေးခဲ့တယ်)  

19. [even-odd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/even-odd.sh)  
(ဖိုင်တစ်ဖိုင်ထဲမှာ ရှိနေတဲ့ စာကြောင်းတွေအထဲက စုံဂဏန်း စာကြောင်းတွေကိုပဲ ရိုက်ထုတ်ခိုင်းချင်တဲ့အခါမျိုး၊ မဂဏန်း စာကြောင်းတွေကိုပဲ ရိုက်ထုတ်ခိုင်းချင်တဲ့အခါမျိုးအတွက် ရေးခဲ့တယ်) 

20. [rm-stopwords.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-stopwords.sh)  
(stop words တွေကို corpus သို့မဟုတ် training data ဖိုင်ကနေ ဖျက်ဖို့အတွက် ရေးခဲ့ပါတယ်)  

21. [rm-spaces-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-spaces-lineno.sh)  
(Website ကနေ ကုဒ်တွေကိုကော်ပီကူးယူတဲ့အခါမှာ တွဲပါလာတဲ့ space, line number တွေကို ဖြုတ်ဖို့အတွက် ရေးခဲ့တယ်)  

22. [blowfish.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/blowfish.sh)  
(Blowfish Cryptography နဲ့ plain text ဖိုင်ကို encode/decode လုပ်ဖို့အတွက် ရေးခဲ့တယ်)  

23. [replace-with-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno.sh)  
(ဖိုင်တစ်ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို လိုင်းနံပါတ်နဲ့ရှာပြီး တခြားစာကြောင်းတွေနဲ့ အစားထိုးဖို့အတွက် သုံးခဲ့တယ်)  

24. [replace-with-lineno2.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno2.sh)  
(အထက်ပါ နံပါတ်၂၃ က ပရိုဂရမ်နဲ့ ဆင်ပါတယ်။ ဖိုင်တစ်ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို လိုင်းနံပါတ်နဲ့ရှာပြီး ပြင်ထားတဲ့စာကြောင်းတွေနဲ့ အစားထိုးဖို့ရေးခဲ့ပါတယ်။ နံပါတ် ၂၃ရဲ့ ပရိုဂရမ်နဲ့ မတူတာက replace-with-lineno2.sh မှာတော့ လိုင်းနံပါတ် တစ်ခုတည်းကို တိုက်စစ်တာမဟုတ်ပဲ၊ အရင် စာကြောင်းအဟောင်းကိုပါ တိုက်စစ်ပြီးတွေ့မှ အစားထိုးပါတယ်။)  

25. [OOV-count.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/OOV-count.sh)  
(Out-Of-Vocabulary စာလုံးတွေကို linux command တစ်ခုဖြစ်တဲ့ comm ကို သုံးပြီးတော့ လွယ်လွယ်ကူကူ ရှာဖွေနိုင်ကြောင်းကို သင်ပေးချင်လို့ ရေးခဲ့ပါတယ်)  

26. [find-blank-lines.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/find-blank-lines.sh)  
(ဖိုလ်ဒါတစ်ခုအောက်မှာသိမ်းထားတဲ့ ဖိုင်တွေထဲမှာ ရှိနေတဲ့ blank line တွေကို ရှာဖို့အတွက် ရေးခဲ့ပါတယ်။ blank line တွေရဲ့ လိုင်းနံပါတ်ကိုပါ ရိုက်ထုတ်ပြပေးပါလိမ့်မယ်)  

27. [dot2png-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2png-pdf.sh)  
(Graph description language နဲ့ ရေးထားတဲ့ dot ဖိုင်ကနေ ပုံဖိုင်format တစ်ခုဖြစ်တဲ့ png အဖြစ်ပြောင်းပြီး၊ အဲဒီ ပုံဖိုင်ကို pdf ဖိုင်ပြောင်းပေးတဲ့ shell script ပါ။)  

28. [add-start-end.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/add-start-end.sh)  
(ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတစ်ကြောင်းချင်းစီကို စာကြောင်းအစ အမှတ်အသား "\<s\>" နဲ့ စာကြောင်းအဆုံး အမှတ်အသား "\<\\s\>" တွေကိုထည့်ဖို့အတွက် ရေးခဲ့တယ်)  

29. [get-words-with-position.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/get-words-with-position.sh)  
(စာကြောင်း ထဲက စာလုံးတွေကို ကိုယ်လိုချင်တဲ့ အပိုင်းအလိုက် ဖြတ်ထုတ်ယူနိုင်ဖို့ ရေးခဲ့တယ်။ စာကြောင်းရဲ့ ဘယ်နေရာကစပြီး ဘယ်နှစ်လုံးမြောက်အထိ ဆိုတာကို command line argument နဲ့ ပေးပြီး ဆွဲထုတ်ယူနိုင်ပါတယ်)  

30. [count-string-length.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/count-string-length.sh)  
(ဖိုင်ထဲမှာရှိနေတဲ့ စာကြောင်းတစ်ကြောင်းချင်းစီရဲ့ စာလုံးအရေအတွက်ကို ရေတွက်ဖို့အတွက် ရေးခဲ့တယ်)  

31. [strip-substring.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/strip-substring.sh)  
(စာကြောင်း (string) ထဲကနေ လိုချင်တဲ့ စာတစ်ပိုင်းတစ်စ (substring) ကို ရှေ့က၊ နောက်ကနေ ပိုင်းဖြတ်ဖို့အတွက် ရေးခဲ့တယ်)  

32. [chk_total_duration.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk_total_duration.sh)  
(speaker တစ်ယောက်ချင်းစီနဲ့ အသံသွင်းထားတဲ့ wavefile တွေက ဘယ်နှစ်နာရီစာ ရှိသလဲ ဆိုတာကို သိချင်လို့ ရေးခဲ့တဲ့ shell script ပါ)  

33. [print-sentenceID-count.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-sentenceID-count.sh)  
(filename စာရင်းတစ်ခုထဲမှာ ရှိနေတဲ့ ဖိုင်နာမည်တွေထဲက SentenceID ကိုဖြတ်ယူပြီး၊ အဲဒီ SentenceID တွေက filename စာရင်းထဲမှာ ဘယ်နှစ်ခါပါဝင်နေသလဲ ဆိုတာကို print လုပ်ဖို့အတွက် ရေးခဲ့ပါတယ်)  

34. [mk-16KHz-mono.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-16KHz-mono.sh)  
(recording လုပ်ထားတဲ့ wave file တွေကို mono channel နဲ့ 16KHz ပြောင်းဖို့အတွက် ရေးခဲ့တယ်)  

35. [mk-spectrogram.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-spectrogram.sh)  
(Wave ဖိုင်တွေကို spectrogram ပုံတွေအဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ)  

36. [group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-UCF11.sh)  
(UCF YouTube Action Data Set ကို class အလိုက် အုပ်စုဖွဲ့ဖို့ သုံးခဲ့တယ်။)  

37. [group-within-group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-within-group-UCF11.sh)  
(shell script no. 36 နဲ့ ဆက်စပ်နေပါတယ်။ group-UCF11.sh ကို run ပြီးသွားတဲ့အခါမှာ စုပြီးသားဖြစ်တဲ့ mpg ဖိုင်တွေကို ထပ်ပြီးတော့ အုပ်စုခွဲဖို့အတွက် သုံးခဲ့ပါတယ်)  

38. [dot2pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2pic.sh)  
(Graph description language နဲ့ ရေးထားတဲ့ dot ဖိုင်ကနေ png, eps, svg ဖိုင်တွေ အဖြစ်ပြောင်း ဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ)  

39. [2mono-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/2mono-pdf.sh)  
(color PDF ဖိုင်ကနေ black and white PDF ဖိုင်အဖြစ် ပြောင်းပေးတဲ့ bash script ပါ)  

40. [calc-bleu-all.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-bleu-all.sh)  
(Machine Translation experiment လုပ်အပြီး ရလာတဲ့ translated output ဖိုင်နဲ့ reference ဖိုင်ကို multi-bleu.perl ဆိုတဲ့ BLEU score calculation လုပ်ပေးတဲ့ perl script ဖိုင်ကို သုံးပြီး တွက်ပြထားတာဖြစ်ပါတယ်။ ဒီနေရာမှာ experiment က တစ်ခုထက်မက လုပ်ထားလို့ အဲဒီ ဖိုလ်ဒါတွေကို looping ပတ်ပြီး ဝင်တွက်ထားတာကို လေ့လာစေချင်ပါတယ်။ bash က အဲဒီလိုမျိုး အသုံးဝင်ပါတယ်။)  

41. [calc-ribes-all.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-ribes-all.sh)  
(နံပါတ် ၄၀ က bash script လိုပါပဲ။ ဒီနေရာမှာတော့ RIBES score ကိုတွက်ပေးတဲ့ RIBES.py ကို သုံးပြထားပါတယ်။ long distance language pair တွေကို machine translation လုပ်တဲ့အခါမှာ RIBES score က အသုံးဝင်ပါတယ်။)  

42. [print-matched-x.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-matched-x.sh)  
(xargs နဲ့ fgrep ကို သုံးပြီးတော့ ကိုယ်လိုချင်တဲ့ စာကြောင်းတွေကို ရှာဖွေဆွဲထုတ်ပြီး၊ matched ဖြစ်တဲ့ စာကြောင်း တွေကို အကြောင်းအရေအတွက် x အတိုင်း print လုပ်ခိုင်းတဲ့ shell script ပါ)  

43. [split-train-dev-test.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/split-train-dev-test.sh)  
(Statistical Machine Translation experiment တွေကို လုပ်တိုင်းမှာ ဒီလိုမျိုး ရှိတဲ့parallel data ဖိုင်ကနေ training data, development data, test data ခွဲဖို့အတွက် ပြင်ဆင်ရတဲ့ bash script ကို ကျွန်တော်ခဏခဏ ရေးဖြစ်ပါတယ်။ သုံးတဲ့အခါမှာ ကိုယ့်ဖိုင်နာမည်နဲ့ ကိုက်အောင်ပြောင်းပေးရတာ၊ for loop condition တွေကို ပြောင်းရတာတွေ ရှိပေမဲ့ SMT လုပ်ချင်တဲ့ သူတွေအတွက် အသုံးဝင်မှာမို့)  

44. [clean-space-all.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/clean-space-all.sh)  
(shell ဖိုင်ထဲကနေ perl script [clean-space.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-space.pl) ကို ခေါ်သုံးပြထားပါတယ်။ SMT မ run ခင်မှာ၊ NLP model တစ်ခုခု မဆောက်ခင်မှာ ဒီလိုမျိုး space ရှင်းတဲ့ အလုပ်မျိုးက လုပ်ရပါတယ်)  















