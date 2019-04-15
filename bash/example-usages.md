# Example usages of bash programs

မှတ်ချက်။ ။ bash ပရိုဂရမ်တွေကို run တဲ့အခါမှာ အောက်ပါအတိုင်း ပုံစံနှစ်မျိုးနဲ့ run လို့ရပါတယ်။  

```bash
$bash program.sh  
```

(သို့မဟုတ်)  

```bash
$./program.sh
```

bash ပရိုဂရမ်ဖိုင်နာမည်ရဲ့ ရှေ့ကနေ bash ဆိုပြီးမရိုက်ပဲနဲ့ run ဖို့အတွက်က  
chmod +x ./program.sh ဆိုပြီး executable mode ကို ပြောင်းပေးထားဖို့ လိုအပ်ပါတယ်။  

## 1.[read-and-move.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/read-and-move.sh)

ကြုံရပါလိမ့်မယ် zip လုပ်ထားတဲ့ ဖိုင်ကို ဖြေလိုက်တဲ့အခါမှာ ဖိုလ်ဒါတစ်ခုအောက်မှာ သိမ်းမပေးပဲနဲ့ လက်ရှိ ဖိုလ်ဒါအောက်မှာပဲ ဖိုင်တွေကို ဖြေချပေးသွားတာမျိုး။  
အဲဒီလိုအချိန်မျိုးမှာ ကျွန်တော်ကတော့ ဖြေချလိုက်တဲ့ ဖိုင်နာမည်တွေကို text ဖိုင်တစ်ဖိုင်မှာ သိမ်းလိုက်ပြီးတော့ read-and-move.sh ပရိုဂရမ်နဲ့ ကိုယ်သိမ်းထားချင်တဲ့ ဖိုလ်ဒါအောက်ကို ရွှေ့ပါတယ်။  

```bash
lar@lar-air:~/tool$ tar -xzvf ./rt_pvc-1.0.0.tgz 
RtAudio.h
RtError.h
Stk.h
Thread.h
chuck_fft.h
pvc.h
chuck_fft.c
RtAudio.cpp
Stk.cpp
Thread.cpp
pvc.cpp
rt_pvc.cpp
makefile.alsa
makefile.osx
makefile.win32
```

အထက်ပါ ဖြေချသွားတဲ့ ဖိုင်နာမည်တွေကို filename.txt ဆိုတဲ့ ဖိုင်အနေနဲ့ သိမ်းလိုက်ပြီးတော့၊ လက်ရှိဖိုလ်ဒါအောက်မှာရှိတဲ့ tmp ဖိုလ်ဒါထဲကို ရွှေ့တဲ့အနေနဲ့  
ဥပမာ run ပြထားပါတယ်။  

```bash
lar@lar-air:~/tool$ ./read-and-move.sh ./filename.txt ./tmp/
moving RtAudio.h to ./tmp/
moving RtError.h to ./tmp/
moving Stk.h to ./tmp/
moving Thread.h to ./tmp/
moving chuck_fft.h to ./tmp/
moving pvc.h to ./tmp/
moving chuck_fft.c to ./tmp/
moving RtAudio.cpp to ./tmp/
moving Stk.cpp to ./tmp/
moving Thread.cpp to ./tmp/
moving pvc.cpp to ./tmp/
moving rt_pvc.cpp to ./tmp/
moving makefile.alsa to ./tmp/
moving makefile.osx to ./tmp/
moving makefile.win32 to ./tmp/
```

## 2.[change-filenames.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/change-filenames.sh)  

ဆိုကြပါစို့။ လက်ရှိရောက်နေတဲ့ path မှာ အောက်ပါအတိုင်း ဖိုလ်ဒါ ၄၅ ဖိုလ်ဒါ ရှိတယ်။  

```bash
ka2pluskha2@asr-proto-1:~/exp/audionet/AudioNet/dl/Speaker2$ ls
1   12  15  18  20  23  26  29  31  34  37  4   42  45  7 
10  13  16  19  21  24  27  3   32  35  38  40  43  5   8 
11  14  17  2   22  25  28  30  33  36  39  41  44  6   9
```
အဲဒီ ဖိုလ်ဒါတစ်ခုချင်းစီမှာလည်း အောက်ပါဥပမာကဲ့သို့ အသံသွင်းထားတဲ့ wave ဖိုင်တွေ အများကြီးရှိတယ်။  
လုပ်ချင်တာက အဲဒီဖိုလ်ဒါ တစ်ခုချင်းစီမှာရှိနေတဲ့ အသံသွင်းထားတဲ့အချိန်အတိုင်းနာမည်ပေးထားတဲ့ wave ဖိုင်တွေကို နာမည်ပြောင်းချင်တယ်။  
ဖိုင်နာမည် ပြောင်းတဲ့အခါမှာလဲ ဖိုလ်ဒါနာမည်တွေဖြစ်တဲ့ "1", "2", "3" စတာတွေကိုပါ အသီသီးတွဲပြီး နာမည်အသစ်ပေးချင်တယ် ဆိုပါစို့။  

```bash
ka2pluskha2@asr-proto-1:~/exp/audionet/AudioNet/dl/Speaker2$ ls ./1
2018-10-13-14_39_13.wav  2018-10-13-14_41_09.wav  2018-10-13-14_42_10.wav  2018-10-13-14_43_56.wav
2018-10-13-14_39_24.wav  2018-10-13-14_41_12.wav  2018-10-13-14_43_07.wav  2018-10-13-14_43_59.wav
2018-10-13-14_39_27.wav  2018-10-13-14_41_15.wav  2018-10-13-14_43_10.wav  2018-10-13-14_44_02.wav
2018-10-13-14_39_30.wav  2018-10-13-14_41_18.wav  2018-10-13-14_43_13.wav  2018-10-13-14_44_05.wav
2018-10-13-14_39_33.wav  2018-10-13-14_41_22.wav  2018-10-13-14_43_16.wav  2018-10-13-14_44_09.wav
2018-10-13-14_40_01.wav  2018-10-13-14_41_25.wav  2018-10-13-14_43_19.wav  2018-10-13-14_44_12.wav
2018-10-13-14_40_04.wav  2018-10-13-14_41_28.wav  2018-10-13-14_43_22.wav  2018-10-13-14_45_30.wav
2018-10-13-14_40_08.wav  2018-10-13-14_41_36.wav  2018-10-13-14_43_25.wav  2018-10-13-14_45_33.wav
2018-10-13-14_40_43.wav  2018-10-13-14_41_39.wav  2018-10-13-14_43_28.wav  2018-10-13-14_45_36.wav
2018-10-13-14_40_48.wav  2018-10-13-14_41_42.wav  2018-10-13-14_43_31.wav  2018-10-13-14_45_38.wav
2018-10-13-14_40_51.wav  2018-10-13-14_41_45.wav  2018-10-13-14_43_34.wav  2018-10-13-14_45_41.wav
2018-10-13-14_40_55.wav  2018-10-13-14_41_48.wav  2018-10-13-14_43_38.wav  2018-10-13-14_45_44.wav
2018-10-13-14_40_58.wav  2018-10-13-14_41_51.wav  2018-10-13-14_43_41.wav  2018-10-13-14_45_47.wav
2018-10-13-14_41_02.wav  2018-10-13-14_41_54.wav  2018-10-13-14_43_50.wav  2018-10-13-14_45_54.wav
2018-10-13-14_41_05.wav  2018-10-13-14_41_57.wav  2018-10-13-14_43_53.wav  2018-10-13-14_45_57.wav
```
အဲဒီအတွက် ./change-filenames.sh ဖိုင်ကို သုံးလို့ရပါတယ်။  
Run မလုပ်ခင်မှာ ./change-filenames.sh ဖိုင်ကို ဖိုလ်ဒါတွေရှိတဲ့ path အောက်ထဲကို ကော်ပီကူးတာဖြစ်ဖြစ် လုပ်ထားပြီးတော့ အောက်ပါအတိုင်း run ပါ။  

```bash
ka2pluskha2@asr-proto-1:~/exp/audionet/AudioNet/dl/Speaker2$./change-filenames.sh
```
ရှိသမျှဖိုလ်ဒါထဲမှာ ရှိတဲ့ wave ဖိုင်တွေရဲ့ နာမည်ကို အောက်ပါအတိုင်း ပြောင်းပေးသွားတာကို တွေ့ရပါလိမ့်မယ်။  
နားလည်အောင်က ./change-filenames.sh မှာ ရေးထားတာကို လေ့လာပါ။  

```bash
ka2pluskha2@asr-proto-1:~/exp/audionet/AudioNet/dl/Speaker2$ ls ./1
spk2-1-10.wav  spk2-1-19.wav  spk2-1-27.wav  spk2-1-35.wav  spk2-1-43.wav  spk2-1-51.wav  spk2-1-5.wav
spk2-1-11.wav  spk2-1-1.wav   spk2-1-28.wav  spk2-1-36.wav  spk2-1-44.wav  spk2-1-52.wav  spk2-1-60.wav
spk2-1-12.wav  spk2-1-20.wav  spk2-1-29.wav  spk2-1-37.wav  spk2-1-45.wav  spk2-1-53.wav  spk2-1-6.wav
spk2-1-13.wav  spk2-1-21.wav  spk2-1-2.wav   spk2-1-38.wav  spk2-1-46.wav  spk2-1-54.wav  spk2-1-7.wav
spk2-1-14.wav  spk2-1-22.wav  spk2-1-30.wav  spk2-1-39.wav  spk2-1-47.wav  spk2-1-55.wav  spk2-1-8.wav
spk2-1-15.wav  spk2-1-23.wav  spk2-1-31.wav  spk2-1-3.wav   spk2-1-48.wav  spk2-1-56.wav  spk2-1-9.wav
spk2-1-16.wav  spk2-1-24.wav  spk2-1-32.wav  spk2-1-40.wav  spk2-1-49.wav  spk2-1-57.wav
spk2-1-17.wav  spk2-1-25.wav  spk2-1-33.wav  spk2-1-41.wav  spk2-1-4.wav   spk2-1-58.wav
spk2-1-18.wav  spk2-1-26.wav  spk2-1-34.wav  spk2-1-42.wav  spk2-1-50.wav  spk2-1-59.wav
```  
## 3.[rm-date-sentences.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-date-sentences.sh)

Experiment တစ်ခုအတွက် tensorflow နဲ့ ဆောက်ထားတဲ့ image recognition မော်ဒယ်တစ်ခု ကို open test လုပ်စဉ်မှာ  
ရလာတဲ့ log ဖိုင်ရဲ့ output က အောက်ပါအတိုင်းပါ။  

```
Testing with open-test data ook for Class1...

2018-10-16 01:54:20.460832: W tensorflow/core/framework/op_def_util.cc:346] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
2018-10-16 01:54:20.828987: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA

Evaluation time (1-image): 0.551s

21 0.33185694
23 0.21179184
20 0.20961815
24 0.07168844
38 0.037272394
2018-10-16 01:54:23.102940: W tensorflow/core/framework/op_def_util.cc:346] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
2018-10-16 01:54:23.310173: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA

Evaluation time (1-image): 0.575s

1 0.90066767
31 0.04104986
29 0.016420923
36 0.012420018
34 0.012266385
2018-10-16 01:54:25.573635: W tensorflow/core/framework/op_def_util.cc:346] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
2018-10-16 01:54:25.776136: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
...
...
...
```

ရက်စွဲတွေနဲ့ စတဲ့ စာကြောင်းတွေက tensorflow မော်ဒယ်ကို သုံးတဲ့အခါမှာ ပေးတဲ့ warning message တွေပါ။  
ရလဒ်တွေကို ကြည့်တဲ့အခါမှာ အဲဒီစာကြောင်းတွေက အနှောက်အယှက်ဖြစ်နေလို့ ရက်စွဲနဲ့စတဲ့ စာကြောင်းတွေကို ဖြုတ်ဖို့အတွက်  
rm-date-sentences.sh ကို အောက်ပါအတိုင်းသုံးခဲ့ပါတယ်။  
(log file ကိုလည်း bash/test-data/ ဖိုလ်ဒါအောက်မှာ refer လုပ်လို့ရအောင် upload လုပ်ပေးထားပါတယ်)  

```bash
./rm-date-sentences.sh ./ot-5person-200k.log > ./ot-5person-200k.log.clean
```

ot-5person-200k.log.clean ဖိုင်ထဲမှာတော့ date နဲ့စတဲ့ စာကြောင်းတွေက ရှင်းထားပြီးသားဖြစ်နေတာကို အောက်ပါအတိုင်း တွေ့ရပါလိမ့်မယ်။  

```
Testing with open-test data ook for Class1...


Evaluation time (1-image): 0.551s

21 0.33185694
23 0.21179184
20 0.20961815
24 0.07168844
38 0.037272394

Evaluation time (1-image): 0.575s

1 0.90066767
31 0.04104986
29 0.016420923
36 0.012420018
34 0.012266385

Evaluation time (1-image): 0.537s

1 0.45257574
21 0.43286347
34 0.06279393
20 0.02177601
29 0.015827697
...
...
...
```

## 4.[print-classID-prediction-result.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-classID-prediction-result.sh)

ဒီ shell script က /test-data/ ဖိုလ်ဒါအောက်မှာ ရှိတဲ့ image classification testing တစ်ခုကနေ ရလာတဲ့ [ot-5person-200k.log](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/ot-5person-200k.log) ဖိုင်ထဲကနေ  
အောက်ပါအတိုင်း Class ID နံပါတ်အလိုက် ဘယ်နှစ်ခု classification ကမှန်တယ်၊ ဘယ်နှစ်ခု မှားတယ် စတာတွေကို analysis လုပ်ရတာလွယ်ဖို့အတွက်  
သုံးခဲ့တဲ့ shell script ပါ။ ဒီ shell script မှာတော့ linux command တွေကို pipe လုပ်ပြီးတွဲသုံးပြထားပါတယ်။ လေ့လာကြည့်ပါ။  

```
Classification Result for Class-1:

Class-1 14
Class-4 2
Class-8 11
Class-19        1
Class-21        2
Class-26        1
Class-34        2
Class-38        1
Class-39        1
Class-40        1

Classification Result for Class-2:

Class-2 21
Class-3 3
Class-4 1
Class-13        2
Class-14        1
Class-17        2
Class-23        1
Class-24        1
Class-26        1
Class-28        1
Class-35        1
Class-37        1

Classification Result for Class-3:

Class-2 1
Class-3 18
Class-4 2
Class-5 1
Class-8 2
Class-11        1
Class-13        5
Class-14        1
Class-15        1
Class-17        1
Class-21        2
Class-24        1
...
...
...
```
## 5.[compare-img-or-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/compare-img-or-pdf.sh)

အောက်ပါ မြန်မာစာကြောင်းတွေထဲမှာ unicode encoding အနေနဲ့ကြည့်မယ်ဆိုရင် မှားတာတွေပါနေပါတယ်။ မြင်နိုင်ပါရဲ့လား။  

```
သြစတြေးလျ ရေကြောင်း သို့ ၀င်ရောက်ခဲ့ ပြီးနောက်
အနည်းဆုံး လူ ၁၁ ဉီး သေဆုံးခဲ့သည် ။ 
အမိမြေ လုံခြုံရေး ဉီးစီးဌာန က
၁၀ဝ,ဝ၀ဝ တွင် တစ် ယောက် နှုန်း သေကြောင်းကြံစည်ခြင်း ရှိ သော်လည်း မြောင်းပိုင်း ဒေသ သည် ၁၀ဝ,ဝ၀ဝ တွင် ၃၀ ကျော် နှုန်း ဖြစ်သည် ။
ရဲ အရာရှိ အများဆုံး ၃၀ သည် ဒေသ စံတော်ချိန် ၆:၀ဝ အေအမ် မှာ
```
ပွင့်ပွင့်လင်းလင်းပြောရရင် မြန်မာစာNLP သုတေသနကို နှစ်တော်တော်ကြာကြာလုပ်နေကြတဲ့သူတွေတောင် ဒီလိုအမှားမျိုးကို သတိမပြုမိကြတဲ့သူတွေ အများကြီးရှိပါတယ်။ အထူးသဖြင့် စာရိုက်တဲ့အခါမှာ ဇော်ဂျီလက်ကွက်၊ ဇော်ဂျီဖောင့်ကို နေ့စဉ်လိုလို အသုံးပြုကြသူများအနေနဲ့က ခက်ခဲမယ်လို့ ယူဆပါတယ်။ အထက်ပါ စာကြောင်းတွေက အဖွဲ့အစည်းတစ်ခုကနေပြီးတော့ corpus အဖြစ် released လုပ်ထားတဲ့ ဒေတာတွေကို ကျွန်တော်က စစ်ဖို့ကြုံလာလို့ တွေ့ရှိခဲ့တဲ့ မြောက်မြားလှစွာသော အမှားတွေထဲက တချို့ကို လက်တွေဥပမာအနေနဲ့ယူပြထားပါတယ်။  

