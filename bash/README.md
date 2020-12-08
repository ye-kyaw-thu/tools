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

45. [mk-g2p-model.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-g2p-model.sh)  
(shell script for building grapheme-to-phoneme model with Phonetisaurus)  

46. [mk-syl-list.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-syl-list.sh)  
(a shell script for list up Myanmar syllables)  

47. [rm-200b-200d.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-200b-200d.sh)  
(ထုံးစံအတိုင်း မြန်မာ syllable တွေမှာ 200b, 200d တွေ ရောပါနေတတ်ပါတယ်။ ဒီ shell script က အဲဒီ မမြင်ရတဲ့ စာလုံးတွေကို ဖယ်ဖို့အတွက် ရေးခဲ့တာပါ။)   

48. [print-char.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-char.sh)  
(ဖိုင်ကို ဖွင့်ဖတ်ပြီး စာလုံး တစ်လုံးချင်းစီ ရိုက်ထုတ်ပေးပါလိမ့်မယ်။ စာတစ်ကြောင်းမှာ character တစ်လုံးစီ ရိုက်ထုတ်ပြီးတော့ enter ခေါက်ဆင်သွားတဲ့ ပုံစံပါ။)  

49. [prepare-10fold-smt-pair.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/prepare-10fold-smt-pair.sh)  
(input ပေးလိုက်တဲ့ ဖိုင် format က "မြန်မာစာကြောင်း|ဘိတ်စာကြောင်း|ထားဝယ်စာကြောင်း" ပါ။ အဲဒီ input ဖိုင်ကို $2 option နဲ့ ပေးလိုက်တဲ့ လိုင်းအရေအတွက်အတိုင်း ဖိုင်ကို ခွဲပေးပါလိမ့်မယ်။ ဒီနေရာမှာတော့ 10-fold cross validation လုပ်ချင်လို့ 10 ပိုင်းခွဲခဲ့ပါတယ်။ ခွဲထားတဲ့ ဖိုင်ကနေမှ SMT experiment run ချင်တဲ့ ဘိတ်စာကြောင်းနဲ့ ထားဝယ်စာကြောင်းတွေကို ဆွဲထုပ်ယူပြီး train, dev, test အဖြစ်ခွဲပေးမှာ ဖြစ်ပါတယ်။)  

50. [rm-ctrl-m.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-ctrl-m.sh)  
(Ctrl-M or ^M ကို perl one liner ကို သုံးပြီး ဖယ်ပြထားတဲ့ ပရိုဂရမ်ပါ။ shell script ထဲကနေ perl one line ကို ခေါ်သုံးပုံကိုလည်း ကျောင်းသားတွေကို သိစေချင်လို့ demo လုပ်ပြထားတာပါ)  

51. [x-letter-word.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/x-letter-word.sh)  
(x letter syllables, x letter words တွေကို ဆွဲထုတ်ဖို့အတွက် သုံးခဲ့တယ်။ input ဖိုင်ကတော့ syllable သို့မဟုတ် word segmentation လုပ်ပေးထားရမယ်။)  

52. [paste-column.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/paste-column.sh)  
(ဖိုင်နှစ်ဖိုင်မှာ ရှိတဲ့ field သို့မဟုတ် column တွေအလိုက် တွဲပေးဖို့အတွက် သုံးခဲ့တယ်)  

53. [lm-building-exec.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/lm-building-exec.sh)  
(SRILM toolkit ကို သုံးပြီးတော့ language model ဘယ်လိုဆောက်ရသလဲ ဆိုတာကို ဒီမိုပြဖို့ ရေးခဲ့တဲ့ bash shell script ပါ  
demo running အတွက် သုံးထားတဲ့ ဖိုင်တွေဖြစ်တဲ့ [my-corpus.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/my-corpus.txt) ဖိုင်နဲ့ [my-test.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/my-test.txt) ဖိုင်ကိုလည်း bash/test-data/ အောက်မှာ upload လုပ်ပေးထားပါတယ်။ ပထမဆုံး LM ဆောက်တဲ့သူတွေအတွက် လေ့လာရ လွယ်ကူအောင် running log ဖိုင်ဖြစ်တဲ့ [lm-building-exec.log](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/lm-building-exec.log) ကိုလည်း တင်ပေးထားပါတယ်)  

