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

## read-and-move.sh

ကြုံရပါလိမ့်မယ် zip လုပ်ထားတဲ့ ဖိုင်ကို ဖြေလိုက်တဲ့အခါမှာ ဖိုလ်ဒါတစ်ခုအောက်မှာ သိမ်းမပေးပဲနဲ့ လက်ရှိ ဖိုလ်ဒါအောက်မှာပဲ ဖိုင်တွေကို ဖြေပေးသွားတာမျိုး။  
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
