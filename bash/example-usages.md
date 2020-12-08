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

## 33. [print-sentenceID-count.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/print-sentenceID-count.sh)  

filename စာရင်းတစ်ခုထဲမှာ ရှိနေတဲ့ ဖိုင်နာမည်တွေထဲက SentenceID ကိုဖြတ်ယူပြီး၊ အဲဒီ SentenceID တွေက filename စာရင်းထဲမှာ ဘယ်နှစ်ခါပါဝင်နေသလဲ ဆိုတာကို print လုပ်ဖို့အတွက် ရေးခဲ့ပါတယ်။ လက်တွေ့သုံးခဲ့တာကတော့ ဖိုင်စာရင်းထဲမှာ ရှိနေတာတွေက recording လုပ်ထားတဲ့ waveဖိုင် နာမည်တွေဖြစ်ပြီးတော့၊ အဲဒီ ဖိုင်နာမည်အထဲမှာ ပါဝင်နေတဲ့ စာကြောင်းနံပါတ် (Sentence ID) တစ်ခုချင်းစီအတွက် အသံဘယ်နှစ်ခါသွင်းထားသလဲ ဆိုတာကို သိအောင် ရှာဖွေတဲ့နေရာဖြစ်ပါတယ်။  

ဥပမာအနေနဲ့ wave file ၁၀၀ဖိုင်ရဲ့ နာမည်ကို list လုပ်ပြီးတော့ သိမ်းထားတဲ့ [100-wave-filenames.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/100-wave-filenames.txt) ကိုတင်ပေးထားပါတယ်။  

ဖိုင်နာမည်မှာ ပါနေတာကတော့  
 * Univ1/Univ2 ကတော့ speaker ရဲ့ တက်ရောက်နေတဲ့ တက္ကသိုလ်ရဲ့ နာမည်ပါ  
 * HninHnin, AungAung တို့ကတော့ speaker တွေရဲ့ နာမည်တွေပါ
 * F/M က ယောကျ်ားလေးလား မိန်းကလေးလား ဆိုတဲ့ information ပါ
 * burmese/shan စတာတွေကတော့ speaker ရဲ့ native language (မိခင်ဘာသာစကား) နဲ့ ပတ်သက်ပြီး သိမ်းထားတာပါ
 * file extension ရဲ့ ရှေ့မှာပါဝင်နေတဲ့ နံပါတ်တွေကတော့ sentenceID ဖြစ်ပါတယ်  
 
```
$ head ./100-wave-filenames.txt
/Univ1-HninHnin-F-25-burmese-2637.wav
/Univ1-AungAung-M-20-burmese-1025.wav
/Univ1-Sabai-F-29-burmese-1403.wav
/Univ1-HtetHtet-M-20-burmese-1025.wav
/Univ1-HlaHla-F-20-burmese-1403.wav
/Univ1-NyeinNyein-M-29-Shan-2324.wav
/Univ2-MyintMyint-F-22-burmese-25.wav
/Univ1-SoeMoe-M-23-burmese-1039.wav
/Univ2-Sandar-F-26-burmese-25.wav
/Univ1-Kaung-M-22-burmese-1005.wav
```

run လိုက်ရင် အောက်ပါအတိုင်း ပထမ ကော်လံက sentenceID ဖြစ်ပြီးတော့၊ ဒုတိယ ကော်လံက ပါဝင်နေတဲ့ အကြိမ်အရေအတွက်ဖြစ်ပါတယ်။  

```
$ ./print-sentenceID-count.sh ./100-wave-filenames.txt 
4 2
12 3
25 3
92 1
127 3
154 3
172 1
210 1
223 3
506 1
693 1
1005 1
1006 1
1022 2
1025 2
1039 1
1175 3
1222 1
1403 2
1430 1
1739 4
1792 2
1949 2
1975 11
2018 5
2049 1
2107 3
2324 1
2408 3
2530 1
2540 1
2637 2
2664 1
2975 4
4039 1
5063 1
5404 3
5975 2
6338 3
6776 4
6889 1
9527 1
9587 1
10001 1
10031 1
12671 4
```

## 34. [mk-16KHz-mono.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-16KHz-mono.sh)  

Recording လုပ်ထားတဲ့ wave ဖိုင်တွေကို sampling rate က 16KHz နဲ့ mono channel အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့ပါတယ်။ run လိုက်ရင် လက်ရှိ ရောက်နေတဲ့ path အောက်မှာ ရှိနေတဲ့ ဖိုလ်ဒါတွေအထဲက wave ဖိုင်တွေအားလုံးကို 16KHz နဲ့ mono channel အဖြစ် ပြောင်းပေးပါလိမ့်မယ်။  

Wave ဖိုင်တွေရဲ့ information (သို့) metadata ကို ကြည့်ချင်ရင်တော့ soxi command ကိုသုံးပါတယ်။ soxi ရဲ့အရှည်ကတော့ SoXI - Sound eXchange Information, display sound file metadata ဖြစ်ပါတယ်။ အသံဖိုင်တွေနဲ့ ပတ်သက်ပြီး အသုံးဝင်တဲ့ command တစ်ခုဖြစ်လို့ မှတ်သားထားသင့်ပါတယ်။  

အသံသွင်းပြီး ရလာတဲ့ original ဖိုင်နမူနာအနေနဲ့ 2018-11-13-20\:43\:15.wav ဖိုင်ကို ကြည့်ကြရအောင်။ ဖိုင်နာမည်က recording လုပ်ခဲ့တဲ့ ရက်စွဲ၊ အချိန်နဲ့ သိမ်းထားတာမို့ command line မှာ ရိုက်တဲ့အခါမှာ ":" သင်္ကေတတွေကို "\\" နဲ့ escape လုပ်ပြီးပြပေးပါလိမ့်မယ်။ အဲဒီဖိုင်ရဲ့ metadata ကို soxi command နဲ့ ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။ ဒီနေရာမှာ Sample Rate က 44.1 KHz ဖြစ်ပြီးတော့ Channels ကလည်း 2 (stereo sound) ဖြစ်နေတာကို တွေ့ကြရပါလိမ့်မယ်။  

```
$ soxi ./2018-11-13-20\:43\:15.wav 

Input File     : './2018-11-13-20:43:15.wav'
Channels       : 2
Sample Rate    : 44100
Precision      : 16-bit
Duration       : 00:00:01.17 = 51465 samples = 87.5255 CDDA sectors
File Size      : 206k
Bit Rate       : 1.41M
Sample Encoding: 16-bit Signed Integer PCM
```

[mk-16KHz-mono.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-16KHz-mono.sh) ပရိုဂရမ်ကို run ပြီးတဲ့အခါမှာတော့ အောက်ပါအတိုင်း ပြောင်းလဲသွားတာကို soxi command နဲ့ ပြန်စစ်ဆေးကြည့်လို့ ရပါလိမ့်မယ်။  

```
$ soxi ./2018-11-13-20\:43\:15.16khz.mono.wav 

Input File     : './2018-11-13-20:43:15.16khz.mono.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:01.17 = 18672 samples ~ 87.525 CDDA sectors
File Size      : 37.4k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM
```
လေ့လာချင်သူတွေအတွက် လေ့လာနိုင်အောင် အထက်ပါ wave ဖိုင်နှစ်ဖိုင်ကိုလည်း GitHub ရဲ့ [https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/wave-files/](https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/wave-files) ဖိုလ်ဒါအောက်မှာ တင်ပေးထားပါတယ်။  

[mk-16KHz-mono.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-16KHz-mono.sh) သုံးတဲ့အခါမှာ ကိုယ်run မယ့် folder 
structure ပေါ်ကို မူတည်ပြီး လိုက်လျောညီထွေဖြစ်အောင် လိုအပ်သလို ပြောင်းလဲရမှာ ဖြစ်ပါတယ်။ တကယ်လို့ 16KHz အဖြစ်ပြောင်းချင်တဲ့ wave ဖိုင်တွေက subfolder နှစ်ခုအောက်မှာ ရှိနေတယ်ဆိုရင် folder ဖတ်တဲ့ for loop ကို အောက်ပါအတိုင်း နှစ်ဆင့် လုပ်ပေးရမှာ ဖြစ်ပါတယ်။ ဖိုင် extension နဲ့ ပတ်သက်ပြီးလဲ ပြင်ချင် ရင် ``` for file in *.wav; ``` ဒီလိုင်းကို ဝင်ပြင်ပါ။  

```bash
$ cat mk-16KHz-mono.sh 
#!/bin/bash

# Changing wave files into 16khz and mono
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan

for fd in */ ; do
   cd ./$fd;
      for fd in */ ; do
         cd ./$fd;
         for file in *.wav; do
            filename_only="${file%.*}"
            sox ./$file -b 16 -r 16k -c 1 ./$filename_only.16khz.mono.wav;
            soxi ./$filename_only.16khz.mono.wav;
         done 
            cd ..;
      done
         cd ..;
done
```
တကယ်လို့ 16khz အဖြစ်ပြောင်းပြီးတဲ့အခါမှာ နဂို wave ဖိုင်ကို ဖျက်ပစ်ချင်တယ်ဆိုရင်တော့ အောက်ပါအတိုင်း coding ကို ပြင်နိုင်ပါတယ်။  

```bash
soxi ./$filename_only.16khz.mono.wav && rm ./$file;
```
ရေးထားတာက soxi နဲ့ 16 KHz အဖြစ်ပြောင်းတဲ့အလုပ်က အောင်အောင်မြင်မြင်နဲ့ ပြီးဆုံးခဲ့ရင် (&& ကိုသုံးထားတယ်) rm. /$file ($file က နဂို wave ဖိုင်ကိုညွှန်းတယ်) $file ကိုဖျက်ပါလို့ ရေးထားတာ ဖြစ်ပါတယ်။ နောက်တချက် သတိပေးချင်တာက mk-16KHz-mono.sh ပရိုဂရမ်ကို ထပ်ခါထပ်ခါ run ရင် ဖိုလ်ဒါအောက်မှာရှိနေတဲ့ wave ဖိုင်တွေကို 16KHz အဖြစ် ပြောင်းပေးမှာမို့ မလိုအပ်တဲ့ ဖိုင်တွေက တိုးတိုးလာမှာ ဖြစ်ပါတယ်။ အောက်ပါ ဥပမာလိုမျိုး  

```
a.wav
a.16khz.mono.wav
a..16khz.mono.16khz.mono.wav
```

## 35. [mk-spectrogram.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-spectrogram.sh)  

Wave ဖိုင်တွေကို spectrogram ပုံတွေအဖြစ်ပြောင်းဖို့အတွက် သုံးခဲ့တဲ့ shell script ပါ။ လက်ရှိရောက်နေတဲ့ path အောက်မှာရှိတဲ့ ဖိုလ်ဒါတစ်ခုချင်းစီရဲ့အထဲကို ဝင်ရောက်ပြီး၊ အဲဒီဖိုလ်ဒါတွေအောက်မှာ ရှိနေတဲ့ Wave ဖိုင်တွေကို spectrogram ပုံ (.png) အဖြစ်ပြောင်း၊ ပြီးတော့ jpg အဖြစ် ပြောင်းပေးပါလိမ့်မယ်။ png ဖိုင်တွေကိုတော့ ဖျက်သွားမှာဖြစ်ပါတယ်။ ကျွန်တော်က အဲဒီအချိန်မှာ သုံးတဲ့ transfer learning သုတေသနအတွက်က jpg ဖိုင်ကို သုံးမှာမို့၊ png ကနေ နောက်ထပ် jpg ဖိုင်အဖြစ် ပြောင်းထားတာ ဖြစ်ပါတယ်။ တကယ်လို့ ခင်ဗျားတို့က jpg ဖိုင် မလိုချင်ဘူး၊ png ဖိုင်ကိုပဲ လိုချင်တယ်ဆိုရင် ``` mogrify -strip -quality 80% -sampling-factor 4:4:4 -format jpg ./*.png; ``` လိုင်းကို comment ပိတ်လိုက်ပါ။ ကိုယ်လိုအပ်သလို ပြင်သုံးပါ။ အသုံးဝင်ပါလိမ့်မယ်။  

ရေးထားတဲ့ script ကို အလွယ်ရှင်းပြရရင် sox command နဲ့ ရှိနေတဲ့ wave ဖိုင်ကို spectrogram ပုံအဖြစ်ပြောင်းချင်ရင် အောက်ပါအတိုင်း command ပေးလို့ရပါတယ်။ ထွက်လာတဲ့ png ဖိုင် ကိုတော့ ပုံတွေကိုဖွင့်ကြည့်တဲ့ command တစ်ခုဖြစ်တဲ့ display command နဲ့ ကြည့်လို့ရပါတယ်။  

```
$ sox ./2018-11-13-20\:43\:15.16khz.mono.wav -n spectrogram -r -o ./2018-11-13-20\:43\:15.16khz.mono.png 
$ display ./2018-11-13-20\:43\:15.16khz.mono.png 
```

လေ့လာချင်သူများအတွက် လေ့လာနိုင်အောင် wave ဖိုင်ကနေပြောင်းထားတဲ့ spectrogram ဖိုင်ကိုလည်း GitHub ရဲ့ [https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/wave-files/](https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/wave-files) ဖိုလ်ဒါအောက်မှာ သိမ်းပေးထားပါတယ်။  

[https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/wave-files/2018-11-13-20:43:15.16khz.mono.wav](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/wave-files/2018-11-13-20:43:15.16khz.mono.wav) ဖိုင်က မြန်မာသရအသံ "အာ" ကို recording လုပ်ထားတာ ဖြစ်ပြီးတော့ output အဖြစ်ထွက်လာမယ့် spectrogram ကတော့ အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/wave-files/2018-11-13-20:43:15.16khz.mono.png" alt="Class-1" width="800x" height="513x" />
</p>