ရည်ရွယ်ချက်ကတော့ ဒီလိုအမှားမျိုးတွေကို နောင်ရှောင်နိုင်ကြဖို့ပါ။  

[compare-img-or-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/compare-img-or-pdf.sh) က ပုံဖိုင်အဖြစ်သိမ်းထားတဲ့ဖိုင်တွေ (.jpg, .png, .tiff, .bmp ...) သို့မဟုတ် PDF ဖိုင်နှစ်ခုကို **ပုံအနေနဲ့** နှိုင်းယှဉ်ကြည့်ပြီးတော့  
မတူတာတွေကို နှိုင်းယှဉ်ပြီးပြပေးဖို့ (highlight လုပ်ပေးဖို့) ရေးခဲ့တဲ့ bash script ဖြစ်ပါတယ်။ ImageMagick package ရဲ့ "compare" command ကို ယူသုံးထားတာမို့ ကိုယ်ရဲ့စက်ထဲမှာ မရှိသေးဘူးဆိုရင် install လုပ်ပြီးမှ စမ်းကြည့်ပါ။  

ဥပမာ run ပြဖို့အတွက် သုံးထားတဲ့ဖိုင်တွေက [test-data/4compare-img-or-pdf/](https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/4compare-img-or-pdf) ဖိုလ်ဒါအောက်မှာ သိမ်းထားပါတယ်။  

```bash
../compare-img-or-pdf.sh ./errors-from-aru-corpus.pdf  ./errors-from-aru-corpus-edited.pdf diff2.png
```
အထက်ပါ command ကို run လိုက်ရင် [diff2.png](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/4compare-img-or-pdf/diff2.png) ဖိုင်ကို output အဖြစ်ရပါလိမ့်မယ်။  

ဒီဥပမာ ဖိုင်မှာ မှားနေတာတွေကတော့ အောက်ပါအတိုင်းပါ  

| အမှား | အမှန် |  
|:-------------:|:-----:|  
| သြ (သ ရရစ်) | ဩ (အက္ခရာ ဩ) |
| ဉီး (ညလေး) | ဥ (အက္ခရာ ဥ) |
| ၀င် (သုည) | ဝင် (ဗျည်း ဝလုံး) |

## 6.[chk-sort-by-columns.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk-sort-by-columns.sh)  
ကျွန်တော် NICT, Kyoto, Japan မှာ အလုပ်လုပ်နေတုန်း ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။ bash ပရိုဂရမ်ရေးတာကို လေ့လာနေတဲ့သူတွေအတွက်လည်း အသုံးဝင်မယ် လို့ယူဆလို့ comment ဘာညာဖြည့်ရေးပြီးတော့ တင်ပေးလိုက်ပါတယ်။  