54. [print-most-common.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-most-common.sh)  
(SRILM toolkit ရဲ့ command တစ်ခုဖြစ်တဲ့ ngram-count ကို သုံးပြီးတော့ အသုံးများဆုံး စာလုံးတွေကို ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တယ်) 

55. [calc-ppl-with-kenlm-query.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-ppl-with-kenlm-query.sh)  
(KenLM ရဲ့ query command ကို သုံးပြီးတော့ ppl including OOVs, ppl excluding OOVs တွေကို တွက်ဖို့အတွက် ရေးခဲ့တယ်)  

56. [mk-two-lm-and-merge.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-two-lm-and-merge.sh)  
(Language model နှစ်ခုကိုဆောက်ပြီးတော့ static interpolation လုပ်တာကို ကျောင်းသားတွေကို ဒီမိုလုပ်ပြဖို့ ရေးခဲ့တယ်)    

57. [mk-class-lm.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-class-lm.sh)  
(word class ကို အခြေခံပြီးမှ language model ဆောက်တာကို ဒီမို လုပ်ပြဖို့အတွက် ရေးခဲ့တယ်)  

58. [get-myPOS-tag.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/get-myPOS-tag.sh)  
(myPOS POS tagged corpus ထဲကနေ tag frequency နဲ့ သုံးထားတဲ့ tag တွေချည်းပဲကို ဆွဲထုတ်ဖို့ ရေးခဲ့တယ်)  

59. [rm-myPOStags.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-myPOStags.sh)  
(myPOS ရဲ့ tag တွေကို testing data အတွက် ပြင်တဲ့အခါမှာ ဖယ်ရပါတယ်။ POS tag တွေကို sed ကို သုံးပြီး ဖယ်ပြထားပါတယ်)  

60. [print-same-col1.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-same-col1.sh)  
(ဖိုင်နှစ်ဖိုင်က ပထမဆုံး field က တူသလားစစ်ပြီးတော့၊ တူခဲ့ရင် အဲဒီ ဖိုင်နှစ်ဖိုင်ထဲက ကိုယ်လိုချင်တဲ့ field တွေကို print လုပ်ပေးတဲ့ shell script ပါ။  
တစ်ခုရှိတာက input file နှစ်ဖိုင် စလုံးကို sorting စီထားပြီးသား condition အတွက် ရေးထားတာ။)  

61. [char-segmentation.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/char-segmentation.sh)  
(NLP အလုပ်တွေမှာ character segementation ဆိုတာ ခဏခဏ လုပ်ကြရပါတယ်။ ဥပမာ မြန်မာစာလုံးပေါင်း အသတ်ကို နှစ်ခါ ထပ်ရိုက်ပြီး မှားထားတာမျိုးကို စစ်ကြည့်တဲ့ အခါမျိုးပါ။ အဲဒီလို စာလုံးတစ်လုံးချင်းစီကို ရိုက်ထုတ်ပေးဖို့အတွက် bash script ရေးရတာကမခက်ပေမဲ့ လိုအပ်တဲ့အခါမှာ အသုံးပြုလို့ရအောင် တင်ပေးလိုက်တယ်။)  

62. [chk-blank-fields.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk-blank-fields.sh)  
(\<TAB\> ခြားပြီး သိမ်းထားတဲ့ ကော်လံသုံးခု သို့မဟုတ် field သုံးခု ရှိတဲ့ ဖိုင်ထဲကနေ blank field ပါနေတဲ့ စာကြောင်းတွေကို လိုင်းနံပါတ်နဲ့တကွ ရိုက်ထုတ်ပြဖို့ ရေးခဲ့တယ်။)  

63. [chk-field-length.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk-field-length.sh)  
(\<TAB\> ခြားပြီး သိမ်းထားတဲ့ ကော်လံသုံးခု သို့မဟုတ် field သုံးခု ရဲ့ length တွေကိုနှိုင်းယှဉ်ကြည်ဖို့ ရေခဲ့ပါတယ်။)  

