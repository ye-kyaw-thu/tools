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

## [read-and-move.sh](https://github.com/ye-kyaw-thu/tools/blob/master/bash/read-and-move.sh)

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

## change-filenames.sh  

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
## rm-date-sentences.sh

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

## print-classID-prediction-result.sh

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
## compare-img-or-pdf.sh

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

## chk-sort-by-columns.sh  
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
## kill-all-detached.sh  
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

## ./unzip-all-with-one-passwd.sh  
ကျွန်တော်နဲ့ ကျောင်းသားတွေအကြားမှာ ဖိုင်တွေ၊ ဒေတာတွေကို ပို့ကြတဲ့အခါမှာ password ခံပြီး၊ zip လုပ်ပြီးတော့ သုံးပါတယ်။ ဒီ shell script က ကျောင်းသူတစ်ယောက်ဆီက ပို့ပေးလိုက်တဲ့ zip ဖိုင်တွေအားလုံးကိုဖြေဖို့အတွက် password တွေကို အကြိမ်ကြိမ်အခါခါ ရိုက်ပေးရမှာကိုပျင်းလို့ ရေးခဲ့တာဖြစ်ပါတယ်။ နောက်တစ်ခုက zip ဖိုင်တဖိုင်စီက ဖိုင်တွေတော်တော်များများကို ချုံ့ထားတာမို့ တစ်ဖိုင်ချင်းစီ unzip လုပ်တာပြီးတာကို ထိုင်မစောင့်ချင်တာကြောင့်လည်း ပါပါတယ်။ zip ဖိုင်တွေအများကြီးကို တူတဲ့ password တစ်ခုတည်းကို သုံးပြီးတော့ ဖြေဖို့လိုအပ်လာတဲ့အခါမှာ အသုံးဝင်ပါလိမ့်မယ်။ နောက်ပြီးတော့ password ကို command line ကနေ ဖတ်တဲ့ပုံစံကိုလည်း bash ရဲ့ "read -s" ကိုလည်း သုံးပြထားပါတယ်။ ဒီ shell script ကို သုံးပုံသုံးနည်း ဥပမာကတော့ အောက်ပါအတိုင်းဖြစ်ပါတယ်။  

```
./unzip-all-with-one-passwd.sh *.zip
```

## ./cut-filename.sh  
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

## ./calc-avg.sh  
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

## ./print-latex-section.sh  
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

## list-mistake-5-suggestion.sh  

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
## mytxt2pdf.sh  

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

## prepare-open-test-data.sh

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

## print-CRLF.sh

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

## group-files.sh  

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

## segmentation.sh

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

## ./split-even-odd-pdf.sh 

ပြည်ထောင်စုသမ္မတမြန်မာနိုင်ငံတော် ဖွဲ့စည်းပုံအခြေခံဥပဒေ (၂၀၀၈ ခုနှစ်) PDF ဖိုင်မှာ အင်္ဂလိပ်စာ စာမျက်နှာပြီးရင်၊ မြန်မာလို ရေးထားတဲ့ မြန်မာစာမျက်နှာ ဆိုပြီး တလှည့်စီပါနေပါတယ်။ တနည်းအားဖြင့် မ ဂဏန်း စာမျက်နှာ (odd pages) တွေက အင်္ဂလိပ်စာ၊ စုံ ဂဏန်း စာမျက်နှာ (even pages) တွေက မြန်မာစာပါ။ အဲဒီ PDF ဖိုင်ထဲကနေ မ ဂဏန်းစာမျက်နှာတွေကို တစ်ဖိုင်၊ စုံ ဂဏန်းစာမျက်နှာတွေကို တဖိုင်စီ သပ်သပ် ခွဲသိမ်းဖို့အတွက် ရေးခဲ့တဲ့ shell script ပါ။ Example running ကတော့ အောက်ပါအတိုင်းပါ။  

```bash
$ ./split-even-odd-pdf.sh ./myanmarconstitution2008mm.pdf 
Total pages in your PDF file: 424
No. of pages of odd.pdf:  212
No. of pages of even.pdf:  212
```
စုံ ဂဏန်းစာမျက်နှာတွေချည်းပဲ စုထားတဲ့ ဖိုင်ကိုတော့ even.pdf ဆိုတဲ့ ဖိုင်နာမည်နဲ့ သိမ်းပေးမှာဖြစ်ပြီး၊  
မ ဂဏန်းစာမျက်နှာတွေချည်းပဲ စုထားတဲ့ ဖိုင်ကိုတော့ odd.pdf ဖိုင်နာမည်နဲ့ သိမ်းပေးသွားမှာဖြစ်ပါတယ်။  
နဂိုဖိုင်ကလည်း ဒီအတိုင်းပဲ ကျန်နေပါလိမ့်မယ်။  