## 36. [group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-UCF11.sh)  
[UCF YouTube Action Data Set](https://www.crcv.ucf.edu/data/UCF_YouTube_Action.php) ကို download လုပ်ပြီး ဖြေချလိုက်တဲ့အခါမှာ အားလုံးက ဖိုလ်ဒါ တစ်ခုတည်း အောက်မှာ ရှိနေလို့။ တခါတလေ action classification လုပ်ဖို့ အတွက် action categories အလိုက် movie ဖိုင်တွေ၊ သက်ဆိုင်ရာဖိုင်တွေကို ဖိုလ်ဒါ တစ်ခုချင်းစီ ခွဲသိမ်း ချင်တဲ့ အခါမျိုး ရှိပါတယ်။ group-UCF11.sh အတွက် အဲဒီအတွက် ရေးခဲ့တဲ့ shell script ပါ။  

```bash
./group-UCF11.sh ./UCF11/
```

run ပြီးသွားတဲ့အခါမှာ အောက်ပါအတိုင်း action category ၁၁ မျိုးအတွက် ဖိုလ်ဒါ ၁၁ ခုပေါ်လာပါလိမ့်မယ်။  

```bash
$ ls
biking  Excluded Videos.txt  group-UCF11.sh  jumping  shooting  swing   walk_dog
diving  golf                 juggle          riding   spiking   tennis
```

## 37. [group-within-group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-within-group-UCF11.sh) 
ဒီ ပရိုဂရမ်က အထက်က shell script no. 36 ပြီးတော့ run တဲ့ပရိုဂရမ်ပါ။   
[UCF YouTube Action Data Set](https://www.crcv.ucf.edu/data/UCF_YouTube_Action.php) ကို download လုပ်ပြီး ဖြေချပြီးတော့ [group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-UCF11.sh) ကို run ပြီး action အုပ်စုလိုက်တူတဲ့ ဗီဒီယိုဖိုင်တွေကို category အလိုက်ခွဲပြီးတော့ စုလိုက်ပါတယ်။ အဲဒီ category အထဲမှာမှ ဗီဒီယိုတွေက အားလုံး ၂၅ ဗီဒီယိုစီပါပါတယ်။ ဒီ shell script no. 37 [group-within-group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-within-group-UCF11.sh) က အဲဒီ ဗီဒီယို ၂၅ ဖိုင်ကို ထပ်ပြီးတော့ ခွဲသိမ်းဖို့အတွက် ရေးခဲ့တာပါ။

အဲဒါကြောင့် group-UCF11.sh ကို run ပြီးမှ group-within-group-UCF11.sh ကို run သွားတဲ့ပုံစံပါ။

ဒီ shell script ပရိုဂရမ် နှစ်ပုဒ်က ကျွန်တော်ရဲ့ ဒေါက်တာတန်း ကျောင်းသူ ဆွေဇင်မိုး (UTYCC) ရဲ့ video level GradCam experiment လုပ်စဉ်မှာ pre-processing အလုပ်ဖြစ်တဲ့ ဗီဒီယိုတွေကို အုပ်စုဖွဲ့ဖို့ ရေးခဲ့တဲ့ ပရိုဂရမ်ဖြစ်ပါတယ်။ တကယ့် လက်တွေ့မှာ shell ပရိုဂရမ်ကို အသုံးချတဲ့ ပုံစံကို မြင်စေချင်လို့ GitHub မှာ တင်ပေးလိုက်ပါတယ်။   

[group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-UCF11.sh) run ပြီးတဲ့အခါမှာ action category တစ်ခုချင်းစီအတွက် mpg ဖိုင်နဲ့ xgtf ဖိုင် (provide overlaid text transcription and annotation) တွေကို စုစည်းပေးထားတာကို တွေ့ရပါလိမ့်မယ်။  

ဥပမာ biking ဖိုလ်ဒါထဲကို ဝင်ကြည့်မယ်ဆိုရင် အောက်ပါအတိုင်း  

```bash
/UCF11/biking# ls
v_biking_01_01.mpg   v_biking_06_01.mpg   v_biking_11_03.mpg   v_biking_17_02.mpg   v_biking_21_05.mpg
v_biking_01_01.xgtf  v_biking_06_01.xgtf  v_biking_11_03.xgtf  v_biking_17_02.xgtf  v_biking_21_05.xgtf
v_biking_01_02.mpg   v_biking_06_02.mpg   v_biking_11_04.mpg   v_biking_17_03.mpg   v_biking_21_06.mpg
v_biking_01_02.xgtf  v_biking_06_02.xgtf  v_biking_11_04.xgtf  v_biking_17_03.xgtf  v_biking_21_06.xgtf
v_biking_01_03.mpg   v_biking_06_03.mpg   v_biking_11_05.mpg   v_biking_17_04.mpg   v_biking_21_07.mpg
v_biking_01_03.xgtf  v_biking_06_03.xgtf  v_biking_11_05.xgtf  v_biking_17_04.xgtf  v_biking_21_07.xgtf
v_biking_01_04.mpg   v_biking_06_04.mpg   v_biking_11_06.mpg   v_biking_17_05.mpg   v_biking_21_08.mpg
v_biking_01_04.xgtf  v_biking_06_04.xgtf  v_biking_11_06.xgtf  v_biking_17_05.xgtf  v_biking_21_08.xgtf
v_biking_02_01.mpg   v_biking_06_05.mpg   v_biking_12_01.mpg   v_biking_17_06.mpg   v_biking_21_09.mpg
v_biking_02_01.xgtf  v_biking_06_05.xgtf  v_biking_12_01.xgtf  v_biking_17_06.xgtf  v_biking_21_09.xgtf
...
...
...
v_biking_05_08.mpg   v_biking_11_01.mpg   v_biking_16_05.mpg   v_biking_21_03.mpg   v_biking_25_03.xgtf
v_biking_05_08.xgtf  v_biking_11_01.xgtf  v_biking_16_05.xgtf  v_biking_21_03.xgtf  v_biking_25_04.mpg
v_biking_05_09.mpg   v_biking_11_02.mpg   v_biking_17_01.mpg   v_biking_21_04.mpg   v_biking_25_04.xgtf
v_biking_05_09.xgtf  v_biking_11_02.xgtf  v_biking_17_01.xgtf  v_biking_21_04.xgtf
```

walk_dog ဖိုလ်ဒါအထဲကို ဝင်ကြည့်မယ်ဆိုရင် အောက်ပါအတိုင်း အုပ်စုဖွဲ့ပေးထားတာကို မြင်တွေ့ရပါလိမ့်မယ်။  

```bash
/data/UCF11/walk_dog# ls
v_walk_dog_01_01.mpg   v_walk_dog_06_01.mpg   v_walk_dog_10_04.mpg   v_walk_dog_16_01.mpg   v_walk_dog_20_07.mpg
v_walk_dog_01_01.xgtf  v_walk_dog_06_01.xgtf  v_walk_dog_10_04.xgtf  v_walk_dog_16_01.xgtf  v_walk_dog_20_07.xgtf
v_walk_dog_01_02.mpg   v_walk_dog_06_02.mpg   v_walk_dog_10_05.mpg   v_walk_dog_16_02.mpg   v_walk_dog_21_01.mpg
v_walk_dog_01_02.xgtf  v_walk_dog_06_02.xgtf  v_walk_dog_10_05.xgtf  v_walk_dog_16_02.xgtf  v_walk_dog_21_01.xgtf
v_walk_dog_01_03.mpg   v_walk_dog_06_03.mpg   v_walk_dog_11_01.mpg   v_walk_dog_16_03.mpg   v_walk_dog_21_02.mpg
v_walk_dog_01_03.xgtf  v_walk_dog_06_03.xgtf  v_walk_dog_11_01.xgtf  v_walk_dog_16_03.xgtf  v_walk_dog_21_02.xgtf
...
...
...
v_walk_dog_05_03.mpg   v_walk_dog_10_01.mpg   v_walk_dog_15_02.mpg   v_walk_dog_20_04.mpg   v_walk_dog_25_04.mpg
v_walk_dog_05_03.xgtf  v_walk_dog_10_01.xgtf  v_walk_dog_15_02.xgtf  v_walk_dog_20_04.xgtf  v_walk_dog_25_04.xgtf
v_walk_dog_05_04.mpg   v_walk_dog_10_02.mpg   v_walk_dog_15_03.mpg   v_walk_dog_20_05.mpg
v_walk_dog_05_04.xgtf  v_walk_dog_10_02.xgtf  v_walk_dog_15_03.xgtf  v_walk_dog_20_05.xgtf
v_walk_dog_05_05.mpg   v_walk_dog_10_03.mpg   v_walk_dog_15_04.mpg   v_walk_dog_20_06.mpg
v_walk_dog_05_05.xgtf  v_walk_dog_10_03.xgtf  v_walk_dog_15_04.xgtf  v_walk_dog_20_06.xgtf
```

တကယ်က UCF11 ဒေတာမှာက category တစ်ခုချင်းစီအတွက် ဗီဒီယိုဖိုင်က နှစ်ဆယ့်ငါးမျိုး ပါဝင်နေလို့ အဲဒါတွေကို ထပ်အုပ်စုဖွဲ့ဖို့အတွက် [group-within-group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-within-group-UCF11.sh) ကိုရေးခဲ့ပါတယ်။  


[group-within-group-UCF11.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/group-within-group-UCF11.sh) ကို run ပြီးတဲ့အခါမှာတော့ အောက်ပါအတိုင်း ဗီဒီယိုဖိုင်တွေကို အုပ်စုဖွဲ့ပြီးသားဆိုတာကို တွေ့မြင်ရပါလိမ့်မယ်။  

```bash
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data# cd UCF11
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11# ls
biking  diving  Excluded Videos.txt  golf  juggle  jumping  riding  shooting  spiking  swing  tennis  walk_dog
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11# cd biking/
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/biking# ls
01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/biking# ls ./01/
v_biking_01_01.mpg   v_biking_01_02.mpg   v_biking_01_03.mpg   v_biking_01_04.mpg
v_biking_01_01.xgtf  v_biking_01_02.xgtf  v_biking_01_03.xgtf  v_biking_01_04.xgtf
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/biking# ls ./02/
v_biking_02_01.mpg   v_biking_02_02.xgtf  v_biking_02_04.mpg   v_biking_02_05.xgtf  v_biking_02_07.mpg
v_biking_02_01.xgtf  v_biking_02_03.mpg   v_biking_02_04.xgtf  v_biking_02_06.mpg   v_biking_02_07.xgtf
v_biking_02_02.mpg   v_biking_02_03.xgtf  v_biking_02_05.mpg   v_biking_02_06.xgtf
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/biking# cd ..
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11# cd tennis
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/tennis# ls
01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/tennis# ls ./01
v_tennis_01_01.mpg   v_tennis_01_02.xgtf  v_tennis_01_04.mpg   v_tennis_01_05.xgtf  v_tennis_01_07.mpg
v_tennis_01_01.xgtf  v_tennis_01_03.mpg   v_tennis_01_04.xgtf  v_tennis_01_06.mpg   v_tennis_01_07.xgtf
v_tennis_01_02.mpg   v_tennis_01_03.xgtf  v_tennis_01_05.mpg   v_tennis_01_06.xgtf
root@2223cfe7eb4a:/home/yekyawthu/exp/vgradcam/data/UCF11/tennis# ls ./25
v_tennis_25_01.mpg   v_tennis_25_02.xgtf  v_tennis_25_04.mpg   v_tennis_25_05.xgtf
v_tennis_25_01.xgtf  v_tennis_25_03.mpg   v_tennis_25_04.xgtf  v_tennis_25_06.mpg
v_tennis_25_02.mpg   v_tennis_25_03.xgtf  v_tennis_25_05.mpg   v_tennis_25_06.xgtf
```

## 38. [dot2pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2pic.sh)
ဒီ shell script က ရှေ့မှာ ရေးပြထားတဲ့ ပရိုဂရမ်နံပါတ် 27. [dot2png-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/dot2png-pdf.sh) လိုပါပဲ dot ဖိုင်ကနေ png, eps, svg ဖိုင်တွေ အဖြစ်ပြောင်းဖို့အတွက် ရေးခဲ့တာပါ။ convert လုပ်တာကို စမ်းဖို့အတွက် dot ဖိုင်ရော၊ run လိုက်ပြီးရင် output ဖိုင်တွေအဖြစ်ထွက်လာမယ့် ဖိုင်တွေကိုကော ဥပမာအနေနဲ့ လေ့လာလို့ ရအောင် bash ဖိုင်တွေရဲ့ test-data ဖိုလ်ဒါ အောက်က dot2pic ဖိုလ်ဒါအထဲမှာ upload လုပ်ပေးထားပါတယ်။  

[dot2pic](https://github.com/ye-kyaw-thu/tools/tree/master/bash/test-data/dot2pic) က original dot ဖိုင်နဲ့ convert လုပ်ပြီးတော့ ထွက်လာတဲ့ output graph ပုံတွေက statistical machine translation နဲ့ ပတ်သက်တဲ့ experiment လုပ်တဲ့အခါမှာ ကျောင်းသူတစ်ယောက်က error ဖြစ်နေကြောင်းပြောလို့ debug လုပ်ဖို့အတွက် သုံးခဲ့တဲ့ ဖိုင်တွေဖြစ်ပါတယ်။  

***shell script 39 ကနေ 64 အထိက အချိန်ရတဲ့အခါ ဖြည့်စွက် ရှင်းပြနိုင်အောင် လုပ်ပါမယ်။  

## 64. [crop-pdf.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/crop-pdf.sh)  

pdftk, pdfcrop ပရိုဂရမ်တွေက အသုံးဝင်တဲ့ pdf tool တွေပါ။ ဒီနေရာမှာတော့ pdfcrop ကို သုံးပြီးတော့ empty ဖြစ်နေတဲ့ margin တွေကို ဖြုတ်တာကို shell script ရေးပြထားပါတယ်။ အရင်ဆုံး [example-crop.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/crop-pdf-example/example-crop.pdf) ဖိုင်ကို ဖွင့်ကြည့်ပါ။ စာမျက်နှာ နံပါတ်-၁ နဲ့ နံပါတ်-၂ က SignWriting ကို Myanmar sign language ရဲ့ ဗျည်းနဲ့ တွဲရေးရတဲ့ သရတွေ၊ သူ့တစ်လုံးတည်း ရပ်တည်နိုင်တဲ့ သရထူး တွေကို mapping လုပ်ထားတဲ့ ဇယား ဖြစ်ပါတယ်။ စာမျက်နှာ နံပါတ်-၃ ကတော့ ပဋ္ဌာနပါဠိ (ပထမတွဲ) စာအုပ်ရဲ့ စာမျက်နှာ နံပါတ် ၁၂ ကို pdftk နဲ့ ဖြတ်ယူထားတာပါ ။ နောက်ဆုံး စာမျက်နှာ ဖြစ်တဲ့ စာမျက်နှာ နံပါတ်-၄ ကတော့ Richard Crang, Sheila Lyons-Sobaski, Robert Wise တို့ ရေးသားထားတဲ့ Plant Anatomy (A Concept-Based Approach to the Structure of Seed Plants) ဆိုတဲ့ free online book စာအုပ်ကနေ ဖြတ်ယူထားတဲ့ စာမျက်နှာပါ။  

crop-pdf.sh ကို သုံးပြီးတော့ minimal margin တွေကိုပဲ ဆွဲထုတ်ကြည့်ရအောင်။  

```bash
./crop-pdf.sh ./example-crop.pdf 
PDFCROP 1.38, 2012/11/02 - Copyright (c) 2002-2012 by Heiko Oberdiek.
==> 1 page written on `pg1-crop.pdf'.
PDFCROP 1.38, 2012/11/02 - Copyright (c) 2002-2012 by Heiko Oberdiek.
==> 1 page written on `pg2-crop.pdf'.
PDFCROP 1.38, 2012/11/02 - Copyright (c) 2002-2012 by Heiko Oberdiek.
==> 1 page written on `pg3-crop.pdf'.
PDFCROP 1.38, 2012/11/02 - Copyright (c) 2002-2012 by Heiko Oberdiek.
==> 1 page written on `pg4-crop.pdf'.
```

ဖြတ်ထားပြီးသား output စာမျက်နှာ တစ်မျက်နှာစီကိုလည်း ဖိုင်တစ်ဖိုင်စီအနေနဲ့ သိမ်းပြထားပါတယ်။  
[pg1-crop.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/crop-pdf-example/pg1-crop.pdf)  
[pg2-crop.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/crop-pdf-example/pg2-crop.pdf)  
[pg3-crop.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/crop-pdf-example/pg3-crop.pdf)  
[pg4-crop.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/crop-pdf-example/pg4-crop.pdf)  

Original input PDF ဖိုင်ဖြစ်တဲ့ [example-crop.pdf](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/crop-pdf-example/example-crop.pdf) နဲ့ နှိုင်းယှဉ်ကြည့်ရင် margin တွေက စာတွေ၊ ပုံတွေရှိတဲ့ အပိုင်းတွေနဲ့ကပ်နေတာကို မြင်သာပါလိမ့်မယ်။  

## 65.[excel2csv-chk-fields.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/from65/excel2csv-chk-fields.sh)  

လက်တွေ့ NLP အတွက် ဒေတာတွေကို ပြင်ဆင်ကြတဲ့ အခါမှာ အော်ရဂျင်နယ်ဒေတာတွေက Excel ကို သုံးပြီးတော့ ပြင်ဆင်ကြတာမျိုးလည်း ရှိတတ်ပါတယ်။ အဲဒါကြောင့် အဲဒီဒေတာတွေကို NLP အလုပ်တွေကို လုပ်ဖို့အတွက်က အရင်ဆုံး Excel က ကော်လံတွေ ခွဲပြီး ရိုက်ထားတဲ့ ဒေတာတွေကို csv (comma-separated values) ဖိုင်အဖြစ် ပြောင်းတာမျိုးကို လုပ်ဖို့ လိုအပ်ပါတယ်။ Excel ဖိုင်ကို Excel software သို့မဟုတ် Linux OS ပေါ်မှာဆိုရင် LibreOffice တို့ကို သုံးပြီးတော့ csv ဖိုင်အဖြစ်လည်း ပြောင်းလို့ရပေမဲ့ command line ကနေပဲ Excel ဖိုင် .xlsx ကို csv ဖိုင်အဖြစ် ပြောင်းတတ်ရင် အရမ်းအဆင်ပြေပါတယ်။ Excel ဖိုင်ထဲမှာပဲ xls နဲ့ xlsx က မတူဘူး ဆိုတာကိုတော့ သိထားသင့်ပါတယ်။ ဒီနေရာမှာတော့ မရှင်းပြတော့ပါဘူး။ xlsx ကနေ csv အဖြစ် ပြောင်းဖို့အတွက် က Github မှာရှိတဲ့ Python ပရိုဂရမ် [https://github.com/dilshod/xlsx2csv](https://github.com/dilshod/xlsx2csv) နဲ့ ပြောင်းလို့ ရပါတယ်။ ဒီနေရာမှာ ရေးထားတဲ့ "excel2csv-chk-fields.sh" shell script ကတော့ အဲဒီ xlsx2csv ကို ကိုယ့်စက်ထဲမှာ installed လုပ်ထားပြီးသားအခြေအနေမှာ၊ bash shell script ထဲကနေ ခေါ် run တဲ့ ပုံစံပါ။  

ဒီ script ကို လက်တွေ့သုံးခဲ့တာကတော့ COVID-19 နဲ့ ပတ်သက်တဲ့ App ကို ကျွန်တော် အလုပ်လုပ်နေတဲ့ ထိုင်းအစိုးရသုတေသန NECTEC မှာ develop လုပ်ထားတာ ရှိပါတယ်။ အဲဒီ app အတွက် မြန်မာစာကို ဘာသာပြန်ထည့်ဖို့နဲ့ တခြား အလုပ်တွေအတွက် Excel ဖိုင်ထဲက Sheet တွေကို တစ်ခုချင်းဆွဲထုတ်ဖို့အတွက်သုံးခဲ့ပါတယ်။ sheet တစ်ခုချင်းစီကို csv ဖိုင်အဖြစ် ဖိုလ်ဒါတစ်ခုအောက်မှာ သိမ်းလိုက်ပြီးတော့ အဲဒီ sheet တစ်ခုစီမှာ field ဘယ်နှစ်ခု ပါသလဲ ဆိုတာကို ရေတွက်ဖို့အတွက် လွယ်လွယ်ရေးထားတဲ့ shell script တစ်ပုဒ် ဖြစ်ပါတယ်။ 

Run တဲ့အခါမှာ command line argument နှစ်ခု ပေးရပါလိမ့်မယ်။ ပထမတစ်ခုက Excel ဖိုင်ရဲ့ ဖိုင်နာမည် ဖြစ်ပြီးတော့၊ ဒုတိယ argument ကတော့ output အဖြစ်ထွက်လာမယ့် csv ဖိုင်တွေကို သိမ်းပေးစေချင်တဲ့ ဖိုလ်ဒါနာမည်ပါ။  
```
./xlsx2csv-chk-fields.sh <Excel-filename> <output-folder-name>  
```   

Run လိုက်လို့ ထွက်လာမဲ့ output screen ကို ဥပမာအနေနဲ့ ပြရရင် အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မယ်။  

```bash
$ ./xlsx2csv-chk-fields.sh ./COVID-19_Languages.xlsx output
Converting xlsx file to csv ...
Finished conversion!
==========

./output/แผ่น17.csv
no. of field: 26
./output/App Info.csv
no. of field: 30
./output/contact รพ..csv
no. of field: 27
./output/contact ผู้รับผิดชอบตามเขต.csv
no. of field: 22
./output/รายชื่อผู้รับผิดชอบติดตามผู้เดิ.csv
no. of field: 25
./output/New Recommendation-DDC.csv
no. of field: 27
./output/User Interface.csv
no. of field: 37
./output/USERS.csv
no. of field: 23
```

## 66. [change-format.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/change-format.sh)  

eg.ko.pos.txt ဖိုင်ထဲမှာ ရှိနေတဲ့ format က အောက်ပါအတိုင်းပါ။ ကိုရီးယား စာကြောင်းတွေကို POS tagger တစ်ခုနဲ့ tagging လုပ်ပြီးတော့ ထွက်လာတဲ့ output example ပါ။ တကယ်တမ်း ဒီ POS tag တွေကို machine translation လုပ်တဲ့ အခါမှာ factor (i.e vector) တစ်ခုအနေနဲ့ ယူသုံးဖို့အတွက် model ဆောက်ဖို့အတွက် input ပေးတဲ့ ပုံစံက အောက်ပါပုံစံအတိုင်းမဟုတ်ပဲ word|tag ဆိုတဲ့ ပုံစံပါ။ change-format.sh က လက်ရှိ format ကနေ ကိုယ်လိုချင်တဲ့ ပုံစံတစ်ခုကို ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ bash one line shell script ပါ။  

```
$ cat ./eg.ko.pos.txt
['여름|NNG', '이|JKS', '되|VV', '자|EC', '못|NNG', '의|JKG', '물|NNG', '이|JKS', '다|MAG', '말라|VV+EC', '버렸|VX+EP', '다|EF', '.|SF']
['구급차|NNG', '좀|MAG', '빨리|MAG', '보내|VV+EC', '주|VX', '시|EP', '겠|EP', '어요|EF', '?|SF']
['저|NP', '는|JX', '밥|NNG', '을|JKO', '먹|VV', '었|EP', '습니다|EF', '.|SF']
['학생|NNG', '시절|NNG', '을|JKO', '돌아보|VV', '다|EF', '.|SF']
['모든|MM', '것|NNB', '이|JKS', '내|NP+JKG', '잘못|NNG', '이|VCP', '지|EC', '유구무언|NNG', '이|VCP', '다|EF', '.|SF']
['그|MM', '녀|NNG', '는|JX', '아직|MAG', '사랑니|NNG', '가|JKS', '안|MAG', '났|VV+EP', '다|EF', '.|SF']
['날|NNG', '이|JKS', '새|VV', '니|EC', '맑|VA', '고|EC', '고요|NNG', '한|XSA+ETM', '아침|NNG', '이|VCP', '었|EP', '다|EF', '.|SF']
['이야기|NNG', '소리|NNG', '가|JKS', '가끔|MAG', '창|NNG', '밖|NNG', '으로|JKB', '새|VV', '어|EC', '나왔|VV+EP', '다|EF', '.|SF']
['미얀마|NNP', '나라|NNG', '부탁|NNG', '합니다|XSV+EF', '.|SF']
['햇빛|NNG', '이|JKS', '너무|MAG', '강해서|VA+EC', '손|NNG', '으로|JKB', '해|NNG', '를|JKO', '가리|VV', '고|EC', '걸|VV', '었|EP', '어요|EF', '.|SF']
```

run တဲ့ အခါမှာတော့ အထက်ပါ ဖိုင်ကို ./change-format.sh ပရိုဂရမ်ကို command line argument အနေနဲ့ pass လုပ်ပေးလိုက်ယုံပါပဲ။ output ကတော့ အောက်မှာ ပြထားတဲ့ အတိုင်းပါပဲ။ script ထဲမှာ "cat -" ကိုသုံးပြထားပါတယ်။ cat command ရဲ့ "-" option ကတော့ STDIN ကနေ input ကို accept လုပ်တဲ့ option ဖြစ်ပါတယ်။  

```
$ ./change-format.sh < ./eg.ko.pos.txt
여름|NNG 이|JKS 되|VV 자|EC 못|NNG 의|JKG 물|NNG 이|JKS 다|MAG 말라|VV+EC 버렸|VX+EP 다|EF .|SF
구급차|NNG 좀|MAG 빨리|MAG 보내|VV+EC 주|VX 시|EP 겠|EP 어요|EF ?|SF
저|NP 는|JX 밥|NNG 을|JKO 먹|VV 었|EP 습니다|EF .|SF
학생|NNG 시절|NNG 을|JKO 돌아보|VV 다|EF .|SF
모든|MM 것|NNB 이|JKS 내|NP+JKG 잘못|NNG 이|VCP 지|EC 유구무언|NNG 이|VCP 다|EF .|SF
그|MM 녀|NNG 는|JX 아직|MAG 사랑니|NNG 가|JKS 안|MAG 났|VV+EP 다|EF .|SF
날|NNG 이|JKS 새|VV 니|EC 맑|VA 고|EC 고요|NNG 한|XSA+ETM 아침|NNG 이|VCP 었|EP 다|EF .|SF
이야기|NNG 소리|NNG 가|JKS 가끔|MAG 창|NNG 밖|NNG 으로|JKB 새|VV 어|EC 나왔|VV+EP 다|EF .|SF
미얀마|NNP 나라|NNG 부탁|NNG 합니다|XSV+EF .|SF
햇빛|NNG 이|JKS 너무|MAG 강해서|VA+EC 손|NNG 으로|JKB 해|NNG 를|JKO 가리|VV 고|EC 걸|VV 었|EP 어요|EF .|SF
```

## 67. [format-mecab-pos.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/format-mecab-pos.sh)  

ဂျပန်စာ Part-of-Speech and Morphological Analyzer တစ်ခုဖြစ်တဲ့ Mecab ကနေ ထွက်လာတဲ့ output ကနေ word/pos, word/pos_subpos ပုံစံကို ပြောင်းယူဖို့ ရေးခဲ့ပါတယ်။ ဒီ shell script ကို မသုံးခင်မှာ ကိုယ့်စက်ထဲမှာ အရင်ဆုံး mecab ကို install လုပ်ထားရမှာဖြစ်ပါတယ်။  
Link: [https://taku910.github.io/mecab/](https://taku910.github.io/mecab/)  

အရင်ဆုံး ဂျပန်စာကြောင်း ခြောက်ကြောင်းကို ရိုက်ထည့်ထားတဲ့ example test file ကို cat command နဲ့ ရိုက်ထုတ်ကြည့်ရအောင်။ ဒီဖိုင်ထဲမှာ ရိုက်ထည့်ထားတဲ့ စာကြောင်း ခြောက်ကြောင်းက ဂျပန်-အင်္ဂလိပ်-တရုပ် [basic expression parallel corpus](http://nlp.ist.i.kyoto-u.ac.jp/index.php?%E6%97%A5%E8%8B%B1%E4%B8%AD%E5%9F%BA%E6%9C%AC%E6%96%87%E3%83%87%E3%83%BC%E3%82%BF) အသေးတစ်ခုကနေ ယူထားတာ ဖြစ်ပါတယ်။  

```
$ cat ./jp.test.txt
それがあるようにいつも思います。
勝とうなどと誰が思うか。
彼がその日の夜の話をする。
彼が計画案の提出期限を一年以内としました。
レベル１の機能に下記の機能をプラスする。
１００名の方々が、夏の夜を思いっきり満喫しました。
```

mecab program ကို jp.test.txt ဖိုင်ကို pass လုပ်ပြီးကြည့်ရင် default က အောက်ပါအတိုင်း ဂျပန်စာလုံး တစ်လုံးချင်းစီ အတွက် POS, Sub POS စတာတွေကို စာကြောင်း တစ်ကြောင်းစီ ရိုက်ထုတ်ပြပါလိမ့်မယ်။  

```
$ mecab ./jp.test.txt
それ	名詞,代名詞,一般,*,*,*,それ,ソレ,ソレ
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
ある	動詞,自立,*,*,五段・ラ行,基本形,ある,アル,アル
よう	名詞,非自立,助動詞語幹,*,*,*,よう,ヨウ,ヨー
に	助詞,副詞化,*,*,*,*,に,ニ,ニ
いつも	副詞,一般,*,*,*,*,いつも,イツモ,イツモ
思い	動詞,自立,*,*,五段・ワ行促音便,連用形,思う,オモイ,オモイ
ます	助動詞,*,*,*,特殊・マス,基本形,ます,マス,マス
。	記号,句点,*,*,*,*,。,。,。
EOS
勝と	動詞,自立,*,*,五段・タ行,未然ウ接続,勝つ,カト,カト
う	助動詞,*,*,*,不変化型,基本形,う,ウ,ウ
など	助詞,副助詞,*,*,*,*,など,ナド,ナド
と	助詞,格助詞,引用,*,*,*,と,ト,ト
誰	名詞,代名詞,一般,*,*,*,誰,ダレ,ダレ
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
思う	動詞,自立,*,*,五段・ワ行促音便,基本形,思う,オモウ,オモウ
か	助詞,副助詞／並立助詞／終助詞,*,*,*,*,か,カ,カ
。	記号,句点,*,*,*,*,。,。,。
EOS
彼	名詞,代名詞,一般,*,*,*,彼,カレ,カレ
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
その	連体詞,*,*,*,*,*,その,ソノ,ソノ
日	名詞,非自立,副詞可能,*,*,*,日,ヒ,ヒ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
夜	名詞,副詞可能,*,*,*,*,夜,ヨル,ヨル
の	助詞,連体化,*,*,*,*,の,ノ,ノ
話	名詞,サ変接続,*,*,*,*,話,ハナシ,ハナシ
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
する	動詞,自立,*,*,サ変・スル,基本形,する,スル,スル
。	記号,句点,*,*,*,*,。,。,。
EOS
彼	名詞,代名詞,一般,*,*,*,彼,カレ,カレ
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
計画	名詞,サ変接続,*,*,*,*,計画,ケイカク,ケイカク
案	名詞,接尾,一般,*,*,*,案,アン,アン
の	助詞,連体化,*,*,*,*,の,ノ,ノ
提出	名詞,サ変接続,*,*,*,*,提出,テイシュツ,テイシュツ
期限	名詞,一般,*,*,*,*,期限,キゲン,キゲン
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
一	名詞,数,*,*,*,*,一,イチ,イチ
年	名詞,接尾,助数詞,*,*,*,年,ネン,ネン
以内	名詞,非自立,副詞可能,*,*,*,以内,イナイ,イナイ
と	助詞,格助詞,一般,*,*,*,と,ト,ト
し	動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
まし	助動詞,*,*,*,特殊・マス,連用形,ます,マシ,マシ
た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。	記号,句点,*,*,*,*,。,。,。
EOS
レベル	名詞,一般,*,*,*,*,レベル,レベル,レベル
１	名詞,数,*,*,*,*,１,イチ,イチ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
機能	名詞,サ変接続,*,*,*,*,機能,キノウ,キノー
に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
下記	名詞,一般,*,*,*,*,下記,カキ,カキ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
機能	名詞,サ変接続,*,*,*,*,機能,キノウ,キノー
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
プラス	名詞,一般,*,*,*,*,プラス,プラス,プラス
する	動詞,自立,*,*,サ変・スル,基本形,する,スル,スル
。	記号,句点,*,*,*,*,。,。,。
EOS
１	名詞,数,*,*,*,*,１,イチ,イチ
０	名詞,数,*,*,*,*,０,ゼロ,ゼロ
０	名詞,数,*,*,*,*,０,ゼロ,ゼロ
名	名詞,接尾,助数詞,*,*,*,名,メイ,メイ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
方々	名詞,一般,*,*,*,*,方々,カタガタ,カタガタ
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
、	記号,読点,*,*,*,*,、,、,、
夏	名詞,一般,*,*,*,*,夏,ナツ,ナツ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
夜	名詞,副詞可能,*,*,*,*,夜,ヨル,ヨル
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
思いっきり	副詞,一般,*,*,*,*,思いっきり,オモイッキリ,オモイッキリ
満喫	名詞,サ変接続,*,*,*,*,満喫,マンキツ,マンキツ
し	動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
まし	助動詞,*,*,*,特殊・マス,連用形,ます,マシ,マシ
た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。	記号,句点,*,*,*,*,。,。,。
EOS
```

"-pos" option နဲ့ run မယ် ဆိုရင် mecab ကနေ ထွက်လာတဲ့ ကော်လံ format ကနေမှ general POS tag information ကိုပဲဆွဲထုတ်ယူပြီး word/pos ပုံံစံ (တနည်းအားဖြင့် ပြောရရင် left-to-right စာကြောင်းပုံစံ) နဲ့ ရိုက်ထုတ်ပေးပါလိမ့်မယ်။  

```
$ ./format-mecab-pos.sh -pos ./jp.test.txt
1 それ/名詞 が/助詞 ある/動詞 よう/名詞 に/助詞 いつも/副詞 思い/動詞 ます/助動詞 。/記号 
2 勝と/動詞 う/助動詞 など/助詞 と/助詞 誰/名詞 が/助詞 思う/動詞 か/助詞 。/記号 
3 彼/名詞 が/助詞 その/連体詞 日/名詞 の/助詞 夜/名詞 の/助詞 話/名詞 を/助詞 する/動詞 。/記号 
4 彼/名詞 が/助詞 計画/名詞 案/名詞 の/助詞 提出/名詞 期限/名詞 を/助詞 一/名詞 年/名詞 以内/名詞 と/助詞 し/動詞 まし/助動詞 た/助動詞 。/記号 
5 レベル/名詞 １/名詞 の/助詞 機能/名詞 に/助詞 下記/名詞 の/助詞 機能/名詞 を/助詞 プラス/名詞 する/動詞 。/記号 
6 １/名詞 ０/名詞 ０/名詞 名/名詞 の/助詞 方々/名詞 が/助詞 、/記号 夏/名詞 の/助詞 夜/名詞 を/助詞 思いっきり/副詞 満喫/名詞 し/動詞 まし/助動詞 た/助動詞 。/記号 
```

"-subpos" option နဲ့ run ရင်တော့ အောက်ပါအတိုင်း word/pos_subpos ပုံစံနဲ့ ရိုက်ထုတ်ပေးပါလိမ့်မယ်။  

```
$ ./format-mecab-pos2.sh -subpos ./jp.test.txt
1 それ/名詞_代名詞 が/助詞_格助詞 ある/動詞_自立 よう/名詞_非自立 に/助詞_副詞化 いつも/副詞_一般 思い/動詞_自立 ます/助動詞_* 。/記号_句点 
2 勝と/動詞_自立 う/助動詞_* など/助詞_副助詞 と/助詞_格助詞 誰/名詞_代名詞 が/助詞_格助詞 思う/動詞_自立 か/助詞_副助詞／並立助詞／終助詞 。/記号_句点 
3 彼/名詞_代名詞 が/助詞_格助詞 その/連体詞_* 日/名詞_非自立 の/助詞_連体化 夜/名詞_副詞可能 の/助詞_連体化 話/名詞_サ変接続 を/助詞_格助詞 する/動詞_自立 。/記号_句点 
4 彼/名詞_代名詞 が/助詞_格助詞 計画/名詞_サ変接続 案/名詞_接尾 の/助詞_連体化 提出/名詞_サ変接続 期限/名詞_一般 を/助詞_格助詞 一/名詞_数 年/名詞_接尾 以内/名詞_非自立 と/助詞_格助詞 し/動詞_自立 まし/助動詞_* た/助動詞_* 。/記号_句点 
5 レベル/名詞_一般 １/名詞_数 の/助詞_連体化 機能/名詞_サ変接続 に/助詞_格助詞 下記/名詞_一般 の/助詞_連体化 機能/名詞_サ変接続 を/助詞_格助詞 プラス/名詞_一般 する/動詞_自立 。/記号_句点 
6 １/名詞_数 ０/名詞_数 ０/名詞_数 名/名詞_接尾 の/助詞_連体化 方々/名詞_一般 が/助詞_格助詞 、/記号_読点 夏/名詞_一般 の/助詞_連体化 夜/名詞_副詞可能 を/助詞_格助詞 思いっきり/副詞_一般 満喫/名詞_サ変接続 し/動詞_自立 まし/助動詞_* た/助動詞_* 。/記号_句点 
```

## 68. [cp-config.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/cp-config.sh)  

SMT experiment တွေကို moses toolkit ကို သုံးပြီးတော့ experiment လုပ်တဲ့ အခါမှာ command line ကနေ shell script ရေးပြီး run တဲ့ ပုံစံမျိုးလည်း ရှိပေမဲ့ နောက်ပိုင်း version တွေမှာ ems system လို config ဖိုင်ပြင်ပြီးတော့ run တာက ပိုအဆင်ပြေပါတယ်။ သို့သော် အဲဒီ အတွက် configuration file တွေကို ကြိုတင်ပြင်ဆင်ရပါတယ်။ အကြမ်းမျဉ်းရှင်းပြရရင် configuration ဖိုင်ဆိုတာက machine translation လုပ်တဲ့အခါမှာ ပြင်ရတဲ့ setting ဖိုင်ပါပဲ။ machine translation မှာ လုပ်ရတဲ့ process တွေက အများကြီး၊ မော်ဒယ်ဆောက်ရတာကလည်း အဆင့်ဆင့်မို့လို့ အဲဒီ process တွေ၊ မော်ဒယ် ဆောက်တဲ့ အပိုင်းတစ်ခုချင်းစီနဲ့ ပတ်သတ်ပြီး ညွှန်ကြားပေးရတာပါ။ ဥပမာ parallel data ကို ဘယ် path အောက်မှာထားထားတယ်၊ moses toolkit ကို ဘယ် path အောက်မှာ install လုပ်ထားတယ်၊ language model ကို ဘယ် third party tool ကို သုံးမယ်၊ alignment ကို ဘယ် လို tool နဲ့ ဘယ်လို parmeter တွေနဲ့ run ခိုင်းမယ် စသည်ဖြင့် setting တွေပါ။ မြင်သာအောင် config.baseline (Phrase Based SMT) အတွက် ပြင်ဆင်ထားတဲ့ config template ဖိုင်ရဲ့ ပထမဆုံး အကြောင်း ၅၀ ကို အောက်မှာ ပြထားပါတယ်။  

```
(base) ye@ykt-pro:~/exp/dw-bk-my/data$ cat -n config.baseline | head -n 50
     1	
     2	### directories that contain tools and data
     3	# 
     4	# moses
     5	#moses-src-dir = /home/ros/mosesdecoder
     6	#moses-src-dir = /home/lar/tool/moses/
     7	moses-src-dir = /home/ye/tool/moses-bin/ubuntu-17.04/moses/
     8	
     9	# moses binaries
    10	moses-bin-dir = $moses-src-dir/bin
    11	
    12	# moses scripts
    13	moses-script-dir = $moses-src-dir/scripts
    14	
    15	# directory where GIZA++/MGIZA programs resides
    16	# external-bin-dir = /home/lar/tool/giza-pp-master/mkcls-v2
    17	#external-bin-dir = /home/lar/tool/giza-pp-master/GIZA++-v2
    18	#external-bin-dir = /home/lar/tool/giza-pp-master/
    19	#external-bin-dir = /home/ye/tool/mgiza/mgizapp/bin
    20	external-bin-dir = /home/ye/tool/giza-pp/GIZA++-v2
    21	
    22	# srilm
    23	#srilm-dir = /data/lttools/training/srilm/srilm-1.6.0/bin/i686-m64
    24	#I haven't installed SRILM yet on Deep Learning Box computer
    25	#srilm-dir = /home/ros/tool/srilm-1.7.1/bin/i686-m64
    26	
    27	# irstlm
    28	#irstlm-dir = $moses-src-dir/irstlm/bin
    29	
    30	# randlm
    31	#randlm-dir = $moses-src-dir/randlm/bin
    32	
    33	# kenlm
    34	
    35	lmplz = $moses-bin-dir/lmplz
    36	
    37	# data
    38	#myrk-data = /home/lar/experiment/my-rk/smt1/t9
    39	#mykc-data = /home/lar/experiment/kachin-myanmar/demo-mykc-smt/4demo/
    40	#mykc-data = /home/lar/experiment/kachin-myanmar/demo-mykc-smt/4demo2/
    41	# myrk-data = /media/lar/Transcend/student/lecture/mtrss/pbsmt-demo/pbsmt/data/
    42	#myrk-data = /home/ye/exp/mlrss-smt/MTRSS/pbsmt/data
    43	#myrk-data = /home/ye/data/corpus-ext/zar-zar-hlaing/data-yandex/data
    44	#myrk-data = /home/ye/data/corpus-ext/zar-zar-hlaing/data-google-then
    45	#myrk-data = /home/ye/data/corpus-ext/zar-zar-hlaing/data-systran-then
    46	myrk-data = /home/ye/exp/dw-bk-my/data/dw-bk/10
    47	
    48	### basic tools
    49	#
    50	# moses decoder

```

[cp-config.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/cp-config.sh) က အထက်မှာ ပြထားတဲ့ config.baseline ဖိုင်ထဲကနေ ဝင်ပြင်ချင်တဲ့ လိုင်းတွေကို ပြင်ပြီးတော့ သိမ်းစေချင်တဲ့ path ကို ဖန်တီးပြီး အဲဒီ path အောက်ကို အသစ်ပြင်ထားတဲ့ ဖိုင်ကို ကော်ပီကူးထည့်ပြထားတဲ့ shell script ဖြစ်ပါတယ်။ ပထမဆုံး machine translation သုတေသနကို စပြီးတော့ နားလည်အောင်လုပ်တဲ့ သူတွေအတွက်က experiment ကို တစ်ခေါက်တည်းပဲ run ကြည့်တာမျိုးဆိုရင်တော့ cp-config.sh က ပြင်ဖို့ မလိုပါဘူး။ သို့သော် တကယ်တမ်း သုတေသန စလုပ်ပြီဆိုရင်တော့ အကြိမ်ကြိမ်အခါခါ run ကြရမယ်၊ ပြီးတော့ language pair တွေကလည်း တစ်ခုထက် မက လုပ်ကြရတာမို့ cp-config.sh လို script မျိုးက ရေးတတ်ဖို့ လိုအပ်ပါတယ်။ code ကို ဝင်ဖတ်ပြီး နားလည်ရင်၊ ရေးတတ်သွားရင် researcher တစ်ယောက်အနေနဲ့ အကြိမ်ကြိမ်အခါခါ လုပ်ရမယ့် အလုပ်တွေအတွက် အသုံးဝင်လာပါလိမ့်မယ်။  

sed command ရဲ့ -i option ကို သုံးပြီး ဝင်ပြင်ပါတယ်။ ဥပမာ အောက်ပါ လိုင်းက ./config.baseline ဖိုင်ထဲက လိုင်းနံပါတ် 46 တစ်ကြောင်းလုံး (.\*) ကို ကိုယ်က အစားထိုးပေးစေချင်တဲ့ variable (${str}${i}) နဲ့ replace လုပ်လိုက်တာဖြစ်ပါတယ်။    

```bash
sed -i "46 s|.*|${str}${i}|" ./config.baseline;
```

အောက်ပါလိုင်းကတော့ အဲဒီ အစားထိုးထားတဲ့ လိုင်းကို screen မှာ ရိုက်ပြဖို့အတွက် ရေးထားတဲ့ statement ဖြစ်ပါတယ်။  

```bash
sed -n 46p ./config.baseline;
```

အဲဒီလို ဝင်ပြင်ပြီးသွားတဲ့ အခါမှာ ပြင်ပြီးသွားတဲ့ config.baseline ဖိုင်ကို ကိုယ်သိမ်းပေးစေချင်တဲ့ path အောက်မှာ၊ ကိုယ်က mkdir နဲ့ ဆောက်ထားတဲ့ path အောက်မှာ ဖိုင်အသစ်တစ်ဖိုင်အနေနဲ့ ဝင်ရေးမှာ ဖြစ်ပါတယ်။ အဲဒီ အလုပ်ကို bash script ရဲ့ for loop နဲ့ 1..10 ဆိုပြီးတော့ ၁၀ခါ လုပ်ခိုင်းထားတာ ဖြစ်ပါတယ်။ ၁၀ခါ ဆိုတာက ဒေတာတွေကို အပိုင်းပိုင်း training, development, test ခွဲပြီးတော့ 10-fold-cross validation experiment လုပ်မှာမို့ ၁၀ခါ ခွဲ ပြီး language-pair တစ်ခုကို run ခိုင်းမှာမို့ပါ။  

```bash
   for i in {1..10}
   do
      sed -i "46 s|.*|${str}${i}|" ./config.baseline;
      echo "Added following line to line no. 45 of \"./config.baseline\" file ...";
      sed -n 46p ./config.baseline;
      echo
      echo "Copying ./config.baseline to ./$f/$i/ ...";
      cp ./config.baseline ./$f/$i/;
```

run လို ပြီးသွားတဲ့ အခါမှာ config.baseline ဖိုင်က ရှိနေမယ့် path ကို မြင်သာအောင် folder structure ကို tree command နဲ့ အောက်ပါအတိုင်း ပြထားပါတယ်။ ပထမဆုံး ထိပ်ဆုံးမှာ တွေ့ရတဲ့ config.baseline က cp.config.sh က ဝင်ပြင်တဲ့ configuration template ဖိုင်ဖြစ်ပါတယ်။ နောက်ထပ် တွေ့ကြရမယ့် 1/ ဖိုလ်ဒါအောက်က၊ 10/ ဖိုလ်ဒါအောက်က၊ 2/ ဖိုလ်ဒါအောက်က config.baseline ဖိုင်တွေကတော့ update လုပ်ထားပြီး ကော်ပီကူးထားတဲ့ config ဖိုင်တွေ ဖြစ်ပါတယ်။ အဲဒီ ဖိုင်တွေက တစ်ဖိုင်နဲ့ တစ်ဖိုင် တူမှာ မဟုတ်ပါဘူး။   

```
(base) ye@ykt-pro:~/exp/dw-bk-my/data$ tree -L 3 | head -60
.
├── config.baseline
├── cp-config.sh
├── DELETE-ALL.sh
├── dw-bk
│   ├── 1
│   │   ├── baseline
│   │   ├── config.baseline
│   │   ├── dev.bk
│   │   ├── dev.dw
│   │   ├── generate_configs.pl
│   │   ├── run1.log
│   │   ├── run-baseline.pl
│   │   ├── run-pbsmt.sh
│   │   ├── steps
│   │   ├── test.bk
│   │   ├── test.dw
│   │   ├── test-sgm
│   │   ├── train.bk
│   │   └── train.dw
│   ├── 10
│   │   ├── baseline
│   │   ├── config.baseline
│   │   ├── dev.bk
│   │   ├── dev.dw
│   │   ├── generate_configs.pl
│   │   ├── run1.log
│   │   ├── run-baseline.pl
│   │   ├── run-pbsmt.sh
│   │   ├── steps
│   │   ├── test.bk
│   │   ├── test.dw
│   │   ├── test-sgm
│   │   ├── train.bk
│   │   └── train.dw
│   ├── 2
│   │   ├── baseline
│   │   ├── config.baseline
│   │   ├── dev.bk
│   │   ├── dev.dw
│   │   ├── generate_configs.pl
│   │   ├── run1.log
│   │   ├── run-baseline.pl
│   │   ├── run-pbsmt.sh
│   │   ├── steps
│   │   ├── test.bk
│   │   ├── test.dw
│   │   ├── test-sgm
│   │   ├── train.bk
│   │   └── train.dw
│   ├── 3
│   │   ├── baseline
│   │   ├── config.baseline
│   │   ├── dev.bk
│   │   ├── dev.dw
│   │   ├── generate_configs.pl
│   │   ├── run1.log
│   │   ├── run-baseline.pl
│   │   ├── run-pbsmt.sh
│   │   ├── steps

```

## 70. [trim-silence.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/trim-silence.sh)  

ပုံမှန်အားဖြင့်က ASR, TTS စတဲ့ speech processing သုတေသနအလုပ်တွေအတွက် စာကြောင်းတစ်ကြောင်းစီကို wave ဖိုင်တစ်ဖိုင်စီအနေနဲ့ အသံဖမ်းထားပြီး အလုပ်လုပ်ကြတာက များပါတယ်။ ဖမ်းထားတဲ့ အသံဖိုင်တွေရဲ့ ရှေ့ပိုင်းမှာ၊ နောက်ပိုင်းမှာ ရှိနေတဲ့ silence အပိုင်းတွေကို ဖြတ်ထုတ်ပေးကြရတဲ့ အခါမျိုး ရှိပါတယ်။ တစ်ဖိုင်ချင်းစီကို လိုက်ဖြတ်နေဖို့ဆိုတာက လက်တွေ့မှာ မဖြစ်နိုင်ပါဘူး အဲဒါကြောင့် shell, perl, python script တွေရေးပြီး လုပ်ကြရပါတယ်။ ဒီ shell script ကတော့ ဥပမာအနေနဲ့ ဖိုလ်ဒါ တစ်ခုအောက်မှာ ရှိနေတဲ့ wave ဖိုင်တွေမှာရှိနေတဲ့ silence အပိုင်းတွေကို ဖြတ်ထုတ်ပြထားတဲ့ shell script ဖြစ်ပါတယ်။ အသုံးဝင်ပါလိမ့်မယ်။  

ဥပမာ ။ ။ ./wave4trim/ ဖိုလ်ဒါထဲမှာ မြန်မာနာမည်တွေကို ဖတ်ပြီး အသံဖမ်းထားတဲ့ wave ဖိုင် ၁၀ဖိုင်ရှိပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/datapreparationsample$ tree ./wave4trim/
./wave4trim/
├── ကောင်းပြည့်စုံ.wav
├── ကျော်စွာဟိဏ်း.wav
├── ကျော်ဇင်မိုး.wav
├── ကျော်လုဇော်.wav
├── ကျော်ဝေယံလင်း.wav
├── ခင်စောလင်း.wav
├── ခင်မာလာကြွယ်.wav
├── တင်နီနီကျော်.wav
├── နန်းရွှေရည်.wav
└── နှင်းနှင်းရည်.wav

0 directories, 10 files
```
run မယ်ဆိုရင်တော့ အောက်ပါအတိုင်း wave file တွေသိမ်းထားတဲ့ ဖိုလ်ဒါကို command line argument အနေနဲ့ပေးပြီး run ပါ။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/datapreparationsample$ bash ./trim-silence.sh ./wave4trim/
trim silence for ./wave4trim//ကောင်းပြည့်စုံ.wav
trimmed filename: ကောင်းပြည့်စုံ.trim.wav
trim silence for ./wave4trim//ကျော်စွာဟိဏ်း.wav
trimmed filename: ကျော်စွာဟိဏ်း.trim.wav
trim silence for ./wave4trim//ကျော်ဇင်မိုး.wav
trimmed filename: ကျော်ဇင်မိုး.trim.wav
trim silence for ./wave4trim//ကျော်လုဇော်.wav
trimmed filename: ကျော်လုဇော်.trim.wav
trim silence for ./wave4trim//ကျော်ဝေယံလင်း.wav
trimmed filename: ကျော်ဝေယံလင်း.trim.wav
trim silence for ./wave4trim//ခင်စောလင်း.wav
trimmed filename: ခင်စောလင်း.trim.wav
trim silence for ./wave4trim//ခင်မာလာကြွယ်.wav
trimmed filename: ခင်မာလာကြွယ်.trim.wav
trim silence for ./wave4trim//တင်နီနီကျော်.wav
trimmed filename: တင်နီနီကျော်.trim.wav
trim silence for ./wave4trim//နန်းရွှေရည်.wav
trimmed filename: နန်းရွှေရည်.trim.wav
trim silence for ./wave4trim//နှင်းနှင်းရည်.wav
trimmed filename: နှင်းနှင်းရည်.trim.wav
```

ဖြတ်ထားတဲ့ ဖိုင်တွေကိုတော့ အော်ရဂျင်နယ် wavefile ရဲ့ basename ရဲ့ နောက်မှာ ".trim.wav" ဆိုတဲ့ extension နဲ့ သိမ်းပေးပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/datapreparationsample$ tree ./wave4trim/
./wave4trim/
├── ကောင်းပြည့်စုံ.trim.wav
├── ကောင်းပြည့်စုံ.wav
├── ကျော်စွာဟိဏ်း.trim.wav
├── ကျော်စွာဟိဏ်း.wav
├── ကျော်ဇင်မိုး.trim.wav
├── ကျော်ဇင်မိုး.wav
├── ကျော်လုဇော်.trim.wav
├── ကျော်လုဇော်.wav
├── ကျော်ဝေယံလင်း.trim.wav
├── ကျော်ဝေယံလင်း.wav
├── ခင်စောလင်း.trim.wav
├── ခင်စောလင်း.wav
├── ခင်မာလာကြွယ်.trim.wav
├── ခင်မာလာကြွယ်.wav
├── တင်နီနီကျော်.trim.wav
├── တင်နီနီကျော်.wav
├── နန်းရွှေရည်.trim.wav
├── နန်းရွှေရည်.wav
├── နှင်းနှင်းရည်.trim.wav
└── နှင်းနှင်းရည်.wav

0 directories, 20 files
```

## 71. [wav2wavform.sh](https://github.com/ye-kyaw-thu/tools/edit/master/bash/wav2wavform.sh)  

wave ဖိုင်ကနေ waveform ပုံစံအဖြစ် ffmpeg ပရိုဂရမ်ကို သုံးပြီးတော့ ပြောင်းပြထားတဲ့ shell script ဖြစ်ပါတယ်။ တစ်ခါတလေမှာ wave ဖိုင်တွေကို waveform ပုံစံအဖြစ်ပြောင်းပြီးတော့ မျက်လုံးနဲ့ သေချာအောင် စစ်ဆေးဖို့ လိုအပ်တဲ့အခါမျိုးမှာအသုံးဝင်ပါလိမ့်မယ်။ ဥပမာ အနေနဲ့ အထက်မှာ ရေးပြထားခဲ့တဲ့ shell script နံပါတ် ၇၀ ရဲ့ output ဖြစ်တဲ့ wave ဖိုင်ရဲ့ အစပိုင်း၊ နောက်ဆုံးပိုင်းတွေမှာ ရှိနေတဲ့ silence ဖြစ်နေတဲ့အပိုင်းတွေကို ဖြတ်ထုတ်ထားတဲ့ trim.wav ဖိုင်ရဲ့ waveform နဲ့ အော်ရဂျင်နယ် silence ပိုင်းတွေကို မဖြတ်ထုတ်ရသေးတဲ့ wav ဖိုင်တွေကို နှိုင်းယှဉ်ကြည့်ကြရအောင်။   

run မယ်ဆိုရင်တော့ ဖိုလ်ဒါနာမည်ကို command line argument အဖြစ်ပေးပြီးတော့ run ပါ။ run တဲ့အခါမှာ အောက်ပါကဲ့သို့ မော်နီတာ screen မှာ wave ဖိုင်တစ်ဖိုင်ချင်းစီကို ပုံအဖြစ်ပြောင်းပေးသွားတဲ့ information တွေကိုမြင်တွေ့ရပါလိမ့်မယ်။ ဒီနေရာမှာတော့ နေရာသက်သာအောင် ဖိုလ်ဒါထဲက ထိပ်ဆုံးတစ်ဖိုင်နဲ့ နောက်ဆုံး တစ်ဖိုင်စာကိုပဲ ပြထားပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/datapreparationsample$ bash ./wav2wavform.sh ./wave4trim/
drawing waveform for ./wave4trim//ကောင်းပြည့်စုံ.trim.wav
ffmpeg version 3.4.6-0ubuntu0.18.04.1 Copyright (c) 2000-2019 the FFmpeg d evelopers
  built with gcc 7 (Ubuntu 7.3.0-16ubuntu3)
  configuration: --prefix=/usr --extra-version=0ubuntu0.18.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Guessed Channel Layout for Input Stream #0.0 : mono
Input #0, wav, from './wave4trim//ကောင်းပြည့်စုံ.trim.wav':
  Duration: 00:00:02.31, bitrate: 705 kb/s
    Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, mono, s16, 705 kb/s
Stream mapping:
  Stream #0:0 (pcm_s16le) -> showwavespic
  showwavespic -> Stream #0:0 (png)
Press [q] to stop, [?] for help
Output #0, image2, to './wave4trim//ကောင်းပြည့်စုံ.trim.png':
  Metadata:
    encoder         : Lavf57.83.100
    Stream #0:0: Video: png, rgba, 640x120 [SAR 1:1 DAR 16:3], q=2-31, 200 kb/s, 68.91 fps, 68.91 tbn, 68.91 tbc
    Metadata:
      encoder         : Lavc57.107.100 png
frame=    1 fps=0.0 q=-0.0 Lsize=N/A time=00:00:00.01 bitrate=N/A speed=1.58x    
video:2kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
...
...
...
drawing waveform for ./wave4trim//နှင်းနှင်းရည်.wav
ffmpeg version 3.4.6-0ubuntu0.18.04.1 Copyright (c) 2000-2019 the FFmpeg developers
  built with gcc 7 (Ubuntu 7.3.0-16ubuntu3)
  configuration: --prefix=/usr --extra-version=0ubuntu0.18.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Guessed Channel Layout for Input Stream #0.0 : mono
Input #0, wav, from './wave4trim//နှင်းနှင်းရည်.wav':
  Duration: 00:00:04.36, bitrate: 705 kb/s
    Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, mono, s16, 705 kb/s
Stream mapping:
  Stream #0:0 (pcm_s16le) -> showwavespic
  showwavespic -> Stream #0:0 (png)
Press [q] to stop, [?] for help
Output #0, image2, to './wave4trim//နှင်းနှင်းရည်.png':
  Metadata:
    encoder         : Lavf57.83.100
    Stream #0:0: Video: png, rgba, 640x120 [SAR 1:1 DAR 16:3], q=2-31, 200 kb/s, 68.91 fps, 68.91 tbn, 68.91 tbc
    Metadata:
      encoder         : Lavc57.107.100 png
frame=    1 fps=0.0 q=-0.0 Lsize=N/A time=00:00:00.01 bitrate=N/A speed=1.73x    
video:2kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown

```

output တွေအနေနဲ့ argument ပေးလိုက်တဲ့ ဖိုလ်ဒါအောက်မှာပဲ .png extension နဲ့ ပုံဖိုင်တွေကို သိမ်းပေးပါလိမ့်မယ်။ အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/datapreparationsample$ tree ./wave4trim/
./wave4trim/
├── ကောင်းပြည့်စုံ.png
├── ကောင်းပြည့်စုံ.trim.png
├── ကောင်းပြည့်စုံ.trim.wav
├── ကောင်းပြည့်စုံ.wav
├── ကျော်စွာဟိဏ်း.png
├── ကျော်စွာဟိဏ်း.trim.png
├── ကျော်စွာဟိဏ်း.trim.wav
├── ကျော်စွာဟိဏ်း.wav
├── ကျော်ဇင်မိုး.png
├── ကျော်ဇင်မိုး.trim.png
├── ကျော်ဇင်မိုး.trim.wav
├── ကျော်ဇင်မိုး.wav
├── ကျော်လုဇော်.png
├── ကျော်လုဇော်.trim.png
├── ကျော်လုဇော်.trim.wav
├── ကျော်လုဇော်.wav
├── ကျော်ဝေယံလင်း.png
├── ကျော်ဝေယံလင်း.trim.png
├── ကျော်ဝေယံလင်း.trim.wav
├── ကျော်ဝေယံလင်း.wav
├── ခင်စောလင်း.png
├── ခင်စောလင်း.trim.png
├── ခင်စောလင်း.trim.wav
├── ခင်စောလင်း.wav
├── ခင်မာလာကြွယ်.png
├── ခင်မာလာကြွယ်.trim.png
├── ခင်မာလာကြွယ်.trim.wav
├── ခင်မာလာကြွယ်.wav
├── တင်နီနီကျော်.png
├── တင်နီနီကျော်.trim.png
├── တင်နီနီကျော်.trim.wav
├── တင်နီနီကျော်.wav
├── နန်းရွှေရည်.png
├── နန်းရွှေရည်.trim.png
├── နန်းရွှေရည်.trim.wav
├── နန်းရွှေရည်.wav
├── နှင်းနှင်းရည်.png
├── နှင်းနှင်းရည်.trim.png
├── နှင်းနှင်းရည်.trim.wav
└── နှင်းနှင်းရည်.wav

0 directories, 40 files
```
  
  
ဥပမာအနေနဲ့ "ကောင်းပြည့်စုံ.png" (trim မလုပ်ခင်) ဖိုင်နဲ့ "ကောင်းပြည့်စုံ.trim.png" (silence အပိုင်းကို trim လုပ်ပြီးသား) waveform တွေကို နှိုင်းယှဉ်ကြည့်ရင် အောက်ပါအတိုင်း အစပိုင်း၊ နောက်ဆုံးအပိုင်းမှာ ရှိနေတဲ့ silence အပိုင်းတွေကို ဖြတ်ထုတ်သွားကြောင်းကို ရှင်းရှင်းလင်းလင်း မြင်ရပါလိမ့်မယ်။   


<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/compare-before-after-trim.png" alt="Comparison between before silence trim and after trim" width="812x180"/>
<p align="center"> Fig. Comparison between before and after silence part trimmed </p>  

## 72. [mytext2pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytext2pic.sh)  

PDF ဖိုင်တွေကနေ ရေးထားတဲ့ မြန်မာစာတွေကို OCR လုပ်မယ့် experiment တွေအတွက် အသုံးဝင်ပါလိမ့်မယ်။ ဒီနေရာမှာတော့ latex ဖိုင်ထဲက "\def" tag ကို shell script ကနေ pass လုပ်တဲ့ ပုံစံကို သုံးပြထားပါတယ်။ ဒီ shell script ကို run ဖို့အတွက် ဖိုင် ၂ဖိုင် လိုအပ်ပါလိမ့်မယ်။ တစ်ဖိုင်ကတော့ အောက်ပါ latex ဖိုင်ပါ။  

```
\ifdefined\mytext
\else
    \def\mytext{မြန်မာစာ}
\fi

\documentclass[border=2pt]{standalone}

\usepackage{varwidth}
\usepackage{fontspec}
\newfontfamily {\myanmarsar}[Script=Myanmar]{Myanmar3}

\begin{document}
\begin{varwidth}{\linewidth}
{\myanmarsar  {\mytext} }
\end{varwidth}

\end{document}
```

latex ကလည်း ကွန်ပျူတာသမားတွေအနေနဲ့ သိထားသင့်ပါတယ်။ အထူးသဖြင့်တော့ စာတမ်းတွေကို format သေသေချာချာပြင်ဆင်ပြီးရေးဖို့အတွက်၊ သင်္ချာဖော်မြူလာတွေကို လှလှပပ ကိုယ့်စာတမ်းထဲမှာ ထည့်ဖို့အတွက် အလွန်အသုံးဝင်ပါတယ်။ အဲဒါကြောင့် research paper ကောင်းကောင်းရေးမယ်လို့ ရည်ရွယ်ထားသူတွေကတော့ ကောင်းကောင်းသုံးတတ်သင့်ပါတယ်။ ဒါ့အပြင့် ပြမယ့် ဥပမာလိုမျိုး PDF ဖိုင်ထုတ်ဖို့ကိစ္စတွေ၊ ပုံဖိုင်တွေ ထုတ်ဖို့ ကိစ္စတွေအတွက်လည်း အသုံးဝင်ပါတယ်။ ဒီနေရာမှာ latex နဲ့ ပတ်သက်ပြီးတော့ အရှည်ရှင်းမပြတော့ပါဘူး။ တချို့ပွိုင့်တွေကိုပဲ ရှင်းပြပါမယ်။  

* "\ifdefined" က "\mytext" ဆိုတဲ့ tag က define လုပ်ထားပြီးသား ဟုတ်မဟုတ် စစ်တဲ့ tag ပါ
* "\usepackage" က latex ရဲ့ package တွေကို ခေါ်သုံးတဲ့ tag ပါ
* "varwidth" package က "minipage" လို package ပါ။ စာမျက်နှာ တစ်မျက်နှစ်စာမျိုး မဟုတ်ပဲ လိုတဲ့ အပိုင်းလေးကိုပဲ print လုပ်ဖို့အတွက် သုံး ပါတယ်။ အသေးစိတ်က  "varwidth" link: [https://ctan.org/pkg/varwidth?lang=en](https://ctan.org/pkg/varwidth?lang=en) ကို လေ့လာပါ
* "fontspec" က ကိုယ်သုံးချင်တဲ့ ဖောင့်ကို declare လုပ်ပြီး သုံးးဖို့အတွက် လိုအပ်တဲ့ package ပါ
* "\newfontfamily" tag ကို သုံးဖို့အတွက်က "fontspec" package လိုအပ်ပါတယ်

အထက်ပါ latex ဖိုင်ကိုလည်း github မှာတင်ပေးထားပါတယ်။  
[https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytext.tex](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytext.tex)  

latex ဖိုင်အပြင် နောက်ထပ်လိုအပ်တဲ့ ဖိုင်ကတော့ ကိုယ်ပုံတွေအဖြစ်သိမ်းချင်တဲ့ မြန်မာစာကြောင်းတွေကို တစ်ကြောင်းချင်းစီရိုက်ထည့်ထားတဲ့ text ဖိုင်တစ်ဖိုင်ပါ။  
ဥပမာအနေနဲ့ စာကြောင်း ၅ကြောင်း ရိုက်ထည့်ပြထားတဲ့ ဖိုင်ကိုလည်း github မှာ တင်ပေးထားပါတယ်။  
Link: [https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytxt4png.txt](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mytxt4png.txt)  

ဖိုင်ထဲမှာ ဥပမာအဖြစ် ရိုက်ထည့်ထားတဲ့ မြန်မာစာကြောင်းတွေကတော့ အောက်ပါအတိုင်းပါ။ "varwidth" package ရဲ့ အလုပ်လုပ်ပုံကို မြင်သာအောင်လို့ character တစ်လုံးထဲရှိတဲ့ စာကြောင်းကော၊ တော်တေါ်ရှည်တဲ့ စာကြောင်းအရှည်ကောကို ရိုက်ထည့်ထားပါတယ်။   

```
က
ခ
ဂ
ကျောင်းဖတ်စာနဲ့ မြန်မာ့ပညာရေးသင်ရိုးထဲက နိုင်ငံရေး
၂၀၂၀ ပြည့်နှစ် ဇွန်လ ၇ ရက်နေ့မှာ ကမ္ဘာရဲ့ အနက်ရှိုင်းဆုံး သမုဒ္ဒရာ ကြမ်းပြင် ဖြစ်တယ်လို့ သတ်မှတ်ထားကြတဲ့ ချယ်လန်ဂျာ ဒိ(ပ်) ရှိရာ ပေ ၃၅,၈၁၀ ရေအနက်ကို ဆင်းခဲ့သူ ဒေါက်တာ ကက်သီ ဆူလီဗန်ဟာ အာကာသပေါ်နဲ့ ကမ္ဘာရဲ့ အနက်ရှိုင်းဆုံး နေရာနှစ်ခုစလုံးကို ပထမဆုံးရောက်သူ ဖြစ်လာခဲ့ပါတယ်။
```

xelatex ကို သုံးပြီးတော့ tex ဖိုင်ကို compile လုပ်ဖို့ ရေးထားတာမို့ ကိုယ့်စက်ထဲမှာ xelatex ကိုတော့ install လုပ်ထားရပါလိမ့်မယ်။ xelatex မဟုတ်ရင်လည်း pdflatex စတဲ့ latex compiler တစ်ခုခုရှိနေရင်လည်း အိုကေပါတယ်။ shell script အထဲက "xelatex" နေရာမှာ "pdflatex" ဆိုတဲ့ စကားလုံးနဲ့ အစားထိုးပါ။ run ပုံ run နည်းကတော့ အောက်ပါအတိုင်း command ပေးပါ။  

```
$bash ./mytext2pic.sh ./mytxt4png.txt
```

အဆင်ပြေပြေနဲ့ run ပြီးသွားရင် စာကြောင်း တစ်ကြောင်းချင်းစီအတွက် png ဖိုင်တွေကို output အဖြစ် ရလာပါလာလိမ့်မယ်။  
အောက်ပါအတိုင်းပါ။  

Filename: line1.png  
<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/line1.png" /></kbd>

Filename: line2.png  
<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/line2.png" /></kbd>  

Filename: line3.png  
<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/line3.png" /></kbd>  

Filename: line4.png  
<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/line4.png" /></kbd>  

Filename: line5.png  
<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/line5.png" /></kbd>  

## 73. [formula-pic.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/formula-pic.sh)  

math formula တွေကို latex format နဲ့ရေးပြီး shell script ကို command line ကနေ pass လုပ်ပေးလိုက်ယုံနဲ့ png ဖိုင်၊ pdf ဖိုင်တွေအဖြစ် အလွယ်တကူဖန်တီးလို့ ရကြောင်းကို ဥပမာ အနေနဲ့ ရေးပြထားတာပါ။ run တဲ့ ပုံစံ ဥပမာ တွေကတော့ အောက်ပါအတိုင်းပါ။  

latex math syntax နဲ့ ရေးထားတဲ့ Statistical Machine Translation (SMT) ဖော်မြူလာကို pass လုပ်ကြည့်ရအောင်။  

```
bash ./formula-pic.sh "\tilde{e} = arg \max_{e} P(e|f) = arg \max_{e} P(f|e) P(e)"
```

အောက်ပါ ပုံကို output ပုံအဖြစ် ထုတ်ပေးပါလိမ့်မယ်။  

<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/stastical-mt.png" /></kbd>  

Statistical Automatic Speech Recognition (Statistical ASR) ကို ကိုယ်စားပြုတဲ့ ဖော်မြူလာကို pass လုပ်ကြည့်ရအောင်။  

```
bash ./formula-pic.sh "W^* = arg \max_{W} P(W/X) = arg \max_{W} P(X/W) P(W)"
```

အောက်ပါ ပုံကို output ပုံအဖြစ် ထုတ်ပေးပါလိမ့်မယ်။  

<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/statistical-asr.png" /></kbd>  

Deep Learning ကို အခြေခံတဲ့ Text to Speech (TTS) ဖော်မြူလာကို ./formula-pic.sh shell script ကို argument ပေးပြီး run ကြည့်ကြရအောင်။  

```
bash ./formula-pic.sh "X = arg \max P(X|Y, \theta)"
```

အောက်ပါ ပုံကို output ပုံအဖြစ် ထုတ်ပေးပါလိမ့်မယ်။  

<kbd><img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/deeplearning-tts.png" /></kbd>  

## 74. [rm-heading-tab-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-heading-tab-lineno.sh)  

line_no.txt ဖိုင်ထဲမှာ စာကြောင်းရဲ့ အစပိုင်းမှာ tab, space နဲ့ လိုင်းနံပါတ်တွေ တပ်ထားတယ်လို့ ဆိုကြပါစို့။  

```
(base) ye@ykt-pro:/media/ye/Transcend/exp/my-ch/data/data/chin/prepare/10-fold$ cat ./line_no.txt 
	Nak-tu-kah motor thar chu va en ka tum a.
	Eng chungchang nge min hrilh i tum a?
  Kei pawh kha-tiang kha ka rin dan chiah a ni.
 14998 Hei hian min tibuai .
 14999 Anni chu engti khawpin nge an rilru a that ?
 15000 Ani chu ka u alawm .
 ```

အဲဒီလို heading space, tab, လိုင်းနံပါတ်တွေကို ဖြုတ်မယ်ဆိုရင် အောက်ပါအတိုင်း filename ကို command line argument အနေနဲ့ pass ပေးပြီး run ရင် ဖြုတ်ပေးပါလိမ့်မယ်။  

 ```
(base) ye@ykt-pro:/media/ye/Transcend/exp/my-ch/data/data/chin/prepare/10-fold$ bash ./rm-heading-tab-lineno.sh ./line_no.txt 
Nak-tu-kah motor thar chu va en ka tum a.
Eng chungchang nge min hrilh i tum a?
Kei pawh kha-tiang kha ka rin dan chiah a ni.
Hei hian min tibuai .
Anni chu engti khawpin nge an rilru a that ?
Ani chu ka u alawm .
```

ရှေဘက်မှာ sed command ကို သုံးပြီးရေးပြခဲ့တဲ့ [21. rm-spaces-lineno.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-spaces-lineno.sh) နဲ့ line_no.txt ဖိုင်ကို ဖြုတ်ကြည့်ရင် လိုင်းနံပါတ်တွေကို ဖြုတ်ပေးမှာ ဖြစ်ပေမဲ့ space နဲ့ tab တို့ကတော့ အောက်ပါအတိုင်း ကျန်နေမှာ ဖြစ်ပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/Transcend/exp/my-ch/data/data/chin/prepare/10-fold$ bash ./rm-spaces-lineno.sh ./line_no.txt 
	Nak-tu-kah motor thar chu va en ka tum a.
	Eng chungchang nge min hrilh i tum a?
  Kei pawh kha-tiang kha ka rin dan chiah a ni.
Hei hian min tibuai .
Anni chu engti khawpin nge an rilru a that ?
Ani chu ka u alawm .
```

## 75. [mk-10cross-data.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mk-10cross-data.sh)  

SMT, NMT experiment တွေလုပ်တဲ့အခါမှာ အထူးသဖြင့် ကျွန်တော်တို့လို့ မြန်မာစာ၊ ကရင်စာ၊ ရှမ်းစာ၊ ချင်းစာ၊ ရခိုင်စာ၊ ပအို့ဝ်စာ ဒေတာတွေကိုပြင်ဆင်ပြီး လုပ်ကြတဲ့အခါမှာ ဒေတာကနည်းတဲ့အတွက်ကြောင့် test set ကို တစ်ခုတည်းထားပြီး လုပ်တာထက် ၁၀ပိုင်း ပိုင်းပြီးတော့ corss-validation (၁၀ ခါ experiment လုပ်၊ test-data ၁၀မျိုးသုံးပြီး ၁၀ခါ testing လုပ်ပြီး၊ ၁၀ခါ evaluation လုပ်) လုပ်ကြရပါတယ်။ အဲဒီ အတွက် parallel data ကို ၁၀ပိုင်းပိုင်းဖို့အတွက် ရေးထားတဲ့ နောက်ထပ် shell script တစ်ပုဒ်ပါ။ အထက်မှာ လည်း တပုဒ်တင်ပေးထားတာ ရှိပါတယ်။ လိုအပ်တဲ့အခါမှာ အဆင်သင့်မရှိတဲ့အခါမှာ ကောက်ပြီး shell script ရေးတာမို့ ...

သုံးပုံသုံးနည်းကတော့ အောက်ပါအတိုင်းပါ  

ပထမဆုံး parallel corpus ရဲ့ format ကို ကြည့်ရအောင်။ source<TAB>target ပုံစံနဲ့ သိမ်းထားပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/Transcend/exp/my-ch/data/data/chin/prepare/10-fold$ head all.mych
ကျွန်တော် မနက်ဖြန် ကား အသစ် တွေ သွား ကြည့် မလို့ ။	Nak-tu-kah motor thar chu va en ka tum a .
မင်း ဘာ တွေ သတင်းပေး မှာလဲ ။	Eng chungchang nge min hrilh i tum a ?
အကြံဉာဏ် ကောင်းတွေ လိုချင် လား ။	Thurawn tha i duh em ?
မင်း ဘာ တွေ သယ် နေတာလဲ ။	Eng nge i put a ?
မင်း ငါ့ကို မ မုန်း ခဲ့ဘူး နော် ၊ မုန်း ခဲ့သလား ။	Min hau lo a ni lawm ni, min hua em ?
အပြင်မှာ မှောင်နေ သေးတယ် ။	Pawn lam chu a la thim .
ကျွန်တော် ခင်ဗျားကို အိမ် လိုက်ပို့ပေးမယ် ။	In inah ka thlah ang che .
မင်း ကတိမပျက် ပါဘူး ။	I thu tiam i bawh pelh lo ve .
ဘယ်သူ အလုပ် လာလုပ် မှာလဲ ။	Tu hna nge i rawn thawh dawn a ?
ကျွန်တော်လည်း အဲဒီလို ထင်တာပဲ ။	Kei pawh kha-tiang kha ka rin dan chiah a ni .

```

run မယ်။  
၁၀ ပိုင်းပိုင်းတဲ့ အခါမှာ တစ်ပိုင်းချင်းစီမှာ ရှိတဲ့ training, development, testing ဒေတာတွေရဲ့ စာကြောင်းရေ အရေအတွက်ကို output ပြပေးပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:/media/ye/Transcend/exp/my-ch/data/data/chin/prepare/10-fold$ bash ./mk-10cross-data.sh all.mych my ch
total lines: 14983

hline: 12994

  12994  207235 1980842 ./train
  500  7966 75372 ./dev
  1489  23792 228501 ./test
hline: 12976

  12976  207010 1980881 ./train
  500  7966 75372 ./dev
  1507  24017 228462 ./test
hline: 13022

  13022  207193 1980750 ./train
  500  7966 75372 ./dev
  1461  23834 228593 ./test
hline: 12968

  12968  207166 1980983 ./train
  500  7966 75372 ./dev
  1515  23861 228360 ./test
hline: 12981

  12981  207022 1980875 ./train
  500  7966 75372 ./dev
  1502  24005 228468 ./test
hline: 12989

  12989  207137 1980896 ./train
  500  7966 75372 ./dev
  1494  23890 228447 ./test
hline: 12957

  12957  207060 1980783 ./train
  500  7966 75372 ./dev
  1526  23967 228560 ./test
hline: 12991

  12991  207217 1980895 ./train
  500  7966 75372 ./dev
  1492  23810 228448 ./test
hline: 12979

  12979  207091 1980902 ./train
  500  7966 75372 ./dev
  1504  23936 228441 ./test
hline: 12990

  12990  207111 1980055 ./train
  500  8001 76225 ./dev
  1493  23881 228435 ./test

```

## 76. [align-GIZA++.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/align-GIZA%2B%2B.sh)  

[GIZA++](https://github.com/moses-smt/giza-pp) toolkit ကို သုံးပြီးတော့ source စာကြောင်းထဲမှာ ရှိတဲ့ စာလုံးတွေကို target ဘက်မှာ ရှိတဲ့ စကားလုံးတွေနဲ့ alignment လုပ်ဖို့အတွက် ရေးခဲ့တဲ့ shell script တစ်ပုဒ်ပါ။

Let's run align-GIZA++.sh

```bash
(base) ye@ykt-pro:~/exp/alignment$ ./align-GIZA++.sh train.en train.th test-align
making .vcb and .snt files
/home/ye/tool/giza-pp/GIZA++-v2/plain2snt.out train.en train.th
train.en -> train.en
train.th -> train.th
WARNING: filtered out empty sentence (source: train.en 2 target: train.th 0).
WARNING: filtered out empty sentence (source: train.en 4 target: train.th 0).
WARNING: filtered out empty sentence (source: train.en 2 target: train.th 0).
WARNING: filtered out empty sentence (source: train.en 3 target: train.th 0).
WARNING: filtered out empty sentence (source: train.en 5 target: train.th 0).
WARNING: filtered out empty sentence (source: train.en 7 target: train.th 0).
##########
head train.en.vcb
2 Yes, 205
3 I 3998
4 like 1401
5 playing 27
6 Thai 63
7 chess. 6
8 Can 781
9 you 4344
10 recommend 76
11 something 153
head train.th.vcb
2 ใช่ 546
3 , 2205
4 ฉัน 6248
5 ชอบ 276
6 เล่น 167
7 หมากรุก 12
8 ไทย 109
9 คุณ 4850
10 มี 1928
11 อะไร 869
##########
head train.en_train.th.snt
1
2 3 4 5 6 7 
2 3 4 5 6 7 8 
1
8 9 10 11 12 13 
9 10 11 12 13 14 15 16 
1
14 15 3 16 17 
4 17 18 19 20 21 22 16 
1
##########
head train.th_train.en.snt
1
2 3 4 5 6 7 8 
2 3 4 5 6 7 
1
9 10 11 12 13 14 15 16 
8 9 10 11 12 13 
1
4 17 18 19 20 21 22 16 
14 15 3 16 17 
1
##########

***** 10 runs. (algorithm:TA)*****
;KategProblem:cats: 80   words: 12554

start-costs: MEAN: 1.87267e+06 (1.86993e+06-1.87668e+06)  SIGMA:2012.12   
  end-costs: MEAN: 1.65206e+06 (1.64965e+06-1.65409e+06)  SIGMA:1110.93   
   start-pp: MEAN: 394.874 (388.193-404.815)  SIGMA:4.95869   
     end-pp: MEAN: 100.361 (98.8681-101.632)  SIGMA:0.691322   
 iterations: MEAN: 309924 (293840-329419)  SIGMA:10723.1   
       time: MEAN: 7.39908 (6.59024-8.48116)  SIGMA:0.587319   
##########
ls *.classes
train.en.classes  train.th.classes
##########
head train.en.classes
"0"	21
"24.7"?	13
"ABC".	13
"Chinese	45
"Gone	56
"Inception"	54
"Li"	6
"Magic	5
"My	30
"National	73
##########

***** 10 runs. (algorithm:TA)*****
;KategProblem:cats: 80   words: 8711

start-costs: MEAN: 1.83711e+06 (1.83263e+06-1.84489e+06)  SIGMA:3226.07   
  end-costs: MEAN: 1.70076e+06 (1.69965e+06-1.70221e+06)  SIGMA:795.356   
   start-pp: MEAN: 188.569 (183.314-197.958)  SIGMA:3.85446   
     end-pp: MEAN: 80.2539 (79.6974-80.9825)  SIGMA:0.400113   
 iterations: MEAN: 216902 (207531-225201)  SIGMA:5901.31   
       time: MEAN: 5.85677 (5.20037-6.70613)  SIGMA:0.492989   
head train.th.classes
!	74
"	57
'ทั้งหมดคุณสามารถกิน'	46
(	80
(ตะวันตก)	52
(รินไวน์)	46
(หอย,กุ้ง	70
(แขกกำลังทานอาหาร.	46
(แซนด์วิชสองชั้น)	4
(โปรตีนในแป้ง)	52
##########
ls *.cats
##########
diff train.en_train.th.snt train.th_train.en.snt
diff: ../train.en_train.th.snt: No such file or directory
##########
making co-occurrence file ...
line 1000
line 2000
line 3000
line 4000
line 5000
line 6000
line 7000
line 8000
line 9000
line 10000
line 11000
line 12000
line 13000
line 14000
line 15000
line 16000
line 17000
line 18000
line 19000
END.
##########
making alignment ...
Parameter 's' changed from '' to 'train.en.vcb'
Parameter 't' changed from '' to 'train.th.vcb'
Parameter 'c' changed from '' to 'train.en_train.th.snt'
Parameter 'coocurrencefile' changed from '' to './train.en_train.th.char.cooc'
Parameter 'o' changed from '2020-07-29.024749.ye' to 'Result'
Parameter 'outputpath' changed from '' to 'test-align'
general parameters:
-------------------
ml = 101  (maximum sentence length)

No. of iterations:
-------------------
hmmiterations = 5  (mh)
model1iterations = 5  (number of iterations for Model 1)
model2iterations = 0  (number of iterations for Model 2)
model3iterations = 5  (number of iterations for Model 3)
model4iterations = 5  (number of iterations for Model 4)
model5iterations = 0  (number of iterations for Model 5)
model6iterations = 0  (number of iterations for Model 6)

parameter for various heuristics in GIZA++ for efficient training:
------------------------------------------------------------------
countincreasecutoff = 1e-06  (Counts increment cutoff threshold)
countincreasecutoffal = 1e-05  (Counts increment cutoff threshold for alignments in training of fertility models)
mincountincrease = 1e-07  (minimal count increase)
peggedcutoff = 0.03  (relative cutoff probability for alignment-centers in pegging)
probcutoff = 1e-07  (Probability cutoff threshold for lexicon probabilities)
probsmooth = 1e-07  (probability smoothing (floor) value )

parameters for describing the type and amount of output:
-----------------------------------------------------------
compactalignmentformat = 0  (0: detailled alignment format, 1: compact alignment format )
hmmdumpfrequency = 0  (dump frequency of HMM)
l = test-align/2020-07-29.024749.ye.log  (log file name)
log = 0  (0: no logfile; 1: logfile)
model1dumpfrequency = 0  (dump frequency of Model 1)
model2dumpfrequency = 0  (dump frequency of Model 2)
model345dumpfrequency = 0  (dump frequency of Model 3/4/5)
nbestalignments = 0  (for printing the n best alignments)
nodumps = 0  (1: do not write any files)
o = test-align/Result  (output file prefix)
onlyaldumps = 0  (1: do not write any files)
outputpath = test-align/  (output path)
transferdumpfrequency = 0  (output: dump of transfer from Model 2 to 3)
verbose = 0  (0: not verbose; 1: verbose)
verbosesentence = -10  (number of sentence for which a lot of information should be printed (negative: no output))

parameters describing input files:
----------------------------------
c = train.en_train.th.snt  (training corpus file name)
d =   (dictionary file name)
s = train.en.vcb  (source vocabulary file name)
t = train.th.vcb  (target vocabulary file name)
tc =   (test corpus file name)

smoothing parameters:
---------------------
emalsmooth = 0.2  (f-b-trn: smoothing factor for HMM alignment model (can be ignored by -emSmoothHMM))
model23smoothfactor = 0  (smoothing parameter for IBM-2/3 (interpolation with constant))
model4smoothfactor = 0.2  (smooting parameter for alignment probabilities in Model 4)
model5smoothfactor = 0.1  (smooting parameter for distortion probabilities in Model 5 (linear interpolation with constant))
nsmooth = 64  (smoothing for fertility parameters (good value: 64): weight for wordlength-dependent fertility parameters)
nsmoothgeneral = 0  (smoothing for fertility parameters (default: 0): weight for word-independent fertility parameters)

parameters modifying the models:
--------------------------------
compactadtable = 1  (1: only 3-dimensional alignment table for IBM-2 and IBM-3)
deficientdistortionforemptyword = 0  (0: IBM-3/IBM-4 as described in (Brown et al. 1993); 1: distortion model of empty word is deficient; 2: distoriton model of empty word is deficient (differently); setting this parameter also helps to avoid that during IBM-3 and IBM-4 training too many words are aligned with the empty word)
depm4 = 76  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
depm5 = 68  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
emalignmentdependencies = 2  (lextrain: dependencies in the HMM alignment model.  &1: sentence length; &2: previous class; &4: previous position;  &8: French position; &16: French class)
emprobforempty = 0.4  (f-b-trn: probability for empty word)

parameters modifying the EM-algorithm:
--------------------------------------
m5p0 = -1  (fixed value for parameter p_0 in IBM-5 (if negative then it is determined in training))
manlexfactor1 = 0  ()
manlexfactor2 = 0  ()
manlexmaxmultiplicity = 20  ()
maxfertility = 10  (maximal fertility for fertility models)
p0 = -1  (fixed value for parameter p_0 in IBM-3/4 (if negative then it is determined in training))
pegging = 0  (0: no pegging; 1: do pegging)

general parameters:
-------------------
ml = 101  (maximum sentence length)

No. of iterations:
-------------------
hmmiterations = 5  (mh)
model1iterations = 5  (number of iterations for Model 1)
model2iterations = 0  (number of iterations for Model 2)
model3iterations = 5  (number of iterations for Model 3)
model4iterations = 5  (number of iterations for Model 4)
model5iterations = 0  (number of iterations for Model 5)
model6iterations = 0  (number of iterations for Model 6)

parameter for various heuristics in GIZA++ for efficient training:
------------------------------------------------------------------
countincreasecutoff = 1e-06  (Counts increment cutoff threshold)
countincreasecutoffal = 1e-05  (Counts increment cutoff threshold for alignments in training of fertility models)
mincountincrease = 1e-07  (minimal count increase)
peggedcutoff = 0.03  (relative cutoff probability for alignment-centers in pegging)
probcutoff = 1e-07  (Probability cutoff threshold for lexicon probabilities)
probsmooth = 1e-07  (probability smoothing (floor) value )

parameters for describing the type and amount of output:
-----------------------------------------------------------
compactalignmentformat = 0  (0: detailled alignment format, 1: compact alignment format )
hmmdumpfrequency = 0  (dump frequency of HMM)
l = test-align/2020-07-29.024749.ye.log  (log file name)
log = 0  (0: no logfile; 1: logfile)
model1dumpfrequency = 0  (dump frequency of Model 1)
model2dumpfrequency = 0  (dump frequency of Model 2)
model345dumpfrequency = 0  (dump frequency of Model 3/4/5)
nbestalignments = 0  (for printing the n best alignments)
nodumps = 0  (1: do not write any files)
o = test-align/Result  (output file prefix)
onlyaldumps = 0  (1: do not write any files)
outputpath = test-align/  (output path)
transferdumpfrequency = 0  (output: dump of transfer from Model 2 to 3)
verbose = 0  (0: not verbose; 1: verbose)
verbosesentence = -10  (number of sentence for which a lot of information should be printed (negative: no output))

parameters describing input files:
----------------------------------
c = train.en_train.th.snt  (training corpus file name)
d =   (dictionary file name)
s = train.en.vcb  (source vocabulary file name)
t = train.th.vcb  (target vocabulary file name)
tc =   (test corpus file name)

smoothing parameters:
---------------------
emalsmooth = 0.2  (f-b-trn: smoothing factor for HMM alignment model (can be ignored by -emSmoothHMM))
model23smoothfactor = 0  (smoothing parameter for IBM-2/3 (interpolation with constant))
model4smoothfactor = 0.2  (smooting parameter for alignment probabilities in Model 4)
model5smoothfactor = 0.1  (smooting parameter for distortion probabilities in Model 5 (linear interpolation with constant))
nsmooth = 64  (smoothing for fertility parameters (good value: 64): weight for wordlength-dependent fertility parameters)
nsmoothgeneral = 0  (smoothing for fertility parameters (default: 0): weight for word-independent fertility parameters)

parameters modifying the models:
--------------------------------
compactadtable = 1  (1: only 3-dimensional alignment table for IBM-2 and IBM-3)
deficientdistortionforemptyword = 0  (0: IBM-3/IBM-4 as described in (Brown et al. 1993); 1: distortion model of empty word is deficient; 2: distoriton model of empty word is deficient (differently); setting this parameter also helps to avoid that during IBM-3 and IBM-4 training too many words are aligned with the empty word)
depm4 = 76  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
depm5 = 68  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
emalignmentdependencies = 2  (lextrain: dependencies in the HMM alignment model.  &1: sentence length; &2: previous class; &4: previous position;  &8: French position; &16: French class)
emprobforempty = 0.4  (f-b-trn: probability for empty word)

parameters modifying the EM-algorithm:
--------------------------------------
m5p0 = -1  (fixed value for parameter p_0 in IBM-5 (if negative then it is determined in training))
manlexfactor1 = 0  ()
manlexfactor2 = 0  ()
manlexmaxmultiplicity = 20  ()
maxfertility = 10  (maximal fertility for fertility models)
p0 = -1  (fixed value for parameter p_0 in IBM-3/4 (if negative then it is determined in training))
pegging = 0  (0: no pegging; 1: do pegging)
Reading vocabulary file from:train.en.vcb

reading vocabulary files 
Reading vocabulary file from:train.th.vcb
WARNING: The following sentence pair has source/target sentence length ration more than
Source vocabulary list has 12555 unique tokens 
Target vocabulary list has 8712 unique tokens 
Calculating vocabulary frequencies from corpus train.en_train.th.snt
Reading more sentence pairs into memory ... 
the maximum allowed limit for a source word fertility
 source length = 1 target length = 10 ratio 10 ferility limit : 9
Shortening sentence 
Sent No: 2729 , No. Occurrences: 1
0 4037 
178 95 1649 425 19 96 264 54 141 16 
WARNING: The following sentence pair has source/target sentence length ration more than
the maximum allowed limit for a source word fertility
 source length = 1 target length = 11 ratio 11 ferility limit : 9
Shortening sentence 
Sent No: 6190 , No. Occurrences: 1
0 6673 
486 113 30 31 17 6 389 55 107 398 21 
WARNING: The following sentence pair has source/target sentence length ration more than
the maximum allowed limit for a source word fertility
 source length = 1 target length = 11 ratio 11 ferility limit : 9
Shortening sentence 
Sent No: 15296 , No. Occurrences: 1
0 10970 
9 211 70 31 241 1300 3160 320 465 15 16 
WARNING: The following sentence pair has source/target sentence length ration more than
the maximum allowed limit for a source word fertility
 source length = 1 target length = 10 ratio 10 ferility limit : 9
Shortening sentence 
Sent No: 18611 , No. Occurrences: 1
0 598 
88 362 250 72 451 1369 136 18 110 16 
ERROR: can not read Corpus fits in memory, corpus has: 19994 sentence pairs.
 Train total # sentence pairs (weighted): 19994
Size of source portion of the training corpus: 141035 tokens
Size of the target portion of the training corpus: 139604 tokens 
In source portion of the training corpus, only 12553 unique tokens appeared
In target portion of the training corpus, only 8710 unique tokens appeared
lambda for PP calculation in IBM-1,IBM-2,HMM:= 139604/(161029-19994)== 0.989854
There are 416386 416386 entries in table
==========================================================
Model1 Training Started at: Wed Jul 29 02:47:49 2020

-----------
Model1: Iteration 1
Model1: (1) TRAIN CROSS-ENTROPY 13.6786 PERPLEXITY 13112.2
Model1: (1) VITERBI TRAIN CROSS-ENTROPY 16.8349 PERPLEXITY 116896
Model 1 Iteration: 1 took: 0 seconds
-----------
Model1: Iteration 2
Model1: (2) TRAIN CROSS-ENTROPY 6.02651 PERPLEXITY 65.187
Model1: (2) VITERBI TRAIN CROSS-ENTROPY 7.35602 PERPLEXITY 163.826
Model 1 Iteration: 2 took: 0 seconds
-----------
Model1: Iteration 3
Model1: (3) TRAIN CROSS-ENTROPY 5.33195 PERPLEXITY 40.2789
Model1: (3) VITERBI TRAIN CROSS-ENTROPY 6.24842 PERPLEXITY 76.0261
Model 1 Iteration: 3 took: 0 seconds
-----------
Model1: Iteration 4
Model1: (4) TRAIN CROSS-ENTROPY 5.07667 PERPLEXITY 33.7467
Model1: (4) VITERBI TRAIN CROSS-ENTROPY 5.77499 PERPLEXITY 54.7579
Model 1 Iteration: 4 took: 0 seconds
-----------
Model1: Iteration 5
Model1: (5) TRAIN CROSS-ENTROPY 4.98187 PERPLEXITY 31.6005
Model1: (5) VITERBI TRAIN CROSS-ENTROPY 5.56481 PERPLEXITY 47.3343
Model 1 Iteration: 5 took: 0 seconds
Entire Model1 Training took: 0 seconds
NOTE: I am doing iterations with the HMM model!
train.en.vcb.classes
ERROR: can not read train.th.vcb.classes

==========================================================
Hmm Training Started at: Wed Jul 29 02:47:49 2020

-----------
Hmm: Iteration 1
A/D table contains 28197 parameters.
Hmm: (1) TRAIN CROSS-ENTROPY 4.94027 PERPLEXITY 30.7022
Hmm: (1) VITERBI TRAIN CROSS-ENTROPY 5.45375 PERPLEXITY 43.8271

Hmm Iteration: 1 took: 1 seconds

-----------
Hmm: Iteration 2
A/D table contains 28197 parameters.
Hmm: (2) TRAIN CROSS-ENTROPY 4.6503 PERPLEXITY 25.1119
Hmm: (2) VITERBI TRAIN CROSS-ENTROPY 4.9816 PERPLEXITY 31.5945

Hmm Iteration: 2 took: 1 seconds

-----------
Hmm: Iteration 3
A/D table contains 28197 parameters.
Hmm: (3) TRAIN CROSS-ENTROPY 4.46308 PERPLEXITY 22.0557
Hmm: (3) VITERBI TRAIN CROSS-ENTROPY 4.72979 PERPLEXITY 26.5344

Hmm Iteration: 3 took: 0 seconds

-----------
Hmm: Iteration 4
A/D table contains 28197 parameters.
Hmm: (4) TRAIN CROSS-ENTROPY 4.34379 PERPLEXITY 20.3054
Hmm: (4) VITERBI TRAIN CROSS-ENTROPY 4.57123 PERPLEXITY 23.7727

Hmm Iteration: 4 took: 1 seconds

-----------
Hmm: Iteration 5
A/D table contains 28197 parameters.
Hmm: (5) TRAIN CROSS-ENTROPY 4.255 PERPLEXITY 19.0933
Hmm: (5) VITERBI TRAIN CROSS-ENTROPY 4.45299 PERPLEXITY 21.9019

Hmm Iteration: 5 took: 1 seconds

ERROR: can not read train.en.vcb.classes
ERROR: can not read train.th.vcb.classes
Entire Hmm Training took: 4 seconds
==========================================================
ERROR: can not read classes from train.en.vcb.classes
ERROR: can not read classes from train.th.vcb.classes
10000
==========================================================
Starting H3333344444:  Viterbi Training
 H3333344444 Training Started at: Wed Jul 29 02:47:53 2020


---------------------
THTo3: Iteration 1

NTable contains #centers(pre/hillclimbed/real): 1 1 1  #al: 91.4825 #alsophisticatedcountcollection: 0 #hcsteps: 0
#peggingImprovements: 0
A/D table contains 28197 parameters.
A/D table contains 32349 parameters.
125550 parameter.
10000p0_count is 124389 and p1 is 7607.42; p0 is 0.942366 p1: 0.0576335
THTo3: TRAIN CROSS-ENTROPY 3.6576 PERPLEXITY 12.6197
THTo3: (1) TRAIN VITERBI CROSS-ENTROPY 3.78055 PERPLEXITY 13.7423

THTo3 Viterbi Iteration : 1 took: 0 seconds

---------------------
Model3: Iteration 2

NTable contains #centers(pre/hillclimbed/real): 1 1 1  #al: 91.8619 #alsophisticatedcountcollection: 0 #hcsteps: 1.48765
#peggingImprovements: 0
A/D table contains 28197 parameters.
A/D table contains 32349 parameters.
125550 parameter.
10000p0_count is 120621 and p1 is 9491.42; p0 is 0.927052 p1: 0.0729478
Model3: TRAIN CROSS-ENTROPY 5.0119 PERPLEXITY 32.2652
Model3: (2) TRAIN VITERBI CROSS-ENTROPY 5.12091 PERPLEXITY 34.7973

Model3 Viterbi Iteration : 2 took: 1 seconds

---------------------
Model3: Iteration 3

NTable contains #centers(pre/hillclimbed/real): 1 1 1  #al: 92.0153 #alsophisticatedcountcollection: 0 #hcsteps: 1.4922
#peggingImprovements: 0
A/D table contains 28197 parameters.
A/D table contains 32124 parameters.
125550 parameter.
10000
p0_count is 118357 and p1 is 10623.4; p0 is 0.917635 p1: 0.0823647
Model3: TRAIN CROSS-ENTROPY 4.91495 PERPLEXITY 30.1681
Model3: (3) TRAIN VITERBI CROSS-ENTROPY 5.00656 PERPLEXITY 32.1457

Model3 Viterbi Iteration : 3 took: 1 seconds

---------------------
Model3: Iteration 4
NTable contains 125550 parameter.
#centers(pre/hillclimbed/real): 1 1 1  #al: 92.1068 #alsophisticatedcountcollection: 0 #hcsteps: 1.45849
#peggingImprovements: 0
A/D table contains 28197 parameters.
A/D table contains 31990 parameters.
10000p0_count is 116708 and p1 is 11448.1; p0 is 0.91067 p1: 0.0893299
Model3: TRAIN CROSS-ENTROPY 4.8728 PERPLEXITY 29.2994
Model3: (4) TRAIN VITERBI CROSS-ENTROPY 4.95697 PERPLEXITY 31.0596

Model3 Viterbi Iteration : 4 took: 1 seconds

---------------------
Model3: Iteration 5

NTable contains 125550#centers(pre/hillclimbed/real): 1 1 1  #al: 92.1822 #alsophisticatedcountcollection: 0 #hcsteps: 1.45524
#peggingImprovements: 0
A/D table contains 28197 parameters.
A/D table contains 31990 parameters.
 parameter.
10000
p0_count is 115398 and p1 is 12102.9; p0 is 0.905076 p1: 0.0949242
Model3: TRAIN CROSS-ENTROPY 4.84786 PERPLEXITY 28.7972
Model3: (5) TRAIN VITERBI CROSS-ENTROPY 4.92797 PERPLEXITY 30.4416

Model3 Viterbi Iteration : 5 took: 0 seconds

---------------------
T3To4: Iteration 6
NTable contains #centers(pre/hillclimbed/real): 1 1 1  #al: 92.2349 #alsophisticatedcountcollection: 8.46289 #hcsteps: 1.45229
#peggingImprovements: 0
D4 table contains 406 parameters.
A/D table contains 28197 parameters.
A/D table contains 31990 parameters.
125550 parameter.
10000
p0_count is 114271 and p1 is 12666.5; p0 is 0.900214 p1: 0.0997855
T3To4: TRAIN CROSS-ENTROPY 4.83086 PERPLEXITY 28.46
T3To4: (6) TRAIN VITERBI CROSS-ENTROPY 4.90814 PERPLEXITY 30.026

T3To4 Viterbi Iteration : 6 took: 1 seconds

---------------------
Model4: Iteration 7
NTable contains 125550 parameter.
#centers(pre/hillclimbed/real): 1 1 1  #al: 92.1613 #alsophisticatedcountcollection: 7.51746 #hcsteps: 1.36486
#peggingImprovements: 0
D4 table contains 406 parameters.
A/D table contains 28197 parameters.
A/D table contains 31093 parameters.
10000
p0_count is 112855 and p1 is 13374.6; p0 is 0.894045 p1: 0.105955
Model4: TRAIN CROSS-ENTROPY 4.73013 PERPLEXITY 26.5406
Model4: (7) TRAIN VITERBI CROSS-ENTROPY 4.80035 PERPLEXITY 27.8643

Model4 Viterbi Iteration : 7 took: 2 seconds

---------------------
Model4: Iteration 8
NTable contains #centers(pre/hillclimbed/real): 1 1 1  #al: 92.1865 #alsophisticatedcountcollection: 7.21797 #hcsteps: 1.47799
#peggingImprovements: 0
D4 table contains 406 parameters.
A/D table contains 28197 parameters.
A/D table contains 31068 parameters.
125550 parameter.
10000
p0_count is 110508 and p1 is 14548; p0 is 0.883668 p1: 0.116332
Model4: TRAIN CROSS-ENTROPY 4.581 PERPLEXITY 23.9341
Model4: (8) TRAIN VITERBI CROSS-ENTROPY 4.64802 PERPLEXITY 25.0723

Model4 Viterbi Iteration : 8 took: 1 seconds

---------------------
Model4: Iteration 9
NTable contains 125550 parameter.
#centers(pre/hillclimbed/real): 1 1 1  #al: 92.2154 #alsophisticatedcountcollection: 7.06962 #hcsteps: 1.55342
#peggingImprovements: 0
D4 table contains 406 parameters.
A/D table contains 28197 parameters.
A/D table contains 31252 parameters.
10000
p0_count is 109123 and p1 is 15240.5; p0 is 0.877452 p1: 0.122548
Model4: TRAIN CROSS-ENTROPY 4.47746 PERPLEXITY 22.2767
Model4: (9) TRAIN VITERBI CROSS-ENTROPY 4.53641 PERPLEXITY 23.2057

Model4 Viterbi Iteration : 9 took: 2 seconds

---------------------
Model4: Iteration 10
NTable contains 125550 parameter.
#centers(pre/hillclimbed/real): 1 1 1  #al: 92.1867 #alsophisticatedcountcollection: 6.92768 #hcsteps: 1.56322
#peggingImprovements: 0
D4 table contains 406 parameters.
A/D table contains 28197 parameters.
A/D table contains 31102 parameters.
Dumping nTable to: test-align/Result.n3.final
p0_count is 108951 and p1 is 15326.7; p0 is 0.876673 p1: 0.123327
Model4: TRAIN CROSS-ENTROPY 4.39995 PERPLEXITY 21.1113
Model4: (10) TRAIN VITERBI CROSS-ENTROPY 4.45124 PERPLEXITY 21.8755
Dumping alignment table (a) to file:test-align/Result.a3.final
Dumping distortion table (d) to file:test-align/Result.d3.final
writing Final tables to Disk 

Model4 Viterbi Iteration : 10 took: 1 seconds
H3333344444 Training Finished at: Wed Jul 29 02:48:03 2020


Entire Viterbi H3333344444 Training took: 10 seconds
==========================================================
writing decoder configuration file to test-align/Result.Decoder.config
Writing PERPLEXITY report to: test-align/Result.perp
Writing source vocabulary list to : test-align/Result.trn.src.vcb
Writing source vocabulary list to : test-align/Result.trn.trg.vcb
Writing source vocabulary list to : test-align/Result.tst.src.vcb
Writing source vocabulary list to : test-align/Result.tst.trg.vcb

Entire Training took: 14 seconds
Program Finished at: Wed Jul 29 02:48:03 2020

==========================================================
##########
finished ...
ls ./test-align/*.final
./test-align/Result.a3.final  ./test-align/Result.d3.final  ./test-align/Result.D4.final  ./test-align/Result.p0_3.final
./test-align/Result.A3.final  ./test-align/Result.d4.final  ./test-align/Result.n3.final  ./test-align/Result.t3.final
##########
Note by Ye ...
output folder name: test-align
GIZA++ learns the translation tables of IBM Model 4, but we are only interested in ".A3.final"
```

## 77. [date-time-info.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/date-time-info.sh)  

နေ့စွဲ၊ ရက်စွဲ၊ အချိန်တွေနဲ့ ပတ်သက်ပြီး မြန်မာလို ရိုက်ထုတ်နိုင်အောင် date command အသုံးပြုပုံကို နမူနာအနေနဲ့ ရေးပြထားတဲ့ shell script ဖြစ်ပါတယ်။  
run လိုက်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:~/4github/date-info$ ./date-time-info.sh 
Output of the date command:
နေ ဩ 8 09:02:35 +0630 2020
==========
Current local's date is: ၂၀၂၀ ဩ ၀၈ စနေ
Current local's 12-hour clock time is: ၀၉:၀၂:၃၅ နံနက်
Current local's 24-hour hour and minute is: ၀၉:၀၂:၃၅ နံနက်
Current Date: 08 ရက် 08 လ 2020 ခုနှစ် (စနေနေ့)
Current Time: 09 နာရီ 02 မိနစ် 35 စက္ကန့်
Current local month: ဩဂုတ်
Current local date and time: ၂၀၂၀ ဩ ၀၈ စနေ ၀၉:၀၂:၃၅ နံနက် +0630
==========
The date of the day before yesterday: တေး ဩ  6 09:02:35 +0630 2020
The date of the day six months and 15 day: ဂါ ဖေ 23 09:02:35 +0630 2021
The day of year of Christmas in the current year: 360
Someone's Birthday in the current year: ၂၀၂၀ ဧပြီ ၂၅ စနေ
```

## 78. [mp4-to-wav.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mp4-to-wav.sh)  

ကွန်ပျူတာတက္ကသိုလ် ဗန်းမော် က TTS လုပ်ဖို့ ပြင်ဆင်နေကြတဲ့ internship ကျောင်းသားများအတွက် Video ဖိုင် ဖြစ်တဲ့ ".mp4" ကနေ TTS မှာ သုံးကြတဲ့ format ဖြစ်တဲ့ wave ဖိုင် ".wav" ကို ပြောင်းတာကို ဥပမာအဖြစ် ရေးပြခဲ့တဲ့ shell script ပါ။  

လက်ရှိ ဖိုလ်ဒါအောက်မှာ အောက်ပါအတိုင်း mp4 ဖိုင် ရှိတယ် ဆိုကြပါစို့ ...   
```
(base) ye@ykt-pro:/media/ye/Transcend/yLab/intern-2/tts/4github$ ls
dawsu-election-1.mp4  mp4-to-wav.sh

(base) ye@ykt-pro:/media/ye/Transcend/yLab/intern-2/tts/4github$ file ./dawsu-election-1.mp4 
./dawsu-election-1.mp4: ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
```

mp4-to-wav.sh ကို သုံးပုံသုံးနည်းကတော့ အောက်ပါအတိုင်းပါ  

```
(base) ye@ykt-pro:/media/ye/Transcend/yLab/intern-2/tts/4github$ time ./mp4-to-wav.sh ./dawsu-election-1.mp4 
ffmpeg version 3.4.8-0ubuntu0.2 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 7 (Ubuntu 7.5.0-3ubuntu1~18.04)
  configuration: --prefix=/usr --extra-version=0ubuntu0.2 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from './dawsu-election-1.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    title           : 3199037790151295
    encoder         : Lavf56.40.101
  Duration: 00:07:16.21, start: -0.022109, bitrate: 112 kb/s
    Stream #0:0(und): Video: h264 (Constrained Baseline) (avc1 / 0x31637661), yuv420p(tv, smpte170m/bt470bg/smpte170m), 400x224, 59 kb/s, 30 fps, 30 tbr, 90k tbn, 60 tbc (default)
    Metadata:
      handler_name    : VideoHandler
    Stream #0:1(eng): Audio: aac (HE-AAC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 47 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
Stream mapping:
  Stream #0:1 -> #0:0 (aac (native) -> mp3 (libmp3lame))
Press [q] to stop, [?] for help
Output #0, mp3, to './dawsu-election-1.mp3':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    TIT2            : 3199037790151295
    TSSE            : Lavf57.83.100
    Stream #0:0(eng): Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp (default)
    Metadata:
      handler_name    : SoundHandler
      encoder         : Lavc57.107.100 libmp3lame
size=    7660kB time=00:07:16.02 bitrate= 143.9kbits/s speed=70.5x    
video:0kB audio:7660kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.004896%
ffmpeg version 3.4.8-0ubuntu0.2 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 7 (Ubuntu 7.5.0-3ubuntu1~18.04)
  configuration: --prefix=/usr --extra-version=0ubuntu0.2 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Input #0, mp3, from './dawsu-election-1.mp3':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    title           : 3199037790151295
    encoder         : Lavf57.83.100
  Duration: 00:07:15.96, start: 0.025057, bitrate: 143 kb/s
    Stream #0:0: Audio: mp3, 44100 Hz, stereo, s16p, 143 kb/s
    Metadata:
      encoder         : Lavc57.10
Stream mapping:
  Stream #0:0 -> #0:0 (mp3 (native) -> pcm_s16le (native))
Press [q] to stop, [?] for help
Output #0, wav, to './dawsu-election-1.wav':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    INAM            : 3199037790151295
    ISFT            : Lavf57.83.100
    Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, stereo, s16, 1411 kb/s
    Metadata:
      encoder         : Lavc57.107.100 pcm_s16le
size=   75096kB time=00:07:15.93 bitrate=1411.2kbits/s speed= 175x    
video:0kB audio:75096kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.000135%

real	0m8.814s
user	0m7.562s
sys	0m0.141s

```

## 79. [my-font-chk.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/my-font-chk.sh)  

Linux စက်ထဲမှာ လက်ရှိ installed လုပ်ထားတဲ့ မြန်မာစာဖောင့်တွေရဲ့ ဖိုင်နာမည်တွေကို list လုပ်ပြဖို့အတွက် ရေးခဲ့တဲ့ bash shell script ပါ။  
တကယ်ကတော့ "fc-list :lang=my" ဆိုပြီး run ရင်လည်း ရပါတယ်။ font filename နဲ့ path ကိုပဲ သီးသန့်ပြစေချင်လို့ "fc-list -f '%{file}\n' :lang=my" ဆိုတဲ့ command ကို သုံးထားခဲ့ပါတယ်။  
ကျွန်တော့စက်မှာ run လိုက်လို့ မြင်ရတဲ့ ဖောင့် ဖိုင်နာမည်စာရင်းကို ဥပမာအဖြစ် ပြသထားပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/Transcend/4github/my-font-chk$ ./my-font-chk.sh 
/home/ye/.local/share/fonts/myanmar3.ttf
/usr/share/fonts/truetype/padauk/PadaukBook-Regular.ttf
/usr/share/fonts/truetype/padauk/Padauk-Bold.ttf
/usr/share/fonts/truetype/padauk/PadaukBook-Bold.ttf
/home/ye/.local/share/fonts/Pyidaungsu-1.8.3_Regular.ttf
/home/ye/.local/share/fonts/Pyidaungsu-1.8.3_Bold.ttf
/usr/share/fonts/truetype/padauk/Padauk-Regular.ttf
/home/ye/.local/share/fonts/Pyidaungsu-1.8.3_Numbers.ttf
```

## 80. [rec-recorder.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/rec-recorder.sh)  

rec command ကို သုံးဖို့အတွက်က sox command ကို ကိုယ့်စက်ထဲမှာ install လုပ်ထားရပါမယ်။  
rec-recorder.sh ကို run ပြီးတော့ အသံဖိုင် သုံးဖိုင် သွင်းကြည့်ပါမယ်။  
ctrl+c ကို သုံးပြီး recording looping ကနေ ထွက်ပါ။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/voice/rec-recorder$ ./rec-recorder.sh 
Press enter when you're ready to record:
rec WARN alsa: can't encode 0-bit Unknown or not applicable

Input File     : 'default' (alsa)
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Sample Encoding: 16-bit Signed Integer PCM

In:0.00% 00:00:01.02 [00:00:00.00] Out:8.19k [!=====|=====!]        Clip:0    ^C
Aborted.
Press enter when you're ready to record:
rec WARN alsa: can't encode 0-bit Unknown or not applicable

Input File     : 'default' (alsa)
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Sample Encoding: 16-bit Signed Integer PCM

In:0.00% 00:00:01.54 [00:00:00.00] Out:16.4k [!=====|=====!]        Clip:0    ^C
Aborted.
Press enter when you're ready to record:
rec WARN alsa: can't encode 0-bit Unknown or not applicable

Input File     : 'default' (alsa)
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Sample Encoding: 16-bit Signed Integer PCM

In:0.00% 00:00:02.56 [00:00:00.00] Out:32.8k [!=====|=====!] Hd:0.0 Clip:0    ^C
Aborted.
Press enter when you're ready to record:^C
```

လက်ရှိ path အောက်မှာ wave ဖိုင် သုံးဖိုင်ကို အောက်ပါအတိုင်း တွေ့ရမှာ ဖြစ်ပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/code4github/voice/rec-recorder$ ls
audio1.wav  audio2.wav  audio3.wav  rec-recorder.sh

```

## 81. [mp42gif.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mp42gif.sh)  

mp4 ဗီဒီယိုဖိုင်ကနေ animated GIF ပုံကို ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ bash script တစ်ပုဒ်ပါ။ အရင်ဆုံး ဗီဒီယိုဖိုင်ကနေ frame တွေအဖြစ် ဖြတ်ထုတ်တာကို ffmpeg command နဲ့ လုပ်ပါတယ်။ ပြီးတော့မှာ convert command နဲ့ animated GIF ပုံအဖြစ် ပြောင်းတဲ့ အလုပ်ကို လုပ်ပါတယ်။ ထွက်လာတဲ့ output GIF ဖိုင်ကိုတော့ eog (Eye of Gnome) command နဲ့ ဖွင့်ကြည့်ပါတယ်။  
code ထဲမှာလည်း command တွေနဲ့ ပတ်သက်ပြီး comment သေချာရေးပေးထားလို့ နားလည်ရ လွယ်ပါလိမ့်မယ်။ run တာကိုလည်း ဥပမာအဖြစ် output screen တွေနဲ့တကွ ပြသထားပါတယ်။  

run လုပ်လိုက်ရင် အောက်ပါလိုမျိုး output screen ကို မြင်ရပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/movie2gif$ ./mp42gif.sh ./AlbertEinsteinInHisOfficeAtPrincetonUniversity.mp4 
ffmpeg version 3.4.8-0ubuntu0.2 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 7 (Ubuntu 7.5.0-3ubuntu1~18.04)
  configuration: --prefix=/usr --extra-version=0ubuntu0.2 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from './AlbertEinsteinInHisOfficeAtPrincetonUniversity.mp4':
  Metadata:
    major_brand     : mp42
    minor_version   : 0
    compatible_brands: isommp42
    creation_time   : 2018-11-21T15:04:46.000000Z
  Duration: 00:00:14.16, start: 0.000000, bitrate: 414 kb/s
    Stream #0:0(und): Video: h264 (Constrained Baseline) (avc1 / 0x31637661), yuv420p, 480x360 [SAR 1:1 DAR 4:3], 317 kb/s, 23.98 fps, 23.98 tbr, 24k tbn, 47.95 tbc (default)
    Metadata:
      creation_time   : 2018-11-21T15:04:46.000000Z
      handler_name    : ISO Media file produced by Google Inc. Created on: 11/21/2018.
    Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 96 kb/s (default)
    Metadata:
      creation_time   : 2018-11-21T15:04:46.000000Z
      handler_name    : ISO Media file produced by Google Inc. Created on: 11/21/2018.
Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> mjpeg (native))
Press [q] to stop, [?] for help
[swscaler @ 0x55a8d178da80] deprecated pixel format used, make sure you did set range correctly
Output #0, image2, to 'frames/frame-%03d.jpg':
  Metadata:
    major_brand     : mp42
    minor_version   : 0
    compatible_brands: isommp42
    encoder         : Lavf57.83.100
    Stream #0:0(und): Video: mjpeg, yuvj420p(pc), 480x360 [SAR 1:1 DAR 4:3], q=2-31, 200 kb/s, 5 fps, 5 tbn, 5 tbc (default)
    Metadata:
      creation_time   : 2018-11-21T15:04:46.000000Z
      handler_name    : ISO Media file produced by Google Inc. Created on: 11/21/2018.
      encoder         : Lavc57.107.100 mjpeg
    Side data:
      cpb: bitrate max/min/avg: 0/0/200000 buffer size: 0 vbv_delay: -1
frame=   72 fps=0.0 q=24.8 Lsize=N/A time=00:00:14.40 bitrate=N/A dup=0 drop=266 speed=31.7x    
video:593kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
(base) ye@ykt-pro:/media/ye/project1/4github/movie2gif$ 
```

အဆင်ပြေပြေနဲ့ run တာကပြီးသွားရင် အောက်ပါလိုမျိုး frame jpg ပုံဖိုင်တွေနဲ့တကွ GIF image ဖိုင်ကိုလည်း frames/ ဖိုလ်ဒါထဲမှာ မြင်တွေ့ရပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/movie2gif$ cd frames/
(base) ye@ykt-pro:/media/ye/project1/4github/movie2gif/frames$ ls
AlbertEinsteinInHisOfficeAtPrincetonUniversity.gif  frame-013.jpg  frame-026.jpg  frame-039.jpg  frame-052.jpg  frame-065.jpg
frame-001.jpg                                       frame-014.jpg  frame-027.jpg  frame-040.jpg  frame-053.jpg  frame-066.jpg
frame-002.jpg                                       frame-015.jpg  frame-028.jpg  frame-041.jpg  frame-054.jpg  frame-067.jpg
frame-003.jpg                                       frame-016.jpg  frame-029.jpg  frame-042.jpg  frame-055.jpg  frame-068.jpg
frame-004.jpg                                       frame-017.jpg  frame-030.jpg  frame-043.jpg  frame-056.jpg  frame-069.jpg
frame-005.jpg                                       frame-018.jpg  frame-031.jpg  frame-044.jpg  frame-057.jpg  frame-070.jpg
frame-006.jpg                                       frame-019.jpg  frame-032.jpg  frame-045.jpg  frame-058.jpg  frame-071.jpg
frame-007.jpg                                       frame-020.jpg  frame-033.jpg  frame-046.jpg  frame-059.jpg  frame-072.jpg
frame-008.jpg                                       frame-021.jpg  frame-034.jpg  frame-047.jpg  frame-060.jpg
frame-009.jpg                                       frame-022.jpg  frame-035.jpg  frame-048.jpg  frame-061.jpg
frame-010.jpg                                       frame-023.jpg  frame-036.jpg  frame-049.jpg  frame-062.jpg
frame-011.jpg                                       frame-024.jpg  frame-037.jpg  frame-050.jpg  frame-063.jpg
frame-012.jpg                                       frame-025.jpg  frame-038.jpg  frame-051.jpg  frame-064.jpg
```

အထက်ပါအတိုင်း ဥပမာအဖြစ် run ပြတဲ့အခါမှာ သုံးခဲ့တဲ့ ဗီဒီယိုဖိုင်ကတော့ YouTube မှာ တင်ထားတဲ့ ရူပဗေဒ သိပ္ပံပညာရှင် "Albert Einstein in his office at Princeton University" ဆိုတဲ့ ဖိုင်ပါ။  
(movie file link: [https://www.youtube.com/watch?v=XUXFCm2h2zk](https://www.youtube.com/watch?v=XUXFCm2h2zk))  

ထွက်လာတဲ့ animated GIF ဖိုင်ကတော့ အောက်ပါအတိုင်းပါ။ Linux command တွေနဲ့က တကယ်အလုပ်တွေ အများကြီးလုပ်လို့ ရပါတယ်။   
Enjoy Linux command and shell script writing !!! :)  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/AlbertEinsteinInHisOfficeAtPrincetonUniversity.gif" alt="output GIF file" />
</p>
<p align="center"> Fig. Converted animated GIF file of Albert Einstein </p>  

## 82. [extract-target-text.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/extract-target-text.sh)  

Statistical Machine Translaiton ရဲ့ approach တစ်ခုဖြစ်တဲ့ OSM model ကနေ ထွက်လာတဲ့ output မှာက တခြား information တွေ အများကြီးရောပါနေပါတယ်။  
အဲဒီဖိုင်ထဲကနေမှာ translated output စာကြောင်းကိုပဲ ဆွဲထုတ်ကြည့်ချင်တဲ့ အခါမျိုး ရှိပါတယ်။ အဲဒီအတွက် ရေးခဲ့တဲ့ script ပါ။  

ဥပမာ အဖြစ် စမ်းပြမယ့် ဖိုင်ထဲမှာက ဘယ်လိုရှိနေတယ်ဆိုတာကို မြင်ရအောင် cat command နဲ့ osm.output.1.best10 ဖိုင်ကို ရိုက်ထုတ်ကြည့်ကြရအောင်။  

```
(base) ye@ykt-pro:/media/ye/Transcend/student/utycc-newR/seminar/3rdSeminar/Myint-Myint-Htay/8aug2020/smt-nbest/osmsecnbest/osm/fs-ps/evaluation$ cat ./osm.output.1.best10 
56 ||| ပျော် စ ရာ လေး ပေါ့ |0-3|  ||| LexicalReordering0= -0.510826 0 0 0 0 0 OpSequenceModel0= -5.9671 0 0 0 0 Distortion0= 0 LM0= -8.68373 WordPenalty0= -5 PhrasePenalty0= 1 TranslationModel0= -2.26139 -13.3128 -1.56823 -12.2852 ||| -1.56055
56 ||| ပျော် စ ရာ တော့ ကောင်း |0-1| တယ် |2-3|  ||| LexicalReordering0= -0.847297 0 0 -0.510826 0 0 OpSequenceModel0= -9.67931 0 0 0 0 Distortion0= 0 LM0= -10.3178 WordPenalty0= -6 PhrasePenalty0= 2 TranslationModel0= -6.53573 -10.4715 -3.10868 -11.5704 ||| -2.14498
56 ||| ​ |0-0| ပျော် |1-1| တယ် |2-3|  ||| LexicalReordering0= -0.922915 0 0 -0.580419 0 0 OpSequenceModel0= -11.8972 0 0 0 0 Distortion0= 0 LM0= -10.7013 WordPenalty0= -3 PhrasePenalty0= 3 TranslationModel0= -7.82417 -6.98941 -4.43382 -3.77572 ||| -2.31397
56 ||| ပျော် စ ရာ တော့ ကောင်း |0-1| တယ် |2-2| ကွာ |3-3|  ||| LexicalReordering0= -0.65553 0 0 -0.596148 0 0 OpSequenceModel0= -10.0593 0 0 0 0 Distortion0= 0 LM0= -14.7554 WordPenalty0= -7 PhrasePenalty0= 3 TranslationModel0= -4.1701 -8.76545 -4.21924 -13.6339 ||| -2.32136
56 ||| ပျော် စ ရာ တော့ ကောင်း |0-1| ပါ တယ် |2-3|  ||| LexicalReordering0= -0.96281 0 0 -0.510826 0 0 OpSequenceModel0= -9.89117 0 0 0 0 Distortion0= 0 LM0= -11.5595 WordPenalty0= -7 PhrasePenalty0= 2 TranslationModel0= -6.84473 -11.0525 -4.37582 -13.9572 ||| -2.33079
56 ||| ​ |0-0| ပျော် |1-1| တယ် |2-2| ကွာ |3-3|  ||| LexicalReordering0= -0.731147 0 0 -0.665742 0 0 OpSequenceModel0= -12.3566 0 0 0 0 Distortion0= 0 LM0= -10.3073 WordPenalty0= -4 PhrasePenalty0= 4 TranslationModel0= -5.45854 -5.28338 -5.54438 -5.8392 ||| -2.34255
56 ||| ပျော် စ ရာ တော့ ကောင်း |0-1| တာ |2-3|  ||| LexicalReordering0= -0.76214 0 0 -0.510826 0 0 OpSequenceModel0= -9.51524 0 0 0 0 Distortion0= 0 LM0= -13.5896 WordPenalty0= -6 PhrasePenalty0= 2 TranslationModel0= -7.58513 -11.2946 -4.6635 -12.8674 ||| -2.37857
56 ||| ပျော် စ ရာ တော့ ကောင်း |0-1| တယ် ကွာ |2-3|  ||| LexicalReordering0= -0.847297 0 0 -0.510826 0 0 OpSequenceModel0= -10.0593 0 0 0 0 Distortion0= 0 LM0= -14.7554 WordPenalty0= -7 PhrasePenalty0= 2 TranslationModel0= -4.87597 -8.76545 -5.28144 -13.6339 ||| -2.41629
56 ||| ​ |0-0| ပျော် |1-1| တယ် ကွာ |2-3|  ||| LexicalReordering0= -0.922915 0 0 -0.580419 0 0 OpSequenceModel0= -12.3566 0 0 0 0 Distortion0= 0 LM0= -10.3073 WordPenalty0= -4 PhrasePenalty0= 3 TranslationModel0= -6.16441 -5.28338 -6.60658 -5.8392 ||| -2.43748
56 ||| ပျော် စ ရာ တော့ ကောင်း |0-1| တယ် |2-2| နော် |3-3|  ||| LexicalReordering0= -0.715248 0 0 -0.596148 0 0 OpSequenceModel0= -10.8704 0 0 0 0 Distortion0= 0 LM0= -12.7345 WordPenalty0= -7 PhrasePenalty0= 3 TranslationModel0= -5.69178 -10.02 -5.05429 -14.4606 ||| -2.47206
```

Example အနေနဲ့ run ပြရရင်တော့ အောက်ပါအတိုင်းပါ။  

```
(base) ye@ykt-pro:/media/ye/Transcend/student/utycc-newR/seminar/3rdSeminar/Myint-Myint-Htay/8aug2020/smt-nbest/osmsecnbest/osm/fs-ps/evaluation$ ./extract-target-text.sh ./osm.output.1.best10 
 ပျော် စ ရာ လေး ပေါ့   
 ပျော် စ ရာ တော့ ကောင်း  တယ်   
 ​  ပျော်  တယ်   
 ပျော် စ ရာ တော့ ကောင်း  တယ်  ကွာ   
 ပျော် စ ရာ တော့ ကောင်း  ပါ တယ်   
 ​  ပျော်  တယ်  ကွာ   
 ပျော် စ ရာ တော့ ကောင်း  တာ   
 ပျော် စ ရာ တော့ ကောင်း  တယ် ကွာ   
 ​  ပျော်  တယ် ကွာ   
 ပျော် စ ရာ တော့ ကောင်း  တယ်  နော် 
```

## 83. [txt2png.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/txt2png.sh)  
text ဖိုင်ထဲမှာ ရိုက်ထည့်ထားတဲ့ မြန်မာစာကြောင်းတွေကို ပုံဖိုင်အဖြစ်ပြောင်းပေးတဲ့ shell script ပါ။

အရင်ဆုံး input.txt ဖိုင်ထဲမှာ ရိုက်ထားတဲ့ မြန်မာစာကြောင်းတွေကို cat command နဲ့ ရိုက်ထုတ်ကြည့်ရအောင်။  

```
$ cat input.txt 
နေကောင်းလား
ထမင်းစားပြီးပြီလား
```

run မယ်ဆိုရင်တော့ input file နာမည်နဲ့ font နာမည်ကို argument တွေအဖြစ် ပေးဖို့ လိုအပ်ပါတယ်။  

```
$./txt2png.sh ./input.txt Myanmar3
```

output.png အဖြစ်နဲ့ သိမ်းပေးမှာဖြစ်လို့ display output.png ဆိုပြီးတော့ ရိုက်ကြည့်ရင် အောက်ပါအတိုင်း image ဖိုင်ကို မြင်ရမှာ ဖြစ်ပါတယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/myanmar3-output.png" alt="converted PNG file" />
</p>

တကယ်လို့ font နာမည်ကို ပိတောက်ဖောင့်နာမည်ပေးပြီး run ရင်တော့ အောက်ပါအတိုင်း ထွက်လာတဲ့ PNG ဖိုင်မှာလည်း စာလုံးပုံစံပြောင်းလဲသွားတာကို မြင်တွေ့ရမှာ ဖြစ်ပါတယ်။  

```
$./txt2png.sh ./input.txt Padauk
```

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/padauk-output.png" alt="converted PNG file" />
</p>


## 84. [pic2histogram.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic2histogram.sh)  
picture ဖိုင်တစ်ဖိုင်ကို color histogram အဖြစ် ပြောင်းသိမ်းဖို့အတွက် ရေးခဲ့တဲ့ script ပါ။  

အရင်ဆုံး example picture ဖိုင်ကို ကြည့်ကြည့်ရအောင်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/ucshinthada-present.jpg" alt="original picture file" width="400x225"/>
</p>
<p align="center"> Fig. Original photo (a present from University of Computer Studies, Hinthada) </p>  

command ကတော့ အောက်ပါအတိုင်းပေးပြီးတော့ run ပါတယ်။  
./pic2histogram.sh <picture-filename> <output-histogram-filename>  
	
```
./pic2histogram.sh ./ucshinthada-present.jpg ./col_hist.png
```

<p align="center"> 
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/col_hist.png" alt="converted histogram picture file" />
</p>
<p align="center"> Fig. Converted histogram file </p> 


## 85. [tesseract-ocr.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/tesseract-ocr.sh)  
လက်ရှိမှာ Google က develop လုပ်နေတဲ့ [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) ကို 2015 လောက်မှာကတည်းက ကျွန်တော် မြန်မာစာနဲ့ ကမ္ဘောဒီယားစာဖြစ်တဲ့ ခမာစာအတွက် OCR မော်ဒယ် ဆောက်ကြည့်တာ၊ စမ်းခဲ့တာတွေကို အမျိုးမျိုးလုပ်ခဲ့ပါတယ်။ မြန်မာစာအတွက် စမ်းထားတာကို အဲဒီတုန်းက MIIT, မန္တလေး ရဲ့ opening ceremony မှာ UCSY က ဆရာမဝင်းပပက အကူအညီတောင်းခဲ့လို့ "Myanmar Printed Character Recognition" ဆိုတဲ့ခေါင်းစဉ်နဲ့ demo လုပ်ပြခဲ့ကြပါသေးတယ်။  

ဒီနေရာမှာတော့ Google က ဆောက်ပေးထားတဲ့ OCR engine ကို လွယ်လွယ်ကူကူနဲ့ command line ကနေ ခေါ်သုံးတာကို လုပ်ကြည့်ထားတဲ့ bash shell script ပါ။ အရင်ဆုံး ကိုယ်စက်ထဲမှာ Tesseract OCR command ကို run လို့ရဖို့အတွက် installation လုပ်ထားမှသာ၊ အခု shell script က မှန်မှန်ကန်ကန် အလုပ်လုပ်ပေးမှာ ဖြစ်ပါတယ်။ Installation ကတော့ Ubuntu Linux OS စက်မှာ ဆိုရင်တော့ "sudo apt-get install tesseract-ocr" command နဲ့ install လုပ်လို့ရပါတယ်။  

နောက်ပြီးတော့ OCR test လုပ်ဖို့အတွက်က စာရိုက်ထားတဲ့ text ဖိုင် သို့မဟုတ် PDF ဖိုင်ကို picture ဖိုင်အဖြစ် (e.g. PNG file) လည်း ပြောင်းပြီးတော့ ပြင်ဆင်ထားဖို့ လိုအပ်ပါတယ်။  
အင်္ဂလိပ်စာ OCR လုပ်ဖို့အတွက်က အထက်မှာ ပြခဲ့တဲ့ apt-get install နဲ့ install လုပ်ခဲ့ယုံနဲ့ "/usr/share/tesseract-ocr/4.00/tessdata/" path အောက်မှာ eng.traineddata ဆိုတဲ့ model ဖိုင်ကိုပါ copy ကူးပေးသွားမှာဖြစ်ပေမဲ့ မြန်မာစာတို့လို တခြား ဘာသာစကားနဲ့ OCR ကို စမ်းကြည့်ဖို့ ဆိုရင်တော့ ကိုယ့်ဖာသာကိုယ် download လုပ်ယူထားရမှာ ဖြစ်ပါတယ်။ ဥပမာအနေနဲ့ မြန်မာစာ OCR ကို လုပ်ဖို့အတွက် လိုအပ်တဲ့ mya.traineddata ဖိုင်ကို အောက်ပါအတိုင်း wget command နဲ့ copy ကူယူလိုက်ပါ။  

```
(base) ye@ykt-pro:/usr/share/tesseract-ocr/4.00/tessdata$ sudo wget https://github.com/tesseract-ocr/tessdata/raw/master/mya.traineddata
[sudo] password for ye: 
--2020-09-10 19:26:45--  https://github.com/tesseract-ocr/tessdata/raw/master/mya.traineddata
Resolving github.com (github.com)... 13.229.188.59
Connecting to github.com (github.com)|13.229.188.59|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/tesseract-ocr/tessdata/master/mya.traineddata [following]
--2020-09-10 19:26:45--  https://raw.githubusercontent.com/tesseract-ocr/tessdata/master/mya.traineddata
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4640591 (4.4M) [application/octet-stream]
Saving to: ‘mya.traineddata’

mya.traineddata                 100%[=====================================================>]   4.42M   517KB/s    in 8.7s    

2020-09-10 19:26:54 (519 KB/s) - ‘mya.traineddata’ saved [4640591/4640591]
```

ဒီနေရာမှာတော့ အရင်ဆုံး မြန်မာစာ OCR ကို စမ်းကြည့်ကြရအောင်။  
input လုပ်မဲ့ ပုံကတော့ အောက်မှာ ပြထားတဲ့ အတိုင်းပါပဲ။ တကယ်က သိချင်လို့ မြန်မာစာကြောင်း\<TAB\>ဘိတ်စာကြောင်း format နဲ့ ရိုက်ထည့်ထားခဲ့တာပါ။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/mya.png" alt="input png file for Myanmar language" width="1142x254"/>
</p>
<p align="center"> Fig. Input PNG file for testing Myanmar language OCR </p>  

မြန်မာစာ အတွက် Tesseract OCR ကို run ပြီး output အဖြစ်ထွက်လာတဲ့ဖိုင်ကို လေ့လာကြည့်ကြရအောင်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/tesseract-ocr$ ./tesseract-ocr.sh mya ./input.png myanmar-output
Tesseract Open Source OCR Engine v4.0.0-beta.1 with Leptonica
Warning. Invalid resolution 0 dpi. Using 70 instead.
Estimating resolution as 305
Detected 34 diacritics
ဝု င္လ
ရိုရင် စိတ် ပြန် ဖြး ငြ မှာဆို ငါ းဝေါး ငရယ ||
ကျွန်တော်သာ သူ့ . နေရာ မှာ ရှ ရင စတ ဖောက်ပြန်သွားမှာ သေရျာတယလံ ငါ သူ နေရာ ငှ ဆု ရှး ဇု ရ ဝ
န် တာ်သာ ရာ ဓှာ ရို င် စိတ် ဖောက်ပြန်သွား မှ ဓှာ သျ တယ | ငါ သူ နေရာ မှာဆု င ရူးဝေ ဓိ နုငရယ [|
ကး စး ဖြ ၉ လ ဖီ င် ပိ င် ယ် ကော်ဖီ လက်ဖက်ရည် သောက်ဝို့လာ [|
မင်း ညစာ နဲ့အတူ ဘာ လိုချင် ပဲ | ကောဲဖီ လား ! လက်ဖက်ရည် လား [| န ညာ ဘာ လွ ရျငရ က မြ် ဖကရည က် |
ကာဖ လကဖက သော လာ
မင်း ညာ နဲ့အတူ ဘာ လိုချင် လဲ | ကော်ဖီ လား | လက်ဖက်ရည် လား | နင ညစာ ဘာ လု မြး ေ က ရည ဝ့
င္လ င်လို သိပ် င်း ဖြး ဒယ်ဇာ ဝိ င် ခေ ရိ ိုင်ရိ အား ကောငး ပေါမယ် [|
ဒါဆို ခင်ဗျား နေလူ့ထုင ~) သပ ကောငးသွားဓမယ [| ဆု န နရထု ) |
```

အကြမ်းမျဉ်းအားဖြင့် ပြောရရင် အထက်မှာ မြင်ရတဲ့ အတိုင်းပဲ မြန်မာစာအတွက်ကတော့ ရလဒ်က မကောင်းပါဘူး။  
ဒီတစ်ခါတော့ ညာဘက်အခြမ်းက ဘိတ်စာကြောင်းတွေကို ဖျက်လိုက်ပြီး ထပ်စမ်းကြည့်ကြရအောင်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/output.png" alt="input png file for Myanmar language" width="1142x254"/>
</p>
<p align="center"> Fig. Input PNG file for testing Myanmar language OCR 2nd time</p> 

shell script ကို run ကြည့်ပြီး OCR ရဲ့ output မြန်မာစာကြောင်းတွေကို ရိုက်ထုတ်ကြည့်တော့ အောက်ပါအတိုင်း ရလဒ်ရရှိပါတယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/tesseract-ocr$ ./tesseract-ocr.sh mya ./output.png myanmar-output2
Tesseract Open Source OCR Engine v4.0.0-beta.1 with Leptonica
Warning. Invalid resolution 0 dpi. Using 70 instead.
Estimating resolution as 304
Detected 35 diacritics
မြ

ကျွန်တော်သာ သူ့ . နေရာ

-ိာ
ဗ
8၈ 8»
၈ 0၀၉
ပိ

၆)
စာ

သွားမှာ သေချာတယ် !;
န္သွားရှ ချာ

၆ ၆
ာ ဗာ

ကျွန်တော်သာ သူ့ နေရာ

၀~ာ
ဉာ
၈ ဗ
ပိ
စေ

င္မ

၆)
စာ

နသွား မှ ဓှာ သျ တယ် [|
ဝ

မင်း င စာ ဒဲအကူ ဘာ လုချ

7

ဖြူ လက်ဖက်ရည် လား |

ဂိ
[ပ
ဖိ
- 0
ပူ
င
ဝဝ
အ
ဂာ
8.
စ္တ
ပိ
စေ
ဂ

ဖြူ ၂ လက်ဖက်ရည် လား |

ထ.
၆၀
ငာ
လှိ
_
၀”
ပိ
၀ာ
ပ
ငာ
(ဟ
ပ
ဂာ
ဧ
ဝာ
```
အထက်ပါအတိုင်း ရလဒ်ကတော့ သိပ်အဆင်မပြေပါဘူး။  
Font ကို လက်ရှိမှာ Myanamar3 ဖောင့်နဲ့ စမ်းထားတာ ဖြစ်ပါတယ်။ တခြား image resolution, line breaking, training လုပ်တုန်းက သုံးခဲ့တဲ့ မြန်မာစာ ဒေတာရဲ့ word segmentation ကိစ္စတွေကိုလည်း ထည့်သွင်းစဉ်းစားဖို့ လိုအပ်ပါလိမ့်မယ်။ အရင်ဆုံး သူ့မော်ဒယ်ကို ကျွန်တော်တို့ လေ့လာကြည့်ဖို့ လိုအပ်တယ်လို့ နားလည်ပါတယ်။  

နောက်ထပ် test လုပ်တဲ့ အနေနဲ့ English OCR ကို စမ်းကြည့်ကြရအောင်။ input PNG ဖိုင်က အောက်မှာ ပြထားတဲ့ အတိုင်းပါပဲ။ ပုံကို browser မှာကြည့်ရတာသေးနေရင် ပုံပေါ်မှာ click နှိပ်ပြီးလည်း ကြည့်လို့ ရပါတယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/eng-monospace.png" alt="input png file for English language" width="1453x1530"/>
</p>
<p align="center"> Fig. Input PNG file for testing English language OCR </p>  

tesseract-ocr.sh ကို run ကြည့်ကြရအောင်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/tesseract-ocr$ ./tesseract-ocr.sh eng ./eng-monospace.png eng-monospace
Tesseract Open Source OCR Engine v4.0.0-beta.1 with Leptonica
Warning. Invalid resolution 0 dpi. Using 70 instead.
Estimating resolution as 416
Paper Title: Unsupervised Neural Machine Translation between Myanmar Sign Language and Myanmar Language
Authors: Swe Zin Moe, Ye Kyaw Thu, Hnin Aye Thant, Nandar Win Min and Thepchai Supnithi

Abstract:
This paper investigate the utility of unsupervised Neural Machine translation (U-NMT) on low-resource Language pairs: Myanmar sign language (MSL) and Myanmar language.

Since state-ofthe-art neural machine translation (NMT) require large amount of parallel sentences, which we do not have for pairs we consider.
We focus primarily on incorporating two different types of monolingual data: translated Myanmar sentences of primary English and myPOS data, only into our Myanmar language side.

We found that the incorporating monolingual data achieved higher performance than the baseline approach.
We prepared four types of training data for U-NMT models and the results clearly show that using the myPOS corpus on incorporating the Myanmar Language monolingual data achieved the highest BLEU scores when compared to other training data.
```

အထက်မှာ မြင်ရတဲ့အတိုင်းပါပဲ။ အင်္ဂလိပ်စာအတွက် ကောင်းကောင်း အလုပ်လုပ်တာကို တွေ့ကြရပါလိမ့်မယ်။  

ကောင်းပြီ ဂျပန်စာအတွက် စမ်းကြည့်ကြရအောင်။ input ထည့်ပေးထားတဲ့ ဖိုင်က ကျွန်တော်က ဂျပန်လို့ ရေးခဲ့တဲ့ essay တစ်ပုဒ်ပါ။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/jpn.png" alt="input png file for Japanese language" width="1426x1906"/>
</p>
<p align="center"> Fig. Input PNG file for testing Japanese language OCR </p>  

tesseract-ocr.sh ကို ဂျပန်စာ OCR အတွက် test လုပ်ကြည့်ကြရအောင်။ ထွက်လာတဲ့ output ဂျပန်စာကြောင်းတွေကို PNG ဖိုင်ထဲက ဂျပန်စာကြောင်းတွေနဲ့ တိုက်ကြည့်ကြရအောင်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/tesseract-ocr$ ./tesseract-ocr.sh jpn ./jpn.png japanese
Tesseract Open Source OCR Engine v4.0.0-beta.1 with Leptonica
Warning. Invalid resolution 0 dpi. Using 70 instead.
Estimating resolution as 475
エ ッ セ イ ② ④ ③ : イ エ チ ョ ウ ト ゥ ` テ レ ビ か ら 学 ぶ 日 本 」

母 国 ミ ャ ン マ ー で は ニ ュ ー ス 番 組 を 除 い て テ レ ビ を ほ と ん ど 見 な か っ た 私 だ が 、

来 日 後 は 時 間 を 見 つ け て は 見 る よ う に な っ た 。

と い う の は 、 日 本 の テ レ ビ 番 組 に は 素 晴 ら し い も の が 多 く 、 学 び の 可 能 性 が 無 限 に 広 が っ て い る か ら だ c。

来 日 当 初 は 、 主 に 日 本 語 の 学 習 の た め に テ レ ビ を 見 て い た

NHK の 教 育 番 組 だ け で な く 、 ド ラ マ か ら 日 常 会 話 や 若 者 の 使 う 日 本 語 な ど を 学 ん だ 。

字 幕 付 き の 番 組 も 多 く 、 漢 字 の 勉 強 に 役 立 っ た 。

日 本 語 が だ ん だ ん 分 か る よ う に な る と 、 ス ポ ー ツ 、 旅 行 、 文 化 、 ド キ ュ メ ン タ リ ー な と ど 、

さ ま ざ ま な 番 組 を 見 る よ う に な り 、 日 本 の 文 化 に 対 す る 理 解 が 少 し ず つ 深 ま っ て い っ た 。

最 近 で は 、 お 笑 い や 政 治 番 組 も 理 解 で き る よ う に な り 、 く だ け た 日 本 語 や 逆 に 硬 い 日 本 語 を 学 ぶ の に 役 立 っ て い る 。

こ の よ う に 日 本 の テ レ ビ 番 組 は 私 に と っ て 貴 重 な 学 び の 場 で あ る が 、

中 で も ド キ ュ メ ン タ リ ー 番 組 か ら は 多 く の こ と を 学 ん だ 。

た と え ば 、 戦 争 体 験 者 の 話 か ら 日 本 の 歴 史 的 事 実 を 初 め て 学 ん だ 。

ミ ャ ン マ ー に い た 時 は 、 戦 争 を 体 験 し た 日 本 人 の 痛 み な ど 全 く 知 ら な か っ た が 、

つ ら い 時 代 を 過 ご し た 日 本 人 の 語 る 内 容 に 強 い 衝 撃 を 受 け 、 戦 争 に つ い て 深 く 考 え る き っ か け と な っ た 。
ま た 、 障 害 を も っ た 人 や 病 気 の 人 が 懸 命 に 生 き よ う と 頑 張 っ て い る 姿 を 描 い た 番 組 を 見 て 、

心 を 揺 さ ぶ ら れ 、 命 の 重 さ に つ い て 考 え さ せ ら れ た 。

歴 史 上 の 偉 人 、 研 究 者 、 政 治 家 な ど 、 日 本 を 変 え る た め に 人 生 を か け て い る 人 に つ い て の 番 組 も よ く 見 る 。
こ の よ う な 立 派 な 人 々 の 努 力 が あ っ た か ら こ そ 、 日 本 は こ こ ま で 豊 か な 国 に な っ た の だ と 実 感 す る 。

そ ん な 時 、 自 分 も で き る こ と を 精 一 杯 や ら ね ば と い う 思 い で 胸 が 熱 く な る 。

も ち ろ ん テ レ ビ が 与 え る 影 響 に は 良 い も の も 悪 い も の も あ り 、 場 合 に よ っ て は 危 険 性 も あ る 。
し か し 、 私 は 、 日 本 の テ レ ビ 番 組 は 素 晴 ら し い 教 育 手 段 の ひ と つ で あ る と 考 え る 。
研 究 を 行 う 上 で 手 が か り と な る よ う な 幅 広 い 知 識 を 得 る こ と も で き 、 私 に と っ て は 知 識 の 宝 庫 と い え る 。

学 会 な ど で 海 外 を 訪 れ た 際 は 、 短 時 間 で も テ レ ビ 番 組 を 見 る よ う に し て い る 。

そ う す る こ と に よ り 、 文 化 、 流 行 、 教 育 な ど に 触 れ る こ と が で き 、 少 し そ の 国 に 近 づ け た よ う な 気 が す る の だ 。

こ の よ う な 経 験 か ら 、 日 本 に 来 た ば か り の 人 へ ヘ ア ド バ イ ス を す る と す れ ば 、 テ レ ビ か ら 学 ぶ 日 本 を お 薦 め し た い 。

わ ず か な 時 間 で も 、 何 か を 学 び 取 ろ う と い う 意 識 を も っ て テ レ ビ を 見 る こ と で 大 い に 勉 強 に な る と い う こ と を 伝 え た い 。

寝 転 が っ て い な が ら リ モ コ ン ひ と つ で 勉 強 が で き る 日 本 で は 、 い く ら で も 知 識 を 増 や し て い く こ と が で き る 。
今 夜 も テ レ ビ を つ け た ま ま 届 眠 り し て 朝 を 迎 え る こ と に な り そ う だ …。

ベ イ エ チ ョ ウ ト ゥ 衣 Ye Kyaw Thu

⑲⑦⑤ 年 、 ミ ャ ン マ ー ( ヤ ン ゴ ン ) 生 ま れ 。②000 年 、Dagon University ( ミ ャ ン マ ー) 物 理 学 部 卒 業 。
⑳0⑥ 年 、 早 稲 田 大 学 大 学 院 国 際 情 報 通 信 研 究 科 修 士 課 程 修 了 。 現 在 、 同 大 学 助 手 。

ヒ ュ ー マ ン ・ コ ン ピ ュ ー タ ・ イ ン タ ラ ク シ ョ ン 、 自 然 言 語 処 理 、

子 供 お よ び 障 害 者 を 対 象 と し た 教 育 に 関 す る 研 究 を 行 い 、 博 士 号 取 得 を 目 指 し て い る 。

趣 味 は 、 武 道 ( 合 気 道 、 テ コ ン ド ー、 カ ン フ ー) 、 読 書 、 旅 行 。

⑳①0 年 ④ 月 ②① 日

```

အထက်မှာ တွေ့ရတဲ့အတိုင်းပါပဲ မြန်မာစာအတွက်သာ ကောင်းကောင်းအလုပ်မလုပ်ပေမဲ့ အင်္ဂလိပ်စာနဲ့ ဂျပန်စာအတွက်က သုံးလို့ရနိုင်လောက်အောင် အလုပ်လုပ်ပေးတာကို တွေ့ကြရပါလိမ့်မယ်။ တစ်ခုတော့ ရှိပါတယ်။ ဒီမှာ သုံးထားတဲ့ မြန်မာစာအတွက် OCR engline က ဘယ်လို approach နဲ့ မော်ဒယ်ဆောက်ထားတာလဲ၊ ဘယ်လို ဒေတာကို သုံးထားတာလဲ၊ update ကော လုပ်ထားရဲ့လား စတဲ့ အချက်တွေပေါ်လည်း အများကြီး မူတည်ပါလိမ့်မယ်။ ကျွန်တော်တို့လို့ မြန်မာလူမျိုး NLP Researcher တွေအတွက်လည်း ဖြည့်စရာ ကွက်လပ်တွေက ရှိနေမှာ သေချာပါတယ်။ Cheers! :) 


## 86. [sylbreak-10fold-mt.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/sylbreak-10fold-mt.sh)  

Machine Translation experiment တွေကို မြန်မာနိုင်အတွင်းမှာ သုံးနေတဲ့ ဗမာစာနဲ့ တခြား တိုင်းရင်းသားဘာသာစကားတွေနဲ့ ပတ်သက်ပြီး လုပ်တဲ့အခါမှာ parallel corpus လည်း မရှိတဲ့အတွက်ကြောင့် corpus ကိုလည်း ကိုယ့်ဖာသာကိုယ် ဆောက်ကြရပါတယ်။ လက်တွေ့ လုပ်ကြတဲ့အခါမှာ parallel corpus တစ်ခုကို ၆လကနေ တစ်နှစ်လောက် အချိန်ယူပြင်ဆင်ကြရပါတယ်။ အဲဒီလောက် ပြင်ဆင်တာတောင်မှ တကယ်တမ်းကက စာကြောင်းရေ နှစ်သောင်းလောက် သုံးသောင်းလောက်ဆိုတဲ့ size က သုတေသနအတွက် experiment အတွက်ကနည်းနေသေးတဲ့အတွက် (အထူးသဖြင့် Neural Machine Translation အတွက်) ရလဒ်ကိုသေချာအောင် 10-fold cross validation လုပ်ပြီးမှ run ကြရပါတယ်။ အဲဒီလို လုပ်တဲ့အခါမှာ word segmentation တစ်ခုတည်းနဲ့သာမကပဲ တခြား sub-word level segmentation တွေနဲ့လည်း machine translation ရဲ့ရလဒ်ကိုကောင်းဖို့ ကြိုးစားကြရပါတယ်။ ဥပမာ syllable segmentation, Byte pair Encoding, Sentencepiece စတာတွေပါ။ ခုချိန်အထိတော့ ကျောင်းသားတွေနဲ့ တိုင်းရင်းသား ဘာသာစကားတော်တော်များများကို machine translation experiment တွေ လုပ်ခဲ့ပြီးပါပြီး အဲဒီအထဲကမှ ဗမာ၊ ရခိုင်၊ ထားဝယ်၊ ဘိတ်၊ ရှမ်း၊ ကရင်၊ ပအို့ဝ့် စတဲ့ ဘာသာရပ်တွေ အတွက် syllable breaking ကို အလွယ်တကူနဲ့ လုပ်လို့ ရပါတယ်။ အခုပရိုဂရမ်ကတော့ အဲဒီလိုလုပ်ကြတဲ့အခါမှာ ကျွန်တော် ဥပမာအနေနဲ့ရေးပြပြီး github မှာတင်ထားတဲ့ [sylbreak.pl](https://github.com/ye-kyaw-thu/sylbreak/blob/master/perl/sylbreak.pl) perl script ကိုဥပမာအနေနဲ့ သုံးပြီးတော့ 10 fold ခွဲထားတဲ့ training, development, test ဒေတာတွေအားလုံးအတွက် syllable segmentation လုပ်တဲ့အခါမှာ သုံးခဲ့တဲ့ shell script တစ်ပုဒ်ပါ။ တကယ့် လက်တွေ့မှာတော့ တိုင်းရင်းသား ဘာသာစကား တစ်ခုစီအတွက် sylbreak ပရိုဂရမ်ရဲ့ Regular Expression ကိုအနည်းငယ် ဝင်ပြင်ဆင်ရပါတယ်။    


ဥပမာအနေနဲ့ ဗမာ-ဘိတ် parallel corpus အတွက် run တဲ့အခါမှာ အောက်ပါလိုမျိုး output ပြပေးပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:~/exp/dw-bk-my/data/my-bk-syl$ ./sylbreak-10fold-smt.sh my bk
cd 1
head  ./train.my
မင်း ဘာ တွေ စီ စဉ် နေ သ လဲ ဆို တာ ငါ့ ကို ပြော သ င့် တာ ပေါ့ ။
သူ ရို့ စာ အုပ် သုံး ထောင် ကျော် ရောင်း ပြီး သွား ပြီ ။
တ ချို့ လူ တွေ ဟာ မွေး ရာ ပါ ဇာတ် မင်း သား တွေ ပဲ ။
တ ချို့ လူ တွေ ဟာ မွေး ရာ ပါ ဇာတ် မင်း သား တွေ ပဲ ။
သူ မ မင်း ကို ဂ ရု စိုက် သ လား ။
ဘယ် လောက် မြ င့် မြတ် သ လဲ ။
မင်း အဲ့ ဒီ မှာ အ လုပ် လုပ် တယ် ။
သူ မ က မင်း နဲ့ သ ဘော တူ မှာ မ ဟုတ် ဘူး ။
မင်း ရဲ့ သွား နှစ် ချောင်း ကို နုတ် ပစ် ရ မည် ။
သူ မ ဆီ ကို မင်း ဖုန်း ဆက် မှာ မ ဟုတ် ဘူး လား ။
head ./dev.my
ခင် ဗျား မ ပြေး သေး ဘူး လား ။
ကျွန် တော့် အစ် မ က လွဲ လို့ အား လုံး ဒီ မှာ ရှိ ပါ တယ် ။
၁ နာ ရီ ပဲ ရှိ သေး သည် သူ မ ည စာ ချက် ပြီး ပြီ ။
ကျေး ဇူး ပြု ၍ လက် ဖက် ရည် တစ် ခွက် လောက် သောက် ပါ မ လား ။
ဆ ရာ ဝန် ဆီ ဘယ် သူ ပဲ လာ လာ ၊ သူ အ ပြင် သွား တယ် လို့ သူ တို့ ကို ပြော လိုက် ပါ ။
သူ မ က ငါ့ ကို သိ တယ် ။
အို ကေ ရုံ ပါ ပဲ ။
သူ မ ငါ့ ကို ဘယ် လို နည်း နဲ့ ချစ် လဲ ။
မင်း ဒီ စာ အုပ် ပြန် ဖတ် မှာ လား ။
သူ မင်း ကို မ ထောက် ခံ ခဲ့ ဘူး လား ။
head ./test.my
သူ မ ခင် ဗျား ကို အဲ့ ဒါ ပေး မှာ မ ဟုတ် ဘူး ။
မင်း ဘယ် သူ့ ကို ဒုက္ခ ပေး ခဲ့ တာ လဲ ။
သိပ် ပြေ တာ ပေါ့ ။
မင်း ဘာ တွေ ရေး နေ တာ လဲ ။
ဆ ရာ လာ ပြီ ။
ဆ ရာ လာ ပြီ ။
သူ အင်္ဂ လိပ် စ ကား ပြော နိုင် လား ။
ခင် ဗျား ဆေး လိပ် လျှော့ သောက် ခဲ့ တယ် ။
သူ တို့ ငွေ မ စု ကြ ဘူး နော် ငွေ စု ကြ သ လား ။
သူ မ က သူ့ ကို သိ ထား တာ ။
==========
head  ./train.bk
နင် ဘာ စီ စဉ် နေ ရယ် ဆို တာ ငါ့ ဝို ပြော သင့် ပေါ့ လန်း ။
သူ လို့ စာ အုပ် သုံး ထောင် ကျော် ရောင်း ပီး ဟော ဘီ ။
ငယ် ငယ် တည်း က မင်း သား လုပ် ဝို့ ဝါ သ နာ ပါ စ ။
ငယ် ငယ် တည်း က မင်း သား လုပ် ဝို့ ဝါ သ နာ ပါ စ ။
ဒယ် ကောင် မ ငယ် နင့် ဝို ဂ ရု စိုက် ရယ် လား ။
ဘ ဇာ လောက် မြ င့် မြတ် ရိ ။
နင် ဒယ် မှာ အ လုပ် လုပ် ဝယ် ။
ဒယ် ကောင် မ ငယ် ဟ မင်း ဟက် သ ဘော တူ မှာ မ ဟုတ် ဝ ။
နင့် ရဲ့ သွား နှစ် ချောင်း ကို နုတ် ပစ် ရ မရ် ။
သူ့ ဆီ ကို နင် ဖုန်း ဆက် မယ် မ ဟုတ် ဝ လား ။
head ./dev.bk
နင် မ ပြေး သေး ရ လား ။
အား လုံး က ဒါ မှာ ဘဲ အစ် မ တစ် ယောက် မ ရှိ ရ ။
၁ နာ ရီ ပဲ ရှိ သေး ရိ ဒယ် ကောင် မ ငယ် ည စာ ချက် ပြီး လေ ။
ကျေး ဇူး ပြု ၍ လက် ဖက် ရည် တစ် ခွက် လောက် သောက် မ လား ။
ဆ ရာ ဝန် နား ဘ သူ ပဲ့ လာ လာ ၊ သူ အ ပြင် သွား ဝယ် လိ သူ့ လို့ ဝို ပြော လိုက် န ။
အဲ့ အ မ လေ ငါ့ ကို သိ ရယ် ။
အို ကေ ရုံ ပဲ ။
ဒယ် ကောင် မ ငယ် ငါ့ ကို ဘာ နည်း ဟင့် ချစ် ရယ် ။
နင် စာ အုပ် ပြန် ဖတ် ဝို့ လား ။
သူ နင့် ကို မ ထောက် ခံ က လား ။
head ./test.bk
သူ ခင် ဗျား ကို ဒယ် ဇာ ပေး ဟုတ် ဝ ။
နင် ဖယ် သူ့ ဝို စိတ် ညစ် ပေး ခဲ့ လဲ ။
သိပ် ပြေ တာ ပေါ့ ။
နင် ဘာ ဇာ တွေ ရေး နေ ရယ် ။
ဆ ရာ လာ နေ ရယ် ။
ဆ ရာ လာ နေ ရယ် ။
သူ အင်္ဂ လိပ် စ ကား ပြော နိုင် လား ။
ခင် ဗျား ဆေး လိပ် လျှော့ သောက် ခဲ့ ရယ် ။
သူ ဝို့ ကျီး ပြား မ စု ရ ၊ စု နေ လား ။
အဲ့ အ မ လေ သူ့ ကို သိ ထား ဇာ ။
==========
cd 2
head  ./train.my
သူ မ ခင် ဗျား ကို အဲ့ ဒါ ပေး မှာ မ ဟုတ် ဘူး ။
မင်း ဘယ် သူ့ ကို ဒုက္ခ ပေး ခဲ့ တာ လဲ ။
သိပ် ပြေ တာ ပေါ့ ။
...
...
...
==========
cd 10
head  ./train.my
သူ မ ခင် ဗျား ကို အဲ့ ဒါ ပေး မှာ မ ဟုတ် ဘူး ။
မင်း ဘယ် သူ့ ကို ဒုက္ခ ပေး ခဲ့ တာ လဲ ။
သိပ် ပြေ တာ ပေါ့ ။
မင်း ဘာ တွေ ရေး နေ တာ လဲ ။
ဆ ရာ လာ ပြီ ။
ဆ ရာ လာ ပြီ ။
သူ အင်္ဂ လိပ် စ ကား ပြော နိုင် လား ။
ခင် ဗျား ဆေး လိပ် လျှော့ သောက် ခဲ့ တယ် ။
သူ တို့ ငွေ မ စု ကြ ဘူး နော် ငွေ စု ကြ သ လား ။
သူ မ က သူ့ ကို သိ ထား တာ ။
head ./dev.my
သူ တို့ မ ကြိုး စား ခဲ့ ကြ ဘူး လား ။
ဒါ ပေ မဲ့ ဒီ လို နဲ့ တင် နိ ဂုံး ချုပ် သွား တာ မ ဟုတ် ပါ ဘူး ။
သူ တို့ ဘယ် သူ့ သ မီး တွေ လဲ ။
ကျွန် တော် ကျွန် တော့် ရဲ့ ခဲ တံ ကို ချွန် ချင် တယ် ။
မ ပြီး သေး ဘူး ။
သူ မ က သူ့ ကို သတ် ခဲ့ တာ လား ။
ငါ ပြန် သ တိ ရ လာ မယ် ထင် တယ် ။
ငါ ပြန် သ တိ ရ လာ မယ် ထင် တယ် ။
အ စွပ် စွဲ ခံ ရ မဲ့ လူ တစ် ယောက် ဟာ ဘယ် လို ခံ စား ရ မ လဲ ဆို တာ မင်း စဉ်း စား ကြ ည့် ။
ငါ စွ န့် လွှတ် မှ ပဲ ရ တော့ မယ် ။
head ./test.my
ဒါ ဘယ် သူ့ ထ မင်း ဘူး လဲ ။
ဒါ ဘယ် သူ့ ထ မင်း ဘူး လဲ ။
သူ မ စိတ် မ ဆိုး ဘူး လား ။
မင်း ရှင်း ပြ တဲ့ အ ဖြေ ။
သူ မ ဘာ အံ့ ဩ ခဲ့ တာ လဲ ။
သူ မ စော စော ထွက် သွား ခဲ့ လို့ ဖြစ် ရ မယ် ။
သူ မ ဘယ် လောက် ထူး ချွန် သ လဲ ။
တောင် တက် သ လား ။
သူ မ ကြာ မ ကြာ အ ရက် သောက် သ လား ။
အဲ ဒါ ခု နစ် ဆ ယ့် ငါး ဆ င့် ကျ ပါ တယ် ။
==========
head  ./train.bk
သူ ခင် ဗျား ကို ဒယ် ဇာ ပေး ဟုတ် ဝ ။
နင် ဖယ် သူ့ ဝို စိတ် ညစ် ပေး ခဲ့ လဲ ။
သိပ် ပြေ တာ ပေါ့ ။
နင် ဘာ ဇာ တွေ ရေး နေ ရယ် ။
ဆ ရာ လာ နေ ရယ် ။
ဆ ရာ လာ နေ ရယ် ။
သူ အင်္ဂ လိပ် စ ကား ပြော နိုင် လား ။
ခင် ဗျား ဆေး လိပ် လျှော့ သောက် ခဲ့ ရယ် ။
သူ ဝို့ ကျီး ပြား မ စု ရ ၊ စု နေ လား ။
အဲ့ အ မ လေ သူ့ ကို သိ ထား ဇာ ။
head ./dev.bk
သူ့ လို မ ကြိုး စား ကြ က လား ။
ဒါ မဲ့ ဒီ လို နဲ့ နိ ဂုံး ချုပ် သွား တာ မ ဟုတ် ဘူး ။
သူ တို့ ဖယ် သူ့ သား သ မီး လဲ ။
ကျ နော့် ကျွန် နော့် ခဲ တံ ဝို ချွန် ချင် ရယ် ။
မ ပြီး သေး ရ ။
သူ က သူ့ ကို သတ် လိုက် ရယ် လား ။
ငါ ပြန် မှတ် မိ မယ် ထင် ရရ် ပဲ့ ။
ငါ ပြန် မှတ် မိ မယ် ထင် ရရ် ပဲ့ ။
အ စွပ် စွဲ ခံ ရ မဲ့ လူ ဘင်း မျိုး ခံ စား ရ မယ် ဆို တာ နင် ပဲ့ စဉ်း စား ကြည့် ။
ငါ စွန့် လွှတ် မှ ဘဲ့ ရ ဝေါ့ မယ် ။
head ./test.bk
အယ့် ဒါ ဘယ် သူ့ ထ မင်း ဘူး ရိ ။
အယ့် ဒါ ဘယ် သူ့ ထ မင်း ဘူး ရိ ။
ဒယ် ကောင် မ ငယ် စိတ် မ ဆိုး ဝ လား ။
နင် ရှင်း ဝိုက် တဲ့ ဖြေ ။
ဒယ် ကောင် မ ငယ် ဘာ အံ့ ဩ ခဲ့ တာ လဲ ။
ဒယ် ကောင် မ ငယ် စော ရီး သွား ပီး နေ မရ် ။
ယင်း ကောင် မ ငယ် ဘ ဇာ လောက် ထူး ချွန် ရိ ။
တောင် တက် ရယ် လား ။
သူ ခ ဏ ခ ဏ အ ရောက် သောက် ရယ် လား ။
အဲ ဒါ ခု နှစ် ဆယ် ငါး ဆင့် ကျ ရယ် ။
==========
```

Folder tree structure ကတော့ အောက်ပါအတိုင်း ရှိပါလိမ့်မယ်။  

```
.
├── 1
│   ├── config.baseline
│   ├── dev.bk
│   ├── dev.my
│   ├── generate_configs.pl
│   ├── run-baseline.pl
│   ├── run-pbsmt.sh
│   ├── test.bk
│   ├── test.my
│   ├── test-sgm
│   │   ├── generate_sgms.pl
│   │   ├── ref2sgm.pl
│   │   ├── src2sgm.pl
│   │   ├── test.bk.ref.sgm
│   │   ├── test.bk.src.sgm
│   │   ├── test.my.ref.sgm
│   │   └── test.my.src.sgm
│   ├── train.bk
│   └── train.my
├── 10
│   ├── config.baseline
│   ├── dev.bk
│   ├── dev.my
│   ├── generate_configs.pl
│   ├── run-baseline.pl
│   ├── run-pbsmt.sh
│   ├── test.bk
│   ├── test.my
│   ├── test-sgm
│   │   ├── generate_sgms.pl
│   │   ├── ref2sgm.pl
│   │   ├── src2sgm.pl
│   │   ├── test.bk.ref.sgm
│   │   ├── test.bk.src.sgm
│   │   ├── test.my.ref.sgm
│   │   └── test.my.src.sgm
│   ├── train.bk
│   └── train.my
├── 2
│   ├── config.baseline
│   ├── dev.bk
│   ├── dev.my
│   ├── generate_configs.pl
│   ├── run-baseline.pl
│   ├── run-pbsmt.sh
│   ├── test.bk
│   ├── test.my
│   ├── test-sgm
│   │   ├── generate_sgms.pl
│   │   ├── ref2sgm.pl
│   │   ├── src2sgm.pl
│   │   ├── test.bk.ref.sgm
│   │   ├── test.bk.src.sgm
│   │   ├── test.my.ref.sgm
│   │   └── test.my.src.sgm
│   ├── train.bk
│   └── train.my
├── 3
│   ├── config.baseline
│   ├── dev.bk
│   ├── dev.my
│   ├── generate_configs.pl
│   ├── run-baseline.pl
│   ├── run-pbsmt.sh
│   ├── test.bk
│   ├── test.my
│   ├── test-sgm
...
...
...
├── 9
│   ├── config.baseline
│   ├── dev.bk
│   ├── dev.my
│   ├── generate_configs.pl
│   ├── run-baseline.pl
│   ├── run-pbsmt.sh
│   ├── test.bk
│   ├── test.my
│   ├── test-sgm
│   │   ├── generate_sgms.pl
│   │   ├── ref2sgm.pl
│   │   ├── src2sgm.pl
│   │   ├── test.bk.ref.sgm
│   │   ├── test.bk.src.sgm
│   │   ├── test.my.ref.sgm
│   │   └── test.my.src.sgm
│   ├── train.bk
│   └── train.my
├── clean-space.pl
├── sylbreak-10fold-smt.sh
└── sylbreak.pl

20 directories, 173 files
```

## 87. [syllable-break-multi-files.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/syllable-break-multi-files.sh)  
[sylbreak.pl](https://github.com/ye-kyaw-thu/sylbreak) ဖိုင်က တကယ်တမ်းက Unicode font ကို သုံးပြီး ရိုက်ထားတဲ့ ဗမာစာကြောင်းတွေကို Regular Expression နဲ့ အလွယ်တကူဖြတ်လို့ ရကြောင်းကို အိုက်ဒီရချပြဖို့အတွက် အကြမ်းနဲ့ ရိုးရိုးရှင်းရှင်းပဲ ရေးထားတာဖြစ်ပါတယ်။ အဲဒါကြောင့် လက်တွေ့ [sylbreak.pl](https://github.com/ye-kyaw-thu/sylbreak) ကို သုံးတဲ့အခါမှာ ပိုထွက်လာတဲ့ multiple space တွေကို cleaning လုပ်ဖို့ လိုအပ်ပါတယ်။ ပြီးတော့ ကိုယ်လုပ်တဲ့ experiment ပေါ်မူတည်ပြီး ဖိုင် ၃ဖိုင်၊ ၄ဖိုင်၊ ၅ဖိုင် စတာတွေကို command line argument ကနေ ပေးပြီး သုံးတဲ့ ပုံစံကိုလည်း ဥပမာ shell script နဲ့ ရေးပြထားတာပါ။ ပိုနေတဲ့ space တွေကို ရှင်းတဲ့ အပိုင်းကတော့ [clean-space.pl](https://github.com/ye-kyaw-thu/tools/blob/master/perl/clean-space.pl) ကို သုံးထားပါတယ်။ တကယ်လက်တွေ syllable breaking ကို ဖြတ်တဲ့အခါမှာ လုပ်တဲ့ ပုံစံကို သိစေချင်လို့ တင်ပေးလိုက်တာပါ။  

ဆိုကြပါစို့ ဗမာစာရိုက်ထားတဲ့ ဖိုင် သုံးဖိုင်က အောက်ပါအတိုင်း ရှိတယ်လို့ ...

```
$ head newg1
ပန်းသီး ဆယ် လုံး
အုန်းသီး ဆယ် လုံး
မာလကာသီး ဆယ် လုံး
သံပုရာသီး ဆယ် လုံး
သရက်သီး ဆယ် လုံး
လိမ္မော်သီး ဆယ် လုံး
သင်္ဘောသီး ဆယ် လုံး
နာနတ်သီး ဆယ် လုံး
ဖရဲသီး ဆယ် လုံး
ပန်းသီး တစ် လုံး
$ head newg2
တစ်ဆယ်
တစ်ဆယ့်တစ်
တစ်ဆယ့်နှစ်
တစ်
နှစ်
သုံး
လေး
ငါး
ခြောက်
ခုနှစ်
$ head newg3
မိသားစု သူငယ်ချင်း များ နှင့် ကျွန်ုပ်
ကျွန်ုပ် ၏ နှစ်သက် သော
ကျွန်တော့် ရဲ့ နှစ်သက် သော
ကျွန်မ ရဲ့ နှစ်သက် သော
ပြန်လည် ဆန်းစစ် ခြင်း ၁
စီမံချက် ၁
ကျွန်ုပ် ၏ ဆွေစဉ်မျိုးဆက် ဇယား 
ကျွန်တော့် ရဲ့ ဆွေစဉ်မျိုးဆက် ဇယား 
ကျွန်မ ရဲ့ ဆွေစဉ်မျိုးဆက် ဇယား 
ကျွန်ုပ် ၏ အိမ် နှင့် အိမ်မွေး တိရစ္ဆာန် များ
```

newg1, newg2, newg3 ဖိုင်သုံးဖိုင်ကို syllable breaking လုပ်မယ်။ ပြီးရင် ပိုနေတဲ့ space တွေကိုပါ cleaning လုပ်မယ်ဆိုရင် အောက်ပါအတိုင်း run ပါ။  

```
(base) ye@ykt-pro:/media/ye/project1/tool/sequence_tagging/sequence_tagging/data/POS/ipa/original-data/syl/syl-breaking$ ./syllable-break-multi-files.sh newg1 newg2 newg3
Syllable breaking of newg1...
head newg1.syl.clean
ပန်း သီး ဆယ် လုံး
အုန်း သီး ဆယ် လုံး
မာ လ ကာ သီး ဆယ် လုံး
သံ ပု ရာ သီး ဆယ် လုံး
သ ရက် သီး ဆယ် လုံး
လိမ္မော် သီး ဆယ် လုံး
သင်္ဘော သီး ဆယ် လုံး
နာ နတ် သီး ဆယ် လုံး
ဖ ရဲ သီး ဆယ် လုံး
ပန်း သီး တစ် လုံး
=====
Syllable breaking of newg2...
head newg2.syl.clean
တစ် ဆယ်
တစ် ဆယ့် တစ်
တစ် ဆယ့် နှစ်
တစ်
နှစ်
သုံး
လေး
ငါး
ခြောက်
ခု နှစ်
=====
Syllable breaking of newg3...
head newg3.syl.clean
မိ သား စု သူ ငယ် ချင်း များ နှင့် ကျွန်ုပ်
ကျွန်ုပ် ၏ နှစ် သက် သော
ကျွန် တော့် ရဲ့ နှစ် သက် သော
ကျွန် မ ရဲ့ နှစ် သက် သော
ပြန် လည် ဆန်း စစ် ခြင်း ၁
စီ မံ ချက် ၁
ကျွန်ုပ် ၏ ဆွေ စဉ် မျိုး ဆက် ဇ ယား
ကျွန် တော့် ရဲ့ ဆွေ စဉ် မျိုး ဆက် ဇ ယား
ကျွန် မ ရဲ့ ဆွေ စဉ် မျိုး ဆက် ဇ ယား
ကျွန်ုပ် ၏ အိမ် နှင့် အိမ် မွေး တိ ရစ္ဆာန် များ
=====
```

## 88. [build-fastalign-pt.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/build-fastalign-pt.sh)  

Machine translation လုပ်ကြတဲ့အခါမှာ ဘာသာစကားတစ်ခုကနေ တခြားဘာသာစကားတစ်ခုကို ဘာသာပြန်ပေးတဲ့ရလဒ်တွေ ကောင်းဖို့အတွက်က နည်းမျိုးစုံနဲ့ experiment အမျိုးမျိုးလုပ်ကြရပါတယ်။ အဲဒီအထဲက တစ်ခုကတော့ alignment ကိုပိုကောင်းအောင် alignment technique အမျိုးမျိုးနဲ့ ပြောင်းလုပ်ကြည့်ကြတာပါ။ [fast_align](https://github.com/clab/fast_align) ဆိုတဲ့ alignment toolkit ကလည်း နာမည်ကြီးတဲ့ toolkit တစ်ခုပါ။ အခု မိတ်ဆက်ပေးမယ့် build-fastalign-pt.sh က fast_align tool ကို သုံးပြီးတော့ ထွက်လာတဲ့ word-to-word aligned output ဖိုင်ကနေ machine translation မှာသုံးတဲ့ phrase table (phrase level အဘိဓာန်လို့ အကြမ်းမျဉ်း နားလည်ပါ) တစ်ခုအဖြစ်ဆောက်ဖို့အတွက် ရေးထားတဲ့ shell script တစ်ပုဒ်ပါ။  

ဒီမို phrase table ဆောက်ပြမယ့် ဖိုလ်ဒါအောက်မှာတော့ အောက်ပါဖိုင်တွေကို ပြင်ထားပါတယ်။  
```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo$ ls
train.my  train.myrk.pipe.forward.align  train.myrk.pipe.reverse.align  train.rk
```

train.my ဖိုင်ကတော့ ဗမာစာကြောင်းတွေကို တစ်ကြောင်းချင်း သိမ်းထားတဲ့ဖိုင်ပါ။  
```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo$ head train.my
မင်း အဲ့ဒါ ကို အခြား တစ်ခုနဲ့ မ ချိတ် ဘူးလား ။
သူမ ဘယ်သူ့ကိုမှ မ မှတ်မိတော့ဘူး ။
အဲ့ဒါ ကျွန်တော် တို့ အတွက် ခက်ခဲ တယ် ။
ခင်ဗျား ပြောခဲ့ သလို ကျွန်တော် ရှင်းပြ ခဲ့တယ် ။
သူ့ကို ထိန်းဖို့ မင်း ပဲ တတ်နိုင်တယ် ။
အဲ့ဒါ ကို ကိုယ် တက်နင်း မိသွား လား ။
ငါ စဉ်းစား သလို စဉ်းစားပါ ။
အတင်းပြော ရတာ မုန်း တယ် ။
နောက်ဆုံး တစ် ကြိမ် သူ့ကို ချစ်ပါတယ် လို့ ပြောခွင့်တောင် မ ရ တော့ဘူး ။
နာဆာ မှ ဒုံးပျံ စတက်တာ နဲ့ သူ မှတ်တမ်း ရေး ခဲ့တယ် ။
```

train.rk ဖိုင်ကတော့ စောစောက ဗမာစာကြောင်းတွေကို ဘာသာပြန်ထားတဲ့ ရခိုင်စာကြောင်းတွေပါ။  
```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo$ head train.rk
မင်း ယင်းချင့် ကို အခြား တစ်ခုနန့်  မ ချိတ် ပါလား ။
ထိုမချေ   တစ်ယောက်လေ့  မ မှတ်မိပါယာ ။
ယင်းချင့် ကျွန်တော်  ရို့ အတွက် ခက်ခ ရေ ။
မင်း ပြောခ ရေပိုင် ကျွန်တော် ယှင်းပြ ခရေ ။
သူ့ကို ထိန်းဖို့ မင်း ရာ တတ်နိုင်ရေ ။
ယင်းချင့် ကို ငါ တက်နင်း မိလား လာ ။
ငါ စဉ်းစား ရေပိုင် စဉ်းစားပါ ။
အတင်းပြော ရစွာ မုန်း ရေ ။
နောက်ဆုံး တစ် ကြိမ် သူ့ကို ချစ်ပါရေ လို့ ပြောခွင့် တောင် မ ရ ပါ။
နာဆာ မှ ဒုံးပျံ စတက်စွာ နန့် သူ မှတ်တမ်း ရွီး ခရေ ။
```

train.myrk.pipe.forward.align ကတော့ forward alignment လုပ်ထားတဲ့ ဖိုင်ပါ။  
```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo$ head train.myrk.pipe.forward.align 
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4 5-5
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 3-3 4-4 5-5 6-6 6-7 7-8 8-9 10-10
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8 9-9
```

train.myrk.pipe.reverse.align ဖိုင်ကတော့ reverse alignment လုပ်ထားတဲ့ ဖိုင်ပါ။  
```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo$ head train.myrk.pipe.reverse.align 
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4 5-5
0-0 1-1 2-2 3-3 4-4 5-5 6-6
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 3-3 4-4
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-8 8-9 10-10
0-0 1-1 2-2 3-3 4-4 5-5 6-6 7-7 8-8 9-9
```

/build-fastalign-pt.sh ကို run မယ်ဆိုရင်တော့ source, target ဘာသာစကားတွေရဲ့ extension နှစ်ခုကို command line argument အနေနဲ့ပေးရပါတယ်။ run လို့ ဘာ error မှမရှိရင်တော့ အောက်ပါလိုမျိုး screen output လုပ်ပေးပါလိမ့်မယ်။  
```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo$ time ./build-fastalign-pt.sh my rk
symal: computing grow alignment: diagonal (1) final (1)both-uncovered (1)
Using SCRIPTS_ROOTDIR: /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts
Use of uninitialized value $_EXTERNAL_BINDIR in concatenation (.) or string at /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/training/train-model.perl line 369.
Use of uninitialized value $_EXTERNAL_BINDIR in concatenation (.) or string at /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/training/train-model.perl line 370.
using gzip 
(4) generate lexical translation table 0-0 @ Thu Nov 26 16:04:29 +0630 2020
(/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.my,/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.rk,/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex)
FILE: /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.rk
FILE: /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.my
FILE: /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/aligned.grow-diag-final-and
!!!!!!!!!!!!!!!!!
Saved: /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.f2e and /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.e2f
(5) extract phrases @ Thu Nov 26 16:04:30 +0630 2020
MAX 7 0 0
/home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/generic/extract-parallel.perl 4 split "sort    " /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/extract /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.rk /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.my /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/aligned.grow-diag-final-and ./model/extract 7 --GZOutput 
Executing: /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/generic/extract-parallel.perl 4 split "sort    " /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/extract /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.rk /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.my /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/aligned.grow-diag-final-and ./model/extract 7 --GZOutput 
Started Thu Nov 26 16:04:30 2020
using gzip 
isBSDSplit=0 
Executing: mkdir -p ./model/tmp.26441; ls -l ./model/tmp.26441 
total=16561 line-per-split=4141 
split -d -l 4141 -a 7 /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.my ./model/tmp.26441/source.split -d -l 4141 -a 7 /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/train.rk ./model/tmp.26441/target.split -d -l 4141 -a 7 /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/aligned.grow-diag-final-and ./model/tmp.26441/align.PhraseExtract v1.5, written by Philipp Koehn et al.PhraseExtract v1.5, written by Philipp Koehn et al.PhraseExtract v1.5, written by Philipp Koehn et al.

phrase extraction from an aligned parallel corpusphrase extraction from an aligned parallel corpus


phrase extraction from an aligned parallel corpus
PhraseExtract v1.5, written by Philipp Koehn et al.
phrase extraction from an aligned parallel corpus
.



merging extract / extract.inv
gunzip -c ./model/tmp.26441/extract.0000000.gz ./model/tmp.26441/extract.0000001.gz ./model/tmp.26441/extract.0000002.gz ./model/tmp.26441/extract.0000003.gz  | LC_ALL=C sort     -T ./model/tmp.26441 2>> /dev/stderr | gzip -c > ./model/extract.sorted.gz 2>> /dev/stderr 
gunzip -c ./model/tmp.26441/extract.0000000.inv.gz ./model/tmp.26441/extract.0000001.inv.gz ./model/tmp.26441/extract.0000002.inv.gz ./model/tmp.26441/extract.0000003.inv.gz  | LC_ALL=C sort     -T ./model/tmp.26441 2>> /dev/stderr | gzip -c > ./model/extract.inv.sorted.gz 2>> /dev/stderr 
Finished Thu Nov 26 16:04:35 2020
(6) score phrases @ Thu Nov 26 16:04:35 +0630 2020
(6.1)  creating table half ./model/phrase-table.half.f2e @ Thu Nov 26 16:04:35 +0630 2020
/home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/generic/score-parallel.perl 4 "sort    " /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/score ./model/extract.sorted.gz /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.f2e ./model/phrase-table.half.f2e.gz  --GoodTuring  0 
Executing: /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/generic/score-parallel.perl 4 "sort    " /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/score ./model/extract.sorted.gz /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.f2e ./model/phrase-table.half.f2e.gz  --GoodTuring  0 
using gzip 
Started Thu Nov 26 16:04:35 2020
/home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/score ./model/tmp.26485/extract.0.gz /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.f2e ./model/tmp.26485/phrase-table.half.0000000.gz --GoodTuring  2>> /dev/stderr 
./model/tmp.26485/run.0.sh./model/tmp.26485/run.1.sh./model/tmp.26485/run.3.sh./model/tmp.26485/run.2.shScore v2.1 -- scoring methods for extracted rules
adjusting phrase translation probabilities with Good Turing discounting
Loading lexical translation table from /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.f2e
....
mv ./model/tmp.26485/phrase-table.half.0000000.gz ./model/phrase-table.half.f2e.gzrm -rf ./model/tmp.26485 
Finished Thu Nov 26 16:04:42 2020
(6.3)  creating table half ./model/phrase-table.half.e2f @ Thu Nov 26 16:04:42 +0630 2020
/home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/generic/score-parallel.perl 4 "sort    " /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/score ./model/extract.inv.sorted.gz /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.e2f ./model/phrase-table.half.e2f.gz --Inverse  1 
Executing: /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/generic/score-parallel.perl 4 "sort    " /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/score ./model/extract.inv.sorted.gz /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.e2f ./model/phrase-table.half.e2f.gz --Inverse  1 
using gzip 
Started Thu Nov 26 16:04:42 2020
/home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/score ./model/tmp.26512/extract.0.gz /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.e2f ./model/tmp.26512/phrase-table.half.0000000.gz --Inverse  2>> /dev/stderr 
./model/tmp.26512/run.0.sh./model/tmp.26512/run.1.sh./model/tmp.26512/run.2.sh./model/tmp.26512/run.3.shScore v2.1 -- scoring methods for extracted rules
using inverse mode
Loading lexical translation table from /media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-fastalign/demo/lex.e2f
....
gunzip -c ./model/tmp.26512/phrase-table.half.*.gz 2>> /dev/stderr| LC_ALL=C sort     -T ./model/tmp.26512  | gzip -c > ./model/phrase-table.half.e2f.gz  2>> /dev/stderr rm -rf ./model/tmp.26512 
Finished Thu Nov 26 16:04:50 2020
(6.6) consolidating the two halves @ Thu Nov 26 16:04:50 +0630 2020
Executing: /home/ye/tool/moses-bin/ubuntu-17.04/moses/scripts/../bin/consolidate ./model/phrase-table.half.f2e.gz ./model/phrase-table.half.e2f.gz /dev/stdout --GoodTuring ./model/phrase-table.half.f2e.gz.coc | gzip -c > ./model/phrase-table.gz
Consolidate v2.0 written by Philipp Koehn
consolidating direct and indirect rule tables
adjusting phrase translation probabilities with Good Turing discounting
..
Executing: rm -f ./model/phrase-table.half.*
head ./model/extract.inv.sorted...
" ||| " ||| 0-0
" ||| " ||| 0-0
" ||| " ||| 0-0
" ||| " ||| 0-0
" ငါ ||| " ငါ ||| 0-0 1-1
" ငါ မ ||| " ငါ မ ||| 0-0 1-1 2-2
" ငါ မ သိ ||| " ငါ မ သိ ||| 0-0 1-1 2-2 3-3
" ငါ မ သိ ပါ " ||| " ငါ မ သိ ဘူး " ||| 0-0 1-1 2-2 3-3 4-4 5-5
" ငါ မ သိ ပါ " လို့ ||| " ငါ မ သိ ဘူး " လို့ ||| 0-0 1-1 2-2 3-3 4-4 5-5 6-6
" ငါ မ သိ ပါ ||| " ငါ မ သိ ဘူး ||| 0-0 1-1 2-2 3-3 4-4
head ./model/extract.sorted...
" ||| " ||| 0-0
" ||| " ||| 0-0
" ||| " ||| 0-0
" ||| " ||| 0-0
" ငါ ||| " ငါ ||| 0-0 1-1
" ငါ မ ||| " ငါ မ ||| 0-0 1-1 2-2
" ငါ မ သိ ||| " ငါ မ သိ ||| 0-0 1-1 2-2 3-3
" ငါ မ သိ ဘူး " ||| " ငါ မ သိ ပါ " ||| 0-0 1-1 2-2 3-3 4-4 5-5
" ငါ မ သိ ဘူး " လို့ ||| " ငါ မ သိ ပါ " လို့ ||| 0-0 1-1 2-2 3-3 4-4 5-5 6-6
" ငါ မ သိ ဘူး ||| " ငါ မ သိ ပါ ||| 0-0 1-1 2-2 3-3 4-4
head ./model/phrase-table...
" ||| " ||| 0.680589 1 0.680589 1 ||| 0-0 ||| 4 4 4 ||| |||
" ငါ ||| " ငါ ||| 0.136996 0.767717 0.136996 0.987342 ||| 0-0 1-1 ||| 1 1 1 ||| |||
" ငါ မ ||| " ငါ မ ||| 0.136996 0.762754 0.136996 0.982454 ||| 0-0 1-1 2-2 ||| 1 1 1 ||| |||
" ငါ မ သိ ||| " ငါ မ သိ ||| 0.136996 0.661168 0.136996 0.974838 ||| 0-0 1-1 2-2 3-3 ||| 1 1 1 ||| |||
" ငါ မ သိ ဘူး " ||| " ငါ မ သိ ပါ " ||| 0.136996 0.304067 0.136996 0.909614 ||| 0-0 1-1 2-2 3-3 4-4 5-5 ||| 1 1 1 ||| |||
" ငါ မ သိ ဘူး " လို့ ||| " ငါ မ သိ ပါ " လို့ ||| 0.136996 0.287631 0.136996 0.869484 ||| 0-0 1-1 2-2 3-3 4-4 5-5 6-6 ||| 1 1 1 ||| |||
" ငါ မ သိ ဘူး ||| " ငါ မ သိ ပါ ||| 0.136996 0.304067 0.136996 0.909614 ||| 0-0 1-1 2-2 3-3 4-4 ||| 1 1 1 ||| |||
" လို့ ||| " လို့ ||| 0.136996 0.945946 0.136996 0.955882 ||| 0-0 1-1 ||| 1 1 1 ||| |||
" လို့ ပြန်ဖြေပါ ||| " လို့ ပြန်ဖြေပါ ||| 0.136996 0.945946 0.136996 0.955882 ||| 0-0 1-1 2-2 ||| 1 1 1 ||| |||
" လို့ ပြန်ဖြေပါ ။ ||| " လို့ ပြန်ဖြေပါ ။ ||| 0.136996 0.942099 0.136996 0.93852 ||| 0-0 1-1 2-2 3-3 ||| 1 1 1 ||| |||
./build-fastalign-pt.sh: line 35: ./split-srctrg.sh: No such file or directory

real	0m25.865s
user	0m31.767s
sys	0m1.282s
```

## 89. [txt2ASL-BSL.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/txt2ASL-BSL.sh)  

ကျွန်တော့်ရဲ့ ဒေါက်တာတန်းကျောင်းသူ တစ်ဦးဖြစ်တဲ့ မနီထွေးအောင် (YTU) ရဲ့ experiment တစ်ခုအတွက် ရှေ့မှာရေးခဲ့တဲ့ shell script နံပါတ် 83. [txt2png.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/txt2png.sh) ကို fingerspelling font နှစ်မျိုးနဲ့ ပြောင်းပြီး update လုပ်ထားတဲ့ ပရိုဂရမ်ပါ။ ASL (American Sign Language) နဲ့ BSL (British Sign Language) တို့ရဲ့ fingerspelling တွေက မတူကြပါဘူး။ ASL က A, B, C, D အစရှိတဲ့ အင်္ဂလိပ်စာ စာလုံးတွေကို လက်တဖက်တည်းပြပြီးတော့၊ BSL ကတော့ လက်နှစ်ဖက်နဲ့ ပြတာဖြစ်ပါတယ်။ အဲဒါကြောင့်မို့လို့ ဖောင့်နှစ်မျိုးကိုသုံးထားတာဖြစ်ပါတယ်။  

ဒီတစ်ခါတော့ ကိုယ်က ASL, BSL fingerspelling စာလုံး ပုံဖိုင်တွေအဖြစ် ရိုက်ထုတ်ချင်တဲ့ အင်္ဂလိပ်စာ စာလုံးတွေကို head.out ဆိုတဲ့ဖိုင်ထဲမှာ သိမ်းထားပါတယ်။  
```
$ cat ./head.out 
thumb
index
middle
ring
pinky
fingernail
knuckles
wrist
palm
fist
```

Run တဲ့အခါမှာတော့ အင်္ဂလိပ်စာစာလုံးတွေ ရိုက်သိမ်းထားတဲ့ ဖိုင်နာမည်ကို command line argument အနေနဲ့ ပေးပြီး run လိုက်ယုံပါပဲ။  
```
$ ./txt2ASL-BSL.sh ./head.out 
txt2ASL-BSL conversion for line no. 1 : thumb
txt2ASL-BSL conversion for line no. 2 : index
txt2ASL-BSL conversion for line no. 3 : middle
txt2ASL-BSL conversion for line no. 4 : ring
txt2ASL-BSL conversion for line no. 5 : pinky
txt2ASL-BSL conversion for line no. 6 : fingernail
txt2ASL-BSL conversion for line no. 7 : knuckles
txt2ASL-BSL conversion for line no. 8 : wrist
txt2ASL-BSL conversion for line no. 9 : palm
txt2ASL-BSL conversion for line no. 10 : fist
```

ဖောင့်တွေကလည်း ကိုယ်စက်ထဲမှာ သေချာ install လုပ်ထားတယ်။ ခေါ်သုံးမယ့် ImageMagick ပရိုဂရမ်ကလည်းကိုယ်စက်ထဲမှာ ရှိတယ်ဆိုရင် အောက်ပါအတိုင်း အင်္ဂလိပ်စာလုံး တစ်လုံးချင်းစီအတွက် <word>-asl.png, <word>-bsl.png ဆိုတဲ့ pattern နဲ့ png ပုံဖိုင်တွေကို shell program ရှိတဲ့ path အောက်မှာပဲ သိမ်းပေးပါလိမ့်မယ်။  
```
$ ls *.png
fingernail-asl.png  fist-bsl.png   knuckles-asl.png  middle-bsl.png   palm-bsl.png   ring-asl.png   thumb-bsl.png
fingernail-bsl.png  index-asl.png  knuckles-bsl.png  montage_asl.png  pinky-asl.png  ring-bsl.png   wrist-asl.png
fist-asl.png        index-bsl.png  middle-asl.png    palm-asl.png     pinky-bsl.png  thumb-asl.png  wrist-bsl.png
```
ပုတွေကိုတော့ တစ်ပုံချင်းစီ မပြတော့ပဲ ASL, BSL fingerspelling မတူတာကိုလည်း နှိုင်းယှဉ်ကြည့်လို့ ရအောင် montage command နဲ့ ဘေးချင်းကပ် နှစ်ပုံချင်းစီ စီပြီးသိမ်းထားတဲ့ ပုံအကြီးတစ်ပုံကိုပဲ လေ့လာနိုင်အောင် တင်ပေးထားလိုက်ပါတယ်။ ပုံတစ်ပုံချင်းစီရဲ့ အောက်မှာလည်း ဖိုင်နာမည်နဲ့ ပုံရဲ့ အရွယ်အစား width နဲ့ height တွေကိုလည်း လေဘယ်ထိုးပေးထားပါတယ်။ အောက်ပါအတိုင်းပါ ...   
	
<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/bash/pic/montage_asl.png" alt="input png file for English language" />
</p>
<p align="center"> Fig. ASL vs BSL fingerspelling output png files for English words </p>  

## 90. [mgiza-align.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/mgiza-align.sh)  

[mgiza](https://github.com/moses-smt/mgiza) ကိုသုံးပြီးတော့ word alignment လုပ်တဲ့ပုံစံကို shell script ရေးပြထားတာ ဖြစ်ပါတယ်။ Machine Translation သုတေသနလုပ်တဲ့သူတွေအတွက် အသုံးဝင်ပါလိမ့်မယ်။ configuration ဖိုင်ကိုလည်း တင်ပေးထားပါတယ်။ အောက်ပါ ရှင်းပြထားတဲ့နေရာကနေလည်း select မှတ်ပြီး copy ကူးယူလို့လည်း ရပါတယ်။  

ဥပမာအနေနဲ့ train.my နဲ့ train.rk နှစ်ဖိုင်ထဲမှာ ရိုက်ထည့်ထားတဲ့ မြန်မာ-ရခိုင် parallel sentence တွေကို mgiza နဲ့ word alignment လုပ်တဲ့ပုံစံကို လေ့လာလို့ရအောင် အကြမ်းရှင်းပြပါမယ်။  

file size ကို အရင်လေ့လာကြည့်ကြရအောင်။ စာကြောင်းရေက အောက်ပါအတိုင်း တစ်ဖိုင်မှာ တစ်သောင်းခြောက်ထောင်ကျော်စီ ရှိပါတယ်။  
```
$ wc ./train.{my,rk}
  16561  114843 1875302 ./train.my
  16561  114843 1854469 ./train.rk
  33122  229686 3729771 total
```
  
train.my ဆိုတဲ့ ဖိုင်မှာတော့ မြန်မာစာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ တန်းစီရိုက်ထည့်ထားပါတယ်။
```
$ head train.my
မင်း အဲ့ဒါ ကို အခြား တစ်ခုနဲ့ မ ချိတ် ဘူးလား ။
သူမ ဘယ်သူ့ကိုမှ မ မှတ်မိတော့ဘူး ။
အဲ့ဒါ ကျွန်တော် တို့ အတွက် ခက်ခဲ တယ် ။
ခင်ဗျား ပြောခဲ့ သလို ကျွန်တော် ရှင်းပြ ခဲ့တယ် ။
သူ့ကို ထိန်းဖို့ မင်း ပဲ တတ်နိုင်တယ် ။
အဲ့ဒါ ကို ကိုယ် တက်နင်း မိသွား လား ။
ငါ စဉ်းစား သလို စဉ်းစားပါ ။
အတင်းပြော ရတာ မုန်း တယ် ။
နောက်ဆုံး တစ် ကြိမ် သူ့ကို ချစ်ပါတယ် လို့ ပြောခွင့်တောင် မ ရ တော့ဘူး ။
နာဆာ မှ ဒုံးပျံ စတက်တာ နဲ့ သူ မှတ်တမ်း ရေး ခဲ့တယ် ။
```

train.rk ဖိုင်ထဲမှာက ရခိုင်စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ တန်းစီ ရိုက်ထည့်ထားပါတယ်။ အထက်က train.my ထဲမှာ ရှိတဲ့ စာကြောင်းတွေနဲ့ အဓိပ္ပါယ်တူတဲ့ စာကြောင်းတွေလည်း ဖြစ်ပါတယ်။ အဲဒီလိုမျိုး ပြင်ထားတာကို machine translation လောကမှာတော့ parallel data ဆိုပြီးတော့ ခေါ်ကြပါတယ်။    
```
$ head train.rk
မင်း ယင်းချင့် ကို အခြား တစ်ခုနန့်  မ ချိတ် ပါလား ။
ထိုမချေ   တစ်ယောက်လေ့  မ မှတ်မိပါယာ ။
ယင်းချင့် ကျွန်တော်  ရို့ အတွက် ခက်ခ ရေ ။
မင်း ပြောခ ရေပိုင် ကျွန်တော် ယှင်းပြ ခရေ ။
သူ့ကို ထိန်းဖို့ မင်း ရာ တတ်နိုင်ရေ ။
ယင်းချင့် ကို ငါ တက်နင်း မိလား လာ ။
ငါ စဉ်းစား ရေပိုင် စဉ်းစားပါ ။
အတင်းပြော ရစွာ မုန်း ရေ ။
နောက်ဆုံး တစ် ကြိမ် သူ့ကို ချစ်ပါရေ လို့ ပြောခွင့် တောင် မ ရ ပါ။
နာဆာ မှ ဒုံးပျံ စတက်စွာ နန့် သူ မှတ်တမ်း ရွီး ခရေ ။
```

[config.template](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/config.template) ကတော့ အောက်ပါအတိုင်းပါ။  

```
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-giza$ cat config.template 
adbackoff 0
compactadtable 1
compactalignmentformat 0
coocurrencefile train.SRC_train.TRG.cooc
corpusfile train.SRC_train.TRG.snt
countcutoff 1e-06
countcutoffal 1e-05
countincreasecutoff 1e-06
countincreasecutoffal 1e-05
countoutputprefix 
d 
deficientdistortionforemptyword 0
depm4 76
depm5 68
dictionary 
dopeggingyn 0
dumpcount 0
dumpcountusingwordstring 0
emalignmentdependencies 2
emalsmooth 0.2
emprobforempty 0.4
emsmoothhmm 2
hmmdumpfrequency 0
hmmiterations 5
log 0
logfile train.SRC_train.TRG_mgiza.log
m1 5
m2 0
m3 3
m4 3
m5 0
m5p0 -1
m6 0
manlexfactor1 0
manlexfactor2 0
manlexmaxmultiplicity 20
maxfertility 10
maxsentencelength 101
mh 5
mincountincrease 1e-07
ml 101
model1dumpfrequency 1
model1iterations 5
model23smoothfactor 0
model2dumpfrequency 0
model2iterations 0
model345dumpfrequency 0
model3dumpfrequency 0
model3iterations 3
model4iterations 3
model4smoothfactor 0.4
model5iterations 0
model5smoothfactor 0.1
model6iterations 0
nbestalignments 0
ncpus 4
nodumps 1
nofiledumpsyn 1
noiterationsmodel1 5
noiterationsmodel2 0
noiterationsmodel3 3
noiterationsmodel4 3
noiterationsmodel5 0
noiterationsmodel6 0
nsmooth 4
nsmoothgeneral 0
numberofiterationsforhmmalignmentmodel 5
onlyaldumps 1
outputfileprefix train.SRC_train.TRG.dict
outputpath 
p 0
p0 0.999
peggedcutoff 0.03
pegging 0
previousa 
previousd 
previousd4 
previousd42 
previoushmm 
previousn 
previousp0 
previoust 
probcutoff 1e-07
probsmooth 1e-07
readtableprefix 
restart 0
sourcevocabularyfile train.SRC.vcb
t1 1
t2 0
t2to3 0
t3 0
t345 0
targetvocabularyfile train.TRG.vcb
tc 
testcorpusfile 
th 0
transferdumpfrequency 0
v 0
verbose 0
verbosesentence -10
```

mgiza နဲ့ alignment လုပ်ဖို့ command ပေးတဲ့အခါမှာ configuration ဖိုင်ရဲ့ နာမည်ကို command line argument အနေနဲ့ပေးပြီး run တဲ့ပုံစံနဲ့ run ပါတယ်။ အဲဒါကြောင့် mgiza-align.sh ကို run တဲ့အခါမှာ ပထမဆုံး config.template ကို source, target ဖိုင်နာမည်တွေနဲ့ ဝင်ပြင်ပြီး [config.update](https://github.com/ye-kyaw-thu/tools/blob/master/bash/test-data/config.update) ဆိုတဲ့ ဖိုင်နာမည်အသစ်နဲ့ သိမ်းပါတယ်။ ဘယ်နေရာတွေကို ဝင်ပြင်သွားတာလည်း ဆိုတာကို မြင်ရအောင်လည်း cat နဲ့ ရိုက်ပြပေးလိုက်ပါတယ်။   

```
$ cat config.update
adbackoff 0
compactadtable 1
compactalignmentformat 0
coocurrencefile train.my_train.rk.cooc
corpusfile train.my_train.rk.snt
countcutoff 1e-06
countcutoffal 1e-05
countincreasecutoff 1e-06
countincreasecutoffal 1e-05
countoutputprefix 
d 
deficientdistortionforemptyword 0
depm4 76
depm5 68
dictionary 
dopeggingyn 0
dumpcount 0
dumpcountusingwordstring 0
emalignmentdependencies 2
emalsmooth 0.2
emprobforempty 0.4
emsmoothhmm 2
hmmdumpfrequency 0
hmmiterations 5
log 0
logfile train.my_train.rk_mgiza.log
m1 5
m2 0
m3 3
m4 3
m5 0
m5p0 -1template
m6 0
manlexfactor1 0
manlexfactor2 0
manlexmaxmultiplicity 20
maxfertility 10
maxsentencelength 101
mh 5
mincountincrease 1e-07
ml 101
model1dumpfrequency 1
model1iterations 5
model23smoothfactor 0
model2dumpfrequency 0
model2iterations 0
model345dumpfrequency 0
model3dumpfrequency 0
model3iterations 3
model4iterations 3
model4smoothfactor 0.4
model5iterations 0
model5smoothfactor 0.1
model6iterations 0
nbestalignments 0
ncpus 4
nodumps 1
nofiledumpsyn 1
noiterationsmodel1 5
noiterationsmodel2 0
noiterationsmodel3 3
noiterationsmodel4 3
noiterationsmodel5 0
noiterationsmodel6 0
nsmooth 4
nsmoothgeneral 0
numberofiterationsforhmmalignmentmodel 5
onlyaldumps 1
outputfileprefix train.my_train.rk.dict
outputpath 
p 0
p0 0.999
peggedcutoff 0.03
pegging 0
previousa 
previousd 
previousd4 
previousd42 
previoushmm 
previousn 
previousp0 
previoust 
probcutoff 1e-07
probsmooth 1e-07
readtableprefix 
restart 0
sourcevocabularyfile train.my.vcb
t1 1
t2 0
t2to3 0
t3 0
t345 0
targetvocabularyfile train.rk.vcb
tc 
testcorpusfile 
th 0
transferdumpfrequency 0
v 0
verbose 0
verbosesentence -10
```
mgiza-align.sh ကိုသုံးပြီး မြန်မာစာနဲ့ ရခိုင် parallel data အကြား alignment လုပ်တာကို ဥပမာ လုပ်ပြထားပါတယ်။  

```
$ ./mgiza-align.sh train.my train.rk config.template 
#!/bin/bash -v

# alignment training with mgiza
# written by Ye, LST, NECTEC, Thailand
# Date: 7 Dec 2020
# Note: You have to install mgiza before you use this shell script
# Note: You also have to prepare parallel data and configuration file
#
# How to run: ./mgiza-align.sh <source> <target> <configfile>
# e.g. time ./mgiza-align.sh train.my train.rk config.template


# updating the SOURCE and TARGET filenames of configfile
find ./$3 -type f -exec sed "s|train.SRC|${1}|g;s|train.TRG|${2}|g" {} \; > config.update
cat config.update;
adbackoff 0
compactadtable 1
compactalignmentformat 0
coocurrencefile train.my_train.rk.cooc
corpusfile train.my_train.rk.snt
countcutoff 1e-06
countcutoffal 1e-05
countincreasecutoff 1e-06
countincreasecutoffal 1e-05
countoutputprefix 
d 
deficientdistortionforemptyword 0
depm4 76
depm5 68
dictionary 
dopeggingyn 0
dumpcount 0
dumpcountusingwordstring 0
emalignmentdependencies 2
emalsmooth 0.2
emprobforempty 0.4
emsmoothhmm 2
hmmdumpfrequency 0
hmmiterations 5
log 0
logfile train.my_train.rk_mgiza.log
m1 5
m2 0
m3 3
m4 3
m5 0
m5p0 -1template
m6 0
manlexfactor1 0
manlexfactor2 0
manlexmaxmultiplicity 20
maxfertility 10
maxsentencelength 101
mh 5
mincountincrease 1e-07
ml 101
model1dumpfrequency 1
model1iterations 5
model23smoothfactor 0
model2dumpfrequency 0
model2iterations 0
model345dumpfrequency 0
model3dumpfrequency 0
model3iterations 3
model4iterations 3
model4smoothfactor 0.4
model5iterations 0
model5smoothfactor 0.1
model6iterations 0
nbestalignments 0
ncpus 4
nodumps 1
nofiledumpsyn 1
noiterationsmodel1 5
noiterationsmodel2 0
noiterationsmodel3 3
noiterationsmodel4 3
noiterationsmodel5 0
noiterationsmodel6 0
nsmooth 4
nsmoothgeneral 0
numberofiterationsforhmmalignmentmodel 5
onlyaldumps 1
outputfileprefix train.my_train.rk.dict
outputpath 
p 0
p0 0.999
peggedcutoff 0.03
pegging 0
previousa 
previousd 
previousd4 
previousd42 
previoushmm 
previousn 
previousp0 
previoust 
probcutoff 1e-07
probsmooth 1e-07
readtableprefix 
restart 0
sourcevocabularyfile train.my.vcb
t1 1
t2 0
t2to3 0
t3 0
t345 0
targetvocabularyfile train.rk.vcb
tc 
testcorpusfile 
th 0
transferdumpfrequency 0
v 0
verbose 0
verbosesentence -10

# mgiza bin path
BIN_DIR=/home/ye/tool/giza-pp/mgiza/mgizapp/bin/

# class building for HMM
$BIN_DIR/mkcls -n10 -p$1 -V$1.vcb.classes

***** 10 runs. (algorithm:TA)*****
;KategProblem:cats: 100   words: 14986

start-costs: MEAN: 1.46895e+06 (1.46465e+06-1.47356e+06)  SIGMA:2567.53   
  end-costs: MEAN: 1.32387e+06 (1.32215e+06-1.32556e+06)  SIGMA:1078.27   
   start-pp: MEAN: 255.417 (247.139-264.481)  SIGMA:4.99486   
     end-pp: MEAN: 84.6639 (83.5572-85.7561)  SIGMA:0.694625   
 iterations: MEAN: 350947 (336745-369750)  SIGMA:10370   
       time: MEAN: 10.0536 (8.88188-11.7336)  SIGMA:0.879291   
$BIN_DIR/mkcls -n10 -p$2 -V$2.vcb.classes

***** 10 runs. (algorithm:TA)*****
;KategProblem:cats: 100   words: 15541

start-costs: MEAN: 1.46837e+06 (1.46521e+06-1.47454e+06)  SIGMA:2633.46   
  end-costs: MEAN: 1.32897e+06 (1.32779e+06-1.33037e+06)  SIGMA:722.614   
   start-pp: MEAN: 245.79 (239.913-257.554)  SIGMA:4.97593   
     end-pp: MEAN: 85.0671 (84.3078-85.9807)  SIGMA:0.468162   
 iterations: MEAN: 363946 (354272-377179)  SIGMA:7447.4   
       time: MEAN: 8.47321 (7.94556-9.53812)  SIGMA:0.456948   

$BIN_DIR/plain2snt $1 $2
train.my -> train.my
train.rk -> train.rk
$BIN_DIR/snt2cooc $1\_$2.cooc $1.vcb $2.vcb $1\_$2.snt
line 1000
line 2000
line 3000
line 4000
line 5000
line 6000
line 7000
line 8000
line 9000
line 10000
line 11000
line 12000
line 13000
line 14000
line 15000
line 16000
END.

$BIN_DIR/mgiza config.update
Starting MGIZA 
Initializing Global Paras 
DEBUG: EnterDEBUG: PrefixDEBUG: LogParsing Arguments 
The following options are from the config file and will be overwritten by any command line options.
Parameter 'coocurrencefile' changed from '' to 'train.my_train.rk.cooc'
Parameter 'corpusfile' changed from '' to 'train.my_train.rk.snt'
Parameter 'logfile' changed from '120-12-08.010540.ye.log' to 'train.my_train.rk_mgiza.log'
Parameter 'm3' changed from '5' to '3'
Parameter 'm4' changed from '5' to '3'
Parameter 'model1dumpfrequency' changed from '0' to '1'
Parameter 'model4smoothfactor' changed from '0.2' to '0.4'
Parameter 'ncpus' changed from '0' to '4'
Parameter 'nodumps' changed from '0' to '1'
Parameter 'nsmooth' changed from '64' to '4'
Parameter 'onlyaldumps' changed from '0' to '1'
Parameter 'outputfileprefix' changed from '120-12-08.010540.ye' to 'train.my_train.rk.dict'
Parameter 'p0' changed from '-1' to '0.999'
Parameter 'sourcevocabularyfile' changed from '' to 'train.my.vcb'
Parameter 'targetvocabularyfile' changed from '' to 'train.rk.vcb'
general parameters:
-------------------
ml = 101  (maximum sentence length)

No. of iterations:
-------------------
hmmiterations = 5  (mh)
model1iterations = 5  (number of iterations for Model 1)
model2iterations = 0  (number of iterations for Model 2)
model3iterations = 3  (number of iterations for Model 3)
model4iterations = 3  (number of iterations for Model 4)
model5iterations = 0  (number of iterations for Model 5)
model6iterations = 0  (number of iterations for Model 6)

parameter for various heuristics in GIZA++ for efficient training:
------------------------------------------------------------------
countincreasecutoff = 1e-06  (Counts increment cutoff threshold)
countincreasecutoffal = 1e-05  (Counts increment cutoff threshold for alignments in training of fertility models)
mincountincrease = 1e-07  (minimal count increase)
peggedcutoff = 0.03  (relative cutoff probability for alignment-centers in pegging)
probcutoff = 1e-07  (Probability cutoff threshold for lexicon probabilities)
probsmooth = 1e-07  (probability smoothing (floor) value )

parameters for describing the type and amount of output:
-----------------------------------------------------------
compactalignmentformat = 0  (0: detailled alignment format, 1: compact alignment format )
countoutputprefix =   (The prefix for output counts)
dumpcount = 0  (Whether we are going to dump count (in addition to) final output?)
dumpcountusingwordstring = 0  (In count table, should actual word appears or just the id? default is id)
hmmdumpfrequency = 0  (dump frequency of HMM)
l = train.my_train.rk_mgiza.log  (log file name)
log = 0  (0: no logfile; 1: logfile)
model1dumpfrequency = 1  (dump frequency of Model 1)
model2dumpfrequency = 0  (dump frequency of Model 2)
model345dumpfrequency = 0  (dump frequency of Model 3/4/5)
nbestalignments = 0  (for printing the n best alignments)
nodumps = 1  (1: do not write any files)
o = train.my_train.rk.dict  (output file prefix)
onlyaldumps = 1  (1: do not write any files)
outputpath =   (output path)
transferdumpfrequency = 0  (output: dump of transfer from Model 2 to 3)
verbose = 0  (0: not verbose; 1: verbose)
verbosesentence = -10  (number of sentence for which a lot of information should be printed (negative: no output))

parameters describing input files:
----------------------------------
c = train.my_train.rk.snt  (training corpus file name)
d =   (dictionary file name)
previousa =   (The a-table of previous step)
previousd =   (The d-table of previous step)
previousd4 =   (The d4-table of previous step)
previousd42 =   (The d4-table (2) of previous step)
previoushmm =   (The hmm-table of previous step)
previousn =   (The n-table of previous step)
previousp0 =   (The P0 previous step)
previoust =   (The t-table of previous step)
restart = 0  (Restart training from a level,0: Normal restart, from model 1, 1: Model 1, 2: Model 2 Init (Using Model 1 model input and train model 2), 3: Model 2, (using model 2 input and train model 2), 4 : HMM Init (Using Model 1 model and train HMM), 5: HMM (Using Model 2 model and train HMM) 6 : HMM (Using HMM Model and train HMM), 7: Model 3 Init (Use HMM model and train model 3) 8: Model 3 Init (Use Model 2 model and train model 3) 9: Model 3, 10: Model 4 Init (Use Model 3 model and train Model 4) 11: Model 4 and on, )
s = train.my.vcb  (source vocabulary file name)
sourcevocabularyclasses =   (source vocabulary classes file name)
t = train.rk.vcb  (target vocabulary file name)
targetvocabularyclasses =   (target vocabulary classes file name)
tc =   (test corpus file name)

smoothing parameters:
---------------------
emalsmooth = 0.2  (f-b-trn: smoothing factor for HMM alignment model (can be ignored by -emSmoothHMM))
model23smoothfactor = 0  (smoothing parameter for IBM-2/3 (interpolation with constant))
model4smoothfactor = 0.4  (smooting parameter for alignment probabilities in Model 4)
model5smoothfactor = 0.1  (smooting parameter for distortion probabilities in Model 5 (linear interpolation with constant))
nsmooth = 4  (smoothing for fertility parameters (good value: 64): weight for wordlength-dependent fertility parameters)
nsmoothgeneral = 0  (smoothing for fertility parameters (default: 0): weight for word-independent fertility parameters)

parameters modifying the models:
--------------------------------
compactadtable = 1  (1: only 3-dimensional alignment table for IBM-2 and IBM-3)
deficientdistortionforemptyword = 0  (0: IBM-3/IBM-4 as described in (Brown et al. 1993); 1: distortion model of empty word is deficient; 2: distoriton model of empty word is deficient (differently); setting this parameter also helps to avoid that during IBM-3 and IBM-4 training too many words are aligned with the empty word)
depm4 = 76  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
depm5 = 68  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
emalignmentdependencies = 2  (lextrain: dependencies in the HMM alignment model.  &1: sentence length; &2: previous class; &4: previous position;  &8: French position; &16: French class)
emprobforempty = 0.4  (f-b-trn: probability for empty word)

parameters modifying the EM-algorithm:
--------------------------------------
m5p0 = -1  (fixed value for parameter p_0 in IBM-5 (if negative then it is determined in training))
manlexfactor1 = 0  ()
manlexfactor2 = 0  ()
manlexmaxmultiplicity = 20  ()
maxfertility = 10  (maximal fertility for fertility models)
ncpus = 4  (Number of threads to be executed, use 0 if you just want all CPUs to be used)
p0 = 0.999  (fixed value for parameter p_0 in IBM-3/4 (if negative then it is determined in training))
pegging = 0  (0: no pegging; 1: do pegging)

Parameter 'sourcevocabularyclasses' changed from '' to 'train.my.vcb.classes'
Parameter 'targetvocabularyclasses' changed from '' to 'train.rk.vcb.classes'
Opening Log File 
Printing parameters 
general parameters:
-------------------
ml = 101  (maximum sentence length)

No. of iterations:
-------------------
hmmiterations = 5  (mh)
model1iterations = 5  (number of iterations for Model 1)
model2iterations = 0  (number of iterations for Model 2)
model3iterations = 3  (number of iterations for Model 3)
model4iterations = 3  (number of iterations for Model 4)
model5iterations = 0  (number of iterations for Model 5)
model6iterations = 0  (number of iterations for Model 6)

parameter for various heuristics in GIZA++ for efficient training:
------------------------------------------------------------------
countincreasecutoff = 1e-06  (Counts increment cutoff threshold)
countincreasecutoffal = 1e-05  (Counts increment cutoff threshold for alignments in training of fertility models)
mincountincrease = 1e-07  (minimal count increase)
peggedcutoff = 0.03  (relative cutoff probability for alignment-centers in pegging)
probcutoff = 1e-07  (Probability cutoff threshold for lexicon probabilities)
probsmooth = 1e-07  (probability smoothing (floor) value )

parameters for describing the type and amount of output:
-----------------------------------------------------------
compactalignmentformat = 0  (0: detailled alignment format, 1: compact alignment format )
countoutputprefix =   (The prefix for output counts)
dumpcount = 0  (Whether we are going to dump count (in addition to) final output?)
dumpcountusingwordstring = 0  (In count table, should actual word appears or just the id? default is id)
hmmdumpfrequency = 0  (dump frequency of HMM)
l = train.my_train.rk_mgiza.log  (log file name)
log = 0  (0: no logfile; 1: logfile)
model1dumpfrequency = 1  (dump frequency of Model 1)
model2dumpfrequency = 0  (dump frequency of Model 2)
model345dumpfrequency = 0  (dump frequency of Model 3/4/5)
nbestalignments = 0  (for printing the n best alignments)
nodumps = 1  (1: do not write any files)
o = train.my_train.rk.dict  (output file prefix)
onlyaldumps = 1  (1: do not write any files)
outputpath =   (output path)
transferdumpfrequency = 0  (output: dump of transfer from Model 2 to 3)
verbose = 0  (0: not verbose; 1: verbose)
verbosesentence = -10  (number of sentence for which a lot of information should be printed (negative: no output))

parameters describing input files:
----------------------------------
c = train.my_train.rk.snt  (training corpus file name)
d =   (dictionary file name)
previousa =   (The a-table of previous step)
previousd =   (The d-table of previous step)
previousd4 =   (The d4-table of previous step)
previousd42 =   (The d4-table (2) of previous step)
previoushmm =   (The hmm-table of previous step)
previousn =   (The n-table of previous step)
previousp0 =   (The P0 previous step)
previoust =   (The t-table of previous step)
restart = 0  (Restart training from a level,0: Normal restart, from model 1, 1: Model 1, 2: Model 2 Init (Using Model 1 model input and train model 2), 3: Model 2, (using model 2 input and train model 2), 4 : HMM Init (Using Model 1 model and train HMM), 5: HMM (Using Model 2 model and train HMM) 6 : HMM (Using HMM Model and train HMM), 7: Model 3 Init (Use HMM model and train model 3) 8: Model 3 Init (Use Model 2 model and train model 3) 9: Model 3, 10: Model 4 Init (Use Model 3 model and train Model 4) 11: Model 4 and on, )
s = train.my.vcb  (source vocabulary file name)
sourcevocabularyclasses = train.my.vcb.classes  (source vocabulary classes file name)
t = train.rk.vcb  (target vocabulary file name)
targetvocabularyclasses = train.rk.vcb.classes  (target vocabulary classes file name)
tc =   (test corpus file name)

smoothing parameters:
---------------------
emalsmooth = 0.2  (f-b-trn: smoothing factor for HMM alignment model (can be ignored by -emSmoothHMM))
model23smoothfactor = 0  (smoothing parameter for IBM-2/3 (interpolation with constant))
model4smoothfactor = 0.4  (smooting parameter for alignment probabilities in Model 4)
model5smoothfactor = 0.1  (smooting parameter for distortion probabilities in Model 5 (linear interpolation with constant))
nsmooth = 4  (smoothing for fertility parameters (good value: 64): weight for wordlength-dependent fertility parameters)
nsmoothgeneral = 0  (smoothing for fertility parameters (default: 0): weight for word-independent fertility parameters)

parameters modifying the models:
--------------------------------
compactadtable = 1  (1: only 3-dimensional alignment table for IBM-2 and IBM-3)
deficientdistortionforemptyword = 0  (0: IBM-3/IBM-4 as described in (Brown et al. 1993); 1: distortion model of empty word is deficient; 2: distoriton model of empty word is deficient (differently); setting this parameter also helps to avoid that during IBM-3 and IBM-4 training too many words are aligned with the empty word)
depm4 = 76  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
depm5 = 68  (d_{=1}: &1:l, &2:m, &4:F, &8:E, d_{>1}&16:l, &32:m, &64:F, &128:E)
emalignmentdependencies = 2  (lextrain: dependencies in the HMM alignment model.  &1: sentence length; &2: previous class; &4: previous position;  &8: French position; &16: French class)
emprobforempty = 0.4  (f-b-trn: probability for empty word)

parameters modifying the EM-algorithm:
--------------------------------------
m5p0 = -1  (fixed value for parameter p_0 in IBM-5 (if negative then it is determined in training))
manlexfactor1 = 0  ()
manlexfactor2 = 0  ()
manlexmaxmultiplicity = 20  ()
maxfertility = 10  (maximal fertility for fertility models)
ncpus = 4  (Number of threads to be executed, use 0 if you just want all CPUs to be used)
p0 = 0.999  (fixed value for parameter p_0 in IBM-3/4 (if negative then it is determined in training))
pegging = 0  (0: no pegging; 1: do pegging)

reading vocabulary files 
Reading vocabulary file from:train.my.vcb
Reading vocabulary file from:train.rk.vcb
Source vocabulary list has 14987 unique tokens 
Target vocabulary list has 15542 unique tokens 
Calculating vocabulary frequencies from corpus train.my_train.rk.snt
Reading more sentence pairs into memory ... 
Corpus fits in memory, corpus has: 16561 sentence pairs.
Compacted Vocabulary, eliminated 1 entries 14986 remains 
Compacted Vocabulary, eliminated 1 entries 15541 remains 
 Train total # sentence pairs (weighted): 16561
Size of source portion of the training corpus: 114843 tokens
Size of the target portion of the training corpus: 114843 tokens 
In source portion of the training corpus, only 14986 unique tokens appeared
In target portion of the training corpus, only 15540 unique tokens appeared
lambda for PP calculation in IBM-1,IBM-2,HMM:= 114843/(131404-16561)== 1
Dictionary Loading complete
Inputfile in train.my_train.rk.cooc
There are 401132 401132 entries in table
cooc file loading completed
TTable initialization OK
Model one initalization OK
==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 1
==========================================================
Model1 Training Started at: ==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
==========================================================
Model1 Training Started at: Model1: Iteration 1
Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 1
Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 1
Main thread done, waiting
Thread 1done
Thread 2done
Thread 3done
Normalizing T 
 DONE Normalizing 
Model1: (1) TRAIN CROSS-ENTROPY 16.084 PERPLEXITY 69465.2
Model1: (1) VITERBI TRAIN CROSS-ENTROPY 19.1616 PERPLEXITY 586447
Model 1 Iteration: 1 took: 0 seconds
-----------
Model1: Iteration 2
==========================================================
Model1 Training Started at: ==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 2
Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 2
==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 2
Main thread done, waiting
Thread 1done
Thread 2done
Thread 3done
Normalizing T 
 DONE Normalizing 
Model1: (2) TRAIN CROSS-ENTROPY 5.12258 PERPLEXITY 34.8378
Model1: (2) VITERBI TRAIN CROSS-ENTROPY 6.41315 PERPLEXITY 85.2215
Model 1 Iteration: 2 took: 0 seconds
-----------
Model1: Iteration 3
==========================================================
Model1 Training Started at: ==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 3Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 3

==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 3
Main thread done, waiting
Thread 1done
Thread 2done
Thread 3done
Normalizing T 
 DONE Normalizing 
Model1: (3) TRAIN CROSS-ENTROPY 4.04175 PERPLEXITY 16.4698
Model1: (3) VITERBI TRAIN CROSS-ENTROPY 4.71873 PERPLEXITY 26.3317
Model 1 Iteration: 3 took: 0 seconds
-----------
Model1: Iteration 4
==========================================================
Model1 Training Started at: ==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 4
Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 4
==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 4
Main thread done, waiting
Thread 1done
Thread 2done
Thread 3done
Normalizing T 
 DONE Normalizing 
Model1: (4) TRAIN CROSS-ENTROPY 3.73331 PERPLEXITY 13.2996
Model1: (4) VITERBI TRAIN CROSS-ENTROPY 4.20747 PERPLEXITY 18.4745
Model 1 Iteration: 4 took: 0 seconds
-----------
Model1: Iteration 5
==========================================================
Model1 Training Started at: ==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 5
==========================================================
Model1 Training Started at: Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 5
Tue Dec  8 01:05:40 2020

-----------
Model1: Iteration 5
Main thread done, waiting
Thread 1done
Thread 2done
Thread 3done
Normalizing T 
 DONE Normalizing 
Model1: (5) TRAIN CROSS-ENTROPY 3.64161 PERPLEXITY 12.4805
Model1: (5) VITERBI TRAIN CROSS-ENTROPY 4.03336 PERPLEXITY 16.3743
Model 1 Iteration: 5 took: 0 seconds
Entire Model1 Training took: 0 seconds
NOTE: I am doing iterations with the HMM model!
Read classes: #words: 14986  #classes: 101
Actual number of read words: 14985 stored words: 14985
Read classes: #words: 15541  #classes: 101
Actual number of read words: 15540 stored words: 15540

==========================================================
Hmm Training Started at: Tue Dec  8 01:05:41 2020

-----------
Hmm: Iteration 1
Dump files 0 it 1 noIterations 5 dumpFreq 0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
Hmm: (1) TRAIN CROSS-ENTROPY 3.60699 PERPLEXITY 12.1846
Hmm: (1) VITERBI TRAIN CROSS-ENTROPY 3.95934 PERPLEXITY 15.5554

Hmm Iteration: 1 took: 0 seconds

-----------
Hmm: Iteration 2
Dump files 0 it 2 noIterations 5 dumpFreq 0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
Hmm: (2) TRAIN CROSS-ENTROPY 1.6599 PERPLEXITY 3.15995
Hmm: (2) VITERBI TRAIN CROSS-ENTROPY 1.77299 PERPLEXITY 3.41761

Hmm Iteration: 2 took: 0 seconds

-----------
Hmm: Iteration 3
Dump files 0 it 3 noIterations 5 dumpFreq 0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
Hmm: (3) TRAIN CROSS-ENTROPY 1.22201 PERPLEXITY 2.33271
Hmm: (3) VITERBI TRAIN CROSS-ENTROPY 1.27811 PERPLEXITY 2.4252

Hmm Iteration: 3 took: 1 seconds

-----------
Hmm: Iteration 4
Dump files 0 it 4 noIterations 5 dumpFreq 0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
Hmm: (4) TRAIN CROSS-ENTROPY 1.11913 PERPLEXITY 2.17216
Hmm: (4) VITERBI TRAIN CROSS-ENTROPY 1.14945 PERPLEXITY 2.2183

Hmm Iteration: 4 took: 0 seconds

-----------
Hmm: Iteration 5
Dump files 0 it 5 noIterations 5 dumpFreq 0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
Hmm: (5) TRAIN CROSS-ENTROPY 1.0651 PERPLEXITY 2.09232
Hmm: (5) VITERBI TRAIN CROSS-ENTROPY 1.08178 PERPLEXITY 2.11664

Hmm Iteration: 5 took: 1 seconds

Entire Hmm Training took: 2 seconds
==========================================================

==========================================================
Starting H333444:  Viterbi Training
 H333444 Training Started at: Tue Dec  8 01:05:43 2020


---------------------
THTo3: Iteration 1
10000
#centers(pre/hillclimbed/real): #centers(pre/hillclimbed/real): 1 11  11  #al:  1  #al: 78.4508 #alsophisticatedcountcollection: 81.0381 #alsophisticatedcountcollection: 0 #hcsteps: 0 #hcsteps: 0
#peggingImprovements: 0
0
#peggingImprovements: 0
#centers(pre/hillclimbed/real): 1 1 1  #al: 78.1967 #alsophisticatedcountcollection: 0 #hcsteps: 0
#peggingImprovements: 0
Thread 1done
Thread 2done
#centers(pre/hillclimbed/real): 1 1 1  #al: 81.4835 #alsophisticatedcountcollection: 0 #hcsteps: 0
#peggingImprovements: 0
Thread 3done
A/D table contains 14764 parameters.
A/D table contains 14596 parameters.
NTable contains 149870 parameter.
p0_count is 113721 and p1 is 561.166; p0 is 0.999 p1: 0.001
THTo3: TRAIN CROSS-ENTROPY 0.639196 PERPLEXITY 1.55746
THTo3: (1) TRAIN VITERBI CROSS-ENTROPY 0.648299 PERPLEXITY 1.56732

THTo3 Viterbi Iteration : 1 took: 0 seconds

---------------------
Model3: Iteration 2
10000
#centers(pre/hillclimbed/real): 1 #centers(pre/hillclimbed/real): 1 1  #al: 1 1 1  #al: 80.3899 #alsophisticatedcountcollection: 79.3385 #alsophisticatedcountcollection: 0 #hcsteps: 01.02459
#peggingImprovements: #centers(pre/hillclimbed/real): 1 1 #centers(pre/hillclimbed/real): 1  #al: 1 78.8107 #alsophisticatedcountcollection: 1 0 #hcsteps: 1  #al: 1.02326
#peggingImprovements: 80.8435 #alsophisticatedcountcollection: 0
0 #hcsteps: 1.02838
#peggingImprovements: 0
 #hcsteps: 1.02394
#peggingImprovements: 0
0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
A/D table contains 14566 parameters.
NTable contains 149870 parameter.
p0_count is 114685 and p1 is 79.1526; p0 is 0.999 p1: 0.001
Model3: TRAIN CROSS-ENTROPY 0.655633 PERPLEXITY 1.57531
Model3: (2) TRAIN VITERBI CROSS-ENTROPY 0.657686 PERPLEXITY 1.57755

Model3 Viterbi Iteration : 2 took: 1 seconds

---------------------
Model3: Iteration 3
10000
#centers(pre/hillclimbed/real): 1 1 1  #al: #centers(pre/hillclimbed/real): #centers(pre/hillclimbed/real): 80.7624 #alsophisticatedcountcollection: 0 #hcsteps: 11.02006
#peggingImprovements: 10
#centers(pre/hillclimbed/real): 1 1 1  #al: 81.0833 #alsophisticatedcountcollection: 0 #hcsteps: 1.02224
#peggingImprovements: 0
 1 1  #al: 79.5516 #alsophisticatedcountcollection: 0 #hcsteps: 1.01978
#peggingImprovements: 0
 1 1  #al: 78.1635 #alsophisticatedcountcollection: 0 #hcsteps: 1.02835
#peggingImprovements: 0
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
A/D table contains 14564 parameters.
NTable contains 149870 parameter.
p0_count is 114672 and p1 is 85.6885; p0 is 0.999 p1: 0.001
Model3: TRAIN CROSS-ENTROPY 0.61343 PERPLEXITY 1.52989
Model3: (3) TRAIN VITERBI CROSS-ENTROPY 0.614797 PERPLEXITY 1.53134

Model3 Viterbi Iteration : 3 took: 0 seconds

---------------------
T3To4: Iteration 4
10000
#centers(pre/hillclimbed/real): 1 1 1  #al: 78.5084 #alsophisticatedcountcollection: 4.76606 #hcsteps: 1.01769
#peggingImprovements: 0
#centers(pre/hillclimbed/real): 1 1 1  #al: 81.2391 #alsophisticatedcountcollection: 4.94041 #hcsteps: 1.01665
#peggingImprovements: 0
#centers(pre/hillclimbed/real): 1 1 1  #al: 79.907 #alsophisticatedcountcollection: 5.44365 #hcsteps: 1.01489
#peggingImprovements: 0
#centers(pre/hillclimbed/real): 1 1 1  #al: 79.952 #alsophisticatedcountcollection: 4.6994 #hcsteps: 1.01492
#peggingImprovements: 0
D4 table contains 1406181 parameters.
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
A/D table contains 14531 parameters.
NTable contains 149870 parameter.
p0_count is 114673 and p1 is 85.2063; p0 is 0.999 p1: 0.001
T3To4: TRAIN CROSS-ENTROPY 0.587123 PERPLEXITY 1.50225
T3To4: (4) TRAIN VITERBI CROSS-ENTROPY 0.587921 PERPLEXITY 1.50308

T3To4 Viterbi Iteration : 4 took: 1 seconds

---------------------
Model4: Iteration 5
10000
#centers(pre/hillclimbed/real): 1 1 1  #al: 81.0773 #alsophisticatedcountcollection: 4.26567 #hcsteps: 1.00854
#peggingImprovements: 0
#centers(pre/hillclimbed/real): 1 1 1  #al: 78.1251 #alsophisticatedcountcollection: 4.0982 #hcsteps: 1.01172
#peggingImprovements: 0
#centers(pre/hillclimbed/real): 1 1 1  #al: 79.8724 #alsophisticatedcountcollection: 4.1409 #hcsteps: #centers(pre/hillclimbed/real): 1.009
#peggingImprovements: 0
1 1 1  #al: 80.5869 #alsophisticatedcountcollection: 4.40257 #hcsteps: 1.00806
#peggingImprovements: 0
D4 table contains 1406181 parameters.
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
A/D table contains 14380 parameters.
NTable contains 149870 parameter.
p0_count is 114694 and p1 is 74.3712; p0 is 0.999 p1: 0.001
Model4: TRAIN CROSS-ENTROPY 1.15587 PERPLEXITY 2.22819
Model4: (5) TRAIN VITERBI CROSS-ENTROPY 1.15639 PERPLEXITY 2.22899

Model4 Viterbi Iteration : 5 took: 0 seconds

---------------------
Model4: Iteration 6
I will write alignment to train.my_train.rk.dict.A3.final.part001
I will write alignment to train.my_train.rk.dict.A3.final.part000
I will write alignment to train.my_train.rk.dict.A3.final.part002
I will write alignment to train.my_train.rk.dict.A3.final.part003
10000
#centers(pre/hillclimbed/real): #centers(pre/hillclimbed/real): 11  #centers(pre/hillclimbed/real): 1 1 1  #al: 11  #al:  1 80.5239 #alsophisticatedcountcollection: 180.1482  #al: 4.18056 #alsophisticatedcountcollection:  #hcsteps: 4.399777.3484 #hcsteps:  #alsophisticatedcountcollection: 1.009321.00862
#peggingImprovements: 0

#peggingImprovements: #centers(pre/hillclimbed/real): 0
4.0198 #hcsteps: 1.00921
#peggingImprovements: 0
1 1 1  #al: 81.7101 #alsophisticatedcountcollection: 4.28522 #hcsteps: 1.00712
#peggingImprovements: 0
D4 table contains 1406181 parameters.
Thread 1done
Thread 2done
Thread 3done
A/D table contains 14764 parameters.
A/D table contains 14343 parameters.
NTable contains 149870 parameter.
p0_count is 114707 and p1 is 67.9809; p0 is 0.999 p1: 0.001
Model4: TRAIN CROSS-ENTROPY 1.15261 PERPLEXITY 2.22315
Model4: (6) TRAIN VITERBI CROSS-ENTROPY 1.15295 PERPLEXITY 2.22368

Model4 Viterbi Iteration : 6 took: 1 seconds
H333444 Training Finished at: Tue Dec  8 01:05:46 2020


Entire Viterbi H333444 Training took: 3 seconds
==========================================================

Entire Training took: 6 seconds
Program Finished at: Tue Dec  8 01:05:46 2020

==========================================================

wc *.A3.final.part*
  11904  205621 1502095 train.my_train.rk.dict.A3.final.part000
  13029  222501 1625394 train.my_train.rk.dict.A3.final.part001
  12222  211823 1551944 train.my_train.rk.dict.A3.final.part002
  12528  215807 1577836 train.my_train.rk.dict.A3.final.part003
  49683  855752 6257269 total
(base) ye@ykt-pro:/media/ye/project1/exp/wfst-mt/exp/word/alignment/my-rk-giza$
```

အထက်မှာမြင်ရတဲ့ screen output ကနေလည်း GIZA++ or mgiza ရဲ့အလုပ်လုပ်ပုံကို အကြမ်းမျဉ်းတော့ လေ့လာနိုင်ပါလိမ့်မယ်။ screen output ရဲ့ နောက်ဆုံးပိုင်းမှာ မြင်ရတဲ့ \*A3.final.part\* ဆိုတဲ့ နာမည်တွေနဲ့ဖိုင်တွေက မြန်မာ-ရခိုင် စာကြောင်းတွေအကြား alignment လုပ်ပြီးထွက်လာတဲ့ ဖိုင်တွေပါ။   

train.my_train.rk.dict.A3.final.part000 ဖိုင်ရဲ့ ထိပ်ဆုံးကနေ စာကြောင်းရေ အကြောင်း နှစ်ဆယ်ကို ရိုက်ထုတ်ကြည့်ရင်အောက်ပါအတိုင်း မြင်ရပါတယ်။  
```
$ head -n 20 train.my_train.rk.dict.A3.final.part000
# Sentence pair (7) source length 5 target length 5 alignment score : 0.084755
ငါ စဉ်းစား ရေပိုင် စဉ်းစားပါ ။ 
NULL ({ }) ငါ ({ 1 }) စဉ်းစား ({ 2 }) သလို ({ 3 }) စဉ်းစားပါ ({ 4 }) ။ ({ 5 }) 
# Sentence pair (9) source length 11 target length 11 alignment score : 1.13641e-08
နောက်ဆုံး တစ် ကြိမ် သူ့ကို ချစ်ပါရေ လို့ ပြောခွင့် တောင် မ ရ ပါ။ 
NULL ({ }) ​နောက်ဆုံး ({ 1 }) တစ် ({ 2 }) ကြိမ် ({ 3 }) သူ့ကို ({ 4 }) ချစ်ပါတယ် ({ 5 }) လို့ ({ 6 }) ပြောခွင့်တောင် ({ 7 8 }) မ ({ 9 }) ရ ({ 10 }) တော့ဘူး ({ }) ။ ({ 11 }) 
# Sentence pair (13) source length 6 target length 6 alignment score : 0.00203375
ဒေချင့် ကို မင်း မှတ်ပုံတင် ဖို့သိလား ။ 
NULL ({ }) ဒါ ({ 1 }) ကို ({ 2 }) ခင်ဗျား ({ 3 }) မှတ်ပုံတင် ({ 4 }) ဦးမလား ({ 5 }) ။ ({ 6 }) 
# Sentence pair (14) source length 6 target length 6 alignment score : 0.0168503
မင်း အဂု ဇာ လုပ် လေး ။ 
NULL ({ }) ခင်ဗျား ({ 1 }) ခု ({ 2 }) ဘာ ({ 3 }) လုပ် ({ 4 }) သလဲ ({ 5 }) ။ ({ 6 }) 
# Sentence pair (16) source length 5 target length 5 alignment score : 0.0194717
ငါ့ လက် ကို တွဲထားနန့် ။ 
NULL ({ }) ကိုယ့် ({ 1 }) လက် ({ 2 }) ကို ({ 3 }) တွဲထားနော် ({ 4 }) ။ ({ 5 }) 
# Sentence pair (18) source length 6 target length 6 alignment score : 3.01904e-08
ဇာချိန် ငါရို့ တွိ ကတ်ဖို့ လေး ။ 
NULL ({ }) ဘယ် ({ 1 }) နှစ်နာရီ ({ }) ငါတို့ ({ 2 }) တွေ့ကြ ({ 3 4 }) မလဲ ({ 5 }) ။ ({ 6 }) 
# Sentence pair (19) source length 11 target length 11 alignment score : 0.00329918
ကောင်းစွာ က ထိုမချေ ကန်ကျောက် အော်ဟစ်နီရေ အတွက် လုံခြုံရေး အထိန်းတိ ပွင့်ကုန် ရေ ။ 
```

train.my_train.rk.dict.A3.final.part001 ဖိုင်ရဲ့ထိပ်ဆုံးစာကြောင်း အကြောင်းနှစ်ဆယ်ကို head command နဲ့ ရိုက်ထုတ်ကြည့်ရအောင်။ "-n 20" ဆိုတာက number of sentence အကြောင်း ၂၀ လို့ argument ပေးတာပါ။    
```
$ head -n 20 train.my_train.rk.dict.A3.final.part001
# Sentence pair (1) source length 9 target length 9 alignment score : 0.00801001
မင်း ယင်းချင့် ကို အခြား တစ်ခုနန့် မ ချိတ် ပါလား ။ 
NULL ({ }) မင်း ({ 1 }) အဲ့ဒါ ({ 2 }) ကို ({ 3 }) အခြား ({ 4 }) တစ်ခုနဲ့ ({ 5 }) မ ({ 6 }) ချိတ် ({ 7 }) ဘူးလား ({ 8 }) ။ ({ 9 }) 
# Sentence pair (2) source length 5 target length 5 alignment score : 0.00533346
ထိုမချေ တစ်ယောက်လေ့ မ မှတ်မိပါယာ ။ 
NULL ({ }) သူမ ({ 1 }) ဘယ်သူ့ကိုမှ ({ 2 }) မ ({ 3 }) မှတ်မိတော့ဘူး ({ 4 }) ။ ({ 5 }) 
# Sentence pair (3) source length 7 target length 7 alignment score : 0.00808222
ယင်းချင့် ကျွန်တော် ရို့ အတွက် ခက်ခ ရေ ။ 
NULL ({ }) အဲ့ဒါ ({ 1 }) ကျွန်တော် ({ 2 }) တို့ ({ 3 }) အတွက် ({ 4 }) ခက်ခဲ ({ 5 }) တယ် ({ 6 }) ။ ({ 7 }) 
# Sentence pair (4) source length 7 target length 7 alignment score : 0.0261447
မင်း ပြောခ ရေပိုင် ကျွန်တော် ယှင်းပြ ခရေ ။ 
NULL ({ }) ခင်ဗျား ({ 1 }) ပြောခဲ့ ({ 2 }) သလို ({ 3 }) ကျွန်တော် ({ 4 }) ရှင်းပြ ({ 5 }) ခဲ့တယ် ({ 6 }) ။ ({ 7 }) 
# Sentence pair (5) source length 6 target length 6 alignment score : 0.0154195
သူ့ကို ထိန်းဖို့ မင်း ရာ တတ်နိုင်ရေ ။ 
NULL ({ }) သူ့ကို ({ 1 }) ထိန်းဖို့ ({ 2 }) မင်း ({ 3 }) ပဲ ({ 4 }) တတ်နိုင်တယ် ({ 5 }) ။ ({ 6 }) 
# Sentence pair (6) source length 7 target length 7 alignment score : 0.000694828
ယင်းချင့် ကို ငါ တက်နင်း မိလား လာ ။ 
NULL ({ }) အဲ့ဒါ ({ 1 }) ကို ({ 2 }) ကိုယ် ({ 3 }) တက်နင်း ({ 4 }) မိသွား ({ 5 }) လား ({ 6 }) ။ ({ 7 }) 
# Sentence pair (8) source length 5 target length 5 alignment score : 0.0609318
အတင်းပြော ရစွာ မုန်း ရေ ။ 
```

## 91. [add-dummy-word-mk-csv.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/add-dummy-word-mk-csv.sh)  

Corpus တစ်ခုကို classificaiton model တွေ ဆောက်ဖို့အတွက် format တစ်ခုကနေ တခြား format တစ်ခုအဖြစ်ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ။ အောက်ပါ run ထားတဲ့ ဥပမာကနေ လုပ်တဲ့အလုပ်ကို နားလည်လိမ့်မယ်လို့ ထင်ပါတယ်။ နားလည်လွယ်အောင် output တွေကိုလည်း အဆင့်ဆင့် print ထုတ်ပေးထားတာမို့ ... ရေးထားတဲ့ shell script ကို ဖတ်ရင်းနဲ့ output လုပ်သွားတာတွေကိုကြည့်ရင်း လေ့လာသွားပါ။  

run မယ်ဆိုရင် ./add-dummy-word-mk-csv.sh \<corpus filename\> ဆိုတဲ့ပုံစံနဲ့ run ယုံပါပဲ။  
အောက်ပါဥပမာက raw.txt ဆိုတဲ့ corpus တစ်ခုကိုသုံးပြီး run လိုက်တဲ့အခါမှာ screen မှာ မြင်ရမယ့် output ဖြစ်ပါတယ်။  

```
$ ./add-dummy-word-mk-csv.sh raw.txt
Information of raw.txt:
wc raw.txt
   7002   64418 1847864 raw.txt
head raw.txt
"သရက်/Fru ကိုင်းကူးနည်း/AgrK လေး/nolabel လည်း/nolabel သိချင်/nolabel ပါ/nolabel တယ်/nolabel",__AgrK__
"ကညွတ်/Veg ကို/nolabel ဘယ်လိုစိုက်/Gro ရင်/nolabel အထွက်တိုး/nolabel မလဲ/nolabel",__Gro__
"ရော်ဘာ/IndRC ကိုင်းကူးနည်း/AgrK ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel လား/nolabel",__AgrK__
နှင်းဆီ/Flo စိုက်နည်း/Gro လေး/nolabel ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel ဦး/nolabel",__Gro__
"နီမတုတ်/BacD တွေ/nolabel ကြောင့်/nolabel ပဲတီစိမ်းပင်/Bea ရဲ့/nolabel အမြစ်/nolabel တွေ/nolabel ထိခိုက်/nolabel နိုင်/nolabel ပါ/nolabel သလား/nolabel",__BacD__
"ကွမ်းသီး/Other စိုက်နည်း/Gro သိချင်/nolabel လို့/nolabel ပါ/nolabel",__Gro__
"သရက်ပင်/Fru က/nolabel အရွက်အဖျားတွေကခြောက်နေ/BacD တယ်/nolabel ဘယ်လိုလုပ်/nolabel ရ/nolabel မလဲ့/nolabel ဆိုတာ/nolabel ကူညီပေး/nolabel ပါ/nolabel အုံး/nolabel",__BacD__
"ငရုတ်ပင်/Veg အသီးကြွေပြီးအပင်ညှိုးနေ/BacD လို့/nolabel ဘာဆေး/nolabel ပက်/nolabel ရ/nolabel လဲ/nolabel",__BacD__
"ကြက်မောက်/Fru မမှည့်ခင်/nolabel အလုံးကျွေ/BacD ကြနေ/nolabel တာ/nolabel ဘာကြောင့်လဲ/nolabel ဘာဆေး/nolabel  သုံး/nolabel ရ/nolabel မလဲ/nolabel",__PlaN__
"စိန်တလုံးသရက်ပင်/Fru ၁/nolabel နှစ်/nolabel သား/nolabel ဘာမြေဆီ/PlaN ကြွေးရင်/nolabel အဆင်ပြေမလဲ/nolabel",__PlaN__

Remove double quotes...
head raw.txt.rmquote
သရက်/Fru ကိုင်းကူးနည်း/AgrK လေး/nolabel လည်း/nolabel သိချင်/nolabel ပါ/nolabel တယ်/nolabel,__AgrK__
ကညွတ်/Veg ကို/nolabel ဘယ်လိုစိုက်/Gro ရင်/nolabel အထွက်တိုး/nolabel မလဲ/nolabel,__Gro__
ရော်ဘာ/IndRC ကိုင်းကူးနည်း/AgrK ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel လား/nolabel,__AgrK__
နှင်းဆီ/Flo စိုက်နည်း/Gro လေး/nolabel ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel ဦး/nolabel,__Gro__
နီမတုတ်/BacD တွေ/nolabel ကြောင့်/nolabel ပဲတီစိမ်းပင်/Bea ရဲ့/nolabel အမြစ်/nolabel တွေ/nolabel ထိခိုက်/nolabel နိုင်/nolabel ပါ/nolabel သလား/nolabel,__BacD__
ကွမ်းသီး/Other စိုက်နည်း/Gro သိချင်/nolabel လို့/nolabel ပါ/nolabel,__Gro__
သရက်ပင်/Fru က/nolabel အရွက်အဖျားတွေကခြောက်နေ/BacD တယ်/nolabel ဘယ်လိုလုပ်/nolabel ရ/nolabel မလဲ့/nolabel ဆိုတာ/nolabel ကူညီပေး/nolabel ပါ/nolabel အုံး/nolabel,__BacD__
ငရုတ်ပင်/Veg အသီးကြွေပြီးအပင်ညှိုးနေ/BacD လို့/nolabel ဘာဆေး/nolabel ပက်/nolabel ရ/nolabel လဲ/nolabel,__BacD__
ကြက်မောက်/Fru မမှည့်ခင်/nolabel အလုံးကျွေ/BacD ကြနေ/nolabel တာ/nolabel ဘာကြောင့်လဲ/nolabel ဘာဆေး/nolabel  သုံး/nolabel ရ/nolabel မလဲ/nolabel,__PlaN__
စိန်တလုံးသရက်ပင်/Fru ၁/nolabel နှစ်/nolabel သား/nolabel ဘာမြေဆီ/PlaN ကြွေးရင်/nolabel အဆင်ပြေမလဲ/nolabel,__PlaN__

Add dummy word for the last labels...
သရက်/Fru ကိုင်းကူးနည်း/AgrK လေး/nolabel လည်း/nolabel သိချင်/nolabel ပါ/nolabel တယ်/nolabel dummy/__AgrK__
ကညွတ်/Veg ကို/nolabel ဘယ်လိုစိုက်/Gro ရင်/nolabel အထွက်တိုး/nolabel မလဲ/nolabel dummy/__Gro__
ရော်ဘာ/IndRC ကိုင်းကူးနည်း/AgrK ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel လား/nolabel dummy/__AgrK__
နှင်းဆီ/Flo စိုက်နည်း/Gro လေး/nolabel ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel ဦး/nolabel dummy/__Gro__
နီမတုတ်/BacD တွေ/nolabel ကြောင့်/nolabel ပဲတီစိမ်းပင်/Bea ရဲ့/nolabel အမြစ်/nolabel တွေ/nolabel ထိခိုက်/nolabel နိုင်/nolabel ပါ/nolabel သလား/nolabel dummy/__BacD__
ကွမ်းသီး/Other စိုက်နည်း/Gro သိချင်/nolabel လို့/nolabel ပါ/nolabel dummy/__Gro__
သရက်ပင်/Fru က/nolabel အရွက်အဖျားတွေကခြောက်နေ/BacD တယ်/nolabel ဘယ်လိုလုပ်/nolabel ရ/nolabel မလဲ့/nolabel ဆိုတာ/nolabel ကူညီပေး/nolabel ပါ/nolabel အုံး/nolabel dummy/__BacD__
ငရုတ်ပင်/Veg အသီးကြွေပြီးအပင်ညှိုးနေ/BacD လို့/nolabel ဘာဆေး/nolabel ပက်/nolabel ရ/nolabel လဲ/nolabel dummy/__BacD__
ကြက်မောက်/Fru မမှည့်ခင်/nolabel အလုံးကျွေ/BacD ကြနေ/nolabel တာ/nolabel ဘာကြောင့်လဲ/nolabel ဘာဆေး/nolabel  သုံး/nolabel ရ/nolabel မလဲ/nolabel dummy/__PlaN__
စိန်တလုံးသရက်ပင်/Fru ၁/nolabel နှစ်/nolabel သား/nolabel ဘာမြေဆီ/PlaN ကြွေးရင်/nolabel အဆင်ပြေမလဲ/nolabel dummy/__PlaN__

Remove manual tagging errors:
head raw.txt.rmquote.dummy.clean:
သရက်/Fru ကိုင်းကူးနည်း/AgrK လေး/nolabel လည်း/nolabel သိချင်/nolabel ပါ/nolabel တယ်/nolabel dummy/__AgrK__
ကညွတ်/Veg ကို/nolabel ဘယ်လိုစိုက်/Gro ရင်/nolabel အထွက်တိုး/nolabel မလဲ/nolabel dummy/__Gro__
ရော်ဘာ/IndRC ကိုင်းကူးနည်း/AgrK ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel လား/nolabel dummy/__AgrK__
နှင်းဆီ/Flo စိုက်နည်း/Gro လေး/nolabel ပြောပြ/nolabel ပေး/nolabel ပါ/nolabel ဦး/nolabel dummy/__Gro__
နီမတုတ်/BacD တွေ/nolabel ကြောင့်/nolabel ပဲတီစိမ်းပင်/Bea ရဲ့/nolabel အမြစ်/nolabel တွေ/nolabel ထိခိုက်/nolabel နိုင်/nolabel ပါ/nolabel သလား/nolabel dummy/__BacD__
ကွမ်းသီး/Other စိုက်နည်း/Gro သိချင်/nolabel လို့/nolabel ပါ/nolabel dummy/__Gro__
သရက်ပင်/Fru က/nolabel အရွက်အဖျားတွေကခြောက်နေ/BacD တယ်/nolabel ဘယ်လိုလုပ်/nolabel ရ/nolabel မလဲ့/nolabel ဆိုတာ/nolabel ကူညီပေး/nolabel ပါ/nolabel အုံး/nolabel dummy/__BacD__
ငရုတ်ပင်/Veg အသီးကြွေပြီးအပင်ညှိုးနေ/BacD လို့/nolabel ဘာဆေး/nolabel ပက်/nolabel ရ/nolabel လဲ/nolabel dummy/__BacD__
ကြက်မောက်/Fru မမှည့်ခင်/nolabel အလုံးကျွေ/BacD ကြနေ/nolabel တာ/nolabel ဘာကြောင့်လဲ/nolabel ဘာဆေး/nolabel သုံး/nolabel ရ/nolabel မလဲ/nolabel dummy/__PlaN__
စိန်တလုံးသရက်ပင်/Fru ၁/nolabel နှစ်/nolabel သား/nolabel ဘာမြေဆီ/PlaN ကြွေးရင်/nolabel အဆင်ပြေမလဲ/nolabel dummy/__PlaN__

Preparing tag only file...
head raw.txt.rmquote.dummy.clean.tag
Fru AgrK nolabel nolabel nolabel nolabel nolabel __AgrK__
Veg nolabel Gro nolabel nolabel nolabel __Gro__
IndRC AgrK nolabel nolabel nolabel nolabel __AgrK__
Flo Gro nolabel nolabel nolabel nolabel nolabel __Gro__
BacD nolabel nolabel Bea nolabel nolabel nolabel nolabel nolabel nolabel nolabel __BacD__
Other Gro nolabel nolabel nolabel __Gro__
Fru nolabel BacD nolabel nolabel nolabel nolabel nolabel nolabel nolabel nolabel __BacD__
Veg BacD nolabel nolabel nolabel nolabel nolabel __BacD__
Fru nolabel BacD nolabel nolabel nolabel nolabel nolabel nolabel nolabel __PlaN__
Fru nolabel nolabel nolabel PlaN nolabel nolabel __PlaN__

Make CSV file for building classification models
head raw.txt.rmquote.dummy.clean.tag.csv
Fru,AgrK,nolabel,nolabel,nolabel,nolabel,nolabel,__AgrK__
Veg,nolabel,Gro,nolabel,nolabel,nolabel,__Gro__
IndRC,AgrK,nolabel,nolabel,nolabel,nolabel,__AgrK__
Flo,Gro,nolabel,nolabel,nolabel,nolabel,nolabel,__Gro__
BacD,nolabel,nolabel,Bea,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,__BacD__
Other,Gro,nolabel,nolabel,nolabel,__Gro__
Fru,nolabel,BacD,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,__BacD__
Veg,BacD,nolabel,nolabel,nolabel,nolabel,nolabel,__BacD__
Fru,nolabel,BacD,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,nolabel,__PlaN__
Fru,nolabel,nolabel,nolabel,PlaN,nolabel,nolabel,__PlaN__

wc raw.txt.rmquote.dummy.clean.tag.csv;
  6781   6781 510443 raw.txt.rmquote.dummy.clean.tag.csv
```