သုံးပုံသုံးနည်း ဥပမာအနေနဲ့ [myG2P](https://github.com/ye-kyaw-thu/myG2P) (version1) အဘိဓာန်ကို shuffle လုပ်ထားတဲ့ဖိုင်ထဲက အကြောင်းတစ်ထောင်ကို [myg2p.ver1.txt.shuf.1k](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/chk-sort-by-columns/myg2p.ver1.txt.shuf.1k) ဆိုတဲ့နာမည်ပေးသိမ်းထားပြီးတော့ အဲဒီဖိုင်ထဲမှာပါတဲ့ ကော်လံတွေအလိုက် sorting စီပြထားပါတယ်။ 

```
lar@lar-air:~/tool/bash/sort-tst/4github$ ./chk-sort-by-columns.sh ./myg2p.ver1.txt.shuf.1k 
No. of columns: 4

head ./myg2p.ver1.txt.shuf.1k.sorted-by-col1:

15	ကကွက်	က ကွက်	ka. gwe'
60	ကတိကဝတ်	က တိ က ဝတ်	ga- di. ka- wu'
78	ကတုတ်ကျင်း	က တုတ် ကျင်း	ga- dou' kyin:
150	ကမျဉ်းနီ	က မျဉ်း နီ	ka- mjin: ni
187	ကရိကထ	က ရိ က ထ	ka- ji. ka- hta.
201	ကရော်ကမည်	က ရော် က မည်	ka- jo ka- me
234	ကလိုင်	က လိုင်	ga- lain
267	ကသစ်	က သစ်	ka- thi'
321	ကင်းစောင့်	ကင်း စောင့်	kin: saun.
330	ကင်းပုန်း	ကင်း ပုန်း	kin: boun:
==========

head ./myg2p.ver1.txt.shuf.1k.sorted-by-col2:

15	ကကွက်	က ကွက်	ka. gwe'
60	ကတိကဝတ်	က တိ က ဝတ်	ga- di. ka- wu'
78	ကတုတ်ကျင်း	က တုတ် ကျင်း	ga- dou' kyin:
150	ကမျဉ်းနီ	က မျဉ်း နီ	ka- mjin: ni
187	ကရိကထ	က ရိ က ထ	ka- ji. ka- hta.
201	ကရော်ကမည်	က ရော် က မည်	ka- jo ka- me
234	ကလိုင်	က လိုင်	ga- lain
267	ကသစ်	က သစ်	ka- thi'
545	ကာရက	ကာ ရ က	ka ra- ka.
754	ကုစား	ကု စား	ku. za:
==========

head ./myg2p.ver1.txt.shuf.1k.sorted-by-col3:

15	ကကွက်	က ကွက်	ka. gwe'
60	ကတိကဝတ်	က တိ က ဝတ်	ga- di. ka- wu'
78	ကတုတ်ကျင်း	က တုတ် ကျင်း	ga- dou' kyin:
150	ကမျဉ်းနီ	က မျဉ်း နီ	ka- mjin: ni
187	ကရိကထ	က ရိ က ထ	ka- ji. ka- hta.
201	ကရော်ကမည်	က ရော် က မည်	ka- jo ka- me
234	ကလိုင်	က လိုင်	ga- lain
267	ကသစ်	က သစ်	ka- thi'
545	ကာရက	ကာ ရ က	ka ra- ka.
754	ကုစား	ကု စား	ku. za:
==========

head ./myg2p.ver1.txt.shuf.1k.sorted-by-col4:

20972	အချမ်းတက်	အ ချမ်း တက်	a- chan: te'
21091	အခြောက်တိုက်ကြွား	အ ခြောက် တိုက် ကြွား	a- chau' tai' kywa:
21079	အခြေတကျ	အ ခြေ တ ကျ	a- chei da- gya.
20954	အချင်းများ	အ ချင်း များ	a- chin: mja:
23732	အပ်ချုပ်ဆိုင်	အပ် ချုပ် ဆိုင်	a' chou' hsain
21033	အချုပ်ကျ	အ ချုပ် ကျ	a- chou' kya.
21846	အဒြ	အ ဒြ	a- da-ra
23568	အအိပ်အနေ	အ အိပ် အ နေ	a- ei' a- nei
23565	အအိပ်ဆတ်	အ အိပ် ဆတ်	a- ei' hsa'
23578	အအေးမိ	အ အေး မိ	a- ei: mi.
==========
```
## 7.[kill-all-detached.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/kill-all-detached.sh)  

ကုမ္ပဏီကြီးတွေမှာ၊ သုတေသနဌာနတွေမှာ အလုပ်လုပ်တဲ့အခါမှာ desktop, notebook ကနေ running server (e.g. cluster server, GPU server, Google cloud server ...) တစ်လုံးအထဲကို ကိုယ့် local terminal ကနေ login ဝင်ပြီးတော့မှ လုပ်ချင်တဲ့ experiment တွေကို run လေ့ရှိပါတယ်။ အထူးသဖြင့် machine learning ကိစ္စတွေ၊ neural network model ဆောက်တဲ့ ကိစ္စတွေကို notebook တို့၊ desktop တို့မှာ လုပ်လေ့မရှိကြပါဘူး။ အဲဒီလို သုံးတဲ့အခါမှာ လုပ်စရာရှိတဲ့အလုပ်တွေကို server မှာ run ထားပြီးတော့ terminal ကနေ ထွက်လိုက်ရင်တောင်၊ ကိုယ့် local စက်ကို shutdown လုပ်လိုက်ရင်တောင်၊ server မှာ run ထားခဲ့တဲ့ ပရိုဂရမ်တွေက ဆက်လက် run နေပြီးတော့ အဲဒီ output screen တွေကိုလည်း လက်ရှိရောက်နေတဲ့ နေရာကနေ အချိန်မရွေးပြန်ဝင်ရောက် ကြည့်ရှုနိုင်အောင် screen ဆိုတဲ့ command ကို သုံးကြပါတယ်။ ဒီ script ကတော့ အဲဒီ screen command ကို သုံးပြီး အလုပ်လုပ်တဲ့အခါမှာ ကြုံရတတ်တဲ့ အလုပ်တွေပြီးနေတာကသေချာပြီးတော့၊ ဝင်ကြည့်ဖို့လည်း မလိုအပ်တော့တဲ့ detached ဖြစ်နေတဲ့ screen တွေအားလုံးကိုရွေးသတ်ဖို့အတွက် ရေးခဲ့တာပါ။ Attached ဖြစ်နေတဲ့ screen session တွေကိုတော့ kill မလုပ်ပဲ ချန်ထားခဲ့ပါလိမ့်မယ်။ ဒီ command ကို run မလုပ်ခင်မှာ detached ဖြစ်နေတဲ့ screen တွေက တကယ်တမ်း အသုံးဝင်မဝင်ကို check လုပ်ပြီးမှ၊ သေချာမှ run ပါလို့ သတိပေးချင်ပါတယ်။    

script ထဲက pipe နဲ့ ချိတ်ပြီး run ပြထားတဲ့ command တွေကို အောက်ပါအတိုင်း တစ်ခုချင်းဖြတ် run ပြထားပြီး၊ comment ပါရေးပေးထားတဲ့အတွက် linux command တွေနဲ့ ရင်းနှီးမှုမရှိတဲ့သူတွေအတွက်လည်း နားလည်ရလွယ်ပါလိမ့်မယ်။  

```bash

# လက်ရှိ attached ဖြစ်နေတဲ့၊ detached ဖြစ်နေတဲ့ screen တွေကို screen -ls command နဲ့ ကြည့်ကြည့်ပါတယ်။  
ka2pluskha2@y-Lab-1:~$ screen -ls
There are screens on:
        29273.pts-1.asr-proto-1 (10/22/2018 05:38:27 PM)        (Attached)
        29213.pts-1.asr-proto-1 (10/22/2018 05:36:14 PM)        (Detached)
        29175.pts-1.asr-proto-1 (10/22/2018 05:34:36 PM)        (Detached)
3 Sockets in /run/screen/S-ka2pluskha2.

# Detached ပါနေတဲ့ စာကြောင်းတွေကိုပဲ grep command နဲ့ ဆွဲထုတ်ပါတယ်။  
ka2pluskha2@y-Lab-1:~$ screen -ls | grep Detached
        29213.pts-1.asr-proto-1 (10/22/2018 05:36:14 PM)        (Detached)
        29175.pts-1.asr-proto-1 (10/22/2018 05:34:36 PM)        (Detached)

# field delimiter ကို dot အဖြစ်သတ်မှတ်ပြီးတော့ field နံပါတ် 1 (ပထမဆုံး ကော်လံ) ကိုပဲ cut command ကို သုံးပြီးတော့ဆွဲထုတ်ထားပါတယ် 
ka2pluskha2@y-Lab-1:~$ screen -ls | grep Detached | cut -d. -f1 
        29213
        29175

# sed command ကို သုံးပြီးတော့ ရှေ့ဆုံးမှာရှိနေတဲ့ TAB စာလုံးကို ဖျက်လိုက်ပါတယ်
ka2pluskha2@y-Lab-1:~$ screen -ls | grep Detached | cut -d. -f1 | sed 's/\t//' 
29213
29175

# xargs command နဲ့ ဝင်လာတဲ့ argument တစ်ခုချင်းစီကို kill command ကို သုံးပြီး session တွေကို သတ်ပစ်လိုက်ပါတယ်
ka2pluskha2@y-Lab-1:~$ screen -ls | grep Detached | cut -d. -f1 | sed 's/\t//' | xargs kill

# screen -ls နဲ့ ပြန်ပြီးတော့ confirm လုပ်ကြည့်တဲ့အခါမှာ detached ဖြစ်နေတဲ့ screen နှစ်ခုစလုံးကို kill လုပ်ပေးတာကို တွေ့ရပါလိမ့်မယ်
ka2pluskha2@y-Lab-1:~$ screen -ls
There is a screen on:
        29273.pts-1.asr-proto-1 (10/22/2018 05:38:27 PM)        (Attached)
1 Socket in /run/screen/S-ka2pluskha2.
```

## 8.[unzip-all-with-one-passwd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/unzip-all-with-one-passwd.sh) 

ကျွန်တော်နဲ့ ကျောင်းသားတွေအကြားမှာ ဖိုင်တွေ၊ ဒေတာတွေကို ပို့ကြတဲ့အခါမှာ password ခံပြီး၊ zip လုပ်ပြီးတော့ သုံးပါတယ်။ ဒီ shell script က ကျောင်းသူတစ်ယောက်ဆီက ပို့ပေးလိုက်တဲ့ zip ဖိုင်တွေအားလုံးကိုဖြေဖို့အတွက် password တွေကို အကြိမ်ကြိမ်အခါခါ ရိုက်ပေးရမှာကိုပျင်းလို့ ရေးခဲ့တာဖြစ်ပါတယ်။ နောက်တစ်ခုက zip ဖိုင်တဖိုင်စီက ဖိုင်တွေတော်တော်များများကို ချုံ့ထားတာမို့ တစ်ဖိုင်ချင်းစီ unzip လုပ်တာပြီးတာကို ထိုင်မစောင့်ချင်တာကြောင့်လည်း ပါပါတယ်။ zip ဖိုင်တွေအများကြီးကို တူတဲ့ password တစ်ခုတည်းကို သုံးပြီးတော့ ဖြေဖို့လိုအပ်လာတဲ့အခါမှာ အသုံးဝင်ပါလိမ့်မယ်။ နောက်ပြီးတော့ password ကို command line ကနေ ဖတ်တဲ့ပုံစံကိုလည်း bash ရဲ့ "read -s" ကိုလည်း သုံးပြထားပါတယ်။ ဒီ shell script ကို သုံးပုံသုံးနည်း ဥပမာကတော့ အောက်ပါအတိုင်းဖြစ်ပါတယ်။  

```
./unzip-all-with-one-passwd.sh *.zip
```

## 9.[cut-filename.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/cut-filename.sh)  

ဖိုင်တွေနဲ့ အလုပ်လုပ်တဲ့အခါမှာ ကျွန်တော်တို့က path မပါပဲ ဖိုင်နာမည်ကိုပဲလိုချင်တဲ့အခါမျိုး၊ extension မပါပဲ ဖိုင်နာမည်ကိုပဲ လိုချင်တဲ့အခါမျိုး၊ ဖိုင်ရဲ့ extension ကိုပဲ check လုပ်ချင်တဲ့ အခါမျိုး ရှိပါတယ်။ အဲဒီအတွက် ရေးထားခဲ့တဲ့ bash shell script ပါ။ သုံးပုံသုံးနည်း ဥပမာ ကတော့ အောက်ပါအတိုင်းပါ။  

```
lar@lar-air:~/tool/bash/4github/filename$ ./cut-filename.sh
usage: cut-filename <filename> [ -p | -np | -f | -e ]
here,
-p or --path for printing path only
-np or --no-path for printing filename without path
-f or --filename for filename without extension
-e or --extension for file extension without name

lar@lar-air:~/tool/bash/4github/filename$ ./cut-filename.sh /home/lar/tool/bash/4github/filename/hello-word.c -p
/home/lar/tool/bash/4github/filename

lar@lar-air:~/tool/bash/4github/filename$ ./cut-filename.sh /home/lar/tool/bash/4github/filename/hello-word.c -np
hello-word.c

lar@lar-air:~/tool/bash/4github/filename$ ./cut-filename.sh /home/lar/tool/bash/4github/filename/hello-word.c -f
/home/lar/tool/bash/4github/filename/hello-word

lar@lar-air:~/tool/bash/4github/filename$ ./cut-filename.sh /home/lar/tool/bash/4github/filename/hello-word.c -e  

```  

## 10.[calc-avg.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/calc-avg.sh)  

ဖိုင်ထဲမှာ ကော်လံတစ်ခုအနေနဲ့ ရှိနေတဲ့ ဂဏန်းတွေအားလုံးရဲ့ ပျှမ်းမျှတန်ဖိုးကို တွက်ထုတ်ဖို့အတွက် ရေးခဲ့ပါတယ်။  

```
$ cat ./no-of-files.txt 
454
337
306
383
345
319
341
297
280
333

$ ./calc-avg.sh ./no-of-files.txt 
33.95
```

## 11.[print-latex-section.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-latex-section.sh)  

International conference စာတမ်းတွေကို အများသောအားဖြင့် latex နဲ့ရေးကြပါတယ်။ အဲဒီလိုရေးထားတဲ့ latex source ဖိုင်ကနေ \section{}, \subsection{} နဲ့ \subsubsection{} tag တွေနဲ့ ရေးထားတဲ့ ခေါင်းစဉ်တွေကို အစဉ်လိုက်ဆွဲထုတ်ဖို့အတွက် ရေးထားတဲ့ script ပါ။  

```
lar@lar-air:~/paper/ona2018/paper/nov23ver1$ ./print-latex-section.sh ./ona.tex 
Introduction
MT for Sign Language
MSL and Myanmar Language
Corpus Preparation
Segmentation
|--Word Segmentation
|--Syllable Segmentation
|--SentencePiece
|--Byte-Pair-Encoding
Experimental Methodology
|--Phrase-based Statistical Machine Translation (PBSMT)
|--Encoder-Decoder Models for NMT
    |----Stacked Recurrent Neural Network (RNN) with Attention
    |----Self-attentional Transformer
    |----Fully Convolutional Models (ConvSeq2Seq)
Experiments
|--Corpus statistics
|--Moses SMT system
|--Framework for NMT
|--Training Details
|--Evaluation
Result and Discussion
Error Analysis on NMT Approaches
Conclusion
```

## 12.[list-mistake-5-suggestion.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/list-mistake-5-suggestion.sh)  

ပေးလိုက်တဲ့ text ဖိုင်ထဲမှာ ရိုက်ထားတဲ့ အင်္ဂလိပ်စာ စာလုံးပေါင်း အမှားတွေနဲ့ ဖြစ်နိုင်ချေရှိတဲ့ spelling suggestion စာလုံး ၅လုံးကို ဘေးချင်းယှဉ် တွဲရိက်ပြပေးဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ။ မှားတဲ့ စာလုံးဘေးမှာရှိနေတဲ့ နံပါတ် ၂ခုအနက် ပထမ နံပါတ်ကတော့ spelling suggestion အဖြစ်ထုတ်ပေးနိုင်တဲ့ စာလုံးအရေအတွက်ကို ဆိုလိုပြီး၊ ဒုတိယနံပါတ်ကတော့ စာလုံးပေါင်းမှားနေတဲ့စာလုံးက စာကြောင်းရဲ့ စာလုံးရေ (i.e. character) ဘယ်နှစ်လုံးမြောက်မှာ ရှာတွေ့တယ်လို့ ဖော်ပြနေတာဖြစ်ပါတယ်။ 

```
lar@lar-air:~/tool/bash/spell$ cat mistakes.txt 
I use to shop at that market.
The doctor will advice you.
How are yuo?
Yes, I am doing NLP research.
This year, I visited Banmaw.
We got better BLEU scores for Myanmar-English machine translation.

lar@lar-air:~/tool/bash/spell$ ./list-mistake-5-suggestion.sh mistakes.txt 
yu|||7 8|||you, yo, Yugo, yup, yuk
NL|||5 16|||LP, NP, NAP, NIP, ALP
Banma|||43 21|||Ban maw, Ban-maw, Banal, Barnum, Bantam
BLE|||6 14|||BLUE, BL EU, BL-EU, BLU, BLEW
```
## 13.[mytxt2pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytxt2pdf.sh)  

မြန်မာစာ စာကြောင်းတွေပါနေတဲ့ text ဖိုင်ကို linux command line tool တွေကို သုံးပြီးတော့ PDF အဖြစ်ပြောင်းတဲ့ အခါမှာ  
မြန်မာစာ စာလုံးတွေကို မှန်မှန်ကန်ကန် မပြသပေးနိုင်တာမျိုးကို ကြုံရပါလိမ့်မယ်။  

အဲဒီအတွက် pandoc ကို သုံးပြီးတော့ သူ့ရဲ့ option တွေဖြစ်တဲ့  
--variable mainfont="Myanmar3" နဲ့ --latex-engine=xelatex ကို တွဲသုံးပြီးတော့  
မြန်မာစာ စာလုံးတွေကို မှန်မှန်ကန်ကန် PDF ဖိုင် output မှာ ပြသပေးနိုင်အောင် ရေးထားတဲ့ bash shell script တစ်ပုဒ်ပါ။  
pandoc က ကိုယ်သုံးနေတဲ့ စက်ထဲမှာ မရှိသေးဘူးဆိုရင်တော့ install လုပ်ရပါလိမ့်မယ်။  

```
$ ./mytxt2pdf.sh reply.txt output.pdf
```

text ဖိုင်ကနေ pdf ဖိုင်ကို ပြောင်းတဲ့အခါမှာ ဘယ်လို error တွေကြုံရသလဲ ဆိုတာနဲ့ပတ်သက်ပြီးတော့  
အသေးစိတ်ကို လေ့လာချင်သူများက ကျွန်တော်ရဲ့ error-overflow repository အောက်မှာ ရှင်းပြထားတာကို ဖတ်ကြည့်ပါ။  
[myanmar-text-to-pdf-conversion-error](https://github.com/ye-kyaw-thu/error-overflow/blob/master/myanmar-text-to-pdf-conversion-error.md)  

## 14.[prepare-open-test-data.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/prepare-open-test-data.sh)  

မော်ဒယ် မဆောက်ခင်မှာ ရှိပြီးသားဒေတာတွေထဲကနေ training data နဲ့ open-test data အဖြစ်ခွဲရပါတယ်။ open-test data ဆိုတာက training လုပ်စဉ်မှာ သုံးထားတဲ့ ဒေတာနဲ့ မတူတဲ့ဒေတာ ကို ဆိုလိုတာပါ။ အဲဒီ ဖယ်ထားတဲ့ open-test ဒေတာကိုသုံးပြီးတော့၊ ဆောက်ထားပြီးသားမော်ဒယ်ကို input လုပ်ပြီး၊ မော်ဒယ်က သူမမြင်ဖူးသေးတဲ့ ဒေတာနဲ့ တွေ့တဲ့အခါမှာ ကောင်းကောင်း classification (တကယ်လို့ လုပ်တဲ့ experiment က classification ဆိုရင်) လုပ်ပေးနိုင်သလားဆိုတာကို confirmation လုပ်ဖို့အတွက်ပါ။  

[prepare-open-test-data.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/prepare-open-test-data.sh) က အဲဒီလိုမျိုး ဒေတာပြင်ဆင်ဖို့ကိစ္စတစ်ခုအတွက် သုံးခဲ့တဲ့ shell script ပါ။  

ဥပမာ။။ ကျွန်တော်တို့မှာ အောက်ပါအတိုင်း ပန်းအမျိုးအစား ၁၇မျိုးနဲ့ ပတ်သတ်တဲ့ ပုံဒေတာတွေကို အောက်ပါဖိုလ်ဒါတွေအတိုင်းခွဲသိမ်းထားတယ် ဆိုပါစို့   

```bash
ye@server1:~/exp/tl/flower-recognition/dataset/train-flower$ tree -L 1
.
├── bluebell
├── buttercup
├── coltsfoot
├── cowslip
├── crocus
├── daffodil
├── daisy
├── dandelion
├── fritillary
├── iris
├── lilyvalley
├── pansy
├── snowdrop
├── sunflower
├── tigerlily
├── tulip
└── windflower
```

အဲဒီ ဖိုလ်ဒါ (flower class တွေပေါ့) တစ်ခုချင်းစီရဲ့ အထဲမှာလည်း image ဖိုင်တွေက အများကြီးရှိနေမှာဖြစ်ပါတယ်။  
မြင်သာအောင် ဥပမာအနေနဲ့ ပြရရင် အောက်ပါအတိုင်း ရှိတာမျိုးပါ။  

```bash
.
├── bluebell
│   ├── image_0002.jpg
│   ├── image_0006.jpg
│   ├── image_0017.jpg
│   ├── image_0030.jpg
│   ├── image_0071.jpg
...
...
...
├── buttercup
│   ├── image_0021.jpg
│   ├── image_0031.jpg
│   ├── image_0043.jpg
│   ├── image_0053.jpg
│   ├── image_0062.jpg
...
...
...
```

အဲဒီ ရှိနေတဲ့ class ဖိုလ်ဒါအသီးသီးထဲက ပုံတချို့ကို ခွဲထုတ်ပြီး (linux command အနေနဲ့ဆိုရင် mv လုပ်တာပါ) open-test ဒေတာအဖြစ်ပြင်ဆင်ဖို့အတွက် သုံးမှာဖြစ်ပါတယ်။ ကိုယ်စက်ထဲမှာ run မလုပ်ခင်မှာ script ထဲက path တွေကို ကိုယ်ဒေတာရှိတဲ့ path, open-test data ကို သိမ်းပေးစေချင်တဲ့ path တွေနဲ့ change ပြီးမှ အသုံးပြုရမှာ ဖြစ်ပါတယ်။  

## 15.[print-CRLF.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-CRLF.sh)

NLP အလုပ်တွေအတွက် ဒေတာတွေကို ပြင်ဆင်တဲ့အခါမှာ အကြောင်းအမျိုးမျိုးကြောင့် ဖိုင်ထဲမှာ ဝင်းဒိုးက စာကြောင်းတွေလည်း ရောပါနေတတ်ပါတယ်။  
file command နဲ့ check လုပ်ရင်အောက်ပါအတိုင်း Linux ရဲ့ စာကြောင်းတစ်ကြောင်းဆုံးတဲ့ အမှတ်အသားစာကြောင်းတွေဖြစ်တဲ့ LF (Line Feed) သာ မကပဲ CRLF (Carriage Return and Line Feed) စာကြောင်းတွေလည်း ပါဝင်နေကြောင်းကို ပြသပေးပါလိမ့်မယ်။  

```bash
$ file ./lf-crlf.txt
./lf-crlf.txt: UTF-8 Unicode text, with CRLF, LF line terminators

```
print-CRLF.sh shell script က အဲဒီလိုမျိုး ဖိုင်တွေထဲကနေ ဘယ်လိုင်းနံပါတ်တွေက CRLF ပါနေသလဲဆိုတာကို grep နဲ့ ဆွဲထုတ်ဖို့အတွက် ရေးပြထားတာပါ။ အောက်ပါအတိုင်း example အနေနဲ့ သုံးပြထားပါတယ်။ [lf-crlf.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/lf-crlf.txt) ဖိုင်ကိုလည်း တင်ပေးထားပါတယ်။  

အရင်ဆုံး lf-crf.txt ဖိုင်ကို cat နဲ့ စာကြောင်းတစ်ကြောင်းစီ ရိုက်ထုတ်ခိုင်းကြည့်ရအောင်။  

```bash
$ cat ./lf-crlf.txt 
လင်းနစ်စာကြောင်း
Windows စာကြောင်းပါ။
ဒီစာကြောင်းကလည်း Windows စာကြောင်းပါ။
ဒီစာကြောင်းကလည်း Windows စာကြောင်းပါ။
Linux line break နဲ့ ဖြတ်ထားတဲ့ စာကြောင်းပါ။
Linux line break နဲ့ ဖြတ်ထားတဲ့ စာကြောင်းပါ။
Linux line break နဲ့ ဖြတ်ထားတဲ့ စာကြောင်းပါ။
ဒီစာကြောင်းကလည်း Windows စာကြောင်းပါ။
```
ပုံမှန်အားဖြင့်က cat command နဲ့ ရိုက်ကြည့်တာမျိုး၊ gedit text editor နဲ့ ဖွင့်ကြည့်တာမျိုးနဲ့က ဘယ်စာကြောင်းက CRLF ကို သုံးထားတာလဲ၊ LF ကိုပဲသုံးထားတာလဲ ဆိုတာကို အထက်ပါအတိုင်း မမြင်နိုင်ပါဘူး။ vi editor သို့မဟုတ် emacs editor တွေကို သုံးပြီးကြည့်မှသာ မြင်ရပါလိမ့်မယ်။  

<p align="center"> 
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/CRLF-eg.png" alt="" width="482x304"/>
</p>
<p align="center"> Fig. emacs editor can display ^M (i.e. CR) symbols </p>  

./print-CRLF.sh ပရိုဂရမ်နဲ့ CRLF နဲ့ အဆုံးသတ်ထားတဲ့ စာကြောင်းတွေကိုပဲ ဆွဲထုတ်ကြည့်ရအောင်။ ရှေ့ဆုံးက နံပါတ်တွေက လိုင်းနံပါတ်တွေဖြစ်ပါတယ်။  

```bash
$ ./print-CRLF.sh ./lf-crlf.txt 
2:Windows စာကြောင်းပါ။
3:ဒီစာကြောင်းကလည်း Windows စာကြောင်းပါ။
4:ဒီစာကြောင်းကလည်း Windows စာကြောင်းပါ။
8:ဒီစာကြောင်းကလည်း Windows စာကြောင်းပါ။
```

## 16.[group-files.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-files.sh)  

လက်ရှိ path အောက်မှာ ဖိုလ်ဒါ နှစ်ခု (1/, 2/) ရှိပြီးတော့

```bash
$ ls
1  2  group-files.sh
```

ဖိုလ်ဒါ 1/ နဲ့ ဖိုလ်ဒါ 2/ ရဲ့အောက်မှာ ပုံဖိုင် ၂၀ စီ အသီးသီးရှိတယ်။

``` bash
$ ls ./1
2018-11-12-13:34:46.16khz.mono.jpg  2018-11-12-13:35:48.16khz.mono.jpg  2018-11-12-13:36:58.16khz.mono.jpg  2018-11-12-13:37:55.16khz.mono.jpg
2018-11-12-13:34:55.16khz.mono.jpg  2018-11-12-13:35:50.16khz.mono.jpg  2018-11-12-13:37:31.16khz.mono.jpg  2018-11-12-13:38:43.16khz.mono.jpg
2018-11-12-13:35:04.16khz.mono.jpg  2018-11-12-13:35:52.16khz.mono.jpg  2018-11-12-13:37:33.16khz.mono.jpg  2018-11-12-13:38:47.16khz.mono.jpg
2018-11-12-13:35:12.16khz.mono.jpg  2018-11-12-13:35:54.16khz.mono.jpg  2018-11-12-13:37:45.16khz.mono.jpg  2018-11-12-13:38:50.16khz.mono.jpg
2018-11-12-13:35:46.16khz.mono.jpg  2018-11-12-13:36:20.16khz.mono.jpg  2018-11-12-13:37:52.16khz.mono.jpg  2018-11-12-13:38:54.16khz.mono.jpg

$ ls ./2
2018-11-12-14:15:52.16khz.mono.jpg  2018-11-12-14:16:30.16khz.mono.jpg  2018-11-12-14:17:15.16khz.mono.jpg  2018-11-12-14:17:31.16khz.mono.jpg
2018-11-12-14:15:56.16khz.mono.jpg  2018-11-12-14:16:34.16khz.mono.jpg  2018-11-12-14:17:18.16khz.mono.jpg  2018-11-12-14:17:34.16khz.mono.jpg
2018-11-12-14:16:00.16khz.mono.jpg  2018-11-12-14:16:39.16khz.mono.jpg  2018-11-12-14:17:21.16khz.mono.jpg  2018-11-12-14:17:36.16khz.mono.jpg
2018-11-12-14:16:22.16khz.mono.jpg  2018-11-12-14:17:09.16khz.mono.jpg  2018-11-12-14:17:26.16khz.mono.jpg  2018-11-12-14:17:58.16khz.mono.jpg
2018-11-12-14:16:28.16khz.mono.jpg  2018-11-12-14:17:12.16khz.mono.jpg  2018-11-12-14:17:29.16khz.mono.jpg  2018-11-12-14:18:01.16khz.mono.jpg
```
ဖိုင် ၅ဖိုင်စီကို ဖိုလ်ဒါ တစ်ခုစီအောက်မှာ ကော်ပီကူးပြီးသိမ်းချင်ရင် option ကို 5 ပေးပြီး run ပါ။  

``` bash
$ ./group-files.sh 5
```
Run ပြီးသွားတဲ့အခါမှာ ဖိုလ်ဒါ 1/ ရဲ့ အောက်မှာ အောက်ပါအတိုင်း ဖိုလ်ဒါ လေးခု (1_1/, 1_2/, 1_3/, 1_4/) အသစ်ဖွဲ့ပေးထားတာကို တွေ့ရှိရပါလိမ့်မယ်။  

```bash
$ ls ./1
1_1                                 2018-11-12-13:35:04.16khz.mono.jpg  2018-11-12-13:35:54.16khz.mono.jpg  2018-11-12-13:37:52.16khz.mono.jpg
1_2                                 2018-11-12-13:35:12.16khz.mono.jpg  2018-11-12-13:36:20.16khz.mono.jpg  2018-11-12-13:37:55.16khz.mono.jpg
1_3                                 2018-11-12-13:35:46.16khz.mono.jpg  2018-11-12-13:36:58.16khz.mono.jpg  2018-11-12-13:38:43.16khz.mono.jpg
1_4                                 2018-11-12-13:35:48.16khz.mono.jpg  2018-11-12-13:37:31.16khz.mono.jpg  2018-11-12-13:38:47.16khz.mono.jpg
2018-11-12-13:34:46.16khz.mono.jpg  2018-11-12-13:35:50.16khz.mono.jpg  2018-11-12-13:37:33.16khz.mono.jpg  2018-11-12-13:38:50.16khz.mono.jpg
2018-11-12-13:34:55.16khz.mono.jpg  2018-11-12-13:35:52.16khz.mono.jpg  2018-11-12-13:37:45.16khz.mono.jpg  2018-11-12-13:38:54.16khz.mono.jpg
```
ထိုနည်းလည်းကောင်း ဖိုလ်ဒါ 2/  ရဲ့အောက်မှာလည်း ဖိုလ်ဒါ လေးခု (2_1/, 2_2/, 2_3/, 2_4/) အသစ်ဖွဲ့ပေးထားတာကို တွေ့ရပါလိမ့်မယ်။  

```bash
$ ls ./2
2018-11-12-14:15:52.16khz.mono.jpg  2018-11-12-14:16:30.16khz.mono.jpg  2018-11-12-14:17:15.16khz.mono.jpg  2018-11-12-14:17:31.16khz.mono.jpg  2_1
2018-11-12-14:15:56.16khz.mono.jpg  2018-11-12-14:16:34.16khz.mono.jpg  2018-11-12-14:17:18.16khz.mono.jpg  2018-11-12-14:17:34.16khz.mono.jpg  2_2
2018-11-12-14:16:00.16khz.mono.jpg  2018-11-12-14:16:39.16khz.mono.jpg  2018-11-12-14:17:21.16khz.mono.jpg  2018-11-12-14:17:36.16khz.mono.jpg  2_3
2018-11-12-14:16:22.16khz.mono.jpg  2018-11-12-14:17:09.16khz.mono.jpg  2018-11-12-14:17:26.16khz.mono.jpg  2018-11-12-14:17:58.16khz.mono.jpg  2_4
2018-11-12-14:16:28.16khz.mono.jpg  2018-11-12-14:17:12.16khz.mono.jpg  2018-11-12-14:17:29.16khz.mono.jpg  2018-11-12-14:18:01.16khz.mono.jpg
```

## 17.[segmentation.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/segmentation.sh)

ဆိုကြပါစို့ thai.txt ဆိုတဲ့ဖိုင်ထဲမှာ တချို့ ထိုင်းစာကြောင်းတွေက စာလုံးမဖြတ်ထား (word segmentation မလုပ်ထား) တဲ့အခြေအနေ။  

```bash
$ cat ./thai.txt
ค่า|โดย|สา|รไ|ปเ|ทอ|ร์ม|ิน|อล|เท่|าไ|หร|่?
นี่|คือ|ใบรับรอง|การลงทะเบียน|และ|ใบเสร็จรับเงิน|ค่า|เล่า|เรียน
ฉัน|ไม่ชอบ|ว่ายน้ำ
คุณสามารถลงไปที่แม่น้ำโดยเรือถ้าคุณต้องการ
นักวิทยาศาสตร์ได้พัฒนาหุ่นยนต์เลียนแบบลักษณะทางกายภาพของสัตว์ครึ่งบกครึ่งน้ำประเภทปลาหมึกชนิดหนึ่ง ซึ่งสามารถทำงานได้ทังบนบกและใต้ทะเล
ฉัน|เข้าใจ
ฉันไม่เข้าใจ
เธอ|พูด|อังกฤษ|ไห|ม?
คุณชอบทำอะไร
คุณพูดภาษาพม่าไหม
```

./segmentation.sh ပရိုဂရမ်က ./thai.txt ဖိုင်ထဲမှာ ရှိတဲ့စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီဖတ်ယူပြီး၊ "|" မပါတဲ့ စာကြောင်းတွေဆိုရင် thai word segmentation လုပ်ပေးတဲ့ ပရိုဂရမ်ကို လက်ဆင့်ကမ်းပြီးတော့ စာလုံးဖြတ်ခိုင်းပါလိမ့်မယ်။  

```bash
$ ./segmentation.sh ./thai.txt 
ค่า|โดย|สา|รไ|ปเ|ทอ|ร์ม|ิน|อล|เท่|าไ|หร|่?
นี่|คือ|ใบรับรอง|การลงทะเบียน|และ|ใบเสร็จรับเงิน|ค่า|เล่า|เรียน
ฉัน|ไม่ชอบ|ว่ายน้ำ
คุณ|สามารถ|ลง|ไป|ที่|แม่น้ำ|โดย|เรือ|ถ้า|คุณ|ต้องการ
นักวิทยาศาสตร์|ได้|พัฒนา|หุ่นยนต์|เลียนแบบ|ลักษณะ|ทางกายภาพ|ของ|สัตว์ครึ่งบกครึ่งน้ำ|ประเภท|ปลาหมึก|ชนิด|หนึ่ง| |ซึ่ง|สามารถ|ทำงาน|ได้|ทัง|บนบก|และ|ใต้|ทะเล
ฉัน|เข้าใจ
ฉัน|ไม่|เข้าใจ
เธอ|พูด|อังกฤษ|ไห|ม?
คุณ|ชอบ|ทำ|อะไร
คุณ|พูด|ภาษา|พม่า|ไหม
```
[thai.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/thai.txt) ဖိုင်ကိုတော့ တင်ပေးထားပါတယ်။  
ထိုင်းစာလုံးဖြတ်ပေးတဲ့ ပရိုဂရမ်ကိုတော့ တင်မထားပါဘူး။  

## 18.[split-even-odd-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/split-even-odd-pdf.sh) 

ပြည်ထောင်စုသမ္မတမြန်မာနိုင်ငံတော် ဖွဲ့စည်းပုံအခြေခံဥပဒေ (၂၀၀၈ ခုနှစ်) PDF ဖိုင်မှာ အင်္ဂလိပ်စာ စာမျက်နှာပြီးရင်၊ မြန်မာလို ရေးထားတဲ့ မြန်မာစာမျက်နှာ ဆိုပြီး တလှည့်စီပါနေပါတယ်။ တနည်းအားဖြင့် မ ဂဏန်း စာမျက်နှာ (odd pages) တွေက အင်္ဂလိပ်စာ၊ စုံ ဂဏန်း စာမျက်နှာ (even pages) တွေက မြန်မာစာပါ။ အဲဒီ PDF ဖိုင်ထဲကနေ မ ဂဏန်းစာမျက်နှာတွေကို တစ်ဖိုင်၊ စုံ ဂဏန်းစာမျက်နှာတွေကို တဖိုင်စီ သပ်သပ် ခွဲသိမ်းဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ။ Example running ကတော့ အောက်ပါအတိုင်းပါ။  

```bash
$ ./split-even-odd-pdf.sh ./myanmarconstitution2008mm.pdf 
Total pages in your PDF file: 424
No. of pages of odd.pdf:  212
No. of pages of even.pdf:  212
```
စုံ ဂဏန်းစာမျက်နှာတွေချည်းပဲ စုထားတဲ့ ဖိုင်ကိုတော့ even.pdf ဆိုတဲ့ ဖိုင်နာမည်နဲ့ သိမ်းပေးမှာဖြစ်ပြီး၊  
မ ဂဏန်းစာမျက်နှာတွေချည်းပဲ စုထားတဲ့ ဖိုင်ကိုတော့ odd.pdf ဖိုင်နာမည်နဲ့ သိမ်းပေးသွားမှာဖြစ်ပါတယ်။  
myanmarconstitution2008mm.pdf ဖိုင်ကလည်း နဂိုအတိုင်းပဲ ကျန်နေပါလိမ့်မယ်။  

## 19. [even-odd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/even-odd.sh)  

[mistake-pair.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/mistake-pair.txt) ဖိုင်ထဲမှာ စာလုံးပေါင်းအမှားတွေနဲ့ အမှန်စာလုံးတွေကို အပေါ်အောက်ဆင့်ရိုက်ထားတယ်ဆိုပါစို့။  

```bash
$ cat -n ./mistake-pair.txt 
     1	တေကိုတိုင်
     2	တွေကိုယ်တိုင်​
     3	အရည်အတွက်
     4	အရေအတွက်
     5	ဈေူကွက်
     6	ဈေးကွက်
     7	ဆ်ုလိုတာ
     8	ဆိုလိုတာ
     9	လူးကြီး
    10	လူကြီး
```

odd line no. စာကြောင်းတွေကိုပဲ print ထုတ်ခိုင်းချင်တဲ့အခါမှာ ဖိုင်နာမည် argument ရဲ့ အနောက်မှာ odd လို့ ရိုက်ထည့်ပြီး argument ပေးပါ။  

```bash
$ ./even-odd.sh ./mistake-pair.txt odd 
တေကိုတိုင်
အရည်အတွက်
ဈေူကွက်
ဆ်ုလိုတာ
လူးကြီး
```

even line no. စာကြောင်းတွေကိုပဲ print ထုတ်ပေးစေချင်တဲ့ အခါမှာ ဒုတိယ argument ကို even လို့ပေးပါ။  

```bash
$ ./even-odd.sh ./mistake-pair.txt even
တွေကိုယ်တိုင်​
အရေအတွက်
ဈေးကွက်
ဆိုလိုတာ
လူကြီး
```
[even-odd.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/even-odd.sh) ပရိုဂရမ်မှာ အောက်ပါအတိုင်း sed ရဲ့ n (next) နဲ့ p (print) ကို သုံးထားပါတယ်။  

```
# even line တွေကို ရိုက်ထုတ်ပေးဖို့အတွက် 
sed -n 'n;p' $1;

# odd line တွေကို ရိုက်ထုတ်ပေးဖို့အတွက်
sed -n 'p;n' $1;
```

## 20. [rm-stopwords.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-stopwords.sh)  

ဆိုကြပါစို့ ကျွန်တော်တို့ ရဲ့ corpus က [my-test.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/rm-stopwords/my-text.txt) ဖိုင်ဖြစ်ပြီး အဲဒီထဲမှာ word segmentation လုပ်ထားပြီးသား စာကြောင်း ၁၂ ကြောင်းရှိတယ်။  

```bash
ကျွန်တော် နဲ့ သူ နဲ့ က သူငယ်ချင်း တွေ ပါ ။
ကျွန်မ မ သွား ဘူး ။
သူငယ်ချင်း အတွက် ဆို အကုန် လုပ်ပေး တယ် ။
သူမ ရဲ့ နဖူး မှာ မှဲ့ အကြီးကြီး ရှိ ပါ တယ် ။
သူမ ကို မ တွေ့ ဖူး ပါ ။
သူ နဲ့ သူမ က ချစ်သူ တွေ ဖြစ် ခဲ့ ကြ တယ် ။
သူ သာ ဆိုရင် သေချာတယ် အောင်မြင် မှာ ။
သူမ မှာ ကွန်ပျူတာ မ ရှိ ဘူး ။
ကျွန်တော် ကောင်းကောင်း သိ နေ တာ က အလုပ် ကြိုးစား တယ် ဆိုတာ လူ တိုင်း မ လုပ် နိုင် ပါ ။
သူ က သူ့ အလုပ် ကို ချစ် တယ် ။
ကျွန်တော် နဲ့ သူ
သူ
```
NLP တချို့ အလုပ်တွေအတွက် အသုံးများတဲ့ စာလုံးတွေ၊ စာကြောင်းတွေ အများစုမှာ ထပ်ခါထပ်ခါ ပါနေတဲ့ စာလုံးတွေ (အင်္ဂလိပ်လိုက stop words လို့ ခေါ်) ကို ဖယ်ဖို့ လိုအပ်ပါတယ်။ အဲဒီအတွက် ကျွန်တော်တို့က stopwords တွေကို စုထားပြီးသား ဆိုပါစို့။ ဥပမာ အနေနဲ့ stopwords  ၁၂လုံးကို [stopwords.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/rm-stopwords/stopwords.txt) ဖိုင်ထဲမှာ သိမ်းပေးထားတယ်။  

```bash
$ cat ./stopwords.txt 
ကျွန်တော်
ကျွန်မ
သူ
သူမ
ကို
မှာ
ရဲ့
အတွက်
နဲ့
ဆိုရင်
ဆိုတာ
က
```

[rm-stopwords.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-stopwords.sh) ပရိုဂရမ်ကိုသုံးပြီးတော့ stop word တွေကို ဖယ်ကြည့်ရအောင်။ (ဒီနေရာမှာ stop word ဖိုင်မှာက စာလုံး ၁၂လုံး၊ corpus ဖိုင်ဖြစ်တဲ့ my-text.txt ဖိုင်မှာကလည်း စာကြောင်း ၁၂ကြောင်း ဖြစ်နေတာက တိုက်ဆိုင်တာပါ။ ခင်ဗျားတို့ stop word ကိုလည်း ကြိုက်သလောက် ထားလို့ရတယ်။ corpus ကလည်း စာကြောင်းရေး သန်းနဲ့ချီရှိရင်လည်း အိုကေပါတယ်။)  

```bash
$ ./rm-stopwords.sh ./stopwords.txt ./my-text.txt
     သူငယ်ချင်း တွေ ပါ ။
 မ သွား ဘူး ။
သူငယ်ချင်း  ဆို အကုန် လုပ်ပေး တယ် ။
  နဖူး  မှဲ့ အကြီးကြီး ရှိ ပါ တယ် ။
  မ တွေ့ ဖူး ပါ ။
    ချစ်သူ တွေ ဖြစ် ခဲ့ ကြ တယ် ။
 သာ  သေချာတယ် အောင်မြင်  ။
  ကွန်ပျူတာ မ ရှိ ဘူး ။
 ကောင်းကောင်း သိ နေ တာ  အလုပ် ကြိုးစား တယ်  လူ တိုင်း မ လုပ် နိုင် ပါ ။
  သူ့ အလုပ်  ချစ် တယ် ။
  

```

coding နဲ့ ပတ်သက်ပြီး ရှင်းပြရရင် အင်္ဂလိပ်စာအတွက်သာ ဆိုရင် ```\<```, ```\>``` သို့မဟုတ် ```\b``` လို regular expression word boundary သင်္ကေတတွေကို သုံးပြီး အလွယ်တကူ stop word တွေကိုပဲ အတိအကျရွေးဖျက်လို့ ရပါတယ်။ ကျွန်တော်တို့ မြန်မာစာအတွက် က အဲဒီ word boundary marker တွေက လိုချင်တဲ့ပုံစံအတိုင်း အလုပ်မလုပ်ပေးနိုင်ပါဘူး။ Unicode အတွက် သတ်မှတ်ထားတဲ့ word boundary marker ```\b{w}``` နဲ့ POSIX word boundary markers တွေဖြစ်တဲ့ ```[[:<:]]``` နဲ့ ```[[:>:]]``` တွေကိုလည်း သုံးကြည့်ခဲ့ပေမယ့် ကျွန်တော်က ``` sed -e "$(sed "s:.*:s/&//ig:" $stopwordFile.tmp)" $corpusFile.tmp | sed 's/<|\||>//g' ``` လိုမျိုး sed command တစ်ခုရဲ့ output ကို နောက်ထပ် sed command တစ်ခုကို ထပ် parsing လုပ်တာကြောင့် အဆင်မပြေတဲ့ အပိုင်းတွေရှိပါတယ်။ အဲဒါကြောင့် ကိုယ်ဖာသာကိုယ် word boundary တစ်ခု သတ်မှတ်ပြီး၊ search လုပ်ပြီး မဖျက်ခင်မှာ အဲဒီ စာလုံးအစ boundary marker```<|``` နဲ့ စာလုံးအဆုံး boundary marker ```|>``` တွေကို stop word ဖိုင်မှာရော corpus ဖိုင်မှာရော အရင်ဆုံး ဝင်ရေးပါတယ်။ ပြီးတော့မှ stop word ဖိုင်ထဲက စာလုံးတွေကို corpus ဖိုင်မှာ ရှာဖျက်ပါတယ်။ ဖျက်ပြီးတဲ့အခါမှာ corpus ဖိုင်ထဲက စောစောက ကျွန်တော် သတ်မှတ်ထားခဲ့တဲ့ word boundary marker တွေကို ဝင်ရှင်းပြီးမှ stop word ဖယ်ထားပြီးသား output အနေနဲ့ screen မှာ ရိုက်ထုတ်ပြပေးပါတယ်။  

မြင်သာအောင် အောက်ပါ လုပ်သွားပုံ အဆင့်ဆင့်ကို လေ့လာကြည့်ပါ။  
ရှာပြီး မဖျက်ခင်မှာ stopwords.txt ဖိုင်ထဲမှာ ရှိနေတဲ့ စာလုံးအားလုံးကို word boundary ဝင်ဖြည့်ပါတယ်။ ပြီးတော့ temp ဖိုင်အဖြစ်သိမ်းထားခဲ့ပါတယ်။  

```bash
$ cat ./stopwords.txt.tmp 
<|ကျွန်တော်|>
<|ကျွန်မ|>
<|သူ|>
<|သူမ|>
<|ကို|>
<|မှာ|>
<|ရဲ့|>
<|အတွက်|>
<|နဲ့|>
<|ဆိုရင်|>
<|ဆိုတာ|>
<|က|>
```

ထိုနည်းလည်းကောင်း corpus ဖိုင်အဖြစ် example ပြထားတဲ့ my-text.txt ဖိုင်ကိုလည်း word boundary ကို ဝင်ဖြည့်ပြီးတော့ temp ဖိုင်အဖြစ်သိမ်းခဲ့ပါတယ်။ အဲဒီ temp ဖိုင်ကို cat လုပ်ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```bash
$ cat ./my-text.txt.tmp
<|ကျွန်တော်|> <|နဲ့|> <|သူ|> <|နဲ့|> <|က|> <|သူငယ်ချင်း|> <|တွေ|> <|ပါ|> <|။|>
<|ကျွန်မ|> <|မ|> <|သွား|> <|ဘူး|> <|။|>
<|သူငယ်ချင်း|> <|အတွက်|> <|ဆို|> <|အကုန်|> <|လုပ်ပေး|> <|တယ်|> <|။|>
<|သူမ|> <|ရဲ့|> <|နဖူး|> <|မှာ|> <|မှဲ့|> <|အကြီးကြီး|> <|ရှိ|> <|ပါ|> <|တယ်|> <|။|>
<|သူမ|> <|ကို|> <|မ|> <|တွေ့|> <|ဖူး|> <|ပါ|> <|။|>
<|သူ|> <|နဲ့|> <|သူမ|> <|က|> <|ချစ်သူ|> <|တွေ|> <|ဖြစ်|> <|ခဲ့|> <|ကြ|> <|တယ်|> <|။|>
<|သူ|> <|သာ|> <|ဆိုရင်|> <|သေချာတယ်|> <|အောင်မြင်|> <|မှာ|> <|။|>
<|သူမ|> <|မှာ|> <|ကွန်ပျူတာ|> <|မ|> <|ရှိ|> <|ဘူး|> <|။|>
<|ကျွန်တော်|> <|ကောင်းကောင်း|> <|သိ|> <|နေ|> <|တာ|> <|က|> <|အလုပ်|> <|ကြိုးစား|> <|တယ်|> <|ဆိုတာ|> <|လူ|> <|တိုင်း|> <|မ|> <|လုပ်|> <|နိုင်|> <|ပါ|> <|။|>
<|သူ|> <|က|> <|သူ့|> <|အလုပ်|> <|ကို|> <|ချစ်|> <|တယ်|> <|။|>
<|ကျွန်တော်|> <|နဲ့|> <|သူ|>
<|သူ|>
```

ပြီးမှ word boundary ဝင်ရေးထားတဲ့ stopwords.txt.tmp ဖိုင်ထဲက စာလုံးတွေကို sed ```"s:.*:s/&//ig:"``` command နဲ့ regular expression search-and-replace pattern ဖြစ်တဲ့ s/search-word/replacement/ig ပုံစံအဖြစ်ပြောင်းပါတယ်။ အောက်ပါအတိုင်းပါ။ ဒီနေရာမှာ i (case insensitive) က မြန်မာစာအတွက် ဆိုရင်မပါလည်း ရပါတယ်။ g (global) ကတော့ စာကြောင်း တစ်ကြောင်းလုံးမှာ တွေ့သမျှအားလုံးကို အစားထိုးပေးခိုင်းတာ ဖြစ်ပါတယ်။  

```bash
$ sed "s:.*:s/&//ig:" ./stopwords.txt.tmp 
s/<|ကျွန်တော်|>//ig
s/<|ကျွန်မ|>//ig
s/<|သူ|>//ig
s/<|သူမ|>//ig
s/<|ကို|>//ig
s/<|မှာ|>//ig
s/<|ရဲ့|>//ig
s/<|အတွက်|>//ig
s/<|နဲ့|>//ig
s/<|ဆိုရင်|>//ig
s/<|ဆိုတာ|>//ig
s/<|က|>//ig
```
အထက်ပါ regular expression pattern နဲ့ corpus ဖိုင်ထဲမှာ ဝင်ရှာပြီး search and replace လုပ်ခိုင်းခဲ့ပါတယ်။ command အပြည့်အစုံက အောက်ပါအတိုင်းပါ။  

```bash
sed -e "$(sed "s:.*:s/&//ig:" $stopwordFile.tmp)" $corpusFile.tmp
```

stop word တွေကို ရှာဖွေပြီး ဖျက်ပြီးသွားတဲ့ အခါမှာ ထွက်လာမယ့် output က အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မယ်။  

```bash
 sed -e "$(sed "s:.*:s/&//ig:" stopwords.txt.tmp)" my-text.txt.tmp
     <|သူငယ်ချင်း|> <|တွေ|> <|ပါ|> <|။|>
 <|မ|> <|သွား|> <|ဘူး|> <|။|>
<|သူငယ်ချင်း|>  <|ဆို|> <|အကုန်|> <|လုပ်ပေး|> <|တယ်|> <|။|>
  <|နဖူး|>  <|မှဲ့|> <|အကြီးကြီး|> <|ရှိ|> <|ပါ|> <|တယ်|> <|။|>
  <|မ|> <|တွေ့|> <|ဖူး|> <|ပါ|> <|။|>
    <|ချစ်သူ|> <|တွေ|> <|ဖြစ်|> <|ခဲ့|> <|ကြ|> <|တယ်|> <|။|>
 <|သာ|>  <|သေချာတယ်|> <|အောင်မြင်|>  <|။|>
  <|ကွန်ပျူတာ|> <|မ|> <|ရှိ|> <|ဘူး|> <|။|>
 <|ကောင်းကောင်း|> <|သိ|> <|နေ|> <|တာ|>  <|အလုပ်|> <|ကြိုးစား|> <|တယ်|>  <|လူ|> <|တိုင်း|> <|မ|> <|လုပ်|> <|နိုင်|> <|ပါ|> <|။|>
  <|သူ့|> <|အလုပ်|>  <|ချစ်|> <|တယ်|> <|။|>
```

အဲဒါကြောင့် နောက်ဆုံးအဆင့်အနေနဲ့ ထွက်လာမယ် output တွေကို ဒီအတိုင်း လွှတ်မပေးလိုက်ပဲ start word boundary နဲ့ stop word boundary တွေကို ```sed 's/<|\||>//g'``` command နဲ့ parsing လုပ်ပြီးမှ screen မှာ output အနေနဲ့ ရိုက်ထုတ်ခိုင်းလိုက်ပါတယ်။  

```bash
$ sed -e "$(sed "s:.*:s/&//ig:" stopwords.txt.tmp)" my-text.txt.tmp | sed 's/<|\||>//g'
     သူငယ်ချင်း တွေ ပါ ။
 မ သွား ဘူး ။
သူငယ်ချင်း  ဆို အကုန် လုပ်ပေး တယ် ။
  နဖူး  မှဲ့ အကြီးကြီး ရှိ ပါ တယ် ။
  မ တွေ့ ဖူး ပါ ။
    ချစ်သူ တွေ ဖြစ် ခဲ့ ကြ တယ် ။
 သာ  သေချာတယ် အောင်မြင်  ။
  ကွန်ပျူတာ မ ရှိ ဘူး ။
 ကောင်းကောင်း သိ နေ တာ  အလုပ် ကြိုးစား တယ်  လူ တိုင်း မ လုပ် နိုင် ပါ ။
  သူ့ အလုပ်  ချစ် တယ် ။
```

ဒီနေရာမှာ word boundary တွေမထည့်ပဲ ဒီအတိုင်း stop word တွေကို ရှာပြီး ဖျက်ရင်ကော မရဘူးလားလို့ မမြင်တဲ့သူတွေလည်း ရှိပါလိမ့်မယ်။ word boundary မထည့်ပဲ ဖျက်ရင် ပြဿနာက stop word တွေအဖြစ် သီးခြားရှိနေတဲ့ စာလုံးတွေတင်သာမကပဲ stop word စာလုံးတွေက sub-word အဖြစ်တွဲပါနေတဲ့ အပိုင်းတွေကိုပါ ဖျက်ထုတ်သွားလို့ပါ။ အောက်ပါ ဥပမာ output ကို လေ့လာကြည့်ရင် နားလည်သွားပါလိမ့်မယ်။  

```bash
$ sed -e "$(sed "s:.*:s/&//ig:" ./stopwords.txt)" ./my-text.txt 
     ငယ်ချင်း တွေ ပါ ။
 မ သွား ဘူး ။
ငယ်ချင်း  ဆို အုန် လုပ်ပေး တယ် ။
မ  နဖူး  မှဲ့ အြီးြီး ရှိ ပါ တယ် ။
မ  မ တွေ့ ဖူး ပါ ။
  မ  ချစ် တွေ ဖြစ် ခဲ့ ြ တယ် ။
 သာ  သေချာတယ် အောင်မြင်  ။
မ  ွန်ပျူတာ မ ရှိ ဘူး ။
 ောင်းောင်း သိ နေ တာ  အလုပ် ြိုးစား တယ်  လူ တိုင်း မ လုပ် နိုင် ပါ ။
  ့ အလုပ်  ချစ် တယ် ။
  

```

Regular expression ရဲ့ word boundary တွေနဲ့ ပတ်သက်ပြီး အသေးစိတ် လေ့လာချင်သူများအတွက်က အောက်ပါ လင့်(ခ်) ကို ဖတ်ကြည့်ပါလို့ တိုက်တွန်းပါတယ်။  
[Regex Boundaries and Delimiters—Standard and Advanced](https://www.rexegg.com/regex-boundaries.html)  

## 21. [rm-spaces-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-spaces-lineno.sh)  

website ကနေ တချို့ coding တွေကို ကိုယ်စက်ထဲမှာ စမ်းrun ဖို့အတွက် ကော်ပီကူးတဲ့အခါမှာ webiste အပေါ်မူတည်ပြီး ကိုယ်လိုချင်တဲ့ coding သာမကပဲ မလိုချင်တဲ့ space တွေ၊ လိုင်းနံပါတ်တွေပါ တွဲပါလာတဲ့အခါမျိုး ကြုံဖူးကြပါလိမ့်မယ်။ အဲဒီလိုအခြေအနေမျိုးအတွက် ကော်ပီကူးထားတဲ့ program ဖိုင်တွေထဲက မလိုချင်တဲ့အပိုင်းတွေကို ဖျက်ထုတ်ဖို့အတွက် ရေးခဲ့တာပါ။  

ဥပမာအနေနဲ့ run ပြဖို့ code-with-lineno.py ဆိုပြီး comment ပဲရေးပြထားတဲ့ fake python ဖိုင်ကို ဖန်တီးခဲ့ပါတယ်။  

```bash
$ cat ./code-with-lineno.py 
    1 ##
    2 # 
    3 # @example Code
    4 # 
    5 # @copyright GNU Public License
    6 # @author written 2011-2012 (www.mynlp.org) 
    7 # @author Supported by the Zero University, 
    8 #   Dept. of Cognitive NLP
    9 # 
   10 # @note

$ ./rm-spaces-lineno.sh ./code-with-lineno.py 
##
# 
# @example Code
# 
# @copyright GNU Public License
# @author written 2011-2012 (www.mynlp.org) 
# @author Supported by the Zero University, 
#   Dept. of Cognitive NLP
# 
# @note
```

## 22. [blowfish.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/blowfish.sh)  

ပုံမှန်အားဖြင့် အရေးကြီးတဲ့ ဒေတာဖိုင်တွေကို အီးမေး(လ်)သုံးပြီး ပို့တဲ့အခါမှာ password ခံပြီး၊ zip လုပ်ပြီး၊ ပို့လေ့ရှိပါတယ်။ တခါတလေမှာ text ဖိုင်တွေကို encyrption လုပ်ပြီး ပို့တာမျိုးလည်း လုပ်လေ့ရှိပါတယ်။ Blowfish (symmetric-key block cipher) ကို သုံးဖို့အတွက် ရေးထားခဲ့တဲ့ shell script ပါ။ သုံးပုံသုံးနည်း နမူနာက အောက်ပါအတိုင်းပါ။  

အရင်ဆုံး plain.txt ဖိုင်ထဲမှာ စာတစ်ကြောင်းရေးထားတာ ရှိပါတယ်။  
```bash
lar@lar-air:~/tool/bash/crypt$ cat plain.txt 
Hello! Blowfish encoding!
``` 

./blowfish.sh ကို သုံးပြီး plain.txt ဖိုင်ကို encode လုပ်ကြည့်ရအောင်  
```bash
lar@lar-air:~/tool/bash/crypt$ ./blowfish.sh ./plain.txt abc123 enc
```
out.enc ဖိုင်ဆိုပြီး encoded ဖိုင်တစ်ဖိုင် ရလာပါလိမ့်မယ်။  
အဲဒီဖိုင်ကို ရိုက်ထုတ်ကြည့်ရင် encode လုပ်ထားတာကို တွေ့ရပါလိမ့်မယ်။  

```bash
lar@lar-air:~/tool/bash/crypt$ cat out.enc
Salted__	��$�T٥,��1��w�F�;W��tG)գ�ԥ�\�ZҔA�
```
blowfish.sh ပရိုဂရမ်နဲ့ decode လုပ်ပြီး ထွက်လာတဲ့ out ဆိုတဲ့ဖိုင်ကို cat command နဲ့ ပြန်ရိုက်ခိုင်းကြည့်ရအောင်   
```bash
lar@lar-air:~/tool/bash/crypt$ ./blowfish.sh ./out.enc abc123 dec
lar@lar-air:~/tool/bash/crypt$ cat out
Hello! Blowfish encoding!
```

တကယ်လို့ pass phrase ပေးတာမှားရင် decode လုပ်လို့မရပါဘူး။  

```bash
lar@lar-air:~/tool/bash/crypt$ ./blowfish.sh ./out.enc abc dec
bad decrypt
140453512398488:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:evp_enc.c:531:
```

## 23.[replace-with-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno.sh)  

NLP အလုပ်တွေမှာ တစ်ခါတလေ ဖိုင်တစ်ဖိုင်ထဲကနေ စာကြောင်း တချို့ကိုပဲ ဆွဲထုတ်ယူပြီး ပြုပြင်မှုတွေလုပ်ပါတယ်။ ပြီးတော့ အဲဒီ ပြင်ထားတဲ့ စာကြောင်းတွေကို နဂိုဖိုင်ထဲမှာ လိုင်းနံပါတ်နဲ့ ပြန်ရှာပြီး အစားထိုးရတဲ့အခါမျိုးတွေရှိတတ်ပါတယ်။ replace-with-lineno.sh က အဲဒီအတွက် ရေးခဲ့ပါတယ်။  

ဥပမာ [oldfile](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/oldfile) ထဲမှာ အောက်ပါစာကြောင်းတွေရှိနေတယ်ဆိုပါစို့။  

```
$ cat oldfile
မအိပ်မနေအသက်ရှည်
တရွာမပြောင်း သူကောင်းမဖြစ်
တနေ့တလံ ပုဂံဘယ်ပြေးမလဲ
ကျားကြီး ခြေရာကြီး
မေးပါများ စကားရ
```

လိုင်းနံပါတ် ၂ စာကြောင်းနဲ့ လိုင်းနံပါတ် ၄ စာကြောင်းကို အောက်ပါ [patchfile](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/patchfile) ထဲမှာ ရေးထားတဲ့ စာကြောင်းနှစ်ကြောင်းနဲ့ အစားထိုးချင်တယ်လို့ဆိုပါစို့။ format ကတော့ line no.\<TAB\>string ဆိုတဲ့ ပုံစံနဲ့ ရေးထားပါတယ်။  
        
```
$ cat patchfile 
2	သေချင်တဲ့ကျား တောပြောင်း
4	ဆင်ပိန် ကျွဲလောက်ရှိ
```

./replace-with-lineno.sh ပရိုဂရမ်ကို patchfile နဲ့ oldfile ကိုပေးပြီး run ကြည့်ရအောင်။  

```
$ ./replace-with-lineno.sh ./patchfile ./oldfile 
```

run ပြီးတဲ့အခါမှာ oldfile ထဲမှာ စာကြောင်းနံပါတ် ၂ နဲ့ ၄ ကို update လုပ်သွားတာကို အောက်ပါအတိုင်း တွေ့ရပါလိမ့်မယ်။  

```
$ cat oldfile
မအိပ်မနေအသက်ရှည်
သေချင်တဲ့ကျား တောပြောင်း
တနေ့တလံ ပုဂံဘယ်ပြေးမလဲ
ဆင်ပိန် ကျွဲလောက်ရှိ
မေးပါများ စကားရ
```

## 24. [replace-with-lineno2.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno2.sh) 

ဥပမာ ကျွန်တော်တို့မှာ မြန်မာစာ စာလုံးပေါင်း သတ်ပုံကျမ်းစာအုပ်ကို Unicode နဲ့ ရိုက်ထားတဲ့ ဖိုင်ရှိတယ်ဆိုပါစို့။  
ဒီနေရာမှာတော့ စာလုံး ၁၀လုံးကိုပဲ ဥပမာအနေနဲ့ အောက်ပါအတိုင်း သုံးပြထားပါတယ်။ 

```
$ cat ./ori.txt
ကဏန်း(သတ္တဝါ)
ကဏန်းမြင်း
ကတညုတတရား
ကတိ
ကတိကဝတ်
ကတောကမျော(ကသောကမျော)
ကတော့(ဆီ)
ကတော်(မင်း စိုး)
ကတိုးကောင်
ကတောက်ကဆတ်
```

အထက်မှာ မြင်ရတဲ့အတိုင်း စာလုံးပေါင်းသတ်ပုံကျမ်းစာအုပ်မှာက တချို့စာလုံးတွေရဲ့ ဘေးမှာ ကွင်းစကွင်းပိတ်နဲ့ ဖြည့်ရှင်းထားတာတွေ ပါပါတယ်။ "ကဏန်း" စာလုံးရဲ့ ဘေးမှာ "သတ္တဝါ" လို့ဖော်ပြထားပြီး၊ ထိုနည်းလည်းကောင်း "ကတော့" ဆိုတဲ့ စာလုံးဘေးမှာတော့ "ဆီ" ဆိုပြီး ဖော်ပြထားပါတယ်။ လုပ်ချင်တာက အဲဒီ ကွင်းစကွင်းပိတ်နဲ့ ပါနေတဲ့ စာလုံးတွေကို ဆွဲထုတ်ပြီး လက်နဲ့ပုံစံပြောင်းရေးမယ်၊ ပြီးတော့ အော်ရဂျင်နယ်ဖိုင်ဖြစ်တဲ့ [ori.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/ori.txt) ဖိုင်ထဲကို ဝင်ရေးချင်တယ် ဆိုကြပါစို့။  

အရင်ဆုံး [ori.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/ori.txt) ဖိုင်ကို လိုင်းနံပါတ်တပ်ပေးစေချင်တော့ ကျွန်တော်တို့ နေ့စဉ်သုံးနေတဲ့ cat command ကို option -n ပေးပြီး run လိုက်ပါတယ်။ အဲဒါဆိုရင် အောက်ပါအတိုင်း စာကြောင်းတစ်ကြောင်းချင်းစီအတွက် လိုင်းနံပါတ်တပ်ပေးပါလိမ့်မယ်။ ကျွန်တော်က အဲဒီ နံပါတ်တပ်ပေးပြီး ရိုက်ထုတ်လာတဲ့ စာကြောင်းတွေကို ori.no.txt ဆိုတဲ့ ဖိုင်နာမည်အသစ်ပေးပြီး သိမ်းလိုက်ပါတယ်။  

```
$ cat -n ./ori.txt > ori.no.txt
$ cat ./ori.no.txt
     1	ကဏန်း(သတ္တဝါ)
     2	ကဏန်းမြင်း
     3	ကတညုတတရား
     4	ကတိ
     5	ကတိကဝတ်
     6	ကတောကမျော(ကသောကမျော)
     7	ကတော့(ဆီ)
     8	ကတော်(မင်း စိုး)
     9	ကတိုးကောင်
    10	ကတောက်ကဆတ်
```

ပြီးတော့ ပြင်ချင်တဲ့ စာကြောင်းတွေဖြစ်တဲ့ ကွင်းစကွင်းပိတ် ပါနေတဲ့ စာကြောင်းတွေချည်းပဲကို grep နဲ့ ဆွဲထုတ်ပြီး 4edit.txt ဆိုတဲ့ ဖိုင်မှာ သိမ်းခဲ့ပါတယ်။ 4edit.txt ဆိုတဲ့ ဖိုင်ထဲမှာတော့ ori.no.txt ဖိုင်ထဲက ကွင်းစကွင်းပိတ်ပါနေတဲ့ စာကြောင်းလေးကြောင်းစလုံး ရှိနေမှာ ဖြစ်ပါတယ်။  

```
$ grep "(" ./ori.no.txt > 4edit.txt
$ cat ./4edit.txt
     1	ကဏန်း(သတ္တဝါ)
     6	ကတောကမျော(ကသောကမျော)
     7	ကတော့(ဆီ)
     8	ကတော်(မင်း စိုး)
```

[4edit.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/4edit.txt) ဖိုင်ကို ကိုယ်ကြိုက်တဲ့ text editor တစ်ခုခုနဲ့ ဖွင့်ပြီး အောက်ပါအတိုင်း ပြင်လိုက်တယ်ဆိုပါစို့။ format ကတော့ field တစ်ခုနဲ့ တစ်ခုအကြားမှာ <TAB> ကီးနဲ့ ခြားပေးထားတဲ့ ပုံစံပါ။ ရှေ့ဆုံးမှာ ရှိနေတဲ့ လိုင်းနံပါတ်တွေအတွက်ထားထားတဲ့ field ရှေ့မှာက cat -n ရဲ့ output ဖြစ်လို့ space တွေပါနေပေမယ့် ကိစ္စမရှိပါဘူး။ ကျွန်တော်တို့က ကိုယ်လိုချင်တဲ့ field ကို <TAB> နဲ့ပဲ ခွဲခြားပြီး ဖတ်မှာမို့လို့ပါ။  
        
```

$gedit 4edit.txt 

     1	ကဏန်း(သတ္တဝါ)	ကဏန်း သတ္တဝါ
     6	ကတောကမျော(ကသောကမျော)	ကတောကမျော
     7	ကတော့(ဆီ)	ဆီကတော့
     8	ကတော်(မင်း စိုး)	မင်းစိုးကတော်

```

[replace-with-lineno2.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/replace-with-lineno2.sh) ဖိုင်ကို အောက်ပါအတိုင်း ./4edit.txt (လက်နဲ့ ပြင်ဆင်ထားတဲဖိုင်) နဲ့ ori.txt (နဂိုဖိုင်) ကို argument အနေနဲ့ ပေးလိုက်ပြီး run လိုက်ရင် ဘယ်လိုင်းတွေကို ပြင်ဆင်သွားတယ်ဆိုတာကို ရိုက်ပြပေးပြီး၊ ပြင်ရမယ့် လိုင်းတွေကိုလည်း လိုင်းနံပါတ်ရော၊ နဂိုစာကြောင်းကိုကော တိုက်ကြည့်ပြီး ori.txt ဖိုင်ကို overwrite လုပ်ပေးသွားမှာ ဖြစ်ပါတယ်။  

```
$ ./replace-with-lineno2.sh ./4edit.txt ./ori.txt
lineNo: 1
originalText: ကဏန်း(သတ္တဝါ)
editedText: ကဏန်း သတ္တဝါ
lineNo: 6
originalText: ကတောကမျော(ကသောကမျော)
editedText: ကတောကမျော
lineNo: 7
originalText: ကတော့(ဆီ)
editedText: ဆီကတော့
lineNo: 8
originalText: ကတော်(မင်း စိုး)
editedText: မင်းစိုးကတော်
```

run ပြီးသွားတဲ့အခါမှာ ori.txt ဖိုင်ကို cat command နဲ့ ရိုက်ပြီး check လုပ်ကြည့်ရင်၊ အောက်ပါအတိုင်း ပြင်ပေးသွားတာကို တွေ့ရပါလိမ့်မယ်။  

```
$ cat ./ori.txt
ကဏန်း သတ္တဝါ
ကဏန်းမြင်း
ကတညုတတရား
ကတိ
ကတိကဝတ်
ကတောကမျော
ဆီကတော့
မင်းစိုးကတော်
ကတိုးကောင်
ကတောက်ကဆတ်
```

## 25. [OOV-count.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/OOV-count.sh)  

ကျွန်တော် ကိုယ်တိုင်လည်း "comm" ကို မသိခဲ့စဉ်က Out-of-Vocabulary (OOV) စာလုံးတွေကို ရိုက်ထုတ်ပြပေးတဲ့ ပရိုဂရမ်ကို perl နဲ့ ရေးတာမျိုး လုပ်ခဲ့ဖူးပါတယ်။ တကယ်က "comm" Linux command နဲ့ဆိုရင် လွယ်လွယ်ကူကူ OOV ကို ရိုက်ထုတ်ခိုင်းလို့ရကြောင်းကို မြန်မာကျောင်းသား/သူတွေကို သိစေချင်လို့ ရေးတင်ပေးလိုက်တာပါ။ လက်ရှိမှာ language model ရဲ့ OOV ရှာပေးတဲ့ tool စတာတွေကိုလည်း လိုအပ်တဲ့အခါမှသာ သုံးပြီး၊ ပုံမှန်အားဖြင့် OOV ကိုတစ်ချက် စစ်ကြည့်ချင်တာမျိုးအတွက်က comm ကိုပဲ သုံးဖြစ်နေပါတယ်။   

ဒီ သုံးပုံသုံးနည်း example အတွက် ...  
ကျွန်တော်ရဲ့ GitHub မှာ တင်ထားတဲ့ mypos ဒေတာကိုပဲ corpus အဖြစ်နဲ့ ယူသုံးပြထားပါတယ်။
အဲဒီ စာလုံးဖြတ်ထားပြီးသား corpus ဖိုင်ကို အောက်ပါအတိုင်း wget command နဲ့ ဒေါင်းလုဒ်လုပ်ယူခဲ့ပါတယ်။

```
$ wget https://raw.githubusercontent.com/ye-kyaw-thu/myPOS/master/corpus-draft-ver-1.0/mypos-dver.1.0.word.txt
--2019-03-24 01:59:15--  https://raw.githubusercontent.com/ye-kyaw-thu/myPOS/master/corpus-draft-ver-1.0/mypos-dver.1.0.word.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3466670 (3.3M) [text/plain]
Saving to: ‘mypos-dver.1.0.word.txt’

mypos-dver.1.0.word.txt               100%[========================================================================>]   3.31M   420KB/s    in 11s     

2019-03-24 01:59:29 (296 KB/s) - ‘mypos-dver.1.0.word.txt’ saved [3466670/3466670]
```

Test-data ဖိုင်ဖြစ်တဲ့ test-data4oov ဖိုင်ထဲမှာတော့ အောက်ပါအတိုင်း ရှိပါတယ်။
တကယ်က OOV ကို တိုင်းတာဖို့အတွက်ဆိုရင် test-data ဖိုင်မှာ လုပ်ထားတဲ့ word segmentation က corpus မှာ ဖြတ်ထားတဲ့ ပုံစံနဲ့ တူကိုတူရပါမယ်။ ဒီနေရာမှာတော့ ကျွန်တော် ဘာမှ မစဉ်းစားထားပဲ ဥပမာ အနေနဲ့ စိတ်ထဲရှိတာကို ကောက်ရိုက်ပြီး၊ ကြုံသလို word segmentation ကို ဖြတ်ထားပါတယ်။ example အနေနဲ့ run ပြချင်တာပဲ မို့လို့ပါ။

```
$ cat ./test-data4oov 
ဒီနေ့ OOV တွက် ပေး တဲ့ shell script ကို ရေး နေ ရင်း ၂၀၁၈ ခုနှစ် အတွက် အကယ်ဒမီ ပေးပွဲ က တီဗီ မှာ လာ နေ လို့ အမေ နဲ့ အတူ ကြည့် ဖြစ် ခဲ့ တယ် ။ နိုင်ငံခြား မှာ နေ တာ အရမ်း ကြာ သွားပြီး၊ မြန်မာ ရုပ်ရှင် လည်း မ ကြည့် ဖြစ် တာ ကြာ ပြီ မို့ မင်းသား ၊ မင်းသမီး တွေ အားလုံး က ကျွန်တော့် အတွက် တော့ အသစ် တွေ ပဲ ဖြစ် နေ ပါ တယ် ။ ဆု ရ သွား တဲ့ ရုပ်ရှင် တွေ ကို လည်း မ ကြည့် ဖူး ပေ မယ့် သူ တို့ တွေ အောင်မြင် တာ ကို ကြားသိ ရ လို့ ဝမ်းသာ ပီတိ ဖြစ် ရ ပါ တယ် ။
```

test-data4oov ဖိုင်ထဲမှာပဲ ရှိပြီးတော့ corpus ဖြစ်တဲ့ mypos-dver.1.0.word.txt ဖိုင်ထဲမှာ မရှိတဲ့ OOV စာလုံးတွေ စကရင်မှာ ရိုက်ထုတ်ပြပေးစေချင်ရင်တော့ အောက်ပါအတိုင်း run ပါ။

```
$ ./OOV-count.sh ./mypos-dver.1.0.word.txt ./test-data4oov 
OOV
script
shell
ဒီနေ့
ပီတိ
ပေးပွဲ
သွားပြီး၊
```

wc command ကို pass လုပ်ပြီးတော့ no. of OOV ကို ရိုက်ထုတ်ခိုင်းလို့လည်း ရပါတယ်။

```
$ ./OOV-count.sh ./mypos-dver.1.0.word.txt ./test-data4oov | wc
      7       7      93
```

OOV စာလုံးတွေကို ဖိုင်တစ်ဖိုင်အနေနဲ့ သိမ်းဆည်းချင်ရင်တော့ အောက်ပါအတိုင်း

```
$ ./OOV-count.sh ./mypos-dver.1.0.word.txt ./test-data4oov > oov.list
```

## 26. [find-blank-lines.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/find-blank-lines.sh)  

find-blank-lines.sh က ဖိုင်တစ်ဖိုင်ထဲမှာရှိနေတဲ့ blank line တွေကို ရှာဖွေဖို့အတွက် သုံးလို့ရပါတယ်။  
ဥပမာ train.my ဖိုင်ထဲမှာ ရှိနေတဲ့ blank line တွေကို လိုင်းနံပါတ်နဲ့တကွ ရိုက်ထုတ်ပေးစေချင်ရင် အောက်ပါအတိုင်း command ပေးပါ။  

```
$ ./find-blank-lines.sh train.my
./train.my:14404:
./train.my:15708:
```

အထက်မှာ မြင်နေရတာက ရှာခိုင်းထားတဲ့ train.my ဖိုင်ထဲမှာ လိုင်းနံပါတ် 14404 နဲ့ 15708 တွေမှာ blank line တွေပါနေတယ်လို့ output လုပ်ပေးတာဖြစ်ပါတယ်။  

တကယ်လို့ လက်ရှိ ဖိုလ်ဒါအောက်မှာ ရှိတဲ့ "tနဲ့စပြီး extension တစ်ခုပါနေတဲ့" ဖိုင်တွေထဲမှာ ရှိနေတဲ့ blank line တွေကို ရှာဖွေချင်ရင်တော့ အောက်ပါပုံစံမျိုး command ပေးပြီး run လို့ရပါတယ်။ တစ်ခု သတိထားရမှာက ခင်ဗျားပေးချင်တဲ့ regular expression တွေမှာ special character တွေ (ဥပမာ \* လိုမျိုး) ပါလာမယ်ဆိုရင် single quote အတွင်းမှာ regular expression ကို ရိုက်ပါ။ မဟုတ်ရင် လိုချင်တဲ့ ပုံစံအတိုင် အလုပ်လုပ်မှာ မဟုတ်ပါဘူး။   

```
$ ./find-blank-lines.sh 't*.*'
./train.my:14404:
./train.my:15708:
./train.rk:12526:
./train.rk:14404:
./train.rk:15708:
```

နားလည်မယ်လို့ထင်ပါတယ်။ အထက်မှာ မြင်နေရတာကတော့ train.my ဖိုင်နဲ့ train.rk ဖိုင်ထဲမှာရှိနေတဲ့ blank line တွေနဲ့ ပါတ်သက်တဲ့ လိုင်းနံပါတ်တွေပါ။ ဒီ shell script က မြန်မာစာနဲ့ ရခိုင်စာကို rule-based machine translation အတွက် ပြင်ဆင်တုန်းမှာ သုံးခဲ့တဲ့ script တစ်ခုဖြစ်ပါတယ်။  

## 27. [dot2png-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2png-pdf.sh)  

[Graph description language](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) က ဂရဖ်တွေကို ရေးဆွဲဖို့အတွက် ဖန်တီးထားတဲ့ programming language တစ်ခုဖြစ်ပြီးတော့ အရမ်းကို အသုံးဝင်ပါတယ်။ အဲဒီ ပရိုဂရမ်ဖိုင်တွေက .dot သို့မဟုတ် .gv ဖိုင်extension အနေနဲ့သိမ်းကြပါတယ်။ dot2png-pdf.sh က ".dot" ဖိုင်ကနေ ပုံဖိုင် format တစ်ခုဖြစ်တဲ့ PNG [(Portable Network Graphics)](https://en.wikipedia.org/wiki/Portable_Network_Graphics) အဖြစ်ပြောင်းဖို့နဲ့ အဲဒီ ပြောင်းပြီးသား ".png" ပုံဖိုင်ကို ဘယ်ကွန်ပျူတာမှာ မဆို အလွယ်တကူကြည့်လို့ရတဲ့ pdf ဖိုင်အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တာ ဖြစ်ပါတယ်။  

NLP အလုပ်နဲ့ ဘယ်လိုပတ်သက်သလဲလို့ မေးလာရင်တော့၊ dot ဂရဖ်တွေက တကယ်က NLP အလုပ်တစ်ခုတင်မကပဲ နေရာပေါင်းစုံမှာ သုံးပါတယ်။ NLP နဲ့ ပတ်သက်တာတစ်ခုကို မြင်သာအောင်လို့ ဥပမာအနေနဲ့ machine translation လုပ်တဲ့အခါမှာ ထွက်လာတဲ့ ".dot" ဖိုင်ကို ယူသုံးပြထားပါတယ်။ Statistical Machine translation လုပ်တဲ့အခါမှာ လုပ်ရတဲ့ အဆင့်တွေက တကယ့်ကို အများကြီးပါပဲ။ တကယ်တမ်း စက်အသစ်တစ်လုံးမှာ run လို့ရအောင် ပြင်ဆင်ရတဲ့အခါမှာလည်း အစပိုင်းမှာ တစ်နေရာမဟုတ် တစ်နေရာမှာ အကြောင်းတစ်ခုခုကြောင့် error တက်ပြီးတော့ ရပ်သွားတပ်ပါတယ်။ အဲဒါကြောင့်မို့ machine translation platform တွေက အများသောအားဖြင့် run သွားတဲ့ အဆင့်တိုင်းကို log အနေနဲ့ မှတ်ပြီး overall process graph အနေနဲ့ dot ဖိုင်ကို ထုတ်ပေးကြပါတယ်။ အဲဒါက debug လုပ်ဖို့အတွက် အင်မတန်အသုံးဝင်ပါတယ်။ ဘယ်နေရာမှာ error တက်သွားတာလဲ ဆိုတာကို လူအနေနဲ့ က အဲဒီ dot ဖိုင်ကို graph ပုံအဖြစ် ပြောင်းပြီး ကြည့်နိုင်လို့ အင်မတန်အသုံးဝင်ပါတယ်။  

ကျွန်တော်ကိုယ်တိုင်လည်း statistical machine translation ကိုလုပ်တဲ့ အခါတိုင်းမှာ ဒီ ဂရဖ်ကို ထုတ်ကြည့်ပြီး debug လုပ်ခဲ့တဲ့ အကြိမ်ပေါင်း မနဲပါဘူး။ လက်ရှိမှာလည်း ထိုင်းဘာသာ နဲ့ မြန်မာဘာသာ အကြား machine translation နဲ့ ပတ်သက်တဲ့ experiment တွေကို လုပ်နေရင်း error တက်လာလို့ ဘယ်နေရာမှာ တက်တာလဲ ဆိုတာကို ရှာဖွေဖို့အတွက် dot ဖိုင်ကို png ဖိုင် ပြောင်းဖြစ်ခဲ့ပါတယ်။ အဲဒါနဲ့ လေ့လာချင်တဲ့ သူတွေအတွက် အသုံးဝင်မှာ သေချာလို့ dot2png-pdf.sh ပရိုဂရမ်ကို တင်ပေးလိုက်ပါတယ်။  

ဆိုကြပါစို့ ကျွန်တော်တို့ [Moses SMT toolkit](http://www.statmt.org/moses/) ကို သုံးပြီးတော့ PBSMT (Phrase-based Machine Translation) approach နဲ့ ထိုင်း-မြန်မာ ဘာသာပြန်တဲ့ experiment ကိုလုပ်ကြည့်တော့ ရလဒ်တွေက ဆိုးဆိုးဝါးဝါးဖြစ်နေတယ်။ အဲဒါကြောင့် ".dot" ဖိုင် ကိုသုံပြီးတော့ debug ကြည့်ကြရအောင်။  

Moses SMT toolkit က ပြီးသွားတဲ့ process တွေအတွက် graph.1.dot လိုမျိုး dot ဖိုင်ကို ထုတ်ပေးပါတယ်။ ကောင်းပြီ။ အောက်ပါအတိုင်း ကျွန်တော်တို့ရဲ့ ဖိုလ်ဒါအောက်မှာ အဲဒီ graph.1.dot ဖိုင်ရယ် ကျွန်တော်ကရေးထားတဲ့ dot2png-pdf.sh ဖိုင်ရယ် စုစုပေါင်း ဖိုင်နှစ်ဖိုင်ရှိနေတဲ့ အခြေအနေနဲ့ သွားကြရအောင်။  

```
$ ls
dot2png-pdf.sh  graph.1.dot
```

[graph.1.dot](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/dot2-png-pdf/graph.1.dot) ဖိုင်ထဲမှာက အောက်ပါလိုမျိုး process flowchart ပုံထုတ်ပေးနိုင်ဖို့ ပရိုဂရမ်ရေးထားတာ ဖြစ်ပါတယ်။ စိတ်ဝင်စားတဲ့သူတွေက လေ့လာနိုင်လို့ရအောင် GitHub မှာ တင်ပေးထားပါတယ်။ လင့်(ခ်)လည်း ချိတ်ပေးထားလို့ အပြာရောင်ဖြစ်နေတဲ့ graph.1.dot နေရာကို ကလစ်နှိပ်ပြီးကြည့်ရင် အဲဒီဖိုင်တစ်ဖိုင်လုံးကို မြင်ရပါလိမ့်မယ်။  

```
$ cat graph.1.dot
digraph Experiment1 {
  ranksep=0;
  subgraph cluster_0 {
    fillcolor="lightyellow";
    shape=box;
    style=filled;
    fontsize=10;
    label="LM:myth";
    55 [label="binarize",shape=box,fontsize=10,height=0,style=filled,fillcolor="#8080ff"];
    56 [label="quantize",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    57 [label="randomize",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    58 [label="train",shape=box,fontsize=10,height=0,style=filled,fillcolor="#8080ff"];
    59 [label="strip",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    60 [label="post-split-factorize",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    61 [label="split",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    62 [label="lowercase",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    63 [label="factorize",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    64 [label="mock-parse",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
    65 [label="tokenize",shape=box,fontsize=10,height=0,style=filled,fillcolor="lightyellow"];
  }
  subgraph cluster_1 {
    fillcolor="lightyellow";
    shape=box;
    style=filled;
    fontsize=10;
    label="EVALUATION:test";
 
...
...
...
```

[graph.1.dot](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/dot2-png-pdf/graph.1.dot) ဖိုင်ကို .png, .pdf ဖိုင် ပြောင်းချင်ရင် အောက်ပါအတိုင်း run ပါ။  

```
$ ./dot2png-pdf.sh ./graph.1.dot
```

run တာက အဆင်ပြေပြေနဲ့ ပြီးစီးသွားရင် အောက်ပါအတိုင်း graph.1.png ဖိုင်နဲ့ graph.1.pdf ဖိုင် နှစ်ဖိုင်ကို output အဖြစ်နဲ့ ထုတ်ပေးပါလိမ့်မယ်။  

```
$ ls 
dot2png-pdf.sh  graph.1.dot  graph.1.pdf  graph.1.png
```

Linux မှာ png ဖိုင်နဲ့ pdf ဖိုင်ကို ဖွင့်ကြည့်ဖို့အတွက် ပရိုဂရမ်တွေအများကြီး ရှိပါတယ်။ ကိုယ့်စက်ထဲမှာ မရှိရင်တော့ အင်တာနက် ချိတ်ထားတဲ့ စက်မှာဆိုရင် sudo apt-get install \<package-name\> လိုမျိုး command နဲ့ ပေးပြီး (Ubuntu OS မှာဆိုရင်) install အလွယ်တကူ လုပ်လို့ ရပါတယ်။ ကျွန်တော်ကတော့ အောက်ပါအတိုင်း png ပုံဖိုင်ကိုဖွင့်ကြည့်ဖို့အတွက် display command ကို သုံးပြီးတော့ pdf ဖိုင်ကိုတော့ evince ပရိုဂရမ်ကိုသုံးပြီး ဖွင့်ကြည့်ခဲ့ပါတယ်။  
        
```
$ display ./graph.1.png 
$ evince ./graph.1.pdf
```

တကယ့်လက်တွေ့ dot ဖိုင်ကနေ ပြောင်းပြီး output အဖြစ်ထွက်လာတဲ့ [graph.1.png](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/dot2-png-pdf/graph.1.png) ဖိုင်ကိုရော [graph.1.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/dot2-png-pdf/graph.1.pdf) ဖိုင်ကိုရော လေ့လာနိုင်ရန် GitHub ရဲ့ ဒီpath [https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/dot2-png-pdf](https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/dot2-png-pdf) မှာ upload လုပ်ပေးထားပါတယ်။  

Download လုပ်ယူပြီးတော့ ကြည့်တာမဟုတ်ပဲ Browser မှာ ဖွင့်ကြည့်ရင်တော့ pdf ဖိုင်က screen မှာ fit ဖြစ်နေလို့ ကြည့်ရတာပိုအဆင်ပြေမယ်လို့ ထင်ပါတယ်။ ဖွင့်ကြည့်ရင် နောက်ပိတ်ဆုံး အဆင့်ဖြစ်တဲ့ evaluation လုပ်တဲ့အခါမှာ အကြောင်းတစ်ခုခုကြောင့် error တက်ခဲ့ကြောင်းကို အနီရောင်နဲ့ပြထားတာကို တွေ့ရပါလိမ့်မယ်။  

## 28. [add-start-end.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/add-start-end.sh)  

[add-start-end.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/add-start-end.sh) က NLP preprocessing အလုပ်တချို့မှာ sentence တစ်ကြောင်းချင်းစီအတွက် စာကြောင်းအစအမှတ်အသား၊ အဆုံးအမှတ်အသားတွေကို ထည့်ပေးဖို့ လိုအပ်လာတဲ့အခါမှာ သုံးတဲ့ shell script ပါ။ ဥပမာ language model ဆောက်တဲ့အခါမျိုး၊ WER (Word Error Rate) တွေကို တွက်တဲ့အခါမျိုးမှာ အဲဒီ စာကြောင်းအစ၊ အဆုံး အမှတ်အသားတွေကိုပြင်ဆင်ပေးရတာမျိုး ရှိပါတယ်။ အများသောအားဖြင့် စာကြောင်းအစ အမှတ်အသားကို "\<s\>" အဖြစ်သုံးပြီးတော့၊ အဆုံးအမှတ်အသားကိုတော့ "\<\\s\>" ဖြစ်ထားတတ်ကြပါတယ်။  

pass လုပ်မယ့် text ဖိုင်ကိုတော့ GitHub မှာ ကျွန်တော်တင်ထားတဲ့၊ ရှိပြီးသား [my-text.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/rm-stopwords/my-text.txt) ကိုပဲသုံးပြီး ဥပမာအနေနဲ့ run ပြထားပါတယ်။   

```
$ ./add-start-end.sh ./my-text.txt 
<s> ကျွန်တော် နဲ့ သူ နဲ့ က သူငယ်ချင်း တွေ ပါ ။ <\s>
<s> ကျွန်မ မ သွား ဘူး ။ <\s>
<s> သူငယ်ချင်း အတွက် ဆို အကုန် လုပ်ပေး တယ် ။ <\s>
<s> သူမ ရဲ့ နဖူး မှာ မှဲ့ အကြီးကြီး ရှိ ပါ တယ် ။ <\s>
<s> သူမ ကို မ တွေ့ ဖူး ပါ ။ <\s>
<s> သူ နဲ့ သူမ က ချစ်သူ တွေ ဖြစ် ခဲ့ ကြ တယ် ။ <\s>
<s> သူ သာ ဆိုရင် သေချာတယ် အောင်မြင် မှာ ။ <\s>
<s> သူမ မှာ ကွန်ပျူတာ မ ရှိ ဘူး ။ <\s>
<s> ကျွန်တော် ကောင်းကောင်း သိ နေ တာ က အလုပ် ကြိုးစား တယ် ဆိုတာ လူ တိုင်း မ လုပ် နိုင် ပါ ။ <\s>
<s> သူ က သူ့ အလုပ် ကို ချစ် တယ် ။ <\s>
<s> ကျွန်တော် နဲ့ သူ <\s>
<s> သူ <\s>
```

## 29. [get-words-with-position.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/get-words-with-position.sh)  

ဆိုကြပါစို့ ကျွန်တော်တို့မှာ အောက်ပါ စာကြောင်း ၁၂ကြောင်းပါ [my-text.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/rm-stopwords/my-text.txt) ဆိုတဲ့ ဖိုင်က ရှိပြီး အဲဒီအထဲက မြန်မာစာလုံးတွေကို ကိုယ်လိုချင်တဲ့ အပိုင်းအလိုက် ဖြတ်ထုတ်ယူချင်တဲ့အခါမျိုး။  

```
$ cat ./my-text.txt 
ကျွန်တော် နဲ့ သူ နဲ့ က သူငယ်ချင်း တွေ ပါ ။
ကျွန်မ မ သွား ဘူး ။
သူငယ်ချင်း အတွက် ဆို အကုန် လုပ်ပေး တယ် ။
သူမ ရဲ့ နဖူး မှာ မှဲ့ အကြီးကြီး ရှိ ပါ တယ် ။
သူမ ကို မ တွေ့ ဖူး ပါ ။
သူ နဲ့ သူမ က ချစ်သူ တွေ ဖြစ် ခဲ့ ကြ တယ် ။
သူ သာ ဆိုရင် သေချာတယ် အောင်မြင် မှာ ။
သူမ မှာ ကွန်ပျူတာ မ ရှိ ဘူး ။
ကျွန်တော် ကောင်းကောင်း သိ နေ တာ က အလုပ် ကြိုးစား တယ် ဆိုတာ လူ တိုင်း မ လုပ် နိုင် ပါ ။
သူ က သူ့ အလုပ် ကို ချစ် တယ် ။
ကျွန်တော် နဲ့ သူ
သူ
```

စာကြောင်းတိုင်းရဲ့ ရှေ့ဆုံးကစာလုံးတွေကိုပဲ ဆွဲထုတ်ယူချင်တယ်ဆိုရင် အစနေရာကို "1" ပေးပြီးတော့၊ range သို့မဟုတ် စာလုံးအရေအတွက်ကိုလည်း "1" အဖြစ် command line argument မှာ ထည့်ပေးယုံပါပဲ။ ဖိုင်နာမည်ကိုလည်း ပေးဖို့ မမေ့ပါနဲ့နော်။ အဲဒါဆိုရင် အောက်ပါအတိုင်း output ရလာပါလိမ့်မယ်။  

```
$ ./get-words-with-position.sh ./my-text.txt 1 1
ကျွန်တော်
ကျွန်မ
သူငယ်ချင်း
သူမ
သူမ
သူ
သူ
သူမ
ကျွန်တော်
သူ
ကျွန်တော်
သူ
```

တကယ်လို့ ရှေ့ဆုံးကနေ စာလုံး ၃လုံးကို ဆွဲထုတ်ယူချင်တယ်ဆိုရင်တော့ "1" "3" ဆိုပြီးတော့ argument ပေးပေးရပါလိမ့်မယ်။  

```
$ ./get-words-with-position.sh ./my-text.txt 1 3
ကျွန်တော် နဲ့ သူ
ကျွန်မ မ သွား
သူငယ်ချင်း အတွက် ဆို
သူမ ရဲ့ နဖူး
သူမ ကို မ
သူ နဲ့ သူမ
သူ သာ ဆိုရင်
သူမ မှာ ကွန်ပျူတာ
ကျွန်တော် ကောင်းကောင်း သိ
သူ က သူ့
ကျွန်တော် နဲ့ သူ
သူ
```

နောက်ထပ် ဥပမာတစ်ခုအနေနဲ့ အစ စာလုံးကို သုံးလုံးမြောက်က လိုချင်လို့ "3" ပေးပြီး၊ စာလုံးနှစ်လုံးကို ဆွဲထုတ်ပေးစေချင်လို့ နောက်ထပ် argument တစ်ခုကိုတော့ "2" ပေးပြီး run ပြထားပါတယ်။ အောက်ပါအတိုင်း ဖိုင်ထဲမှာရှိနေတဲ့ စာကြောင်းတိုင်းက သုံးလုံးမြောက်က စာလုံးတွေနဲ့ နောက်က ကပ်လျှက်ရှိတဲ့ စာလုံးတစ်လုံးကိုလည်း ဆွဲထုတ်ပေးပါလိမ့်မယ်။  

```
$ ./get-words-with-position.sh ./my-text.txt 3 2
သူ နဲ့
သွား ဘူး
ဆို အကုန်
နဖူး မှာ
မ တွေ့
သူမ က
ဆိုရင် သေချာတယ်
ကွန်ပျူတာ မ
သိ နေ
သူ့ အလုပ်
သူ
```

တစ်ခု သတိထားစေချင်တာက စာကြောင်းတိုင်းမှာ ရှိနေတဲ့ စာလုံးအရေအတွက်က တူချင်မှ တူပါလိမ့်မယ်။ အဲဒါကြောင့် ပေးလိုက်တဲ့ argument ရဲ့ position က မဖြစ်နိုင်ဘူးဆိုရင်တော့ အဲဒီလို စာကြောင်းတွေအတွက်က blank line တွေအဖြစ်ပဲ output ကထုတ်ပေးပါလိမ့်မယ်။ အောက်မှာ run ပြထားတာကို လေ့လာကြည့်ပါ။  

```
lar@lar-air:~/tool/bash/4github/set-usage$ ./get-words-with-position.sh ./my-text.txt 10 1



။

တယ်


ဆိုတာ



```

## 30. [count-string-length.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/count-string-length.sh)  

ဖိုင်ထဲမှာ ရှိတဲ့စာကြောင်းတွေ တစ်ကြောင်းချင်းစီရဲ့ no. of character အရေအတွက်ကို သိချင်လို့ ရေးခဲ့တဲ့ bash shell script ပါ။  
ဥပမာ အနေနဲ့ [my-text2.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/my-text2.txt)ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို ရေကြည့်ကြရအောင်။ [my-text2.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/my-text2.txt) ဖိုင်ထဲမှာတော့ အောက်ပါအတိုင်း မြန်မာစာကြောင်း စုစုကြောင်း ၈ကြောင်းရှိပါတယ်။  

```
$ cat ./my-text2.txt
ကခဂဃင
စဆ
ဇဈည
ကျန်းဂန်သာလို့ မာပါစ
$၁၀၀၀
ပညာရေးအသက်အာမခံဟာ ကလေးတွေရဲ့ ပညာရေးအတွက် အထောက်အပံ့ဖြစ်စေမယ့်အာမခံအမျိုးအစားဖြစ်
တက္ကသိုလ်
ဒီနှစ် သင်္ကြန် မကျပါ။
```

count-string-length.sh ပရိုဂရမ်ကို သုံးပြီး စာကြောင်းထဲမှာ ရှိတဲ့ စာလုံး (character) တစ်လုံးချင်းစီကို ရေတွက်ကြည့်မယ်ဆိုရင်တော့ ရေတွက်ချင်တဲ့ ဖိုင်နာမည်ကို argument အနေနဲ့ ပေးပေးယုံပါပဲ။ ဒီနေရာမှာ "တက္ကသိုလ်" နဲ့ "သင်္ကြန်" တိုလို ပါဌ်ဆင့် စာလုံးတွေဆိုရင်တော့ ဆင့်ဖို့အတွက် သုံးထားတဲ့ unicode character (U1039) ကိုလည်းထည့်ရေတွက်မှာ ဖြစ်ပါတယ်။  

```
$ ./count-string-length.sh ./my-text2.txt
5
2
3
20
5
80
9
22
```

## 31. [strip-substring.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/strip-substring.sh)  

string ထဲကနေ substring (စာကြောင်းရဲ့ အစိတ်အပိုင်းတစ်ခု) ကို ပိုင်းဖြတ်ယူဖို့အတွက် ရေးထားခဲ့တဲ့ bash ပရိုဂရမ်ဖြစ်ပါတယ်။  
ခွင့်ပြုထားတဲ့ option က စုစုပေါင်း လေးမျိုးရှိပါတယ်။ အရှည်ရေးမယ်ဆိုရင် front-shortest (စာကြောင်းရဲ့ ရှေ့ဆုံးကနေပြီးတော့ shortest matching)၊ back-shortest (စာကြောင်းရဲ့ နောက်ဆုံးကနေ shortest-matching)၊ front-longest (စာကြောင်းရဲ့ ရှေ့ဆုံးကနေ longest-matching)၊ back-longest (စာကြောင်းရဲ့ နောက်ဆုံးနေရာကနေ longest-matching) ဆိုပြီး option တွေကိုပေးလို့ရပါတယ်။ fs, bs, fl, bl ဆိုပြီးတော့လည်း အတိုရိုက်ပြီး ကိုယ် strip လုပ်ချင်တဲ့ ပုံစံကို သတ်မှတ်ပေးလို့ ရပါတယ်။ run တဲ့အခါမှာ ဘာ option မှာ မပေးရင် help screen ပုံစံမျိုးအနေနဲ့ ခွင့်ပြုထားတဲ့ option တွေကို ပြပေးပါလိမ့်မယ်။  

```
$ ./strip-substring.sh
options: front-shortest|fs, back-shortest|bs, front-longest|fl and back-longest|bl
```

run တဲ့ပုံစံအပြည့်အစုံကတော့ ./strip-substring \[fs|bs|fl|bl\] "string" "sub_string" ဆိုတဲ့ ပုံစံပါ။  

အောက်ပါ ဥပမာက "ကျားဆိုမှကျား" ဆိုတဲ့ စာကြောင်းကနေ "fs" ဆိုတဲ့ option နဲ့ "\*ကျား" (ရှေ့မှာ ရှိချင်တဲ့ စာလုံးရှိပြီး ကျားဆိုတဲ့ စကားလုံးနဲ့ ဆုံးတဲ့) ဆိုတဲ့ Regular Expression နဲ့ ရှာခိုင်းရင် မြင်ရမယ့် output ကို ပြသထားတာဖြစ်ပါတယ်။  

```
$ ./strip-substring.sh fs "ကျားဆိုမှကျား" "*ကျား"
strip_option:fs, string:ကျားဆိုမှကျား, sub_string:*ကျား
stripping from front (shortest match)
ဆိုမှကျား
```

bs option အဖြစ်ပြောင်းပြီး ရှာကြည့်ရင်တော့ အောက်ပါအတိုင်း ရလဒ်ကို ထုတ်ပေးပါလိမ့်မယ်။  

```
$ ./strip-substring.sh bs "ကျားဆိုမှကျား" "*ကျား"
stripping from back (shortest match)
ကျားဆိုမှ
```

fl, bl နဲ့ ရှာကြည့်ရင်တော့ စာကြောင်းတစ်ကြောင်းလုံးကို strip လုပ်သွားတာကို မြင်ကြရပါလိမ့်မယ်။  

```
$ ./strip-substring.sh fl "ကျားဆိုမှကျား" "*ကျား"
stripping from front (longest match)

$ ./strip-substring.sh bl "ကျားဆိုမှကျား" "*ကျား"
stripping from back (longest match)
```

## 32. [chk_total_duration.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/chk_total_duration.sh)  

ဒီ shell script က speaker တစ်ယောက်ချင်းစီရဲ့ အသံဖိုင်တွေ (i.e. .wav) ကို ဖိုလ်ဒါတွေမှာ ခွဲပြီး သိမ်းထားတာက စုစုပေါင်း ဘယ်နှစ်နာရီ၊ ဘယ်နှစ်မိနစ်၊ ဘယ်နှစ်စက္ကန့်လောက် ရှိသလဲ ဆိုတာကို ရှာဖွေဖို့အတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။  

သုံးပုံသုံးနည်းကတော့ wave ဖိုင်တွေ သိမ်းထားတဲ့ ဖိုလ်ဒါတွေရဲ့ root folder မှာ ဒီ chk_total_duration.sh ကို ထားပြီး run ယုံပါပဲ။ တခြား ပရိုဂရမ် parameter လည်း ပေးဖို့ မလိုအပ်ပါဘူး။  

လေ့လာတဲ့သူတွေအတွက် နားလည်ရလွယ်အောင် coding ကို မြန်မာလို comment ရေးပေးပြီး အကျဉ်းရှင်းပြပါမယ်။  


```

# "." က လက်ရှိ ဖိုလ်ဒါ
# -name "*.wav" က .wav extension နဲ့ ဆုံးတဲ့ ဖိုင်နာမည်တွေကို ရှာပေးပါ
# "> wavefiles.txt" က ရှာတွေ့တဲ့ .wav ဖိုင်နာမည်နဲ့တကွ folder path တွေကို wavefiles.txt ဆိုတဲ့ ဖိုင်နာမည်နဲ့ သိမ်းခိုင်းထားတာပါ။
find . -name "*.wav" > wavefiles.txt

# အထက်မှာ သိမ်းခဲ့တဲ့ wavefiles.txt ထဲက ဖိုင်နာမည် တစ်ကြောင်းချင်းစီကို cat command နဲ့ ရိုက်ထုတ်တယ်  
# ပြီးတော့ bash ရဲ့ read ဖတ်ယူပြီး filename ဆိုတဲ့ variable မှာ သိမ်းပါတယ်။ အဲဒီအလုပ်ကို while နဲ့ looping ပတ်ပြီး ဖိုင်နာမည်အားလုံးကို ဖတ်ခိုင်းထားပါတယ်။  
# အဲဒီ ရလာတဲ့ ဖိုင်နာမည်တွေကို "soxi" command ကို pass လုပ်ပြီးတော့ duration ကို စက္ကန့်နဲ့ ရိုက်ပြခိုင်းပါတယ်။  
# -D option က စက္ကန့်နဲ့ ရိုက်ပြပါလို့ လုပ်ခိုင်းထားတာ ဖြစ်ပါတယ်။  
cat ./wavefiles.txt | while read -r filename
#head ./wavefiles.txt | while read -r filename # for checking quickly ...
do
   soxi -D $filename

done > secondsfile #soxi command ကနေ တွက်ပြီး ရလာတဲ့ wave ဖိုင် တစ်ခုချင်းစီရဲ့ duration seconds တွေကို secondsfile ဆိုတဲ့ နာမည်နဲ့ သိမ်းခိုင်းထားတာပါ

# စက္ကန့်ကနေ သူနဲ့ ညီမျှတဲ့ နာရီ၊ မိနစ်၊ စက္ကန်အဖြစ် လူက ဖတ်ရတာ အဆင်ပြေတဲ့ format ကို ပြောင်းတာဖြစ်ပါတယ်။  
sec2hr_min_sec() {
 hr=$(bc <<< "${1}/3600")
 min=$(bc <<< "(${1}%3600)/60")
 sec=$(bc <<< "${1}%60")
 printf "%02d:%02d:%05.2f\n" $hr $min $sec
}

# ကိုယ်ရဲ့ စက်ထဲမဟာ jq ဆိုတာ ရှိတယ်ဆိုရင် jq ကိုသုံးပြီးတော့ ပေါင်းခိုင်းလို့လည်း ရပါတယ်။  
#total_seconds=$(cat ./secondsfile | jq -s 'add' )

# ကျွန်တော်ကတော့ paste ကို သုံးတာက ဘယ်Linux စက်မှာ မဆို အဆင်ပြေမှာမို့ paste command ကိုလည်း သုံးပြထားပါတယ်။  
# -d option မှာ delimiter ကို "+" ပေးပြီး ဖိုင်တစ်ဖိုင်ချင်းစီရဲ့ duration time တွေကို "+" နဲ့ ချိတ်ဆက်ပါတယ်။
# ပြီးတော့မှာ အဲဒီ ချိတ်ဆက်ထားတဲ့ စာကြောင်း အရှည်ကြီးကို bc command ကို pass လုပ်ပြီးတော့ plus လုပ်ခိုင်းတာပါ။  
total_seconds=$(cat ./secondsfile | paste -s -d+ - | bc)
echo $(sec2hr_min_sec $total_seconds)

```

အထက်ပါ script ကို run လိုက်ရင် ထွက်လာမယ့် output ဖိုင်တွေကို အိုက်ဒီယာရအောင် ပြရရင် အောက်ပါအတိုင်းဖြစ်ပါလိမ့်မယ်။  

```
$ head wavefiles.txt 
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2000.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2001.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2002.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2003.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2004.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2005.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2006.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2007.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2008.wav
./S32/S32(2000_2100)/CompanyA-MgMg-M-25-burmese-2009.wav
```

secondsfile ထဲမှာတော့ အောက်ပါ အတိုင်း wave ဖိုင် တစ်ဖိုင်ချင်းစီရဲ့ duration စက္ကန့်တွေကို သိမ်းထားပါလိမ့်မယ်။  

```
$ head secondsfile 
7.192381
4.940045
5.706304
6.588662
9.653696
7.053061
6.635102
5.381224
7.354921
5.009705
```

chk-total-duration.sh ကို run ရင် စကရင်မှာ မြင်ရမယ့် လူတွေအတွက် ဖတ်ရတာအဆင်ပြေတဲ့ နာရီ၊ မိနစ်၊ စက္ကန့် ပုံစံကတော့ အောက်ပါအတိုင်း ဖြစ်ပါတယ်။   

```
$ ./chk-total-duration.sh
58:12:50.01
```

