# Example usages of python scripts

## 1.[chk-token.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/chk-token.py)  

chk-token.py က parallel text ဖိုင် နှစ်ဖိုင်ထဲက token အရေအတွက် မတူတဲ့စာကြောင်း၊ တနည်းအားဖြင့် word segmentation ဖြတ်ထားတာ မညီတဲ့ စာကြောင်းတွေကို ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တာဖြစ်ပါတယ်။ [writing.txt](https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/writing.txt) ဖိုင်ထဲမှာ word segmentation လုပ်ထားတဲ့ မြန်မာစာ စာကြောင်း စုစုပေါင်း ၅ကြောင်း အောက်ပါအတိုင်း ရှိပါတယ်။  

```
$ cat ./writing.txt 
အဓိက ကျ တဲ့ မေးခွန်း တွေ မေး ကြည့်
စကား ပြော အရမ်း ကောင်း တယ်
မင်္ဂလာ ပါ ဆရာမ
သာဓု သာဓု သာဓု ပါ
မေမြို့မှာ နေ ပါ တယ် ဗျ
```

[reading.txt](https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/reading.txt) ဖိုင်ထဲမှာတော့ ဖတ်တဲ့အခါမှာ ထွက်တဲ့ အသံထွက်အတိုင်းရေးသားထားတဲ့ စာကြောင်း ၅ကြောင်းပါ။  

```
$ cat reading.txt 
အဓိက ကျ ဒဲ့ မေးခွန်း ဒွေ မေး ကြည့်
ဇဂါး ပြော အရမ်း ကောင်းတယ်
မင်ဂလာပါ ဆရာမ
သာဓု သာဓု သာဓု ဘာ
မေမြို့ မှာ နေ ဘာ ဒယ် ဗျ
```

အထက်ပါ ဖိုင်နှစ်ဖိုင်မှာ token ဖြတ်ထားတာ မညီတဲ့ စာကြောင်းအတွဲ သုံးစုံရှိနေပါတယ်။ အဲဒီ စာကြောင်းတွေကို tab ကီးခြားပြီး ကော်လံနှစ်ခုအနေနဲ့ ရိုက်ထုတ်ပြစေချင်ရင် အောက်ပါအတိုင်း input ဖိုင် နှစ်ဖိုင်ရဲ့ နောက်ဆုံးမှာ 3rd argument အနေနဲ့ $'\t' ဆိုပြီး parameter ပေးပါ။  

```
$ python ./chk-token.py ./writing.txt ./reading.txt $'\t'
စကား ပြော အရမ်း ကောင်း တယ်	ဇဂါး ပြော အရမ်း ကောင်းတယ်
မင်္ဂလာ ပါ ဆရာမ	မင်ဂလာပါ ဆရာမ
မေမြို့မှာ နေ ပါ တယ် ဗျ	မေမြို့ မှာ နေ ဘာ ဒယ် ဗျ
```

တကယ်လို့ token အရေအတွက် မတူတဲ့ စာကြောင်းအတွဲတွေကို အပေါ်အောက်ဆင့်ပြီး နှိုင်းယှဉ်ပြစေချင်ရင်တော့ 3rd command line argument ကို $'\n' ပေးပြီးတော့ run ပါ။  