64. [crop-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/crop-pdf.sh)  
(PDF ဖိုင်ထဲကနေ empty ဖြစ်နေတဲ့ margin တွေကို ဖြတ်ထုတ်ဖို့ ရေးခဲ့တဲ့ shell script ပါ။ စာမျက်နှာ တစ်ခုလုံးကနေ စာသားတွေပဲ ရှိနေတဲ့ အပိုင်းကိုပဲ လိုချင်တဲ့အခါ အသုံးဝင်ပါလိမ့်မယ်။ OCR engine အတွက် PDF ဖိုင်ကနေ စာသားရှိတဲ့ အပိုင်းတွေကို input လုပ်ဖို့နေရာမျိုး၊ figure တွေရှိတဲ့ အပိုင်းတွေကိုပဲ PDF အနေနဲ့ quality မကျအောင် ဖြတ်ထုတ်ချင်တဲ့ အခါမျိုးမှာ အသုံးဝင်ပါလိမ့်မယ်။)

65. [excel2csv-chk-fields.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/from65/excel2csv-chk-fields.sh)  
(Excel ဖိုင် (xls မဟုတ်ပဲ .xlsx) ထဲက sheet တစ်ခုချင်းစီကို csv ဖိုင်တွေအဖြစ် ပြောင်းပြီးတော့ field တွေ ဘယ်နှစ်ခုပါသလဲဆိုတာကို ရေတွက်ပေးပါလိမ့်မယ်)  

66. [change-format.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/change-format.sh)  
(format တစ်ခုကနေ ကိုယ်လိုချင်တဲ့ format ကို ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ one line shell script ပါ)  

67. [format-mecab-pos.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/format-mecab-pos.sh)  
(ဂျပန်စာ Part-of-Speech and Morphological Analyzer ကနေ ထွက်လာတဲ့ output ကနေ word/pos, word/pos_subpos ပုံစံကို ပြောင်းယူဖို့ ရေးခဲ့တယ်။)  


68. [cp-config.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/cp-config.sh)  
(Stastical Machine Translation (SMT) experiment တွေကို အများကြီး လုပ်တဲ့ အခါမှာ configuration file တွေ perl script တွေရဲ့ တချို့ လိုင်းတွေကို ဝင်ပြင်ပြီး သက်ဆိုင်ရာ ဖိုလ်ဒါအောက်ကို ကော်ပီကူးဖို့အတွက်ပြင်ဆင်ရပါတယ်။ အဲဒီအတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။ )  

69. [DELETE-ALL.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/DELETE-ALL.sh)  
(SMT ကို moses toolkit သုံးပြီး လုပ်တဲ့အခါမှာ တခါတလေ အကြောင်းအမျိုးမျိုးကြောင့် run ထားတဲ့ ဖိုလ်ဒါတွေကို ဝင်ဖျက်ရတာမျိုး ရှိပါတယ်။ ဒီဥပမာကတော့ language pair သုံးခုအတွက် 10-fold cross validation လုပ်ထားတာမို့ စုစုပေါင်း baseline ဖိုလ်ဒါက ၆၀ ရှိပါတယ်။ အဲဒါကို တစ်ခေါက် တစ်ခေါက် rm command နဲ့ တစ်ခုချင်းဖျက်မနေရအောင် ရေးပြီးသုံးခဲ့တဲ့ bash script ဥပမာ တစ်ပုဒ်ဖြစ်ပါတယ်)  

70. [trim-silence.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/trim-silence.sh)  
(အသံဖမ်းထားတဲ့ waveဖိုင်တွေရဲ့ အစပိုင်း၊ နောက်ဆုံးပိုင်းမှာရှိတဲ့ silence ဖြစ်နေတဲ့ အပိုင်းတွေကို ဖြတ်ထုတ်ပြထားတဲ့ shell script ပါ။ ဒီ script ကို သုံးပြီးတော့ ကိုယ့်ရဲ့ အသံဖိုင်တွေအတွက် အဆင်ပြေအောင် ဖြတ်မယ့် silence duration, volume တို့ကို ညှိပြီးတော့ အသုံးပြုပါ)  

