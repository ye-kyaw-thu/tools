# Example usages of python scripts

## 1.[chk-token.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/chk-token.py)  

chk-token.py က parallel text ဖိုင် နှစ်ဖိုင်ထဲက token အရေအတွက် မတူတဲ့စာကြောင်း၊ တနည်းအားဖြင့် word segmentation ဖြတ်ထားတာ မညီတဲ့ စာကြောင်းတွေကို ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တာဖြစ်ပါတယ်။ [writing.txt](https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/writing.txt) ဖိုင်ထဲမှာ word segmentation လုပ်ထားတဲ့ မြန်မာစာ စာကြောင်း စုစုပေါင်း ၅ကြောင်း အောက်ပါအတိုင်း ရှိပါတယ်။  

```bash
$ cat ./writing.txt 
အဓိက ကျ တဲ့ မေးခွန်း တွေ မေး ကြည့်
စကား ပြော အရမ်း ကောင်း တယ်
မင်္ဂလာ ပါ ဆရာမ
သာဓု သာဓု သာဓု ပါ
မေမြို့မှာ နေ ပါ တယ် ဗျ
```

[reading.txt](https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/reading.txt) ဖိုင်ထဲမှာတော့ ဖတ်တဲ့အခါမှာ ထွက်တဲ့ အသံထွက်အတိုင်းရေးသားထားတဲ့ စာကြောင်း ၅ကြောင်းပါ။  

```bash
$ cat reading.txt 
အဓိက ကျ ဒဲ့ မေးခွန်း ဒွေ မေး ကြည့်
ဇဂါး ပြော အရမ်း ကောင်းတယ်
မင်ဂလာပါ ဆရာမ
သာဓု သာဓု သာဓု ဘာ
မေမြို့ မှာ နေ ဘာ ဒယ် ဗျ
```

အထက်ပါ ဖိုင်နှစ်ဖိုင်မှာ token ဖြတ်ထားတာ မညီတဲ့ စာကြောင်းအတွဲ သုံးစုံရှိနေပါတယ်။ အဲဒီ စာကြောင်းတွေကို tab ကီးခြားပြီး ကော်လံနှစ်ခုအနေနဲ့ ရိုက်ထုတ်ပြစေချင်ရင် အောက်ပါအတိုင်း input ဖိုင် နှစ်ဖိုင်ရဲ့ နောက်ဆုံးမှာ 3rd argument အနေနဲ့ $'\t' ဆိုပြီး parameter ပေးပါ။  

```bash
$ python ./chk-token.py ./writing.txt ./reading.txt $'\t'
စကား ပြော အရမ်း ကောင်း တယ်	ဇဂါး ပြော အရမ်း ကောင်းတယ်
မင်္ဂလာ ပါ ဆရာမ	မင်ဂလာပါ ဆရာမ
မေမြို့မှာ နေ ပါ တယ် ဗျ	မေမြို့ မှာ နေ ဘာ ဒယ် ဗျ
```

တကယ်လို့ token အရေအတွက် မတူတဲ့ စာကြောင်းအတွဲတွေကို အပေါ်အောက်ဆင့်ပြီး နှိုင်းယှဉ်ပြစေချင်ရင်တော့ 3rd command line argument ကို $'\n' ပေးပြီးတော့ run ပါ။  

```bash
$ python ./chk-token.py ./writing.txt ./reading.txt $'\n'
စကား ပြော အရမ်း ကောင်း တယ်
ဇဂါး ပြော အရမ်း ကောင်းတယ်
မင်္ဂလာ ပါ ဆရာမ
မင်ဂလာပါ ဆရာမ
မေမြို့မှာ နေ ပါ တယ် ဗျ
မေမြို့ မှာ နေ ဘာ ဒယ် ဗျ
```
## 2. [numpy-array-element-compare.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/numpy-array-element-compare.py)  

file1.txt ထဲမှာ ရှိတဲ့စာကြောင်းတွေကို ရိုက်ထုတ်ကြည့်ရအောင်။  

```bash
$ cat file1.txt 
Language as syllables
for your reference
Statistical Machine Translation
Mg Mg is a boy .
I am working on Myanmar-Rakhine machine translation .
```
file2.txt ထဲမှာ ရှိတဲ့စာကြောင်းတွေကို ရိုက်ထုတ်ကြည့်ရအောင်။  

```bash
$ cat file2.txt 
Language as tensors
for your refreshment
Neural Machine Translation
Mg Mg are a boy .
I am working on Rakhine-Myanmar machine translation .
```

./numpy-array-element-compare.py ပရိုဂရမ်ကို file1.txt နဲ့ file2.txt ကို command line argument အနေနဲ့ပေးပြီး စစ်ခိုင်းရင် အောက်ပါအတိုင်း output လုပ်ပေးပါလိမ့်မယ်။ numpy array နှစ်ခု ကိုတိုက်ကြည့်ပြီး မတူတဲ့ စာလုံးတွေရှိနေတဲ့ နေရာမှာ False ဆိုပြီး ပြပေးမှာ ဖြစ်ပါတယ်။  

```bash
$ python ./numpy-array-element-compare.py ./file1.txt ./file2.txt 
[ True  True False]
[ True  True False]
[False  True  True]
[ True  True False  True  True  True]
[ True  True  True  True False  True  True  True]
```