```
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

```
$ cat file1.txt 
Language as syllables
for your reference
Statistical Machine Translation
Mg Mg is a boy .
I am working on Myanmar-Rakhine machine translation .
```
file2.txt ထဲမှာ ရှိတဲ့စာကြောင်းတွေကို ရိုက်ထုတ်ကြည့်ရအောင်။  

```
$ cat file2.txt 
Language as tensors
for your refreshment
Neural Machine Translation
Mg Mg are a boy .
I am working on Rakhine-Myanmar machine translation .
```

./numpy-array-element-compare.py ပရိုဂရမ်ကို file1.txt နဲ့ file2.txt ကို command line argument အနေနဲ့ပေးပြီး စစ်ခိုင်းရင် အောက်ပါအတိုင်း output လုပ်ပေးပါလိမ့်မယ်။ numpy array နှစ်ခု ကိုတိုက်ကြည့်ပြီး မတူတဲ့ စာလုံးတွေရှိနေတဲ့ နေရာမှာ False ဆိုပြီး ပြပေးမှာ ဖြစ်ပါတယ်။  

```
$ python ./numpy-array-element-compare.py ./file1.txt ./file2.txt 
[ True  True False]
[ True  True False]
[False  True  True]
[ True  True False  True  True  True]
[ True  True  True  True False  True  True  True]
```

## 3. [char-count-element-wise.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char-count-element-wise.py)  

အရင်ဆုံး [my.txt](https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/my.txt) ဖိုင်ထဲမှာ ရှိတဲ့စာကြောင်းတွေကို ရိုက်ထုတ်ကြည့်ရအောင်။  
```
$ cat ./my.txt 
သမီး နေကောင်း ရဲ့ လား ။
ထမင်း စား ပြီး ပြီ လား ။
စာအုပ် တွေ ကော ဖတ် ရဲ့ လား ။
```

အထက်ပါ my.txt ဖိုင်ထဲက စာလုံးတစ်လုံးချင်းစီမှာ မြန်မာစာလုံး "လား" ဆိုတာ ဘယ်နေရာတွေမှာ ပါနေသလဲ ဆိုတာကို ရှာကြည့်ချင်ရင် အောက်ပါအတိုင်း run ပါ။  

```
$ python ./char-count-element-wise.py ./my.txt လား
[0 0 0 1 0]
[0 0 0 0 1 0]
[0 0 0 0 0 1 0]
```

## 4. [char-startswith-element-wise.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/char-startswith-element-wise.py)

အရင်ဆုံး [my.txt](https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/my.txt) ဖိုင်ထဲမှာ ရှိတဲ့စာကြောင်းတွေကို ရိုက်ထုတ်ကြည့်ရအောင်။   
```
$ cat ./my.txt 
သမီး နေကောင်း ရဲ့ လား ။
ထမင်း စား ပြီး ပြီ လား ။
စာအုပ် တွေ ကော ဖတ် ရဲ့ လား ။
```

အထက်ပါ my.txt ဖိုင်ထဲက စာလုံးတစ်လုံးချင်းစီမှာ မြန်မာစာလုံး "ပ" နဲ့စတဲ့ စာလုံးတွေက ဘယ်နေရာတွေမှာပါနေသလဲ ဆိုတာကို ရှာကြည့်ချင်ရင် အောက်ပါအတိုင်း run ပါ။  

```
$ python ./char-startswith-element-wise.py ./my.txt ပ
[0 0 0 0 0]
[0 0 1 1 0 0]
[1 0 0 0 0 0 0]
```

## 5. [fuzzy-match.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/fuzzy-match.py)  

[myG2P](https://github.com/ye-kyaw-thu/myG2P) ထဲမှာရှိတဲ့ phoneme တွေကို fuzzy matching နဲ့ ဆွဲထုတ်ကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ python script ပါ။  

f4 ဆိုတဲ့ ဖိုင်က myG2P ထဲက ကော်လံနံပါတ် ၄ ကိုပဲ (phoneme အပိုင်းတွေကိုပဲ) cut command နဲ့ ဖြတ်ထုတ်ထားတဲ့ ဖိုင်ပါ။ အဲဒီဖိုင်ကို phoneme dictionary အနေနဲ့ သုံးခဲ့ပါတယ်။ အောက်ပါ ဥပမာက စက်ရုပ်ရဲ့ phoneme ဖြစ်တဲ့ "se' jou'" ကို fuzzy matching လုပ်ကြည့်ပြီး ရလာတဲ့ top 5 ပါ။  

```
$ python ./fuzzy-match.py ./f4 "se' jou"
[("se' jou'", 100), ("se' se'", 95), ('jou. jou.', 95), ('jou: jou:', 95), ("se' joun", 93)]
```

ရလာတဲ့ output တွေကို မြန်မာစာလုံးနဲ့ပါ တိုက်ကြည့်ရင်တော့ အောက်ပါအတိုင်း ဖြစ်ပါတယ်။ ထပ်တူဖြစ်တဲ့ phoneme "se' jou'" အပြင် တခြား Levenshtein distance နီးစပ်တဲ့ phoneme စာလုံးတွေကိုပါဆွဲထုတ်ပေးပါလိမ့်မယ်။ ကျွန်တော်က coding ထဲက ```suggestedWord = process.extract(searchWord, dictWords, limit=limit)``` ဆိုတဲ့ statement မှာ limit တန်ဖိုးကို 5 လို့ ပေးထားခဲ့လို့ စာလုံး ၅လုံးကိုပဲ ပြပေးတာဖြစ်ပါတယ်။ တကယ်လို့ ကိုယ်က စာလုံး ၁၀လုံး ဆွဲထုတ်ချင်ရင် တန်ဖိုးကို 10 ဆိုပြီး ထားပေးရမှာ ဖြစ်ပါတယ်။ ဆွဲထုတ်ပြထားတဲ့ phoneme ရဲ့ နောက်မှာ ကပ်ပါနေတဲ့ နံပါတ်တွေကတော့ [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) တန်ဖိုးတွေဖြစ်ပါတယ်။  

```
စက် ရုပ်	se' jou'
စက် စက်	se' se'
ရို့ ရို့	jou. jou.
စက် ရုံ	se' joun
```

နောက်ထပ် phoneme အသစ် တစ်ခု "ra- khain" (ရခိုင်) ကို fuzzy-match.py ပရိုဂရမ်နဲ့ search လုပ်ကြည်ရအောင်။  

```
$ python ./fuzzy-match.py ./f4 "ra- khain"
[('ra- khain', 100), ('a- khain', 94), ('a- kha.', 90), ("a- kha'", 90), ('a- kha', 90)]
```


```
ရ ခိုင်	ra- khain
အ ခိုင်	a- khain
အ ခ	a- kha.
အ ခတ်	a- kha'
အ ခါ	a- kha
```

```
$ python ./fuzzy-match.py ./f3 "စာလု"
[('စ လုံး', 100), ('စ လုံး', 100), ('စာ စီ', 95), ('စာ စီ', 95), ('စာ လုံး', 95)]

$ python ./fuzzy-match.py ./f3 "ခ လုပ်"
[('ခါး ချပ်', 95), ('ခို လှုံ', 95), ('ခိုး ချ', 95), ('ခိုး ပြေး', 95), ('ခု ခံ', 95)]

$ python ./fuzzy-match.py ./f3 "ခိုး"
[('က ချ လာ', 90), ('က ချင်', 90), ('က ချေ သည်', 90), ('က စော့ ခါး', 90), ('က တိုး ခွာ', 90)]
```

https://github.com/seatgeek/fuzzywuzzy/blob/master/test_fuzzywuzzy.py