71. [wav2wavform.sh](https://github.com/ye-kyaw-thu/tools/edit/master/bash/wav2wavform.sh)  
(ဖိုလ်ဒါတစ်ခုအောက်ထဲမှာ သိမ်းထားတဲ့ wave ဖိုင်တွေကနေ waveform ပုံတွေအဖြစ် ပြောင်းပေးတဲ့ ပရိုဂရမ်ပါ။ အထက်က shell script နံပါတ် ၇၀ နဲ့လည်း ဆက်စပ်နေပါတယ်)  

72. [mytext2pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytext2pic.sh)  
(ဖိုင်ထဲမှာ သိမ်းထားတဲ့ မြန်မာစာကြောင်း တစ်ကြောင်းချင်းစီကို ပုံဖိုင်အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ ဖိုင်ပါ။ Language Understanding Lab., ရဲ့ internship ကျောင်းသားတွေအတွက် ပြင်ဆင်ခဲ့စဉ်က ရေးထားခဲ့ ...)  

73. [formula-pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/formula-pic.sh)  
(shell script example နံပါတ် ၇၂ နဲ့ ဆက်စပ်ပါတယ်။ formula-pic.sh မှာတော့ သင်္ချာဖော်မြူလာကို latex ရေးတဲ့ ပုံစံနဲ့ ရေးပြီး အလွယ်တကူ ဖော်မြူလာပုံတွေ အဖြစ် ဖန်တီးတာကို လက်တွေ့ လုပ်ပြထားတာ ဖြစ်ပါတယ်။ နေရာ အမျိုးမျိုးမှာ အသုံးဝင်ပါလိမ့်မယ်။)  

74. [rm-heading-tab-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-heading-tab-lineno.sh)  
(စာကြောင်းရဲ့ ရှေ့ဆုံးမှာ ရှိနေတဲ့ Tab, space, line number တွေကို ဖျက်ဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ။ perl one-liner ကို သုံးပြထားပါတယ်။)  

75. [mk-10cross-data.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-10cross-data.sh)  
(10-fold cross validation machine translation လုပ်ဖို့အတွက် parallel corpus ကို ၁၀ပိုင်း ပိုင်းဖို့ ရေးခဲ့တဲ့ bash script နောက်တပုဒ်ပါ။ မြန်မာ-ချင်း MT experiment အတွက် သုံးခဲ့တယ်။)  

76. [align-GIZA++.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/align-GIZA%2B%2B.sh)  
(GIZA++ alignment toolkit ကို သုံးပြီး alignment လုပ်ပေးမယ့် script ဖြစ်ပါတယ်။ ကိုယ့်စက်ထဲမှာ GIZA++ ကို အရင် install လုပ်ထားရပါမယ်)  

77. [date-time-info.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/date-time-info.sh)  
(Linux မှာက powerful ဖြစ်တဲ့ command တွေက ပြောလို့ မကုန်နိုင်လောက်အောင် အများကြီးပါပဲ။ အဲဒီအထဲက "date" command ကိုသုံးပြီးတော့ နေ့စွဲ၊ အချိန်တွေကို ကိုယ်လိုချင်တဲ့ format နဲ့ ဆွဲယူသုံးတာတွေကို ဒီမို ရေးပြထားတာဖြစ်ပါတယ်)  

78. [mp4-to-wav.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mp4-to-wav.sh)  
(mp4 ဖိုင်ကနေ audio အပိုင်းကိုပဲ ဆွဲထုတ်ယူပြီး wave file format အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ)  

79. [my-font-chk.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/my-font-chk.sh)  
(ကိုယ့် Linux စက်ထဲမှာ install လုပ်ထားတဲ့ မြန်မာစာဖောင့်ဖိုင်တွေကို list လုပ်ပြဖို့အတွက် ရေးခဲ့ပါတယ်)  

80. [rec-recorder.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rec-recorder.sh)  
(rec command ကို သုံးပြီးတော့ အသံဖမ်းပြီး wave ဖိုင်တွေအဖြစ် နံပါတ်စဉ်အလိုက် သိမ်းပေးတဲ့ shell command ပါ)  

81. [mp42gif.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mp42gif.sh)  
(mp4 ဗီဒီယိုဖိုင်ကနေ animated GIF ပုံအဖြစ်ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ bash shell script ပါ)  

82. [extract-target-text.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/extract-target-text.sh)  
(moses MT engine ရဲ့ OSM model ကနေ ထွက်လာတဲ့ ouput ကနေ ပုံမှန် စာကြောင်းအဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ script ပါ)  

83. [txt2png.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/txt2png.sh)  
(text ဖိုင်ထဲမှာ ရိုက်ထားတဲ့ မြန်မာစာကြောင်းတွေကို PNG ပုံဖိုင်အဖြစ်ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ bash shell script ပါ)  

84. [pic2histogram.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic2histogram.sh)  
(ပုံဖိုင်ကနေ histogram ထုတ်ဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ)  

85. [tesseract-ocr.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/tesseract-ocr.sh)  
(Google ရဲ့ OCR engine ဖြစ်တဲ့ Tesseract ကို command line ကနေ အလွယ်တကူ စမ်းကြည့်စဉ်မှာ သုံးခဲ့တဲ့ bash shell script တစ်ပုဒ်ပါ)  

86. [sylbreak-10fold-mt.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/sylbreak-10fold-smt.sh)  
(10 fold Statistical Machine Translation ကို syllable ဖြတ်ထားတဲ့ ဒေတာနဲ့ လုပ်ဖို့အတွက် ပြင်ဆင်စဉ်မှာ အသုံးပြုဖို့ ရေးခဲ့တဲ့ script တစ်ပုဒ်ပါ)  

87. [syllable-break-multi-files.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/syllable-break-multi-files.sh)  
(ဖိုင် တစ်ဖိုင်ထက်မက syllable ဖြတ်တာကို ဥပမာ run ပြထားတာပါ။ bash scripting ရဲ့ $* ကိုလည်း ကျောင်းသားတွေ သိစေချင်လို့ သုံးပြထားတာလည်း ပါပါတယ်။)  

88. [build-fastalign-pt.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/build-fastalign-pt.sh)  
([fast_align](https://github.com/clab/fast_align) နဲ့ parallel data ကို alignment လုပ်ပြီးထွက်လာတဲ့ alignment output ကနေ phrase-table ဆောက်ဖို့အတွက် သုံးခဲ့တဲ့ shell script ပါ။ ဒီ script ကို သုံးမယ်ဆိုရင် [moses](http://www.statmt.org/moses/) ရဲ့ running script တွေက ကိုယ့်စက်ထဲမှာ ရှိနေမှ ရပါမယ်)  

89. [txt2ASL-BSL.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/txt2ASL-BSL.sh)  
(အင်္ဂလိပ်စာလုံး၊ စာကြောင်းတွေကနေ American Sign Language နဲ့ British Sign Language ရဲ့ fingerspelling ပုံတွေအဖြစ် ပြောင်းဖို့အတွက်ရေးခဲ့တဲ့ shell script တစ်ပုဒ်ပါ။ ရှေ့က 83. txt2png.sh နဲ့ အတူတူပါပဲ font ပြောင်းသုံးတာပါပဲ)  

90. [mgiza-align.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mgiza-align.sh)  
([mgiza](https://github.com/moses-smt/mgiza) ကလည်း နာမည်ကြီးတဲ့ word alignment tool တစ်ခုဖြစ်ပါတယ်။ သုံးပုံသုံးနည်းကို script ရေးပြထားတာ ဖြစ်ပါတယ်)  

91. [add-dummy-word-mk-csv.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/add-dummy-word-mk-csv.sh)  
(ပြင်ထားတဲ့ corpus ရဲ့ format ""သရက်/Fru ကိုင်းကူးနည်း/AgrK လေး/nolabel လည်း/nolabel သိချင်/nolabel ပါ/nolabel တယ်/nolabel",\_\_AgrK\_\_" ဆိုတဲ့ ပုံစံကနေ CSV ဖိုင် format နှစ်ခုဖြစ်တဲ့ Fru,AgrK,nolabel,nolabel,nolabel,nolabel,nolabel,\_\_AgrK\_\_ format နဲ့ "Fru AgrK nolabel nolabel nolabel nolabel nolabel",\_\_AgrK\_\_ format အဖြစ်ကိုပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ bash shell script တစ်ပုဒ်ပါ)  
