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

[myG2P](https://github.com/ye-kyaw-thu/myG2P) ထဲမှာရှိတဲ့ phoneme တွေကို fuzzy matching နဲ့ ဆွဲထုတ်ကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ python script ပါ။ သုံးထားတဲ့ Python library ကတော့ [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) ပါ။  

command argument အဖြစ်ပေးထားတဲ့အထဲက f4 ဆိုတဲ့ ဖိုင်က myG2P (grapheme-to-phoneme) အဘိဓာန်ထဲက ကော်လံနံပါတ် ၄ ကိုပဲ (phoneme အပိုင်းတွေကိုပဲ) cut command နဲ့ ဖြတ်ထုတ်ထားတဲ့ ဖိုင်ပါ။ အဲဒီဖိုင်ကို phoneme dictionary အနေနဲ့ သုံးခဲ့ပါတယ်။ အောက်ပါ ဥပမာက စက်ရုပ်ရဲ့ phoneme ဖြစ်တဲ့ "se' jou'" ကို fuzzy matching လုပ်ကြည့်ပြီး ရလာတဲ့ top 5 phoneme list ပါ။  

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

ရလဒ်ကတော့ အောက်ပါအတိုင်း ရခဲ့ပါတယ်။  

```
ရ ခိုင်	ra- khain
အ ခိုင်	a- khain
အ ခ	a- kha.
အ ခတ်	a- kha'
အ ခါ	a- kha
```

တကယ်က fuzzy-match.py မှာ ကျွန်တော်သုံးပြထားတာက extraction လုပ်တဲ့အပိုင်း (process.extract) ပဲဖြစ်ပါတယ်။ တခြား support လုပ်ထားတဲ့ library function တွေကို အသေးစိတ်လေ့လာချင်သူများကတော့ [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) ရဲ့ library ဖိုင်ကို ဝင်ဖတ်တာ၊ test run လုပ်ဖို့အတွက် ရေးပေးထားတဲ့ [test_fuzzywuzzy.py](https://github.com/seatgeek/fuzzywuzzy/blob/master/test_fuzzywuzzy.py) ကို လေ့လာတာမျိုး လုပ်ပါလို့ အကြံဉာဏ်ပေးချင်ပါတယ်။  

တစ်ခု သတိပေးချင်တာက လက်ရှိ "fuzzywuzzy" library က မြန်မာစာလုံးတွေကို တိုက်ရိုက် ထည့်ပြီး fuzzy matching လုပ်ရင် အောက်ပါ ဥပမာတွေအတိုင်း အဆင်ပြေမှာ မဟုတ်ပါဘူး။  

```
$ python ./fuzzy-match.py ./f3 "စာလု"
[('စ လုံး', 100), ('စ လုံး', 100), ('စာ စီ', 95), ('စာ စီ', 95), ('စာ လုံး', 95)]

$ python ./fuzzy-match.py ./f3 "ခ လုပ်"
[('ခါး ချပ်', 95), ('ခို လှုံ', 95), ('ခိုး ချ', 95), ('ခိုး ပြေး', 95), ('ခု ခံ', 95)]

$ python ./fuzzy-match.py ./f3 "ခိုး"
[('က ချ လာ', 90), ('က ချင်', 90), ('က ချေ သည်', 90), ('က စော့ ခါး', 90), ('က တိုး ခွာ', 90)]
```

မြန်မာစာအတွက် fuzzy matching လုပ်ဖို့ အတွက်ဆိုရင်တော့ လက်ရှိ library မှာ force_ascii=force_ascii ဆိုတဲ့အပိုင်းတွေကို force_ascii=False ဆိုပြီး ပြင်သုံးရမယ်လို့ ထင်ပါတယ်။ ကျွန်တော်လေ့လာမိသလောက် test run ပရိုဂရမ်မှာ အင်္ဂလိပ်စာမဟုတ်တဲ့ တခြားဘာသာစကားတွေအတွက်တော့ unicode တန်ဖိုးတွေအဖြစ်ပြောင်းလိုက်ပြီးတော့ ```force_ascii=False``` ဆိုပြီး run ပြထားတာကို အောက်ပါအတိုင်း တွေ့ရပါတယ်။  

```
        # Cyrillic.
        s1 = "\u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433"
        s2 = "\u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442"
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

        # Chinese.
        s1 = "\u6211\u4e86\u89e3\u6570\u5b66"
        s2 = "\u6211\u5b66\u6570\u5b66"
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)
```

## 7. [korean-breaks.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/korean-breaks.py)  

Statistical Machine Translation (SMT) experiment တစ်ခုအတွက် ကိုရီးယား စာကြောင်းတွေကို morphological based segmentation လုပ်ဖို့အတွက် ရေးခဲ့တဲ့ python script ပါ။ သုံးပုံသုံးနည်း နဲ့ run ထားစဉ်မှာ တွေ့ရတဲ့ screen output တချို့က အောက်ပါအတိုင်းပါ။  

testing လုပ်ဖို့အတွက် ကိုရီးယားစာကြောင်းတွေ ရိုက်ထည့်ထားတဲ့ input ဖိုင်ကို cat command နဲ့ ရိုက်ထုတ်ကြည့်ရအောင်။  

```
$ cat ./tst.ko
컴퓨터에 오피스 2003 를 설치해 주세요 .
이 길은 저기서 둘로 갈라지다 .
높은 산에 올라가면 기압이 낮아져 귀가 멍멍해 진다 .
이약을 먹소 있어요 .
그 책을 이쪽으로 가져와라 .
실례지만 몇 살입니까 ?
약속을 합시다 .
독서는 나의 유일한 위로가 된다 .
저는 차를 몰고 가다가 눈에 띄는 가게 앞에 차를 세웠어요 .
보통 호수공원까지 버스로 1 시간 10 분쯤 걸립니다 .
```

-word option နဲ့ ဖြတ်ရင်တော့ input ပေးလိုက်တဲ့ ဖိုင်ထဲက စာကြောင်းတွေရဲ့ spacing ကို အခြေခံပြီးတော့ ဖြတ်ပေးတာပါ။ word segmentation ဆိုတာထက် machine translation အတွက် ပြင်ဆင်တဲ့ အပိုင်းဆိုရင် ပိုမှန်ပါလိမ့်မယ်။  

```
$ python ./korean-breaks.py ./tst.ko -word
컴퓨터에 오피스 2003 를 설치해 주세요 .
이 길은 저기서 둘로 갈라지다 .
높은 산에 올라가면 기압이 낮아져 귀가 멍멍해 진다 .
이약을 먹소 있어요 .
그 책을 이쪽으로 가져와라 .
실례지만 몇 살입니까 ?
약속을 합시다 .
독서는 나의 유일한 위로가 된다 .
저는 차를 몰고 가다가 눈에 띄는 가게 앞에 차를 세웠어요 .
보통 호수공원까지 버스로 1 시간 10 분쯤 걸립니다 .
```

-morph option နဲ့ ဖြတ်ကြည့်ရင် အောက်ပါအတိုင်း ဖြတ်ပေးပါလိမ့်မယ်။  

```
$ python ./korean-breaks.py ./tst.ko -morph
컴퓨터 에 오피스 2003 를 설치 해 주 세요 .
이 길 은 저기 서 둘 로 갈라지 다 .
높 은 산 에 올라가 면 기압 이 낮 아 져 귀 가 멍멍 해 진다 .
이약 을 먹 소 있 어요 .
그 책 을 이쪽 으로 가져와라 .
실례 지만 몇 살 입니까 ?
약속 을 합시다 .
독서 는 나 의 유일 한 위로 가 된다 .
저 는 차 를 몰 고 가 다가 눈 에 띄 는 가게 앞 에 차 를 세웠 어요 .
보통 호수 공원 까지 버스 로 1 시간 10 분 쯤 걸립니다 .
```

-pos option နဲ့ ဖြတ်ရင်တော့ POS tagging ပါ လုပ်ပေးပါလိမ့်မယ်။  

```
$ python ./korean-breaks.py ./tst.ko -pos
[('컴퓨터', 'NNG'), ('에', 'JKB'), ('오피스', 'NNP'), ('2003', 'SN'), ('를', 'JKO'), ('설치', 'NNG'), ('해', 'XSV+EC'), ('주', 'VX'), ('세요', 'EP+EF'), ('.', 'SF')]
[('이', 'MM'), ('길', 'NNG'), ('은', 'JX'), ('저기', 'NP'), ('서', 'JKB'), ('둘', 'NR'), ('로', 'JKB'), ('갈라지', 'VV'), ('다', 'EF'), ('.', 'SF')]
[('높', 'VA'), ('은', 'ETM'), ('산', 'NNG'), ('에', 'JKB'), ('올라가', 'VV'), ('면', 'EC'), ('기압', 'NNG'), ('이', 'JKS'), ('낮', 'VA'), ('아', 'EC'), ('져', 'VX+EC'), ('귀', 'NNG'), ('가', 'JKS'), ('멍멍', 'MAG'), ('해', 'VV+EC'), ('진다', 'VX+EF'), ('.', 'SF')]
[('이약', 'NNG'), ('을', 'JKO'), ('먹', 'VV'), ('소', 'EC'), ('있', 'VX'), ('어요', 'EF'), ('.', 'SF')]
[('그', 'MM'), ('책', 'NNG'), ('을', 'JKO'), ('이쪽', 'NP'), ('으로', 'JKB'), ('가져와라', 'VV+EF'), ('.', 'SF')]
[('실례', 'NNG'), ('지만', 'VCP+EC'), ('몇', 'MM'), ('살', 'NNBC'), ('입니까', 'VCP+EF'), ('?', 'SF')]
[('약속', 'NNG'), ('을', 'JKO'), ('합시다', 'VV+EF'), ('.', 'SF')]
[('독서', 'NNG'), ('는', 'JX'), ('나', 'NP'), ('의', 'JKG'), ('유일', 'NNG'), ('한', 'XSA+ETM'), ('위로', 'NNG'), ('가', 'JKS'), ('된다', 'VV+EF'), ('.', 'SF')]
[('저', 'NP'), ('는', 'JX'), ('차', 'NNG'), ('를', 'JKO'), ('몰', 'VV'), ('고', 'EC'), ('가', 'VX'), ('다가', 'EC'), ('눈', 'NNG'), ('에', 'JKB'), ('띄', 'VV'), ('는', 'ETM'), ('가게', 'NNG'), ('앞', 'NNG'), ('에', 'JKB'), ('차', 'NNG'), ('를', 'JKO'), ('세웠', 'VV+EP'), ('어요', 'EF'), ('.', 'SF')]
[('보통', 'NNG'), ('호수', 'NNG'), ('공원', 'NNG'), ('까지', 'JX'), ('버스', 'NNG'), ('로', 'JKB'), ('1', 'SN'), ('시간', 'NNG'), ('10', 'SN'), ('분', 'NNBC'), ('쯤', 'XSN'), ('걸립니다', 'VV+EF'), ('.', 'SF')]
```

## 8. [epitranscribe.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/epitranscribe.py)  

Epitran က ဘာသာစကားပေါင်း ၆၉ ခုအတွက် (လက်ရှိ ဗားရှင်းမှာ ကျွန်တော် ရေတွက်ထားသလောက်) IPA (International Phonetic Alphabet) transcribe လုပ်ဖို့ develop လုပ်ထားတဲ့ tool ပါ။ Link: [https://github.com/dmort27/epitran](https://github.com/dmort27/epitran)   

ကျောင်းသားတွေကို သုံးခိုင်းတဲ့အခါမှာ အခက်အခဲတစ်ခုဖြစ်တာက အော်ရဂျင်နယ် ကုဒ်က Python2 နဲ့ ရေးထားတာမို့၊ ခုနောက်ပိုင်း စက်ထဲမှာ ရှိတဲ့ Python3 နဲ့ သုံးနေတဲ့ ပရိုဂရမ်တွေထဲကနေ ခေါ်သုံးဖို့ လုပ်တဲ့အခါမှာ ကုဒ်ကို အနည်းငယ်ဝင်ပြင်ဆင်ရပါတယ်။ အဲဒီအတွက် ဝယ်ပြင်ထားတဲ့ကုဒ်ကို တင်ပေးထားပြီး သုံးပုံသုံးနည်းကိုလည်း သိစေချင်လို့ Github မှာ တင်ပေးထားလိုက်တယ်။  

ဆိုကြပါစို့ ကျွန်တော်တို့မှာ အောက်ပါအတိုင်း မြန်မာနာမည်တွေကို သိမ်းထားတဲ့ ဖိုင်ရှိတယ်။  

```
(base) ye@ykt-pro:~/tool/epitran/epitran/y-test$ cat ./example.txt 
စိုး ရာ ဇာ
ဖြိုး ထက် ဝေ
ကောင်း ခန့် ညို
ခင် ငြိမ်း စံ
ကပ် ဇ ထန်
ခင် ဇာ ခြည် ဝင်း
```

IPA transcribe ကို အောက်ပါအတိုင်း လုပ်လို့ ရပါတယ်။ တချို့ speech processing နဲ့ ပတ်သက်တဲ့ experiment တွေအတွက် အသုံးဝင်ပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:~/tool/epitran/epitran/y-test$ cat ./example.txt | python ../bin/epitranscribe.py "mya-Mymr"
so ja za
pʰəjo tʰəkɛʔ we
kaʊɴ kʰaɴ ɲo
kʰɪɴ d͡ʑeɪɴ saɴ
kaʔ zə tʰaɴ
kʰɪɴ za t͡ɕʰi wɪɴ
```

## 9. [plot-unicode-char.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/plot-unicode-char.py)  

run ပြီးသွားတဲ့အခါမှာ python script ရှိတဲ့ path အောက်မှာ plot-unicode-char.png ဆိုတဲ့ ပုံထွက်လာပါလိမ့်မယ်။  
```
$ python ./plot-unicode-char.py 
$ ls
plot-unicode-char.png  plot-unicode-char.py
```

ပုံကတော့ အောက်ပါအတိုင်းပါ  

<img src="https://github.com/ye-kyaw-thu/tools/blob/master/python/test-data/plot-unicode-char.png" alt="output graph" width="640x480"/>
<p align="center"> Fig. plot-unicode-char.png </p>  

## 10. [en-sentence-tokenizer.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/en-sentence-tokenizer.py)  

NLTK library ကို သုံးပြီး ရေးထားတဲ့ sentence tokenizer ပါ။  
input ပေးတာကတော့ stdin ကနေရော file ကို argument parsing လုပ်ပြီးတော့ရော နှစ်မျိုးစလုံး ပေးလို့ ရပါတယ်။  

stdin ကနေ ပေးပြီး run တဲ့ ဥပမာ...  
```
$ echo "Hello! This is Ye. I hope you remember me. We met at InterSpeech 2019. I attended your paper presentation. We also discussed about zeroshot ASR. Please keep in touch!" | python ./en-sentence-tokenizer.py 
['Hello!', 'This is Ye.', 'I hope you remember me.', 'We met at InterSpeech 2019.', 'I attended your paper presentation.', 'We also discussed about zeroshot ASR.', 'Please keep in touch!']

```

file ကို command line ကနေ argument အနေနဲ့ ပေးပြီး run တဲ့ ဥပမာ...  

```
$ cat ./en.text.txt 
Hello! This is Ye. I hope you remember me. We met at InterSpeech 2019. I attended your paper presentation. We also discussed about zeroshot ASR. Please keep in touch!
$ python ./en-sentence-tokenizer.py ./en.text.txt 
['Hello!', 'This is Ye.', 'I hope you remember me.', 'We met at InterSpeech 2019.', 'I attended your paper presentation.', 'We also discussed about zeroshot ASR.', 'Please keep in touch!']

```

## 11. [en-word-tokenizer.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/en-word-tokenizer.py)  

အင်္ဂလိပ်စာ က မြန်မာစာနဲ့ မတူပဲ ရေးကတည်းက စာလုံး တစ်လုံးချင်းစီကို space ခြားပြီး ရေးကြပေမဲ့ NLP အလုပ်တွေကို လုပ်ကြတဲ့အခါမှာ အင်္ဂလိပ်စာကိုလည်း word tokenization လုပ်ဖို့ လိုအပ်ပါတယ်။ NLTK library ကတော့ ကိုယ့်စက်ထဲမှာ installation လုပ်ထားမှ အခု python script က error မပေးပဲ အလုပ်လုပ်သွားပါလိမ့်မယ်။ အောက်ပါ example running လုပ်ထားတာတွေကို လေ့လာပြီး ကိုယ်လိုသလို ပြင်ဆင်ပြီး သုံးသွားကြပါ။  

input ဖိုင်က အောက်ပါအတိုင်း စာကြောင်း ခုနစ်ကြောင်း ပါဝင်ပါတယ်။  
```
$ cat ./en.sentence.txt 
Hello!
This is Ye.
I hope you remember me.
We met at InterSpeech 2019.
I attended your paper presentation.
We also discussed about zeroshot ASR.
Please keep in touch!
```

input ဖိုင်ကို အောက်ပါအတိုင်း အမျိုးမျိုး command line parsing လုပ်ပြီး word tokenization လုပ်ခိုင်းလို့ ရပါတယ်။  
```
$ python ./en-word-tokenizer.py ./en.sentence.txt 
['Hello', '!']
['This', 'is', 'Ye', '.']
['I', 'hope', 'you', 'remember', 'me', '.']
['We', 'met', 'at', 'InterSpeech', '2019', '.']
['I', 'attended', 'your', 'paper', 'presentation', '.']
['We', 'also', 'discussed', 'about', 'zeroshot', 'ASR', '.']
['Please', 'keep', 'in', 'touch', '!']
```

```
$ cat en.sentence.txt | python ./en-word-tokenizer.py 
['Hello', '!']
['This', 'is', 'Ye', '.']
['I', 'hope', 'you', 'remember', 'me', '.']
['We', 'met', 'at', 'InterSpeech', '2019', '.']
['I', 'attended', 'your', 'paper', 'presentation', '.']
['We', 'also', 'discussed', 'about', 'zeroshot', 'ASR', '.']
['Please', 'keep', 'in', 'touch', '!']
```

```
$ python ./en-word-tokenizer.py < ./en.sentence.txt 
['Hello', '!']
['This', 'is', 'Ye', '.']
['I', 'hope', 'you', 'remember', 'me', '.']
['We', 'met', 'at', 'InterSpeech', '2019', '.']
['I', 'attended', 'your', 'paper', 'presentation', '.']
['We', 'also', 'discussed', 'about', 'zeroshot', 'ASR', '.']
['Please', 'keep', 'in', 'touch', '!'] 
```

## 12. [en-tokenization-on-punctuation.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/en-tokenization-on-punctuation.py)  

အထက်က ပရိုဂရမ်မှာ သုံးပြခဲ့တဲ့ word_tokenize library က တကယ်က TreebankWordTokenizer class ကို wrapper function အနေနဲ့ ခေါ်သုံးထားတာပါ။ အဲဒီလို မလုပ်ပဲ TreebankWordTokenizer ကိုပဲ တန်းခေါ်ပြီး သုံးလို့လည်း ရပါတယ်။ word tokenized လုပ်ပြီး ထွက်လာတဲ့ output ကတော့ အတူတူပဲ ဖြစ်ပါလိမ့်မယ်။ ဒီ နံပါတ် 12 ပရိုဂရမ်မှာ အဓိက ရေးပြထားတာက အင်္ဂလိပ်ဘာသာရဲ့ punctuation သင်္ကေတတွေကို tokenization လုပ်တဲ့အခါမှာ ပုံစံနှစ်မျိုးနဲ့ tokenize လုပ်လို့ ရကြောင်း၊ output နှစ်မျိုး ဖြစ်နိုင်ကြောင်း ကို ဖြစ်ပါတယ်။   

အောက်ပါ running example မှာ "Don't" နဲ့ "can't" တို့ကို tokenize လုပ်တဲ့အခါမှာ မတူတဲ့ ပုံစံနှစ်မျိုးနဲ့ ဖြတ်ပေးကြောင်းကို မြင်ရမှာ ဖြစ်ပါတယ်။ ကိုယ် လုပ်မယ့် NLP task အပေါ်ကို မူတည်ပြီးတော့ အဆင်ပြေတဲ့ tokenizer ကို ယူသုံးပါ။  

```
$ echo "Don't do it! I can't stand it!" | python ./en-tokenization-on-punctuation.py 
Treebank:  ['Do', "n't", 'do', 'it', '!', 'I', 'ca', "n't", 'stand', 'it', '!']
WordPunct ['Don', "'", 't', 'do', 'it', '!', 'I', 'can', "'", 't', 'stand', 'it', '!']
```

## 13. [filter-en-stopwords.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/filter-en-stopwords.py)  

NLTK library ကို သုံးပြီးတော့ အင်္ဂလိပ်စာကြောင်းတွေထဲက stopword တွေကို filter လုပ်တာကို ဒီမိုရေးပြထားတာပါ။ stopword တွေက တချို့ NLP အလုပ်တွေအတွက် အနှောက်အယှက်ဖြစ်ပါတယ်။ ဥပမာ စာကြောင်း တစ်ကြောင်းချင်းစီရဲ့ အဓိပ္ပါယ်ကို နားလည်အောင် ကြိုးစားဖို့အတွက် ဆောက်တဲ့ မော်ဒယ်တွေအတွက် ဆိုရင် စာကြောင်းတိုင်းလိုလိုမှာ ကြိမ်ဖန်များစွာ ပါဝင်နေတဲ့ stopword တွေကို preprocessing အပိုင်းမှာ အရင်ဆုံး ဖြုတ်လိုက်တာမျိုး လုပ်ကြရပါတယ်။ NLP R&D လုပ်မယ့် ကျောင်းသားတွေက ဒီ stopword ကိစ္စကိုလည်း သိထားသင့်ပါတယ်။  

en.sentence.txt ဆိုတဲ့ ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို အရင်ဆုံး cat command နဲ့ ရိုက်ထုတ်ကြည့်ရအောင်...  
```
$ cat ./en.sentence.txt 
Hello!
This is Ye.
I hope you remember me.
We met at InterSpeech 2019.
I attended your paper presentation.
We also discussed about zeroshot ASR.
Please keep in touch!
Can't work!
```

stopword တွေကို filter လုပ်ခိုင်းပြီး ထွက်လာတဲ့ output စာကြောင်းတွေကို လေ့လာကြည့်ရအောင်...  
```
$ python ./filter-en-stopwords.py ./en.sentence.txt 
['Hello', '!']
['This', 'Ye', '.']
['I', 'hope', 'remember', '.']
['We', 'met', 'InterSpeech', '2019', '.']
['I', 'attended', 'paper', 'presentation', '.']
['We', 'also', 'discussed', 'zeroshot', 'ASR', '.']
['Please', 'keep', 'touch', '!']
['Ca', "n't", 'work', '!']
```

NLTK library ကို install လုပ်ထားပေမဲ့ ကိုယ့်ရဲ့ စက်ထဲမှာ stopword resource ဖိုင်က download မလုပ်ထားရသေးရင် run တဲ့အခါမှာ error ပေးပါလိမ့်မယ်။ အဲဒီလိုမျိုးဆိုရင် အောက်မှာ လုပ်ပြထားတဲ့အတိုင်း stopword ကို အရင်ဆုံး ကိုယ့်စက်ထဲကို download လုပ်ပြီးမှ run ပါ။  

```
$ python
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> nltk.download('stopwords')
[nltk_data] Downloading package stopwords to /home/ye/nltk_data...
[nltk_data]   Unzipping corpora/stopwords.zip.
True
>>> exit()
```

## 14. [mk-QR-code.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk-QR-code.py)  

QR Code ကို ပုံစံအမျိုးမျိုးနဲ့ application အမျိုးမျိုးမှာ အသုံးပြုနေကြတာကို သတိပြုမိပါလိမ့်မယ်။ ဒီ mk-QR-code.py ကတော့ qrcode ဆိုတဲ့ python library တစ်ခုကို သုံးပြီးတော့ QR code တွေကို ဘယ်လို အလွယ်တကူ ဖန်တီးယူလို့ ရသလဲဆိုတာကို ရေးပြထားတဲ့ python code ပါ။ qrcode library က ကိုယ့်စက်ထဲမှာ မရှိသေးရင်တော့ ```pip install qrcode``` ဆိုတဲ့ command ရိုက်ပြီး အရင်ဆုံး install လုပ်ဖို့ မမေ့ပါနဲ့။  သုံးပုံ သုံးနည်းကတော့ အောက်ပါအတိုင်းပါ။  

QR code လုပ်စေချင်တဲ့ web link တစ်ခုကို echo command နဲ့ပဲ ဖြစ်ဖြစ် parse လုပ်ပြီး run တဲ့ပုံစံက အောက်ပါအတိုင်းပါ...
```
$ echo "https://github.com/ye-kyaw-thu" | python ./mk-QR-code.py 
```

အဆင်ပြေပြေနဲ့ run လို့ ပြီးသွားတယ်ဆိုရင် mk-QR-code.py ရှိတဲ့ path မှာပဲ qrcode-1.jpg ဆိုတဲ့ ဖိုင်အသစ် ကိုတွေ့ရပါလိမ့်မယ်။  
```
$ ls
mk-QR-code.py  qrcode-1.jpg
```

link တွေ အများကြီးကို QR Code လုပ်ချင်တယ်ဆိုရင် အောက်ပါ links4QRcode.txt ဖိုင်ထဲမှာ ရိုက်ပြထားသလို link address တွေကို တစ်ကြောင်းချင်းစီ တန်းစီ ရိုက်ထားရင် အိုကေပါတယ်။  
```
$ cat ./links4QRcode.txt 
https://github.com/ye-kyaw-thu
https://sites.google.com/site/yekyawthunlp/
https://twitter.com/ye_edu/
```

အထက်မှာ ဥပမာအနေနဲ့ ဖန်တီးခဲ့တဲ့ links4QRcode.txt ကို mk-QR-code.py ပရိုဂရမ်ကို argument parsing အနေနဲ့ input လုပ်ပြီး run ကြည့်ကြရအောင်...
```
$ python ./mk-QR-code.py < ./links4QRcode.txt 
```

run ပြီးသွားတဲ့အခါမှာ အောက်ပါအတိုင်း qrcode-{1,2,3}.jpg ဆိုပြီး ပုံသုံးပုံ ရလာပါလိမ့်မယ်။  
```
$ ls
links4QRcode.txt  mk-QR-code.py  qrcode-1.jpg  qrcode-2.jpg  qrcode-3.jpg
```
<br />
qrcode-1.jpg ဖိုင်ကို မိုဘိုင်းဖုန်းရဲ့ ကင်မရာနဲ့ပဲ ဖြစ်ဖြစ် scan ဖတ်ပြီး GitHub ကို ဝင်ကြည့်လို့ ရပါလိမ့်မယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/qrcode-1.jpg" alt="drawing" width="300"/>  
</p>  
<div align="center">
  Fig. QR code for my GitHub link: https://github.com/ye-kyaw-thu  
</div>   

<br />
qrcode-2.jpg ဖိုင်ကတော့ homepage ရဲ့ link ဖြစ်ပါတယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/qrcode-2.jpg" alt="drawing" width="300"/>  
</p>  
<div align="center">
  Fig. QR code for my Homepage Link: https://sites.google.com/site/yekyawthunlp/  
</div>   

<br />
qrcode-1.jpg ဖိုင်ကို မိုဘိုင်းဖုန်းရဲ့ ကင်မရာနဲ့ပဲ ဖြစ်ဖြစ် scan ဖတ်ပြီး twitter account link ကို ဝင်ကြည့်လို့ ရပါလိမ့်မယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/qrcode-3.jpg" alt="drawing" width="300"/>  
</p>  
<div align="center">
  Fig. QR code for my Twitter Link: https://twitter.com/ye_edu/  
</div>   

<br />
QR Code တွေကို python ပရိုဂရမ်ထဲကနေ ဖတ်ပြီး နဂို link တွေကို ပြန်ရိုက်ထုတ်ပေးချင်ရင်တော့ cv2 library ကို သုံးပြီး လုပ်လို့ ရပါတယ်။  
Reference: https://pypi.org/project/qrcode/   
အောက်ပါ ဥပမာကိုလေ့လာပါ။  

```
import cv2
QRdetector = cv2.QRCodeDetector()
val, points, straight_qrcode = QRdetector.detectAndDecode(cv2.imread("qrcode-2.jpg"))
print(val)
```

တကယ်လို့ ကိုယ့်စက်ထဲမှာ OpenCV က installation မလုပ်ထားရသေးဘူး ဆိုရင်တော့ ```pip install opencv-python``` နဲ့ install လုပ်ယူပါ။  

## 15. [wu-palmer-similarity.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/wu-palmer-similarity.py)  

အင်္ဂလိပ်စာလုံး နှစ်လုံးကို Wu and Palmer Similarity တိုင်းတာကြည့်ထားတဲ့ ပရိုဂရမ်ပါ။  
ဘာသာဗေဒ မှာ [Word senses](https://en.wikipedia.org/wiki/Word_sense) လို့ခေါ်တဲ့ technical term တစ်ခု ရှိပါတယ်။ စကားလုံးရဲ့ တိုက်ရိုက် အဓိပ္ပါယ် သာမကပဲ စာကြောင်းတွေထဲမှာ သုံးပုံသုံးနည်းအမျိုးမျိုး နဲ့အတူတွဲပါနေတဲ့ အဓိပ္ပါယ် အားလုံးကို ခြုံငုံမိတဲ့ အဓိပ္ပါယ်ကို ဆိုလိုပါတယ်။ ဥပမာ အင်္ဂလိပ်စာလုံး "bank" မှာ ဆိုရင် သုံးတဲ့ စာကြောင်းပေါ်မူတည်ပြီးတော့ sense နှစ်မျိုးရှိပါတယ်။ တစ်မျိုးက "ဘဏ်" ဆိုတဲ့ အဓိပ္ပါယ်ရပြီးတော့ နောက်တစ်မျိုးကတော့ "ကမ်းပါး" ဆိုတဲ့ အဓိပ္ပါယ်ပါ။ ဒီ python program မှာတော့ Wordnet မှာ သတ်မှတ်ထားတဲ့ စကားလုံးတစ်လုံးချင်းစီရဲ့ ဒေတာအပေါ်အများကြီး မူတည်ပါလိမ့်မယ်။ Wu and Palmer ရဲ့ score ကတော့ သုည အထက်ကနေ ၁ အထိ ကြားထဲမှာ ရှိတဲ့ တန်ဖိုး တစ်ခုခု ဖြစ်ပါလိမ့်မယ်။ ပိုမြင်သာအောင် ရေးရရင် ```0 < score <=1``` ပါ။ အဲဒါကြောင့် score က သုည ဘယ်တော့မှ ရမှာ မဟုတ်ပါဘူး ဘာကြောင့်လဲ ဆိုတော့ တွက်တဲ့ ဖော်မြူလာက [LCS (Least Common Subsumer)](https://stackoverflow.com/questions/18629469/what-is-least-common-subsumer-and-how-to-compute-it/18631789#:~:text=According%20to%20this%20paper%2C%20Least,by%20the%20is%2Da%20relation.) ပေါ်ကိုမူတည်ပြီးတွက်လို့ပါ။   

အသေးစိတ် လေ့လာချင်တဲ့သူတွေကတော့ အောက်ပါ သုတေသန စာတမ်းကို ဖတ်ပြီး လေ့လာပါ။  
```
@inproceedings{wu-palmer-1994-verb,
    title = "Verb Semantics and Lexical Selection",
    author = "Wu, Zhibiao  and
      Palmer, Martha",
    booktitle = "32nd Annual Meeting of the Association for Computational Linguistics",
    month = jun,
    year = "1994",
    address = "Las Cruces, New Mexico, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P94-1019",
    doi = "10.3115/981732.981751",
    pages = "133--138",
}
```

တိုင်းတာချင်တဲ့ အင်္ဂလိပ်စာလုံး နှစ်လုံးကို space ခြားပြီး ရိုက်ပေးရပါမယ်။  echo command နဲ့လည်း အောက်ပါအတိုင်း command line argument အနေနဲ့ pass လုပ်ပြီး Wu and Palmer Similarity ဘယ်လောက်ရှိသလဲ ဆိုတာကို တိုင်းတာလို့ ရပါတယ်။ "Burma" နဲ့ "Myanmar" ကို တိုင်းတာကြည့်ရင် 1.0 ရတာကို တွေ့ရပါလိမ့်မယ်။  

```
$ echo "Burma Myanmar" | python ./wu-palmer-similarity.py 
Burma, Myanmar:  1.0
```

ရေးထားတဲ့ Python ပရိုဂရမ်က text file ထဲက space ခြားပြီး ရိုက်ပေးထားတဲ့ စာလုံးအတွဲတွေကိုလည်း တစ်တွဲချင်းစီ တိုင်းတာပေးတာမျိုးလည်း လုပ်ပေးအောင် ရေးထားပါတယ်။ word-pair.txt ထဲမှာ အောက်ပါ စာလုံးတွေ ကို space ခြားပြီးတော့ ရိုက်ထားတယ် ဆိုကြပါစို့...  

```
$ cat ./word-pair.txt 
Burma Myanmar
Hello hi
happy sad
flower gun
Aikido Judo
Taekwondo Karate
Karate Boxing
Karate Swimming
Karate Football
Karate Basketball
Swimming Diving
Python Pascal
Yangon Tokyo
Yangon Bangkok
Tokyo Kyoto
```

wu-palmer-similarity.py ကို အောက်ပါလိုမျိုး word-pair.txt ဖိုင်ကို ဖတ်ခိုင်းပြီး run လို့ရပါတယ်။ တွက်ပြီးထွက်လာတဲ့ score တွေကတော့ အောက်ပါအတိုင်းပါ။  

```
$ python ./wu-palmer-similarity.py < ./word-pair.txt 
Burma, Myanmar:  1.0
Hello, hi:  1.0
happy, sad:  None
flower, gun:  0.38095238095238093
Aikido, Judo:  0.9
Taekwondo, Karate:  0.9
Karate, Boxing:  0.6
Karate, Swimming:  0.6
Karate, Football:  0.6
Karate, Basketball:  0.6
Swimming, Diving:  0.4444444444444444
Python, Pascal:  0.09090909090909091
Yangon, Tokyo:  0.9090909090909091
Yangon, Bangkok:  0.9090909090909091
Tokyo, Kyoto:  0.8571428571428571
```

## 16. [nltk-en-pos-tagger.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/nltk-en-pos-tagger.py)  

NLTK library ကိုသုံးပြီး အင်္ဂလိပ်စာ စာကြောင်းတွေကို POS tagging လုပ်ကြည့်ရအောင်...  
အရင်ဆုံး echo command ကို သုံးပြီးတော့ "Who am I?" လို့ ရေးထားတဲ့ စာကြောင်းကို command line argument အနေနဲ့ ပေးကြည့်ရအောင်။  

```
$ echo "Who am I?" | python ./nltk-en-pos-tagger.py 
Who/WP am/VBP I/PRP ?/.
```

ဖိုင်တစ်ဖိုင်ကို POS tagging လုပ်ခိုင်းဖို့အတွက် အရင်ဆုံး ပြင်ဆင်ထားတဲ့ ဖိုင်ထဲမှာ ဘယ်လို စာကြောင်းတွေရှိသလဲ ဆိုတာကို cat command နဲ့ ရိုက်ထုတ်ခိုင်းကြည့်ရအောင်။  

```
$ cat ./Quotes-By-Famous-Scientists.txt 
Somewhere, something incredible is waiting to be known.
― Carl Sagan

Common Sense is that which judges the things given to it by other senses.
― Leonardo da Vinci

There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
― Albert Einstein

Physics isn’t the most important thing. Love is.
― Richard Feynman

The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge.
― Stephen Hawking

The first principle is that you must not fool yourself – and you are the easiest person to fool.
― Richard Feynman

Tact is the knack of making a point without making an enemy.
― Sir Isaac Newton

A man who dares to waste one hour of time has not discovered the value of life.
― Charles Darwin

Dreams are often most profound when they seem the most crazy.
― Sigmund Freud

The sun, with all the planets revolving around it, and depending on it, can still ripen a bunch of grapes as though it had nothing else in the universe to do.
― Galileo Galilei

Until man duplicates a blade of grass, nature can laugh at his so-called scientific knowledge.
― Thomas Edison

The love for all living creatures is the most noble attribute of man.
― Charles Darwin

Although I cannot move and I have to speak through a computer, in my mind I am free.
― Stephen Hawking

Blushing is the most peculiar and most human of all expressions.
― Charles Darwin

Flowers are restful to look at. They have neither emotions nor conflicts.
― Sigmund Freud
```

နာမည်ကြီး သိပ္ပံပညာရှင်တွေရဲ့ အယူအဆတွေကို ထင်ဟပ်တဲ့ အဆိုအမိန့်တွေပါ။  
ဟုတ်ပြီ။ အဲဒီဖိုင်ကို POS tagging လုပ်ခိုင်းကြည့်ရအောင်...   

```
$ python ./nltk-en-pos-tagger.py < ./Quotes-By-Famous-Scientists.txt 
Somewhere/RB ,/, something/NN incredible/JJ is/VBZ waiting/VBG to/TO be/VB known/VBN ./.
―/JJ Carl/NNP Sagan/NNP

Common/JJ Sense/NNP is/VBZ that/IN which/WDT judges/NNS the/DT things/NNS given/VBN to/TO it/PRP by/IN other/JJ senses/NNS ./.
―/JJ Leonardo/NNP da/NN Vinci/NN

There/EX are/VBP only/RB two/CD ways/NNS to/TO live/VB your/PRP$ life/NN ./. One/CD is/VBZ as/IN though/IN nothing/NN is/VBZ a/DT miracle/NN ./. The/DT other/JJ is/VBZ as/IN though/IN everything/NN is/VBZ a/DT miracle/NN ./.
―/NN Albert/NNP Einstein/NNP

Physics/NNS isn/VBP ’/JJ t/VBP the/DT most/RBS important/JJ thing/NN ./. Love/NNP is/VBZ ./.
―/JJ Richard/NNP Feynman/NNP

The/DT greatest/JJS enemy/NN of/IN knowledge/NN is/VBZ not/RB ignorance/NN ,/, it/PRP is/VBZ the/DT illusion/NN of/IN knowledge/NN ./.
―/NN Stephen/NNP Hawking/NNP

The/DT first/JJ principle/NN is/VBZ that/IN you/PRP must/MD not/RB fool/VB yourself/PRP –/JJ and/CC you/PRP are/VBP the/DT easiest/JJS person/NN to/TO fool/NN ./.
―/JJ Richard/NNP Feynman/NNP

Tact/NN is/VBZ the/DT knack/NN of/IN making/VBG a/DT point/NN without/IN making/VBG an/DT enemy/NN ./.
―/NN Sir/NNP Isaac/NNP Newton/NNP

A/DT man/NN who/WP dares/VBZ to/TO waste/VB one/CD hour/NN of/IN time/NN has/VBZ not/RB discovered/VBN the/DT value/NN of/IN life/NN ./.
―/NN Charles/NNP Darwin/NNP

Dreams/NNS are/VBP often/RB most/JJS profound/JJ when/WRB they/PRP seem/VBP the/DT most/RBS crazy/JJ ./.
―/NN Sigmund/NNP Freud/NNP

The/DT sun/NN ,/, with/IN all/PDT the/DT planets/NNS revolving/VBG around/IN it/PRP ,/, and/CC depending/VBG on/IN it/PRP ,/, can/MD still/RB ripen/VB a/DT bunch/NN of/IN grapes/NNS as/IN though/IN it/PRP had/VBD nothing/NN else/RB in/IN the/DT universe/NN to/TO do/VB ./.
―/JJ Galileo/NNP Galilei/NNP

Until/IN man/NN duplicates/VBZ a/DT blade/NN of/IN grass/NN ,/, nature/NN can/MD laugh/VB at/IN his/PRP$ so-called/JJ scientific/JJ knowledge/NN ./.
―/NN Thomas/NNP Edison/NNP

The/DT love/NN for/IN all/DT living/NN creatures/NNS is/VBZ the/DT most/RBS noble/JJ attribute/NN of/IN man/NN ./.
―/NN Charles/NNP Darwin/NNP

Although/IN I/PRP can/MD not/RB move/VB and/CC I/PRP have/VBP to/TO speak/VB through/IN a/DT computer/NN ,/, in/IN my/PRP$ mind/NN I/PRP am/VBP free/JJ ./.
―/NN Stephen/NNP Hawking/NNP

Blushing/NNP is/VBZ the/DT most/RBS peculiar/JJ and/CC most/JJS human/JJ of/IN all/DT expressions/NNS ./.
―/NN Charles/NNP Darwin/NNP

Flowers/NNS are/VBP restful/JJ to/TO look/VB at/IN ./. They/PRP have/VBP neither/DT emotions/NNS nor/CC conflicts/NNS ./.
―/NN Sigmund/NNP Freud/NNP

```

**သိစေချင်တာက 100% မှန်ကန်တဲ့ POS tagger ဆိုတာက ဘယ်ဘာသာစကားအတွက်မှ မရှိပါဘူး**  

## 17. [folder-file-dict.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/folder-file-dict.py)  

[audio_exploration code](https://github.com/phrasenmaeher/audio_exploration) ကို သုံးဖို့ ပြင်ခဲ့တဲ့ python script ပါ။ script ထဲမှာ assign လုပ်ထားတဲ့ path ကနေ full path အားလုံးကို ဆွဲထုတ်ပြီး၊ folder path ကို Python dictionary key အဖြစ်ထားပြီး အဲဒီအောက်က filename တွေကို value list အဖြစ်ထားပေးတဲ့ dictionary creation ပရိုဂရမ်ပါ။  

ဥပမာ အောက်ပါ tt/ ဆိုတဲ့ဖိုလ်ဒါထဲမှာ subfolder 1/, 2/, abc/ ဖိုလ်ဒါသုံးခုရှိပြီးတော့ အဲဒီ ဖိုလ်ဒါတွေအောက်မှာလည်း text ဖိုင် အသီးသီး ရှိကြတယ် ဆိုပါစို့။  

```
$ tree ./tt/
./tt/
├── 1
│   ├── file1.txt
│   └── file2.txt
├── 2
│   ├── file1.txt
│   ├── file2.txt
│   └── file3.txt
└── abc
    ├── fileA.txt
    └── fileB.txt

3 directories, 7 files
```

folder-file-dict.py ပရိုဂရမ်ကို run ရင် အောက်ပါ print ထုတ်ပေးတဲ့အတိုင်း Python dictionary ဆောက်ပေးသွားမှာ ဖြစ်ပါတယ်။  

```
$ python ./folder-file-dict.py 
{'tt/abc': ['fileA.txt', 'fileB.txt'], 'tt/2': ['file1.txt', 'file3.txt', 'file2.txt'], 'tt/1': ['file1.txt', 'file2.txt']}
```

တကယ်တမ်း ဒီ ပရိုဂရမ်နဲ့ စမ်းရေးထားတဲ့ function ကို audio_exploration library အတွက် စမ်းခဲ့တာက wave ဖိုင်တွေပါ။   
ကွန်ပျူတာတက္ကသိုလ် ဗန်းမော်မှာ စာသွားသင်ရင်းနဲ့ recording လုပ်ထားတဲ့ ဗမာစာ ဗျည်း၊ သရသံ wave ဖိုင်တွေထဲက open test ဖိုလ်ဒါနဲ့ run တာကို ဥပမာအနေနဲ့ ပြပါမယ်။  

```
$ tree -L 2 dataset2/ot-data/ 
dataset2/ot-data/
├── consonant
│   ├── 1
│   ├── 10
│   ├── 11
│   ├── 12
│   ├── 13
│   ├── 14
│   ├── 15
│   ├── 16
│   ├── 17
│   ├── 18
│   ├── 19
│   ├── 2
│   ├── 20
│   ├── 21
│   ├── 22
│   ├── 3
│   ├── 4
│   ├── 5
│   ├── 6
│   ├── 7
│   ├── 8
│   └── 9
└── vowel
    ├── 1
    ├── 10
    ├── 11
    ├── 12
    ├── 2
    ├── 3
    ├── 4
    ├── 5
    ├── 6
    ├── 7
    ├── 8
    └── 9

36 directories, 0 files
```

ဥပမာ consonant/1/ ဖိုလ်ဒါအောက်က ဖိုင်တွေက ဗမာစာ ဗျည်း "ကကြီး" ရဲ့အသံပါ။ တစ်ဖိုင်ချင်းစီက တစ်ယောက်ချင်းစီ အသံတွေပါ။  
အသေးစိတ်က ဒီ Github link (https://github.com/ye-kyaw-thu/Spectrograms-of-Myanmar-Speech) မှာ လေ့လာပါ။  

```
$ tree -L 3 dataset2/ot-data/ | head -n 50
dataset2/ot-data/
├── consonant
│   ├── 1
│   │   ├── 2018-11-12-13:34:35.16khz.mono.wav
│   │   ├── 2018-11-12-13:39:11.16khz.mono.wav
│   │   ├── 2018-11-12-13:39:21.16khz.mono.wav
│   │   ├── 2018-11-12-13:44:16.16khz.mono.wav
│   │   ├── 2018-11-12-13:51:05.16khz.mono.wav
│   │   ├── 2018-11-12-13:52:28.16khz.mono.wav
│   │   ├── 2018-11-12-13:52:40.16khz.mono.wav
│   │   ├── 2018-11-12-13:55:26.16khz.mono.wav
│   │   ├── 2018-11-12-13:57:02.16khz.mono.wav
│   │   ├── 2018-11-12-13:57:10.16khz.mono.wav
│   │   ├── 2018-11-12-14:00:24.16khz.mono.wav
│   │   ├── 2018-11-12-14:04:42.16khz.mono.wav
│   │   ├── 2018-11-12-14:04:53.16khz.mono.wav
│   │   ├── 2018-11-12-14:05:48.16khz.mono.wav
│   │   ├── 2018-11-12-14:07:01.16khz.mono.wav
│   │   ├── 2018-11-12-14:07:15.16khz.mono.wav
│   │   ├── 2018-11-12-14:10:44.16khz.mono.wav
│   │   ├── 2018-11-12-14:13:15.16khz.mono.wav
│   │   ├── 2018-11-12-14:13:34.16khz.mono.wav
│   │   └── 2018-11-12-14:14:28.16khz.mono.wav
│   ├── 10
│   │   ├── 2018-11-12-16:25:18.16khz.mono.wav
│   │   ├── 2018-11-12-16:25:25.16khz.mono.wav
│   │   ├── 2018-11-12-16:25:40.16khz.mono.wav
│   │   ├── 2018-11-12-16:26:44.16khz.mono.wav
│   │   ├── 2018-11-12-16:28:05.16khz.mono.wav
│   │   ├── 2018-11-12-16:28:12.16khz.mono.wav
│   │   ├── 2018-11-12-16:28:48.16khz.mono.wav
│   │   ├── 2018-11-12-16:28:58.16khz.mono.wav
│   │   ├── 2018-11-12-16:29:05.16khz.mono.wav
│   │   ├── 2018-11-12-16:29:22.16khz.mono.wav
│   │   ├── 2018-11-12-16:29:23.16khz.mono.wav
│   │   ├── 2018-11-12-16:29:26.16khz.mono.wav
│   │   ├── 2018-11-12-16:30:16.16khz.mono.wav
│   │   ├── 2018-11-12-16:30:28.16khz.mono.wav
│   │   ├── 2018-11-12-16:30:53.16khz.mono.wav
│   │   ├── 2018-11-12-16:31:40.16khz.mono.wav
│   │   ├── 2018-11-12-16:31:47.16khz.mono.wav
│   │   ├── 2018-11-12-16:32:17.16khz.mono.wav
│   │   ├── 2018-11-12-16:34:00.16khz.mono.wav
│   │   └── 2018-11-12-16:35:03.16khz.mono.wav
│   ├── 11
│   │   ├── 2018-11-12-18:45:10.16khz.mono.wav
│   │   ├── 2018-11-12-18:45:58.16khz.mono.wav
│   │   ├── 2018-11-12-18:46:10.16khz.mono.wav
│   │   ├── 2018-11-12-18:46:27.16khz.mono.wav
│   │   ├── 2018-11-12-18:47:27.16khz.mono.wav
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/audio_exploration$
```

တကယ်တမ်း audio_exploration library ကို ကိုယ့်စက်ထဲမှာ install လုပ်ပြီး run တဲ့အခါမှာ အောက်ပါအတိုင်းပါ။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/audio_exploration$ streamlit run ./dataset_overview.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.222.40.142:8501

```

Browser မှာ အောက်ပါလိုမျိုး wave ဖိုင်တွေကို waveplot အဖြစ်၊ spectrogram ပုံ အဖြစ်၊ MFCC ပုံတွေအဖြစ် အမျိုးမျိုး graph ထုတ်ကြည့်ပြီး လေ့လာလို့ ရပါတယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/audio-exploration-combined.png" alt="drawing" width="1800"/>  
</p>  
<div align="center">
  Fig. Exploring audio datasets with Streamlit and audio_exploration github code  
</div>   

## 18. [csv-str2mapping123.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/csv-str2mapping123.py)   

ကော်လံ ၆ခု ရှိတဲ့ CSV (Comma-Separated Values) ဖိုင်ထဲက ကော်လံနံပါတ် ၄ နဲ့ ကော်လံနံပါတ် ၅ တို့မှာ ရှိနေတဲ့ ဗမာစာ စာကြောင်းတွေကို proposed mapping 1, 2, 3 အဖြစ် ပြောင်းပေးတဲ့ Python ပရိုဂရမ်ပါ။  
Mapping 1, 2, 3 ဆိုတာက ဗမာစာ စာကြောင်းတွေကို similarity တိုင်းတဲ့အခါမှာ အသံထွက်ဆင်တူတာတွေနဲ့ ဗမာစာရဲ့သဘာဝအရ similar ဖြစ်တဲ့ စာကြောင်းတွေကို distance တွက်ပေးနိုင်ဖို့အတွက် ခိုင်ဆုဝေနဲ့ ကျွန်တော် proposed လုပ်ခဲ့တဲ့ mapping သုံးမျိုးပါ။ အသေးစိတ်ကိုတော့ [NSURL 2019 Paper](https://aclanthology.org/2019.nsurl-1.14/)) စာတမ်းနဲ့ [JIIST 2020 Journal Paper](https://github.com/ye-kyaw-thu/papers/blob/master/JIIST-April-2020/no.4.my-string-similarity.pdf) ဂျာနယ်စာတမ်းတွေမှာ ဖော်ပြထားပါတယ်။  

ဥပမာအနေနဲ့ input လုပ်မယ့် CSV ဖိုင်က အောက်ပါအတိုင်း format အတိုင်း ရှိပါတယ်။   

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/exp/chk-myint2htay-program/LSTMcoding_28july2021/data-map1$ cat ./head.train.csv 
id,senid1,senid2,sentence1,sentence2,is_duplicate
0,1,2,ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။,ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။,0
1,3,4,ဆက် ကြိုးစား ကြ ပါ,ဆက် ပြီး ကြိုးစား ပေး ပါ,1
2,5,6,သီချင်း အားလုံး ကြိုက် တယ်,အရမ်း ကြိုက် တဲ့ သီချင်း လေး,1
3,7,8,လေးစား ဂုဏ်ယူ ရ ပါ သည်,အားကျ အတုယူ ရ ပါ သည်,0
4,9,10,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။,0
5,11,12,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။,1
6,13,14,ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။,ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။,0
7,15,16,လေးစား တယ် အား လည်း ကျ မိ တယ်,မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ,0
8,17,18,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။,1
```

Mapping 1 အဖြစ် ပြောင်းမယ် ဆိုရင် --map option ကို 1 ထားထားပေးပါ။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/exp/chk-myint2htay-program/LSTMcoding_28july2021/data-map1$ python ./csv-str2mapping123.py --csvFile head.train.csv --map 1
id,senid1,senid2,sentence1,sentence2,is_duplicate
0,1,2,ကynတar် သတinကyr ရin ကinဘyr ကiu ကynတar် ပyar ပr မe s,ကinဘyr ရe သတin ကiu သu ပyar မ ပe ကynတar် ကyr ရ တar တe s,0
1,3,4,စd ကyiuစr ကy ပr,စd ပyi ကyiuစr ပa ပr,1
2,5,6,သiကyin အrလun ကyiud တe,အရn ကyiud တe သiကyin လa,1
3,7,8,လaစr ဂunရu ရ ပr သi,အrကy အတuရu ရ ပr သi,0
4,9,10,သu ကiu တa ပiu inr အရn စidဝinစr နa ပyi s,သu ကiu တa ပiu inr အရn ရinကun နa ပyi s,0
5,11,12,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလiအပd သr ကe တe s,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလi သr ကe တe s,1
6,13,14,ဒr ကiu ဝe မe လiu စinစr နa တr အတar်ပe ပyစ် နa တe s,ဒr ကiu ဝe ကe လiud တr မn တe လiu ကynတar် ထin တe s,0
7,15,16,လaစr တe အr လi ကy မi တe,မလaမစr မ လud နe အတuရu ပr,0
8,17,18,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ပunတuကu ထr တd ကy သi s,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ကiuကy ထr တd ကy သi s,1
```

Mapping 2 အဖြစ် ပြောင်းမယ် ဆိုရင် --map option မှာ 2 ထားထားပေးပါ။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/exp/chk-myint2htay-program/LSTMcoding_28july2021/data-map1$ python ./csv-str2mapping123.py --csvFile head.train.csv --map 2
id,senid1,senid2,sentence1,sentence2,is_duplicate
0,1,2,ကydတar် သတdကyr ရd ကdပyr ကiu ကydတar် ပyar ပr ပe s,ကdပyr ရe သတd ကiu သu ပyar ပ ပe ကydတar် ကyr ရ တar တe s,0
1,3,4,စd ကyiuစr ကy ပr,စd ပyi ကyiuစr ပa ပr,1
2,5,6,သiကyd ကrလun ကyiud တe,ကရd ကyiud တe သiကyd လa,1
3,7,8,လaစr ကudရu ရ ပr သi,ကrကy ကတuရu ရ ပr သi,0
4,9,10,သu ကiu တa ပiu ကr ကရd စidဝdစr တa ပyi s,သu ကiu တa ပiu ကr ကရd ရdကud တa ပyi s,0
5,11,12,ကr တiu ပeကu က ကပyiu တa စi ကiu ပကyrကတ ကလiကပd သr ကe တe s,ကr တiu ပeကu က ကပyiu တa စi ကiu ပကyrကတ ကလi သr ကe တe s,1
6,13,14,တr ကiu ဝe ပe လiu စiစr တa တr ကတar်ပe ပyစ် တa တe s,တr ကiu ဝe ကe လiud တr ပd တe လiu ကydတar် တd တe s,0
7,15,16,လaစr တe ကr လi ကy ပi တe,ပလaပစr ပ လud တe ကတuရu ပr,0
8,17,18,ကလa ပyr သi ကeကe ကတiက ပiပ i ပunရid ကiu ပunတuကu တr တd ကy သi s,ကလa ပyr သi ကeကe ကတiက ပiပ i ပunရid ကiu ကiuကy တr တd ကy သi s,1
```

Mapping 3 အဖြစ် convert လုပ်ချင်တယ်ဆိုရင်တော့ --map option နေရာကို 3 ထားပြီး run ရမှာဖြစ်ပါတယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/exp/chk-myint2htay-program/LSTMcoding_28july2021/data-map1$ python ./csv-str2mapping123.py --csvFile head.train.csv --map 3
id,senid1,senid2,sentence1,sentence2,is_duplicate
0,1,2,cydckclrk ccckrcyrr cck cckcyrr cud cydckclrk cylr crr cck s,cckcyrr cur ccckr cud cd cylr cd cu cydckclrk cyrr c clrr cck s,0
1,3,4,cck cyudrcrr cy cr,cck cyur cyudrcrr clr cr,1
2,5,6,cucyckr crrcdur cyudck cck,ccckr cyudck cur cucyckr clr,1
3,7,8,clrcrr cdckcd c cr cck,crrcy ccdcd c cr cck,0
4,9,10,cdr cud cdlr cudr cr ccckr cuckcckcrr cl cyu s,cdr cud cdlr cudr cr ccckr cckcdck cl cyu s,0
5,11,12,cr cudr cucdr c ccyudr cdl cu cud ccyrcc ccckccck cdrr cur cck s,cr cudr cucdr c ccyudr cdl cu cud ccyrcc ccck cdrr cur cck s,1
6,13,14,cr cud cck cck cudr cckrcrr cl cr cclrkcu cyck cl cck s,cr cud cck cur cudck cr cdck cck cudr cydckclrk cck cck s,0
7,15,16,clrcrr cck crr cckr cy cu cck,cclrccrr c cdck cur ccdcd cr,0
8,17,18,cclr cyrr cck cckcck ccckrc cuc I cducuck cud cducdcdr crr cck cy cck s,cclr cyrr cck cckcck ccckrc cuc I cducuck cud cudrcy crr cck cy cck s,1
```

input ဖိုင်ကို cat နဲ့ ရိုက်ထုတ်ပြီး pipe နဲ့ parse လုပ်တာမျိုးလည်း လုပ်လို့ ရပါတယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/exp/chk-myint2htay-program/LSTMcoding_28july2021/data-map1$ cat ./head.train.csv | python ./csv-str2mapping123.py --map 1
id,senid1,senid2,sentence1,sentence2,is_duplicate
0,1,2,ကynတar် သတinကyr ရin ကinဘyr ကiu ကynတar် ပyar ပr မe s,ကinဘyr ရe သတin ကiu သu ပyar မ ပe ကynတar် ကyr ရ တar တe s,0
1,3,4,စd ကyiuစr ကy ပr,စd ပyi ကyiuစr ပa ပr,1
2,5,6,သiကyin အrလun ကyiud တe,အရn ကyiud တe သiကyin လa,1
3,7,8,လaစr ဂunရu ရ ပr သi,အrကy အတuရu ရ ပr သi,0
4,9,10,သu ကiu တa ပiu inr အရn စidဝinစr နa ပyi s,သu ကiu တa ပiu inr အရn ရinကun နa ပyi s,0
5,11,12,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလiအပd သr ကe တe s,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလi သr ကe တe s,1
6,13,14,ဒr ကiu ဝe မe လiu စinစr နa တr အတar်ပe ပyစ် နa တe s,ဒr ကiu ဝe ကe လiud တr မn တe လiu ကynတar် ထin တe s,0
7,15,16,လaစr တe အr လi ကy မi တe,မလaမစr မ လud နe အတuရu ပr,0
8,17,18,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ပunတuကu ထr တd ကy သi s,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ကiuကy ထr တd ကy သi s,1
```

Command usage help screen က -h or --help နဲ့ ကြည့်လို့ ရပါတယ်။   

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/exp/chk-myint2htay-program/LSTMcoding_28july2021/data-map1$ python ./csv-str2mapping123.py --help
usage: csv-str2mapping123.py [-h] [-i [CSVFILE]] [-m MAP]

optional arguments:
  -h, --help            show this help message and exit
  -i [CSVFILE], --csvFile [CSVFILE]
  -m MAP, --map MAP     assign mapping type, 1 for Phonetic, 2 for Sound and 3
                        for Vowel Position
```

## 19. [str2mapping123.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/str2mapping123.py)  

အထက်က နံပါတ် ၁၈ ပရိုဂရမ်နဲ့ အခြေခံအားဖြင့်က အတူတူပါပဲ။ input ဖိုင်ကို CSV ဖိုင် မဟုတ်ပဲ text file နဲ့ သုံးလို့ရဖို့အတွက် ရေးပြထားတာပါ။  
သုံးပုံသုံးနည်းက အောက်ပါအတိုင်းပါ...  

ဥပမာ input ဖိုင်က...  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ cat input.txt 
စိန်မျောက်မျောက် ကာတွန်း ဖန်တီးသူ ကာတွန်းဦးမြေဇာ
လှိုင်းဘွဲ့နဲ့ ကော့ကရိတ်မြို့နယ်ကြားမှာ ရေကြီးပြီး လမ်းပြတ်သွား
```

Mapping 1 အဖြစ် ပြောင်းမယ်ဆိုရင်...  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2mapping123.py --inputFile ./input.txt --map 1
စinမyardမyard ကrတn ပnတiသu ကrတnuiမyaဇr
လiuinဘeနe ကarကရidမyiuနeကyrမr ရaကyiပyi လnပydသr
```

Mapping 2 အဖြစ် ပြောင်းမယ်ဆိုရင်...  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2mapping123.py --inputFile ./input.txt --map 2
စidပyardပyard ကrတd ပdတiသu ကrတduiပyaစr
လiudပeတe ကarကရidပyiuတeကyrပr ရaကyiပyi လdပydသr
```

Mapping 3 အဖြစ် ပြောင်းမယ်ဆိုရင်...  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2mapping123.py --inputFile ./input.txt --map 3
cuckcylrckcylrck crcdckr cckcurcd crcdckrIurcylcr
cdudckrcdurcur clrrccuckcyudrcckcyrrcdr clcyurcyur cckrcyckcdrr
```

help screen ကတော့ ပုံမှန် command line တွေရဲ့ help ကို ခေါ်ကြည့်သလိုပဲ "-h" or "--help" နဲ့ ကြည့်လို့ ရပါတယ်။  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2mapping123.py -h
usage: str2mapping123.py [-h] [-i [INPUTFILE]] [-m MAP]

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUTFILE], --inputFile [INPUTFILE]
  -m MAP, --map MAP     assign mapping type, 1 for Phonetic, 2 for Sound and 3
                        for Vowel Position
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ 
```

## 20. [str2my-edit-distances.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/str2my-edit-distances.py)  

str2my-edit-distance.py မှာတော့ mapping ပြောင်းပေးယုံသာမကပဲ အဲဒီပြောင်းထားတဲ့ mapping တွေနဲ့ edit distance အမျိုးမျိုးတွက်ကြည့်ဖို့အတွက် ရေးထားတာ ဖြစ်ပါတယ်။  

ဒီ Python code မှာက အသုံးပြုရတဲ့ option တွေက များပါတယ်။  
Help Screen ကိုခေါ်ပြီး အရင်ဆုံး ပေးရမယ့် option တွေကို နားလည်အောင် လေ့လာစေချင်ပါတယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --help
usage: str2my-edit-distances.py [-h] [-m MAP] [-d DISTANCE]
                                [-f FIELD_DELIMITER] [-s SKIP_HEADER]
                                [-o ORIGINAL_STRINGS]
                                [inputFile] string1_field string2_field

positional arguments:
  inputFile             input filename of the CSV file
  string1_field         field number of String1 in the CSV file, default=1
  string2_field         field number of String2 in the CSV file, default=2

optional arguments:
  -h, --help            show this help message and exit
  -m MAP, --map MAP     assign mapping type, "1" for Phonetic, "2" for Sound
                        and "3" for Vowel Position, "0" for skip mapping
                        process (e.g. when you calculate baseline edit
                        distance with raw Myanmar sentences, you can also use
                        --map 0 for English sentences)
  -d DISTANCE, --distance DISTANCE
                        assign distance measures: levenshtein,
                        damerau_levenshtein, hamming_distance, jaro_winkler,
                        cosine, jaccard
  -f FIELD_DELIMITER, --field_delimiter FIELD_DELIMITER
                        assign field delimiter such as $'\t' for <TAB>, ','
                        for comma, default=","
  -s SKIP_HEADER, --skip_header SKIP_HEADER
                        skip CSV header line or no distance calculation for
                        the first line. "1" for true and "0" for false,
                        default=1
  -o ORIGINAL_STRINGS, --original_strings ORIGINAL_STRINGS
                        printing original input string1 and string2, "1" for
                        true and "0" for false, default=1
        
```

ဒီ ပရိုဂရမ်မှာ ကို လက်တွေ့ စမ်း run ပြဖို့အတွက် ဥပမာအဖြစ် သုံးမယ့် CSV ဖိုင်က အောက်ပါအတိုင်းပါ။  
ကော်လံ သို့မဟုတ် field စုစုပေါင်း ခြောက်ခု ရှိပါတယ်။  
CSV ဖိုင်ရဲ့ feature တစ်ခုဖြစ်တဲ့ header line လည်း ပါပါတယ်။  
အဲဒီ ကော်လံ ခြောက်ခုထဲကနေမှ string similarity measure လုပ်ဖို့အတွက်က ဗမာစာ စာကြောင်းတွေ ပါတဲ့ field no. 4 နဲ့ no. 5 ကို သုံးမှာ ဖြစ်ပါတယ်။  

```
$ cat ./head.train.csv 
id,senid1,senid2,sentence1,sentence2,is_duplicate
0,1,2,ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။,ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။,0
1,3,4,ဆက် ကြိုးစား ကြ ပါ,ဆက် ပြီး ကြိုးစား ပေး ပါ,1
2,5,6,သီချင်း အားလုံး ကြိုက် တယ်,အရမ်း ကြိုက် တဲ့ သီချင်း လေး,1
3,7,8,လေးစား ဂုဏ်ယူ ရ ပါ သည်,အားကျ အတုယူ ရ ပါ သည်,0
4,9,10,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။,0
5,11,12,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။,1
6,13,14,ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။,ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။,0
7,15,16,လေးစား တယ် အား လည်း ကျ မိ တယ်,မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ,0
8,17,18,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။,1
```
   
Running usage ကို ဥပမာအနေနဲ့ အလွယ်ဆုံး ပြရရင် အောက်ပါအတိုင်းပါ။ ဒီနေရာမှာတော့  
- --map 1 ဆိုတာက mapping 1 အဖြစ် ပြောင်းဖို့ argument ပေးထားတာပါ။  
- --distance 'levenshtein' ကတော့ Levenshtein edit-distance ကို တွက်ပေးပါလို့ argument ပေးထားတာပါ။  
- ./head.train.csv ကတော့ input filename ကို argument ပေးထားတာပါ။  
- 4 ဆိုတာကတော့ ပထမဆုံး string ကို CSV ဖိုင်ထဲကနေ ကော်လံနံပါတ် ၄ နေရာကနေ ယူပါလို့ argument ပေးထားတာပါ။  
- 5 ဆိုတာကတော့ string similarity တွက်ဖို့အတွက် နှိုင်းယှဉ်ဖို့ စာကြောင်း နှစ်ကြောင်းလိုတာမို့ ဒုတိယ စာကြောင်းကိုတော့ ကော်လံနံပါတ် ၅ နေရာကနေ ယူပါလို့ option ပေးထားတာ ဖြစ်ပါတယ်။  

အဲဒီ option တွေကို သုံးပြီး run ရင် အောက်ပါအတိုင်း output ပေးပါလိမ့်မယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --map 1 --distance 'levenshtein' ./head.train.csv 4 5
ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။,ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။,27
ဆက် ကြိုးစား ကြ ပါ,ဆက် ပြီး ကြိုးစား ပေး ပါ,6
သီချင်း အားလုံး ကြိုက် တယ်,အရမ်း ကြိုက် တဲ့ သီချင်း လေး,16
လေးစား ဂုဏ်ယူ ရ ပါ သည်,အားကျ အတုယူ ရ ပါ သည်,7
သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။,6
ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။,3
ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။,ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။,23
လေးစား တယ် အား လည်း ကျ မိ တယ်,မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ,16
ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။,5
```

Mapping 1, 2, 3 က help screen မှာ ရှင်းပြထားတဲ့အတိုင်းပါပဲ။ Mapping 1 က Phonetic နဲ့ ဆိုင်ပါတယ်။ Mapping 2 ကတော့ Sound (ဗမာသံတွေကို ထွက်ရတဲ့အပိုင်း) နဲ့ ဆိုင်ပါတယ်။ Mapping 3 ကတော့ Vowel Position (ဗမာဗျည်း နဲ့ သရတွေကို တွဲပေးရတဲ့ ပုံစံ) ကို အခြေခံထားတာ ဖြစ်ပါတယ်။ အသေးစိတ်ကတော့ published လုပ်ထားတဲ့ စာတမ်းနှစ်စောင်ကို ဝင်ဖတ်ပါလို့ အကြံပေးချင်ပါတယ်။  

ဒီတစ်ခါတော့ Mapping 2 နဲ့ ပြောင်းပြီးမှ edit distance ကို တွက်ချင်တာမို့ --map 2 ဆိုတဲ့ option ပေးပြီး run ပြထားတာ ဖြစ်ပါတယ်။   
အထက်မှာ တွက်ပြထားတဲ့ --map 1 ရဲ့ levenshtein distance value တွေနဲ့ မတူတဲ့ စာကြောင်းတွေပါလာတာကို တွေ့ရပါလိမ့်မယ်။   

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --map 2 --distance 'levenshtein' ./head.train.csv 4 5
ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။,ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။,25
ဆက် ကြိုးစား ကြ ပါ,ဆက် ပြီး ကြိုးစား ပေး ပါ,6
သီချင်း အားလုံး ကြိုက် တယ်,အရမ်း ကြိုက် တဲ့ သီချင်း လေး,14
လေးစား ဂုဏ်ယူ ရ ပါ သည်,အားကျ အတုယူ ရ ပါ သည်,6
သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။,6
ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။,3
ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။,ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။,20
လေးစား တယ် အား လည်း ကျ မိ တယ်,မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ,15
ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။,5
```

ဒီတစ်ခါတော့ --map 3 ဆိုတဲ့ option နဲ့ run ကြည့်ပြီး ထွက်လာတဲ့ levenshtein distance value တွေကို လေ့လာကြည့်ရအောင်...  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --map 3 --distance 'levenshtein' ./head.train.csv 4 5
ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။,ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။,23
ဆက် ကြိုးစား ကြ ပါ,ဆက် ပြီး ကြိုးစား ပေး ပါ,7
သီချင်း အားလုံး ကြိုက် တယ်,အရမ်း ကြိုက် တဲ့ သီချင်း လေး,14
လေးစား ဂုဏ်ယူ ရ ပါ သည်,အားကျ အတုယူ ရ ပါ သည်,5
သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။,5
ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။,4
ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။,ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။,22
လေးစား တယ် အား လည်း ကျ မိ တယ်,မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ,14
ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။,5
```

ဒီတစ်ခေါက်မှာတော့ --distance 'cosine' ဆိုတဲ့ option ပေးပြီးတော့ Mapping 3 နဲ့ ပြောင်းထားတဲ့ string နှစ်ကြောင်းကို Cosine distance တွက်ခိုင်းကြည့်ရအောင်...  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --map 3 --distance 'cosine' ./head.train.csv 4 5
ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။,ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။,0.5345224838248488
ဆက် ကြိုးစား ကြ ပါ,ဆက် ပြီး ကြိုးစား ပေး ပါ,0.6708203932499369
သီချင်း အားလုံး ကြိုက် တယ်,အရမ်း ကြိုက် တဲ့ သီချင်း လေး,0.4472135954999579
လေးစား ဂုဏ်ယူ ရ ပါ သည်,အားကျ အတုယူ ရ ပါ သည်,0.5999999999999999
သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။,သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။,0.8999999999999998
ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။,ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။,0.9285714285714286
ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။,ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။,0.7624437362098716
လေးစား တယ် အား လည်း ကျ မိ တယ်,မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ,0.0
ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။,ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။,0.9523809523809523
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$
```

အထက်ပါ run ပြခဲ့တာတွေက --field_delimiter (field သို့မဟုတ် column တွေကို ဘာ စာလုံးနဲ့ ခြားထားတာလဲ ဆိုတာကို သတ်မှတ်ပေးတာ) နဲ့ --skip_header (input file ထဲက ပထမဆုံးစာကြောင်း ကို skip လုပ်သွားမှာလား သို့မဟုတ် edit distance တွက်ခိုင်းမှာလား ဆိုတာကို သတ်မှတ်ပေးတာ) option တွေကို မပေးပဲ ထားခဲ့ပါတယ်။ အဲဒီ option နှစ်ခုကို မပေးပဲ ထားရင် ပရိုဂရမ်က default value တွေနဲ့ပဲထားပြီး run ပေးသွားမှာ ဖြစ်ပါတယ်။ Help screen မှာလည်း မြင်ရတဲ့ အတိုင်းပါပဲ။ သူတို့ရဲ့ default option တွေက --field_delimiter အတွက်က ',' ဖြစ်ပြီးတော့ --skip_header အတွက်ကတော့ 1 ဖြစ်ပါတယ်။ အဲဒါကြောင့် Python code ကို run တဲ့အခါမှာ field တွေကို ဖြတ်ထုတ်ယူတဲ့အချိန်မှာ ကော်မာနဲ့ပဲ ဖြတ်ယူပြီး၊ ပထမဆုံး header line ကို edit distance မတွက်ပဲနဲ့ skip လုပ်သွားပေးမှာ ဖြစ်ပါတယ်။  

တကယ်က အဲဒီ option နှစ်ခုကို default setting အနေနဲ့ပဲ ထည့်သုံးပြီး run ပြရရင် အောက်ပါအတိုင်း command ပေးသွားရမှာ ဖြစ်ပါတယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --field_delimiter ',' --skip_header 1 --map 1 --distance 'levenshtein' --original_strings 0 ./head.train.csv 4 5
ကynတar် သတinကyr ရin ကinဘyr ကiu ကynတar် ပyar ပr မe s,ကinဘyr ရe သတin ကiu သu ပyar မ ပe ကynတar် ကyr ရ တar တe s,27
စd ကyiuစr ကy ပr,စd ပyi ကyiuစr ပa ပr,6
သiကyin အrလun ကyiud တe,အရn ကyiud တe သiကyin လa,16
လaစr ဂunရu ရ ပr သi,အrကy အတuရu ရ ပr သi,7
သu ကiu တa ပiu inr အရn စidဝinစr နa ပyi s,သu ကiu တa ပiu inr အရn ရinကun နa ပyi s,6
inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလiအပd သr ကe တe s,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလi သr ကe တe s,3
ဒr ကiu ဝe မe လiu စinစr နa တr အတar်ပe ပyစ် နa တe s,ဒr ကiu ဝe ကe လiud တr မn တe လiu ကynတar် ထin တe s,23
လaစr တe အr လi ကy မi တe,မလaမစr မ လud နe အတuရu ပr,16
ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ပunတuကu ထr တd ကy သi s,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ကiuကy ထr တd ကy သi s,5
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ 
```

--field_delimiter နဲ့ --skip_header ဆိုတဲ့ option နှစ်ခုက ကိုယ် input လုပ်မယ့် ဖိုင်အပေါ်ကို မူတည်ပြီးတော့ အပြောင်းအလဲ လုပ်ပေးရမှာမို့ အရေးကြီးတဲ့ option နှစ်ခု ဖြစ်ပါတယ်။  
ဥပမာ အထက်မှာ သုံးပြခဲ့တဲ့ ./head.train.csv ဖိုင်ကိုပဲ --skip_header 0 ထားမိပြီးတော့ ပရိုဂရမ်ကို run မယ်ဆိုရင် header line (sentence1,sentence2) ကိုလည်း setting လုပ်ထားတဲ့ --map 1 နဲ့ ပြောင်းချပြီးတော့ levenshtein တွက်သွားမှာ ဖြစ်တဲ့အတွက် output က အောက်ပါအတိုင်း ရလာမှာ ဖြစ်ပါတယ်။ ဂရုပြုမိမယ်လို့ ထင်ပါတယ်။ output ရဲ့ ထိပ်ဆုံးမှာ LLLLLLLL1,LLLLLLLL2,1 ဆိုတဲ့ စာကြောင်းက ပါနေတာကို...  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --field_delimiter ',' --skip_header 0 --map 1 --distance 'levenshtein' --original_strings 0 ./head.train.csv 4 5
LLLLLLLL1,LLLLLLLL2,1
ကynတar် သတinကyr ရin ကinဘyr ကiu ကynတar် ပyar ပr မe s,ကinဘyr ရe သတin ကiu သu ပyar မ ပe ကynတar် ကyr ရ တar တe s,27
စd ကyiuစr ကy ပr,စd ပyi ကyiuစr ပa ပr,6
သiကyin အrလun ကyiud တe,အရn ကyiud တe သiကyin လa,16
လaစr ဂunရu ရ ပr သi,အrကy အတuရu ရ ပr သi,7
သu ကiu တa ပiu inr အရn စidဝinစr နa ပyi s,သu ကiu တa ပiu inr အရn ရinကun နa ပyi s,6
inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလiအပd သr ကe တe s,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလi သr ကe တe s,3
ဒr ကiu ဝe မe လiu စinစr နa တr အတar်ပe ပyစ် နa တe s,ဒr ကiu ဝe ကe လiud တr မn တe လiu ကynတar် ထin တe s,23
လaစr တe အr လi ကy မi တe,မလaမစr မ လud နe အတuရu ပr,16
ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ပunတuကu ထr တd ကy သi s,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ကiuကy ထr တd ကy သi s,5
```

ဒီ str2my-edit-distance ပရိုဂရမ်က comma နဲ့ ခြားထားတဲ့ CSV ဖိုင်နဲ့ပဲ run လို့ ရတာမဟုတ်ပါဘူး။  
NLP field မှာ အသုံးများတဲ့ ```\<TAB\>``` နဲ့ ခြားထားတာတို့ တခြား character တွေနဲ့ ခြားထားတဲ့ input file တွေနဲ့လည်း အသုံးပြုလို့ ရအောင် ရည်ရွယ်ပြီး ရေးထားပါတယ်။   
ပြီးတော့ field ကလည်း ဘယ်နှစ်ခု ပါရမယ် ဆိုတာမျိုး သတ်မှတ်ထားတာ မဟုတ်ပါဘူး။ အနည်းဆုံးတော့ string similarity တွက်ဖို့အတွက် ကော်လံနှစ်ခုကတော့ လိုအပ်ပေမဲ့ ကော်လံနှစ်ခုနဲ့ အထက် variation အမျိုးမျိုး ဖြစ်တာကို လက်ခံပေးနိုင်ပါတယ်။  
ဥပမာ practical running အနေနဲ့ ဒီတစ်ခေါက် သုံးမယ့် input file က အောက်ပါအတိုင်း field နှစ်ခုပဲ ပါဝင်ပြီးတော့ အဲဒီ field or column နှစ်ခုကိုလည်း ```\<TAB\>``` ကီးရိုက်ပြီး ခြားထားတယ်လို့ ဆိုကြပါစို့...  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ cat f4-5.tab.txt 
ကျွန်တော် သတင်းကြား ရင် ခင်ဗျား ကို ကျွန်တော် ပြော ပါ့ မယ် ။	ခင်ဗျား ရဲ့ သတင်း ကို သူ ပြော မှ ပဲ ကျွန်တော် ကြား ရ တော့ တယ် ။
ဆက် ကြိုးစား ကြ ပါ	ဆက် ပြီး ကြိုးစား ပေး ပါ
သီချင်း အားလုံး ကြိုက် တယ်	အရမ်း ကြိုက် တဲ့ သီချင်း လေး
လေးစား ဂုဏ်ယူ ရ ပါ သည်	အားကျ အတုယူ ရ ပါ သည်
သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း စိတ်ဝင်စား နေ ပြီ ။	သူ့ ကို တွေ့ ဖို့ ငါ အရမ်း ရင်ခုန် နေ ပြီ ။
ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည်အပတ် သွား ခဲ့ တယ် ။	ငါ တို့ ပဲခူး က အမျိုး တွေ ဆီ ကို မကြာခဏ အလည် သွား ခဲ့ တယ် ။
ဒါ ကို ဝယ် မယ် လို့ စဉ်းစား နေ တာ အတော်ပဲ ဖြစ် နေ တယ် ။	ဒါ ကို ဝယ် ခဲ့ လိုက် တာ မှန် တယ် လို့ ကျွန်တော် ထင် တယ် ။
လေးစား တယ် အား လည်း ကျ မိ တယ်	မလေးမစား မ လုပ် နဲ့ အတုယူ ပါ
ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ပုံတူကူး ထား တတ် ကြ သည် ။	ကလေး များ သည် ငယ်ငယ် ကတည်းက မိဘ ၏ ပုံရိပ် ကို ခိုးချ ထား တတ် ကြ သည် ။
```

အထက်ပါ input ဖိုင်နဲ့ --map 1 ပြောင်းပြီးတော့ Levenshtein distance တွက်ကြည့်ရင် အောက်ပါအတိုင်း output ရလာပါလိမ့်မယ်။  
တစ်ခု သတိထားစေချင်တာက Python ပရိုဂရမ်တွေကို ```\<TAB\>``` ကီးကို command line argument ပေးတဲ့အခါမှာ ပုံမှန် string ပေးတဲ့ ပုံစံမျိုးဖြစ်တဲ့ single quote, double quote ပိတ်ထားတဲ့ ပုံစံအထဲမှာ \t ကို ရိုက်ထည့်ရုံတင်နဲ့ မရပဲ $ sign ကို ရှေ့မှာ ခံပေးရပါတယ်။ အဲဒါကြောင့် --field_delimiter $'\t' သို့မဟုတ် --field_delimiter $"\t" ဆိုတဲ့ ပုံစံမျိုးနဲ့ အသုံးပြုရပါလိမ့်မယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/Transcend/paper/next-paper/ksw/exp/paper/chk4myint2htay/str2map$ python ./str2my-edit-distances.py --field_delimiter $'\t' --skip_header 0 --map 1 --distance 'levenshtein' --original_strings 0 ./f4-5.tab.txt 1 2
ကynတar် သတinကyr ရin ကinဘyr ကiu ကynတar် ပyar ပr မe s,ကinဘyr ရe သတin ကiu သu ပyar မ ပe ကynတar် ကyr ရ တar တe s,27
စd ကyiuစr ကy ပr,စd ပyi ကyiuစr ပa ပr,6
သiကyin အrလun ကyiud တe,အရn ကyiud တe သiကyin လa,16
လaစr ဂunရu ရ ပr သi,အrကy အတuရu ရ ပr သi,7
သu ကiu တa ပiu inr အရn စidဝinစr နa ပyi s,သu ကiu တa ပiu inr အရn ရinကun နa ပyi s,6
inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလiအပd သr ကe တe s,inr တiu ပeကu က အမyiu တa စi ကiu မကyrကန အလi သr ကe တe s,3
ဒr ကiu ဝe မe လiu စinစr နa တr အတar်ပe ပyစ် နa တe s,ဒr ကiu ဝe ကe လiud တr မn တe လiu ကynတar် ထin တe s,23
လaစr တe အr လi ကy မi တe,မလaမစr မ လud နe အတuရu ပr,16
ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ပunတuကu ထr တd ကy သi s,ကလa မyr သi ineine ကတiက မiဘ i ပunရid ကiu ကiuကy ထr တd ကy သi s,5
```
        
## 21. [mypos2upos.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mypos2upos.py)  

[myPOS](https://github.com/ye-kyaw-thu/myPOS) မှာ သုံးထားတဲ့ tag set ကို [Universal POS tag set](http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf) အဖြစ် ပြောင်းဖို့အတွက် စမ်းရေးထားခဲ့တဲ့ ပရိုဂရမ်ပါ။ နောက်ပိုင်းမှာ လက်ရှိ Mapping ကို အပြောင်းအလဲ လုပ်တာမျိုးလည်း ဖြစ်ကောင်းဖြစ်နိုင်ပါတယ်။  

# Convertion of myPOS to Universal POS

Testing Note ...  
Mapping က အပြောင်းအလဲ ရှိနိုင်တယ်။ စမ်းပြီး conversion လုပ်ကြည့်ထားတာကို မှတ်သားထားခဲ့တဲ့ note ပါ။  
လက်ရှိ mypos2upos.py ပရိုဂရမ်ထဲမှာ သုံးထားတဲ့ mypos to universal POS က အောက်ပါအတိုင်းပါ။  

```
#abb	X
#adj	ADJ
#adv	ADV
#conj	CONJ
#fw	X
#int	INTJ
#n	NOUN
#num	NUM
#part	PRT
#ppm	ADP
#pron	PRON
#punc	.
#sb	.
#tn	NUM
#v	VERB
```

Note: # တကယ်တမ်းက #int INTJ ကို #int X အဖြစ် ပြောင်းသင့်တယ်။   

## Head of myPOS corpus (version 3.0)

test conversion အတွက် ပြင်ထားတဲ့ ဖိုင်ပါ။ myPOS (version 3.0) ကနေ ထိပ်ဆုံးစာကြောင်း ၁၀ကြောင်းကို head လုပ်ထားတဲ့ ဖိုင်ပါ။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ cat ./head.mypos.txt 
ဒီ/adj ဆေး/n က/ppm ၁၀၀/num ရာခိုင်နှုန်း/n ဆေးဘက်ဝင်/adj အပင်/n များ/part မှ/ppm ဖော်စပ်/v ထား/part တာ/part ဖြစ်/v တယ်/ppm ။/punc
အသစ်/n ဝယ်/v ထား/part တဲ့/part ဆွယ်တာ/n က/ppm အသီး/n ထ/v နေ/part ပါ/part ပေါ့/part ။/punc
မ/part ကျန်းမာ/v လျှင်/conj နတ်/n|ဆရာ/n ထံ/ppm မေးမြန်း/v ၍/conj သက်ဆိုင်ရာ/n နတ်/n တို့/part အား/ppm ပူဇော်ပသ/v ရ/part သည်/ppm ။/punc
ပေဟိုင်/n|ဥယျာဉ်/n ။/punc
နဝမ/adj အိပ်မက်/n ကောသလ/n|မင်း/n|အိပ်မက်/n ၉/num နက်ရှိုင်း/adj ကျယ်ဝန်း/adj သော/part ရေကန်/n ကြီး/adj တစ်/tn ခု/part တွင်/ppm သတ္တဝါ/n တို့/part ဆင်း/v ၍/conj ရေသောက်/v ကြ/part ၏/ppm ။/punc
အပြင်ပန်း/n ကြည့်/v ရင်/conj ခက်/adj သလို/part ထင်/v ရ/part ပေမယ့်/conj တကယ့်/adj လက်တွေ့/n အခြေအနေ/n က/ppm တော့/part အဲဒီ/pron လို/ppm မ/part ဟုတ်/v ပါ/part ဘူး/part ။/punc
8/fw bit/fw ပုံရိပ်/n တစ်/tn ခု/part သည်/ppm 256/fw color/fw သို့မဟုတ်/conj gray/fw scale/fw များ/part ကို/ppm အထောက်အကူ/n ပြု/v သည်/ppm ။/punc
ကိုရီးယား/n ဝတ်စုံ/n မှာ/ppm ပန်း/n ဒီဇိုင်း/n နဲ့/conj အဝါရောင်/n က/ppm လိုက်ဖက်/v လိမ့်/part မယ်/part ထင်/v တယ်/ppm ။/punc
သို့နှင့်/conj မဂ္ဂဇင်း/n မှ/ppm တစ်ဆင့်/adv သတင်းစာ/n ကို/ppm ပါ/part တိုးချဲ့/v လိုက်/part သောအခါ/conj တွင်/ppm ဘက်ပတစ်/n|ကျောင်း/n သို့/ppm မ/part ပြန်/v တော့/part ဘဲ/part ထို/adj မဂ္ဂဇင်း/n ၊/punc သတင်းစာ/n နှစ်/tn ခု/part စလုံး/part တွင်/ppm ပင်/part တည်းဖြတ်/v သည့်/part ဘက်/n မှ/ppm ဆက်လက်/adv လုပ်ကိုင်/v လေ/part တော့/part သည်/ppm ။/punc
တစ်/tn ကျပ်သား/n ။/punc
```

## Converting myPOS (version 3) to Universal POS

ပထမဆုံး myPOS corpus တစ်ခုလုံး မဟုတ်ပဲနဲ့ ၁၀ကြောင်းလောက်ကိုပဲ စမ်းပြောင်း ကြည့်ရအောင်ပါ...   

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ python ./mypos2upos.py ./head.mypos.txt 
ဒီ/ADJ ဆေး/NOUN က/ADP ၁၀၀/NUM ရာခိုင်နှုန်း/NOUN ဆေးဘက်ဝင်/ADJ အပင်/NOUN များ/PRT မှ/ADP ဖော်စပ်/VERB ထား/PRT တာ/PRT ဖြစ်/VERB တယ်/ADP ။/.
အသစ်/NOUN ဝယ်/VERB ထား/PRT တဲ့/PRT ဆွယ်တာ/NOUN က/ADP အသီး/NOUN ထ/VERB နေ/PRT ပါ/PRT ပေါ့/PRT ။/.
မ/PRT ကျန်းမာ/VERB လျှင်/CONJ နတ်/NOUN|ဆရာ/NOUN ထံ/ADP မေးမြန်း/VERB ၍/CONJ သက်ဆိုင်ရာ/NOUN နတ်/NOUN တို့/PRT အား/ADP ပူဇော်ပသ/VERB ရ/PRT သည်/ADP ။/.
ပေဟိုင်/NOUN|ဥယျာဉ်/NOUN ။/.
နဝမ/ADJ အိပ်မက်/NOUN ကောသလ/NOUN|မင်း/NOUN|အိပ်မက်/NOUN ၉/NUM နက်ရှိုင်း/ADJ ကျယ်ဝန်း/ADJ သော/PRT ရေကန်/NOUN ကြီး/ADJ တစ်/NUM ခု/PRT တွင်/ADP သတ္တဝါ/NOUN တို့/PRT ဆင်း/VERB ၍/CONJ ရေသောက်/VERB ကြ/PRT ၏/ADP ။/.
အပြင်ပန်း/NOUN ကြည့်/VERB ရင်/CONJ ခက်/ADJ သလို/PRT ထင်/VERB ရ/PRT ပေမယ့်/CONJ တကယ့်/ADJ လက်တွေ့/NOUN အခြေအနေ/NOUN က/ADP တော့/PRT အဲဒီ/PRON လို/ADP မ/PRT ဟုတ်/VERB ပါ/PRT ဘူး/PRT ။/.
8/X bit/X ပုံရိပ်/NOUN တစ်/NUM ခု/PRT သည်/ADP 256/X color/X သို့မဟုတ်/CONJ gray/X scale/X များ/PRT ကို/ADP အထောက်အကူ/NOUN ပြု/VERB သည်/ADP ။/.
ကိုရီးယား/NOUN ဝတ်စုံ/NOUN မှာ/ADP ပန်း/NOUN ဒီဇိုင်း/NOUN နဲ့/CONJ အဝါရောင်/NOUN က/ADP လိုက်ဖက်/VERB လိမ့်/PRT မယ်/PRT ထင်/VERB တယ်/ADP ။/.
သို့နှင့်/CONJ မဂ္ဂဇင်း/NOUN မှ/ADP တစ်ဆင့်/ADV သတင်းစာ/NOUN ကို/ADP ပါ/PRT တိုးချဲ့/VERB လိုက်/PRT သောအခါ/CONJ တွင်/ADP ဘက်ပတစ်/NOUN|ကျောင်း/NOUN သို့/ADP မ/PRT ပြန်/VERB တော့/PRT ဘဲ/PRT ထို/ADJ မဂ္ဂဇင်း/NOUN ၊/. သတင်းစာ/NOUN နှစ်/NUM ခု/PRT စလုံး/PRT တွင်/ADP ပင်/PRT တည်းဖြတ်/VERB သည့်/PRT ဘက်/NOUN မှ/ADP ဆက်လက်/ADV လုပ်ကိုင်/VERB လေ/PRT တော့/PRT သည်/ADP ။/.
တစ်/NUM ကျပ်သား/NOUN ။/.
```

## Through Piping

input file ကို cat နဲ့ ရိုက်ထုတ်ပြီး pipe ကတဆင့်လည်း parse လုပ်လို့ ရပါတယ်။  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ cat ./head.mypos.txt | python ./mypos2upos.py 
ဒီ/ADJ ဆေး/NOUN က/ADP ၁၀၀/NUM ရာခိုင်နှုန်း/NOUN ဆေးဘက်ဝင်/ADJ အပင်/NOUN များ/PRT မှ/ADP ဖော်စပ်/VERB ထား/PRT တာ/PRT ဖြစ်/VERB တယ်/ADP ။/.
အသစ်/NOUN ဝယ်/VERB ထား/PRT တဲ့/PRT ဆွယ်တာ/NOUN က/ADP အသီး/NOUN ထ/VERB နေ/PRT ပါ/PRT ပေါ့/PRT ။/.
မ/PRT ကျန်းမာ/VERB လျှင်/CONJ နတ်/NOUN|ဆရာ/NOUN ထံ/ADP မေးမြန်း/VERB ၍/CONJ သက်ဆိုင်ရာ/NOUN နတ်/NOUN တို့/PRT အား/ADP ပူဇော်ပသ/VERB ရ/PRT သည်/ADP ။/.
ပေဟိုင်/NOUN|ဥယျာဉ်/NOUN ။/.
နဝမ/ADJ အိပ်မက်/NOUN ကောသလ/NOUN|မင်း/NOUN|အိပ်မက်/NOUN ၉/NUM နက်ရှိုင်း/ADJ ကျယ်ဝန်း/ADJ သော/PRT ရေကန်/NOUN ကြီး/ADJ တစ်/NUM ခု/PRT တွင်/ADP သတ္တဝါ/NOUN တို့/PRT ဆင်း/VERB ၍/CONJ ရေသောက်/VERB ကြ/PRT ၏/ADP ။/.
အပြင်ပန်း/NOUN ကြည့်/VERB ရင်/CONJ ခက်/ADJ သလို/PRT ထင်/VERB ရ/PRT ပေမယ့်/CONJ တကယ့်/ADJ လက်တွေ့/NOUN အခြေအနေ/NOUN က/ADP တော့/PRT အဲဒီ/PRON လို/ADP မ/PRT ဟုတ်/VERB ပါ/PRT ဘူး/PRT ။/.
8/X bit/X ပုံရိပ်/NOUN တစ်/NUM ခု/PRT သည်/ADP 256/X color/X သို့မဟုတ်/CONJ gray/X scale/X များ/PRT ကို/ADP အထောက်အကူ/NOUN ပြု/VERB သည်/ADP ။/.
ကိုရီးယား/NOUN ဝတ်စုံ/NOUN မှာ/ADP ပန်း/NOUN ဒီဇိုင်း/NOUN နဲ့/CONJ အဝါရောင်/NOUN က/ADP လိုက်ဖက်/VERB လိမ့်/PRT မယ်/PRT ထင်/VERB တယ်/ADP ။/.
သို့နှင့်/CONJ မဂ္ဂဇင်း/NOUN မှ/ADP တစ်ဆင့်/ADV သတင်းစာ/NOUN ကို/ADP ပါ/PRT တိုးချဲ့/VERB လိုက်/PRT သောအခါ/CONJ တွင်/ADP ဘက်ပတစ်/NOUN|ကျောင်း/NOUN သို့/ADP မ/PRT ပြန်/VERB တော့/PRT ဘဲ/PRT ထို/ADJ မဂ္ဂဇင်း/NOUN ၊/. သတင်းစာ/NOUN နှစ်/NUM ခု/PRT စလုံး/PRT တွင်/ADP ပင်/PRT တည်းဖြတ်/VERB သည့်/PRT ဘက်/NOUN မှ/ADP ဆက်လက်/ADV လုပ်ကိုင်/VERB လေ/PRT တော့/PRT သည်/ADP ။/.
တစ်/NUM ကျပ်သား/NOUN ။/.
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$
```

## Converting the Whole myPOS Corpus

myPOS (version 3.0) corpus တစ်ခုလုံးကို conversion လုပ်ကြည့်ပြီး wc command သုံးပြီး word count လုပ်ကြည့်တာပါ။  
Error ဘာညာ ရှိနိုင်သလားလို့...  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ cat ./mypos-ver.3.0.txt | python ./mypos2upos.py > ./mypos-ver.3.0.upos.txt 
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ wc ./mypos-ver.3.0.txt 
  43196  537232 9581543 ./mypos-ver.3.0.txt
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ wc ./mypos-ver.3.0.upos.txt 
  43196  537232 9907159 ./mypos-ver.3.0.upos.txt
```

Conversion လုပ်ပြီး ထွက်လာတဲ့ output ဖိုင်ကို shuffle လုပ်လိုက်ပြီး မျက်လုံးနဲ့ စစ်ဆေးကြည့်ထားတာပါ။  
Shuffle လုပ်ပြီးတော့ ထိပ်ဆုံးက ၁၀ကြောင်းကို print ထုတ်ကြည့်ရအောင်...  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ shuf ./mypos-ver.3.0.upos.txt | head
ရှေး/ADJ ခေတ်/NOUN နိုင်ငံ/NOUN များ/PRT ဖြစ်/VERB သော/PRT ဗက်ဗီလုံးနီးယား/NOUN ၊/. ပယ်လက်စတိုင်/NOUN နှင့်/CONJ ဂရိ/NOUN တို့/PRT တွင်/ADP တွေ့/VERB ရှိ/PRT ရ/PRT သော/PRT မြင်း/NOUN များ/PRT မှာ/ADP အမြင်/NOUN အားဖြင့်/ADP ထွားကျိုင်း/ADJ ၍/CONJ အာရပ်/NOUN|မြင်း/NOUN ကဲ့သို့/PRT ကြော့ကြော့ရှင်းရှင်း/ADJ မ/PRT ရှိ/VERB ကြ/PRT ချေ/PRT ။/.
အကြောင်းရင်း/NOUN မှာ/ADP အခြား/ADJ သော/PRT Hardware/X ရောင်းချ/VERB|သူ/NOUN များ/PRT မှ/ADP IBM/X ၏/ADP System/X ကို/ADP အတု/NOUN ပြုလုပ်/VERB ကြ/PRT မည်/ADP ကို/ADP စိုးရိမ်/VERB ၍/CONJ ဖြစ်/VERB သည်/ADP ။/.
အဲဒီ/PRON အိမ်သာ/NOUN က/ADP ပျက်/VERB နေ/PRT လား/PRT မ/PRT သိ/VERB ဘူး/PRT ။/.
အကြောင်းမဲ့/ADV လူ/NOUN ကို/ADP မုန်းတီး/VERB နေ/PRT တယ်/ADP ။/.
မ/PRT ဟုတ်/VERB ဘူး/PRT ၊/. ကျွန်တော့်/PRON အိမ်/NOUN က/ADP တခြား/NOUN မြို့/NOUN မှာ/ADP ။/.
ဒီ/ADJ နေရာ/NOUN ကို/ADP စိတ်ဝင်စား/VERB ရ/PRT တဲ့/PRT အကြောင်း/NOUN က/ADP ဘာ/PRON လဲ/PRT ။/.
ဖန်သားပြင်/NOUN Screen/X ပေါ်/NOUN တွင်/ADP ပုံရိပ်/NOUN များ/PRT ကို/ADP ရေးခြယ်/VERB ရန်/CONJ အသုံးပြု/VERB သည့်/PRT Program/X များ/PRT တွင်/ADP Pixel/X များ/PRT ကို/ADP အဖွင့်/NOUN အပိတ်/NOUN လုပ်/VERB ပေး/PRT ရ/PRT သည်/ADP ။/.
ဂရုမစိုက်/VERB လို့/PRT မ/PRT ဖြစ်/VERB ဘူး/PRT လေ/PRT ။/. ကျန်းမာရေး/NOUN က/ADP အရေးကြီး/VERB တယ်/ADP ။/. ကျန်းမာ/VERB တယ်/ADP ဆို/VERB ရင်/CONJ စည်းစိမ်/NOUN ချမ်းသာ/VERB ရ/PRT တာ/PRT နဲ့/ADP အတူတူ/ADV ပဲ/PRT ပေါ့/PRT ။/. နေမကောင်း/VERB လို့/PRT ဆရာဝန်/NOUN ကို/ADP ပေး/VERB ရ/PRT မယ့်/ADP ဆေးကုခ/NOUN|ငွေ/NOUN မ/PRT ကုန်/VERB တာ/PRT ပေါ့/PRT ။/.
ဟင့်အင်း/PRT ။/. အဲဒါ/PRON က/ADP တိုက်ရိုက်/ADJ ရထား/NOUN ။/.
ဟင်းသီးဟင်းရွက်/NOUN တွေ/PRT ကို/ADP ဆေးကြော/VERB ပြီး/CONJ တော့/PRT ရေခဲသေတ္တာ/NOUN ထဲ/ADP ထည့်/VERB ထား/PRT ပါ/PRT ။/.
```

shuffle လုပ်ပြီး နောက်ဆုံးမှာ ရှိတဲ့စာကြောင်း ၁၀ကြောင်းကို ကြည့်ကြည့်ရအောင်...  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ shuf ./mypos-ver.3.0.upos.txt | tail
အနီးဆုံး/ADJ စာတိုက်/NOUN ဘယ်/PRON မှာ/ADP ရှိ/VERB ပါ/PRT သလဲ/PRT ။/.
ခင်ဗျား/PRON လမ်း/NOUN ၃၀/NUM မှာ/ADP ဆင်း/VERB ပါ/PRT ။/.
ကျွန်တော့်/PRON ကိုယ်စား/ADV သူ့/PRON ကို/ADP နှုတ်ဆက်/VERB ပါ/PRT တယ်/ADP ။/.
နံနက်စာ/NOUN အပြင်/CONJ တခြား/ADJ ဘာ/PRON လို/VERB သေး/PRT လဲ/PRT ။/.
ကြက်ဥ/NOUN ခေါက်ဆွဲ/NOUN
မူလတန်း/NOUN နှင့်/CONJ အလယ်တန်း/NOUN|ကျောင်း/NOUN များ/PRT လည်း/PRT ရှိ/VERB ၏/ADP ။/.
ခရီးဆောင်/ADJ လက်ဆွဲသေတ္တာ/NOUN အကြီး/NOUN နဲ့/CONJ အရောင်/NOUN က/ADP အစိမ်း/NOUN|ရောင်/NOUN ဖြစ်/VERB ပါ/PRT တယ်/ADP ။/.
MS/X DOS/X ၏/ADP ရောင်းအား/NOUN သည်/ADP မိုက်ခရိုဆော့ဖ်/NOUN ကို/ADP ဆော့ဖ်ဝဲ/NOUN ထုတ်လုပ်/VERB|မှု/PRT များ/PRT ၏/ADP အဓိက/NOUN ကစားသမား/NOUN နေရာ/NOUN ရောက်/VERB အောင်/CONJ ပို့ဆောင်/VERB ပေး/PRT နိုင်/PRT ခဲ့/PRT သည်/ADP ။/.
တစ်/NUM ယောက်/PRT ယောက်/PRT က/ADP မီးသတ်ဗူး/NOUN ကို/ADP ဘယ်လို/ADV သုံး/VERB ရ/PRT တယ်/ADP ဆို/VERB တာ/PRT သိ/VERB လား/PRT ။/.
ဤ/ADJ တစ်/NUM ကြိမ်/PRT တွင်/ADP အင်္ဂလိပ်/NOUN တို့/PRT သည်/ADP ကျန်/VERB ရှိ/PRT နေ/PRT သေး/PRT သည့်/PRT ကမ်းရိုးတန်း/NOUN|ဒေသ/NOUN များ/PRT ဖြစ်/VERB သည့်/PRT ဧရာဝတီ/NOUN ၊/. ရန်ကုန်/NOUN နှင့်/CONJ ပဲခူး/NOUN တို့/PRT အား/ADP သိမ်းပိုက်/VERB ခဲ့/PRT သည်/ADP ။/.
```

head, tail command နှစ်ခု သုံးပြီး random ဆွဲထုတ်ကြည့်တဲ့ ပုံစံတမျိုးပါပဲ...  

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$ shuf ./mypos-ver.3.0.upos.txt | head -n 10000 | tail
ည/NOUN ၁၂/NUM နာရီ/NOUN မှာ/ADP ကြိုတင်/ADV မှာယူ/VERB|မှု/PRT ကတ်ပြား/NOUN များ/PRT ကို/ADP တံခါး/NOUN မှာ/ADP ချိတ်ဆွဲ/VERB ထား/PRT ရ/PRT ပါ/PRT မယ်/ADP ။/.
အတွင်းပိုင်း/NOUN မြင်ကွင်း/NOUN နဲ့/CONJ အခန်း/NOUN တစ်/NUM ခန်း/NOUN ။/.
အများကြီး/ADJ ကျေးဇူးတင်/VERB ပါ/PRT တယ်/ADP ။/.
ဒီလို/PRON နဲ့/ADP ကျွန်မ/PRON ဟာ/PRT မြွေ/NOUN နဲ့/ADP ပတ်သက်/VERB တဲ့/PRT စာအုပ်စာတမ်း/NOUN တွေ/PRT ၊/. နိုင်ငံခြား/NOUN|ဝတ္ထု/NOUN တွေ/PRT ကို/ADP လေ့လာ/VERB ဖတ်/VERB ကြည့်/PRT ပါ/PRT တယ်/ADP ။/.
တရုတ်/NOUN|ပြည်/NOUN လာရောက်/VERB လည်ပတ်/VERB တဲ့/PRT ကမ္ဘာလှည့်ခရီးသည်/NOUN တိုင်း/ADP လိုလို/PRT ရှေးဟောင်း/ADJ နန်းတော်/NOUN ကို/ADP လာရောက်/VERB လည်ပတ်/VERB ကြည့်ရှု/VERB ခဲ့/PRT ပါ/PRT တယ်/ADP ။/.
အရမ်း/ADV ကို/ADP ကြိုးကြိုးစားစား/ADV အားကစား/NOUN လုပ်/VERB လိုက်/PRT တာ/PRT ရေဆာ/VERB လိုက်/PRT တာ/PRT ။/.
ကျွန်တော်/PRON ကား/NOUN|လတ်/ADJ တစ်/NUM စီး/PRT ငှား/VERB ချင်/PRT တယ်/ADP ။/.
ဒီ/ADJ နေ့/NOUN ကျွန်တော်/PRON အလုပ်ရှုပ်/VERB နေ/PRT လို့/PRT မနက်ဖြန်/NOUN မှာ/ADP တွေ့/VERB ပါရစေ/ADP ။/.
လက်ဖက်ရည်/NOUN တစ်/NUM ခွက်/NOUN လို/VERB ချင်/PRT ပါ/PRT တယ်/ADP ။/.
အကြွေး/NOUN ကို/ADP ပေးဆပ်/VERB တယ်/ADP ဆို/VERB တာ/PRT သဘာဝကျ/VERB ပါ/PRT တယ်/ADP ။/.
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/4github/mypos2upos$
```

အကြမ်းမျဉ်းအားဖြင့် အဆင်ပြေပုံတော့ ရပါတယ်။  

## To Do

- check RDR parsing accuracy with U-POS
- Rethink Mapping between myPOS and U-POS  

## Reference

1. http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf  
2. https://github.com/slavpetrov/universal-pos-tags  

## 22. [isolation-forest.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/isolation-forest.py)  

## Prepare CSV File

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ ./random-no.sh 80 100 90 > eng1
(base) ye@:/media/ye/project2/4github/isolation-forest$ ./random-no.sh 5 40 10 > eng2
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc eng1
 90  90 273 eng1
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc eng2
10 10 30 eng2
(base) ye@:/media/ye/project2/4github/isolation-forest$ shuf ./eng1 > eng1.shuf
(base) ye@:/media/ye/project2/4github/isolation-forest$ shuf ./eng2 > eng2.shuf
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc id
100 100 292 id
(base) ye@:/media/ye/project2/4github/isolation-forest$ ./random-no.sh 60 100 85 > maths1
(base) ye@:/media/ye/project2/4github/isolation-forest$ ./random-no.sh 50 55 15 > maths2
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc maths1
 85  85 257 maths1
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc maths2
15 15 45 maths2
(base) ye@:/media/ye/project2/4github/isolation-forest$ shuf ./maths1 > maths1.shuf
(base) ye@:/media/ye/project2/4github/isolation-forest$ shuf ./maths2 > maths2.shuf
(base) ye@:/media/ye/project2/4github/isolation-forest$ cat eng1.shuf eng2.shuf > english
(base) ye@:/media/ye/project2/4github/isolation-forest$ cat maths1.shuf maths2.shuf > mathematics
(base) ye@:/media/ye/project2/4github/isolation-forest$ paste id english mathematics -d"," > mark-list.csv
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc ./mark-list.csv 
100 100 897 ./mark-list.csv
(base) ye@:/media/ye/project2/4github/isolation-forest$ head ./mark-list.csv 
1,96,82
2,82,94
3,96,83
4,81,93
5,91,87
6,93,94
7,99,76
8,87,99
9,97,98
10,82,76
(base) ye@:/media/ye/project2/4github/isolation-forest$ tail ./mark-list.csv 
91,38,55
92,36,51
93,15,51
94,25,50
95,12,50
96,17,51
97,23,53
98,21,54
99,33,54
100,39,55
```

## Add CSV Header

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ sed -i '1s/^/ID,English,Mathematics\n/' ./mark-list.csv 
(base) ye@:/media/ye/project2/4github/isolation-forest$ head ./mark-list.csv 
ID,English,Mathematics
1,96,82
2,82,94
3,96,83
4,81,93
5,91,87
6,93,94
7,99,76
8,87,99
9,97,98
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc ./mark-list.csv 
101 101 920 ./mark-list.csv
(base) ye@:/media/ye/project2/4github/isolation-forest$
```

## Python Code for Isolation-Forest

coding က အောက်ပါအတိုင်း...  

```
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# Reading CSV
marks=pd.read_csv('mark-list.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)

#print(marks)

## for only English ## 

# Training
# n_estimators=100 means 100 trees
# "contamination" means % of randomness present in our dataset
# max_features means how many featues you need to include while training the isolation-forest algorithm, here 1.0 means it draw single feature from the dataset
model=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.2), max_features=1.0)
model.fit(marks[['English']])

# Prediction
marks['anomailes_scores_eng']=model.decision_function(marks[['English']])
marks['anomaly_eng']=model.predict(marks[['English']])

# here, 1 for good data and -1 for bad data
#print(marks.head(10))
print(marks)
```

## Error

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ python ./isolation-forest.py 
Traceback (most recent call last):
  File "./isolation-forest.py", line 3, in <module>
    from sklearn.ensemble import isolationForest
ImportError: cannot import name 'isolationForest' from 'sklearn.ensemble' (/home/ye/anaconda3/lib/python3.7/site-packages/sklearn/ensemble/__init__.py)
(base) ye@:/media/ye/project2/4github/isolation-forest$ pip install -U sklearn
Requirement already satisfied: sklearn in /home/ye/anaconda3/lib/python3.7/site-packages/sklearn-0.0-py3.7.egg (0.0)
Requirement already satisfied: scikit-learn in /home/ye/anaconda3/lib/python3.7/site-packages (from sklearn) (0.24.2)
Requirement already satisfied: numpy>=1.13.3 in /home/ye/anaconda3/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.20.3)
Requirement already satisfied: threadpoolctl>=2.0.0 in /home/ye/anaconda3/lib/python3.7/site-packages (from scikit-learn->sklearn) (3.0.0)
Requirement already satisfied: joblib>=0.11 in /home/ye/anaconda3/lib/python3.7/site-packages (from scikit-learn->sklearn) (0.17.0)
Requirement already satisfied: scipy>=0.19.1 in /home/ye/anaconda3/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.4.1)
WARNING: You are using pip version 21.2.4; however, version 21.3 is available.
You should consider upgrading via the '/home/ye/anaconda3/bin/python -m pip install --upgrade pip' command.
(base) ye@:/media/ye/project2/4github/isolation-forest$ python ./isolation-forest.py 
Traceback (most recent call last):
  File "./isolation-forest.py", line 3, in <module>
    from sklearn.ensemble import isolationForest
ImportError: cannot import name 'isolationForest' from 'sklearn.ensemble' (/home/ye/anaconda3/lib/python3.7/site-packages/sklearn/ensemble/__init__.py)
(base) ye@:/media/ye/project2/4github/isolation-forest$
```

တကယ်မှန်တာက "I" အကြီးဖြစ်ရမယ်...  

```python
from sklearn.ensemble import IsolationForest
```

## Results

comment နဲ့ အဖွင့်အပိတ်လုပ်ပြီးတော့ setting နှစ်ခုနဲ့ run  ခဲ့တယ်  

- Math အတွက်ပဲ anomaly ဖြစ်တာကိုပဲ ဆွဲထုတ်ကြည့်ခဲ့တယ်
- English အတွက်ပဲ anomaly ဖြစ်တာကိုပဲ ဆွဲထုတ်ကြည့်ခဲ့တယ်

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ python ./isolation-forest.py > result-maths
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc result-maths 
 101  605 6767 result-maths
(base) ye@:/media/ye/project2/4github/isolation-forest$ python ./isolation-forest.py > result-eng
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc result-eng 
 101  605 6565 result-eng
```

## Extract Only Column6=-1

column နံပါတ် 4 က သင်္ချာအမှတ်တွေ...  
တမင် အမှတ်စာရင်းမှာ အမှတ်အများနဲ့ အနည်း ကွာအောင် simulation လုပ်ခဲ့တာက အောက်ပါအတိုင်း...  
$ ./random-no.sh 60 100 85 > maths1
./random-no.sh 50 55 15 > maths2  

ပုံမှန် မဟုတ်ဘူးလို့ isolation forest algorithm နဲ့ ဆွဲထုတ်ပြီး ရလာတဲ့ Result က အောက်ပါအတိုင်း...  

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ awk '$6 == "-1" {print}' ./result-maths 
7     8       87           99              -0.016155            -1
19   20       91           99              -0.016155            -1
22   23       87           97              -0.019141            -1
41   42       87          100              -0.067182            -1
79   80       81           61              -0.017755            -1
80   81       84          100              -0.067182            -1
85   86       88           50              -0.005495            -1
86   87       93           50              -0.005495            -1
87   88       93           55              -0.007067            -1
88   89       82           50              -0.005495            -1
89   90       88           52              -0.057606            -1
90   91       38           55              -0.007067            -1
91   92       36           51              -0.015743            -1
92   93       15           51              -0.015743            -1
93   94       25           50              -0.005495            -1
94   95       12           50              -0.005495            -1
95   96       17           51              -0.015743            -1
96   97       23           53              -0.042398            -1
99  100       39           55              -0.007067            -1
```

column နံပါတ် 3 က အင်္ဂလိပ်စာ အမှတ်တွေ...  
တမင် အမှတ်စာရင်းမှာ အမှတ်နည်းအောင် လုပ်ခဲ့တာက အောက်ပါအတိုင်း...  
$ ./random-no.sh 80 100 90 > eng1
$ ./random-no.sh 5 40 10 > eng2  

ပုံမှန် မဟုတ်ဘူးလို့ isolation forest algorithm နဲ့ ဆွဲထုတ်ပြီး ရလာတဲ့ Result က အောက်ပါအတိုင်း...  

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ awk '$6 == "-1" {print}' ./result-eng 
10   11      100           88             -0.071508           -1
16   17       98           67             -0.005852           -1
30   31      100           78             -0.071508           -1
40   41       80           75             -0.044913           -1
53   54       80           96             -0.044913           -1
66   67       80           84             -0.044913           -1
83   84      100           66             -0.071508           -1
84   85       98           72             -0.005852           -1
90   91       38           55             -0.096913           -1
91   92       36           51             -0.101730           -1
92   93       15           51             -0.129156           -1
93   94       25           50             -0.109295           -1
94   95       12           50             -0.195488           -1
95   96       17           51             -0.118600           -1
96   97       23           53             -0.093191           -1
97   98       21           54             -0.107667           -1
98   99       33           54             -0.123024           -1
99  100       39           55             -0.124135           -1
(base) ye@:/media/ye/project2/4github/isolation-forest$
```

## Running for Both Fields

python code ကို အောက်ပါအတိုင်း ပြင်ဆင်ပြီး run ခဲ့...  
```python
## for both Eng and Maths ## 

model=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.2), max_features=1.0)
model.fit(marks[['English', 'Mathematics']])

# Prediction
marks['anomailes_scores_both']=model.decision_function(marks[['English', 'Mathematics']])
marks['anomaly_for_both']=model.predict(marks[['English', 'Mathematics']])

# here, 1 for good data and -1 for bad data
print(marks)
```

ရလဒ်က အောက်ပါအတိုင်း...  

```
(base) ye@:/media/ye/project2/4github/isolation-forest$ python ./isolation-forest.py > result-both
(base) ye@:/media/ye/project2/4github/isolation-forest$ wc result-both 
 101  605 7171 result-both
(base) ye@:/media/ye/project2/4github/isolation-forest$ awk '$6 == "-1" {print}' ./result-both 
8     9       97           98              -0.052318                -1
10   11      100           88              -0.018649                -1
19   20       91           99              -0.011254                -1
53   54       80           96              -0.019112                -1
80   81       84          100              -0.031858                -1
85   86       88           50              -0.003485                -1
86   87       93           50              -0.030615                -1
87   88       93           55              -0.000100                -1
88   89       82           50              -0.048489                -1
89   90       88           52              -0.003559                -1
90   91       38           55              -0.060058                -1
91   92       36           51              -0.088425                -1
92   93       15           51              -0.070496                -1
93   94       25           50              -0.087898                -1
94   95       12           50              -0.140936                -1
95   96       17           51              -0.058938                -1
96   97       23           53              -0.068335                -1
97   98       21           54              -0.077298                -1
98   99       33           54              -0.068356                -1
99  100       39           55              -0.066577                -1
(base) ye@:/media/ye/project2/4github/isolation-forest$ 
```

## 24. [how-name-eq-main-work.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/how-name-eq-main-work.py)    
```if __name__ == '__main__':``` ရဲ့ အလုပ်လုပ်ပုံကို နားလည်စေဖို့ ဥပမာ ရေးပြထားတဲ့ python code ပါ။

Python code ရေးတဲ့အခါမှာ C, C++ တို့နဲ့ မတူပဲ main method မရှိလည်း run ပေးတာကို သိကြပါလိမ့်မယ်။ ပြီးတော့ ```if __name__ == '__main__':``` ဆိုတဲ့ ပုံစံမျိုးနဲ့ main method ကို Python code ထဲမှာ သတ်မှတ်ပြီး သုံးတာမျိုးကိုလည်း တွေ့ဖူးကြပါလိမ့်မယ်။ အဲဒါကြောင့် main method က Python programming language မှာ ဘယ်လို ပုံစံမျိုးနဲ့ အလုပ်လုပ်နေသလဲ ဆိုတာကို ရှင်းပြချင်ပါတယ်။  

တကယ်က Python interpreter က python script တစ်ခုကို running မလုပ်ခင်မှာ ```__name__``` ဆိုတဲ့ special variable တစ်ခုကို အရင်ဆုံး assign လုပ်ပေးပါတယ်။ အဲဒီလို လုပ်တဲ့အခါမှာ Python script ကို command line ကနေ ခေါ် run တာလား သို့မဟုတ် module တစ်ခုအနေနဲ့ import နဲ့ လှမ်းခေါ်သုံးထားတာလား ဆိုတဲ့ အပေါ်ကို မူတည်ပြီးတော့ ```__name__``` special variable ကို assign လုပ်တဲ့ပုံစံက ကွဲပြားသွားပါလိမ့်မယ်။  

တကယ်လို့ command line ကနေ ```python /how-name-eq-main-work.py``` လိုမျိုး ခေါ်ပြီး run တဲ့အခါမှာတော့ ```__name__``` ကို ```__main__``` ဆိုပြီး assign လုပ်ပေးပါလိမ့်မယ်။ အဲဒီလို မဟုတ်ပဲနဲ့ module တစ်ခုအနေနဲ့ import နဲ့ ခေါ်သုံးတဲ့ အခါမှာတော့ ```__name__``` special variable ကို ခေါ်သုံးတဲ့ module name ကို assign လုပ်ပေးသွားပါလိမ့်မယ်။ ဥပမာ ```__main__=eg_module```  

### main method ရဲ့ အလုပ်လုပ်ပုံ

```__name__``` ကို ```__main__``` ဆိုပြီး assign လုပ်လိုက်ပြီ ဆိုရင်တော့ program ထဲမှာ ရေးထားတဲ့ run ပေးလို့ရတဲ့ statement တွေအားလုံးကို run အပေါ်ကနေအောက်ဖက်ကို လိုင်းတစ်ခုခြင်းစီ ဆင်းလာတဲ့ ပုံစံနဲ့ run ပေးသွားမှာ ဖြစ်ပါတယ်။ ဒါ့အပြင့် main method ထဲမှာ ရေးထားတဲ့ statement တွေကိုလည်း run ပေးမှာ ဖြစ်ပါတယ်။  

```__name__``` ကို module name တစ်ခုခု assign လုပ်ထားတဲ့ အခါမှာတော့ အဲဒီ module ထဲက run ပေးလို့ ရတဲ့ statement တွေကို အပေါ်ကနေ အောက်ဖက်ကို အဆင့်ဆင့် run ပေးသွားမှာ ဖြစ်ပေမဲ့ အဲဒီ module ထဲမှာ ရှိတဲ့ main method အောက်က statement တွေကိုတော့ run ပေးမှာ မဟုတ်ပါဘူး။ အဲဒါကြောင့် how-name-eq-main-work.py ကို run ကြည့်ရင် အောက်ပါအတိုင်း output လုပ်ပေးတာကို တွေ့ရမှာ ဖြစ်ပါတယ်။  

```
$ python ./how-name-eq-main-work.py 
eg-module.py ထဲကနေ print လုပ်လိုက်တာပါ!
main method ရဲ့ အပြင်မှာပါ ...
main method ရဲ့ အထဲမှာပါ ...
```

## 25. [f1-score-calc.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/f1-score-calc.py)   

True/False ဆိုတဲ့ class နှစ်ခုရှိတဲ့ classification ရဲ့ output နဲ့ မှန်ကန်တဲ့ အဖြေဖြစ်တဲ့ Reference ကို F1-score တွက်ကြည့်ရအောင်။  
တကယ်က F1-score မှာ average micro နဲ့ average macro ဆိုပြီးတွက်တဲ့ ပုံစံနှစ်မျိုးရှိတယ်။ အသေးစိတ်ကို coding ထဲမှာလည်း comment တွေ ရေးပေးထားပါတယ်။  

```python
"""
 F1-score calculation example for single 
written by Ye Kyaw Thu, LST, NECTEC, Thailand
Date: 26 Oct 2021

# Reference:
https://datascience.stackexchange.com/questions/15989/micro-average-vs-macro-average-performance-in-a-multiclass-classification-settin
http://rushdishams.blogspot.com/2011/08/micro-and-macro-average-of-precision.html
"""

# micro-average နဲ့ macro-average က တွက်ပုံက အနည်းငယ်ကွဲပြားတယ်။ အဲဒါကြောင့် အဖြေကလည်း တထပ်တည်း တူမှာမဟုတ်ဘူး။
# micro-average ကတော့ class အမျိုးအစားကွဲ ရှိသလောက် ကိုအားလုံးစုပေါင်းပြီးမှ average တွက်တဲ့ ပုံစံပါ။
# အသေးစိတ်ပြောရရင် true-positive တွေ အားလုံးပေါင်း၊ false-positive တွေ အားလုံးပေါင်း၊ false-negative တွေ အားလုံးကိုလည်း ပေါင်းပြီးမှ
# တွက်သွားတဲ့ ပုံစံပါ။ အောက်ပါအတိုင်းပါ...  
# P = TP/(TP+FP), R = TP/TP+FN
# အဲဒါကြောင့် micro-average က multi-class classification အတွက် ပိုသင့်တော်ပါတယ်။
# အထူးသဖြင့် ဒေတာထဲမှာ class အမျိုးအစား ပါဝင်မှု အရေအတွက်က မညီမျှနိုင်တဲ့မျိုးအခြေအနေမျိုးမှာပါ။
# ဥပမာ class အမျိုးအစား တစ်ခုမှာ အရေအတွက်က အရမ်းကြီးများနေတဲ့ case မျိုးမှာ...  

# macro-average က class တစ်ခုချင်းစီအတွက် သပ်သပ်စီ တွက်ပြီးမှ average ယူတယ်။ class အားလုံးကို ညီတူညီမျှပဲ ထားပြီး စဉ်းစားတယ်။
# macro-average တွက်တဲ့ ပုံစံက 
# macro-average-precision = P1+P2/2 (true, false class နှစ်မျိုးပဲ ရှိလို့)
# macro-average-recall = R1 + R2/2
# system တစ်ခု အနေနဲ့ သို့မဟုတ် model တစ်ခုရဲ့ dataset ပေါ်မှာ ရလာတဲ့ performance ကို ကြည့်ဖို့အတွက် အသုံးဝင်တယ်
# NLP သမားတွေ၊ ML သမားတွေ ပြောနေကြတဲ့ precision, recall, F1-socre တွေက default က macro ပါ

# module, package loading
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, f1_score
import random


# prepare reference data
# ture, false တွေကို အကြိမ် ၁၀၀ ကျပန်း ယူလိုက်ပြီး reference အနေနဲ့ ထားလိုက်တာ
reference = [random.choice([True, False])  for x in range(100)]
print("Reference: ", reference)

# simulation of model prediction
# model တစ်ခုခုက ခန့်မှန်းပြီး ထွက်လာတဲ့ အဖြေကိုလည်း အထက်ကလိုပါပဲ အကြိမ် ၁၀၀ ကျပန်း ယူလိုက်ပြီး list တစ်ခု ဆောက်လိုက်တာပါ
prediction = [random.choice([True, False])  for x in range(100)]
print("\nModel Output: ", prediction)

# confusion matrix
print("\nConfusion matrix:")
print(confusion_matrix(reference, prediction, labels=[True, False]))

#calculate F1 score
precision=precision_score(reference, prediction)
print("\nParameter: average=micro")
print("Precision: ", precision)
recall=recall_score(reference, prediction)
print("Recall: ", recall)
score=f1_score(reference, prediction)
print("F1 Score: ", score)

precision=precision_score(reference, prediction, average='macro')
print("\nParameter: average=macro")
print("Precision: ", precision)
recall=recall_score(reference, prediction, average='macro')
print("Recall: ", recall)
score=f1_score(reference, prediction, average='macro')
print("F1 Score: ", score)

# using classification_report()
print("\nClassification_report():")
print(classification_report(reference, prediction, labels=[True, False]))
```

Run ကြည့်ရင် output အနေနဲ့ အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
(base) ye@:/media/ye/project2/4github/4students/f1-score$ python ./f1-score-calc.py 
Reference:  [True, False, True, False, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, False, True, False, False, False, False, True, False, True, True, False, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, True, True, False, True, False, True, True, False, False, True, True, False, True, False, False, True, False, True, False, True, True, True, False, False, True, False, True, True, False, False, True, False, False, True, False, False, False]

Model Output:  [False, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, False, False, False, True, True, True, True, False, True, True, True, False, False, False, False, False, True, True, False, False, False, True, True, True, True, False, True, True, False, False, False, False, False, False, True, False, False, True, False, False, True, False, True, False, False, False, True, False, False, False, True, True, False, True, True, True, False, False, True, True, True, False, True, False, True, False, True, True, False, True, False, False, True, True, False, True, False]

Confusion matrix:
[[30 20]
 [23 27]]

Parameter: average=micro
Precision:  0.5660377358490566
Recall:  0.6
F1 Score:  0.5825242718446602

Parameter: average=macro
Precision:  0.5702529104777199
Recall:  0.5700000000000001
F1 Score:  0.5696126513862476

Classification_report():
              precision    recall  f1-score   support

        True       0.57      0.60      0.58        50
       False       0.57      0.54      0.56        50

    accuracy                           0.57       100
   macro avg       0.57      0.57      0.57       100
weighted avg       0.57      0.57      0.57       100

(base) ye@:/media/ye/project2/4github/4students/f1-score$ 
```

## 26. [multi-class-f1.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/multi-class-f1.py)  

F1-score တွက်တာကိုပဲ ဒီတစ်ခါတော့ multi-class classification problem အတွက် evaluation လုပ်တဲ့ အနေနဲ့ တွက်ပြထားတာဖြစ်ပါတယ်။ ဥပမာကတော့ လူတိုင်းနားလည်ရလွယ်တဲ့ အံစာတုံးခေါက်ကစားနည်းကိုပဲ အခြေခံထားပါတယ်။ ပထမဆုံး ကွန်ပျူတာကနေ ကျပန်း အံစာတုံးအခါ ၁၀၀ ခေါက်လိုက်ပြီးတော့ အဲဒီရလဒ်ကို ကစားသမားနှစ်ယောက် (simulated player နှစ်ယောက်) ရဲ့ အံစာတုန်းခေါက်ထားတဲ့ ရလဒ်တွေနဲ့ နှိုင်းယှဉ်ပြီး F1-score တွက်တာကို ဥပမာအနေနဲ့ ရေးပြထားတာပါ။ ဒီနေရာမှာ အံစာတုံးခေါက်လိုက်ရင် ဖြစ်နိုင်ချရှိတဲ့ နံပါတ်(၁) ကနေ နံပါတ်(၆) ကို class တစ်ခုချင်းစီအနေနဲ့ထားပြီးတော့ F1-score တွက်သွားတာ ဖြစ်ပါတယ်။  

တွက်ပေးတဲ့ function ကတော့ sklearn module ကနေ အောက်ပါအတိုင်း ခေါ်သုံးထားပါတယ်။  

```python
from sklearn.metrics import f1_score
```

multi-class-f1.py ကို command line မှာ run လိုက်ရင် မြင်ရမယ့် output တွေကတော့ အောက်ပါအတိုင်းဖြစ်ပါတယ်။  
ခင်ဗျားတို့ စက်ထဲမှာ run တဲ့အခါမှာအခုပြထားတဲ့ ရလဒ်နဲ့ကတူမှာ မဟုတ်ဘူးနော်။ တစ်ခေါက် run တိုင်းမှာ ကျပန်း (random) ခေါက်ခေါက်သွားမှာမို့ပါ။  

```
(base) ye@:/media/ye/project2/4github/4students/f1-score$ python ./multi-class-f1.py 
Dice roll by a model:  [2, 2, 3, 1, 5, 3, 6, 3, 2, 2, 1, 6, 1, 3, 6, 1, 1, 3, 3, 4, 4, 3, 6, 6, 3, 3, 4, 1, 5, 3, 4, 5, 2, 2, 6, 2, 4, 3, 3, 2, 3, 4, 5, 3, 3, 3, 2, 4, 1, 2, 1, 1, 6, 2, 5, 4, 6, 1, 6, 1, 6, 4, 4, 6, 4, 3, 5, 6, 5, 4, 6, 3, 6, 1, 3, 3, 2, 6, 3, 1, 3, 1, 1, 2, 1, 4, 6, 2, 5, 3, 1, 6, 2, 6, 5, 5, 6, 4, 2, 4]
Dice roll by player1:  [2, 4, 5, 3, 2, 5, 4, 1, 2, 2, 5, 6, 1, 5, 2, 5, 6, 3, 6, 6, 6, 1, 4, 2, 2, 5, 5, 5, 4, 5, 6, 3, 3, 5, 2, 6, 3, 6, 2, 6, 4, 3, 5, 4, 3, 3, 1, 3, 2, 3, 3, 1, 1, 2, 3, 4, 1, 2, 3, 6, 3, 4, 6, 5, 2, 1, 3, 5, 1, 6, 6, 1, 3, 6, 3, 6, 6, 3, 4, 4, 5, 2, 6, 4, 5, 1, 5, 3, 6, 5, 3, 2, 4, 5, 2, 6, 3, 5, 2, 6]
Dice roll by player2:  [2, 6, 1, 3, 3, 4, 6, 3, 5, 3, 2, 6, 6, 1, 5, 1, 3, 5, 4, 6, 1, 3, 4, 3, 2, 1, 2, 3, 1, 1, 2, 4, 5, 4, 6, 3, 2, 6, 1, 6, 3, 2, 3, 5, 4, 1, 6, 2, 3, 6, 4, 5, 1, 1, 6, 2, 2, 1, 3, 4, 5, 2, 1, 1, 4, 4, 3, 3, 6, 3, 3, 1, 4, 5, 2, 4, 3, 6, 3, 2, 6, 1, 4, 5, 5, 3, 1, 4, 3, 4, 6, 4, 2, 1, 4, 3, 5, 2, 1, 1]
F1-score for player1:  [0.14285714 0.3030303  0.18181818 0.14814815 0.06896552 0.1025641 ]
F1-score for player2:  [0.16216216 0.12903226 0.17777778 0.0625     0.         0.23529412]
(base) ye@:/media/ye/project2/4github/4students/f1-score$
```

## 27. [language-detect.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/language-detect.py)  

googletrans library ရဲ့ Translator ကို အောက်ပါအတိုင်း input လုပ်တယ်။  

```python
from googletrans import Translator
```

ပြီးတော့မှ translate.detect() function ကနေ return ပြန်လာတဲ့ value ကို print ထုတ်ပေးလိုက်တာပါ။  

```
$ python ./language-detect.py 
input: နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။
language:  my

input: 元気です。毎日働いています。
language:  ja

input: My name is Ye Kyaw Thu.
language:  en

input: กระดาษสีถ่ายเอกสาร 1 A4 80 แกรม ฟ้า 500 แผ่น
language:  th

input: နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။ 元気です。毎日働いています。
language:  my

input: 元気です。毎日働いています。နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။
language:  my

input: N dai tsi n tsin hpe tsi gawk kaw sa shaw la u.
language:  ha

input: NÀ HPÀRVT LĒGA TÌQCVNG SĒ GØ̀ MĒRØ DAQ Ó .
language:  sm

input: အဲဝယ်ဟှား ခံဗျား ဟှို အဲဇာ ပေး ဟှို့ မှုဝ ။
language:  my
```

အထက်မှာ ဥပမာ အနေနဲ့ run ပြထားတဲ့ အတိုင်းပါပဲ။  
ဘာသာစကား နှစ်ခု ရောလိုက်ရင် detection က မှားနိုင်ပါတယ်။ ထိုနည်းလည်းကောင်း မြန်မာ Unicode ဇယားထဲမှာပါတဲ့ မြန်မာစာလုံးတွေကို သုံးထားရင် dialect language တွေဖြစ်တဲ့ ရခိုင်၊ ထားဝယ်၊ ဘိတ် တို့ကိုလည်း မြန်မာဘာသာ (i.e. my) အနေနဲ့လည်း return ပြန်ပေးပါလိမ့်မယ်။ alphabet ကို သုံးတဲ့ မြန်မာတိုင်းရင်းသား ဘာသာစကား string တွေကို input လုပ်ရင်လည်း မှန်မှန်ကန်ကန် detect လုပ်မပေးနိုင်တာကို တွေ့ရပါလိမ့်မယ်။  

## 28. [python-list-eg.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/python-list-eg.py)  

Python ရဲ့ list ကို အသုံးဝင်တဲ့ ပုံစံ ခြောက်မျိုးအနေနဲ့ သုံးပြထားတာပါ။  
သိထားခြင်းအားဖြင့် NLP/AI အလုပ်တွေရဲ့ preprocessing/post-editing ကိစ္စတွေအတွက် အသုံးဝင်ပါလိမ့်မယ်။  
Run ကြည့်ရင် အောက်ပါလိုမျိုး output ကို မြင်ရပါလိမ့်မယ်။  

```
(base) ye@:/media/ye/project2/4github/4students/python-list$ python ./python-list-eg.py 
list1:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
after slicing with slice(4, 10, 1):  [5, 6, 7, 8, 9, 10]
apply "10*x" to every element of the list1 with "map":  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
original string:  ဒီညတော့ ဂျူးပဲပုပ်ကြော နဲ့ ညစာ စားမယ်
after reversing a list:  ်ယမးာစ ာစည ့ဲန ာေြက်ပုပဲပးူျဂ ့ာေတညီဒ
မူလတန်း, In English "primary school", 5 years course.
အလယ်တန်း, In English "middle school", 3 years course.
အထက်တန်း, In English "high school", 2 years course.
even_odd_dict:  {'odd': [1, 3, 5, 7, 9], 'even': [2, 4, 6, 8, 10]}
After joining all list values:  [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
after merging two lists:  {'Cafe Latte': 60, 'American Coffee': 45, 'Matcha Latte': 70, 'Cappuccino': 60, 'Lemon Tea': 55}
(base) ye@:/media/ye/project2/4github/4students/python-list$
```

## 29. https://github.com/ye-kyaw-thu/tools/blob/master/python/split-train-test.py

Machine Translation မှာ သုံးတဲ့ parallel corpus ကို training data, test data အဖြစ် ခွဲတာကို လက်တွေ့ လုပ်ကြည့်ကြရအောင်။  

ဥပမာ အနေနဲ့ ကိုယ့်ဆီမှာက အင်္ဂလိပ်စာ၊ မြန်မာစာ၊ ထိုင်းစာ အတွက်က ဖိုင်သုံးဖိုင်အနေနဲ့ခွဲပြီး ရှိနေတယ် ဆိုကြပါစို့...  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ wc data.{en,my,th}
  14577  200464 1004773 data.en
  14577  229186 3544131 data.my
  14577   33224 2301540 data.th
  43731  462874 6850444 total
```

parallel data ဖြစ်ရမယ်။ လိုင်းအရေအတွက်တွေက တူရမယ်။ side-by-side တွဲကြည့်ရင် အဓိပ္ပါယ်တူတဲ့ စာကြောင်းတွေ ဖြစ်ရမယ်။  
နောက်ထပ် အရေးကြီးတာက blank line တွေ မပါပါစေနဲ့။ မျက်လုံးနဲ့ ဖိုင်တစ်ဖိုင်ချင်းစီကို ဖွင့်စစ်တာ၊ ဒေတာတွေကို လေ့လာတာ၊ cleaning လုပ်တာတွေက အရင်ဆုံး လုပ်သင့်ပါတယ်။  
ထိပ်ဆုံး သုံးကြောင်းကိုပဲ ရိုက်ထုတ်ခိုင်းကြည့်ရင် အောက်ပါလိုမျိုး ဖိုင်ပါ။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ head -3 data.en
Hello
Are you Mr.Tun Tun ?
Nice to meet you .
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ head -3 data.my
မင်္ဂလာပါ ။
ခင်ဗျား က မစ္စတာ ထွန်းထွန်း ဖြစ် ပါ သလား ။
ခင်ဗျား ကို တွေ့ ရတာ ဝမ်းသာ ပါ တယ် ။
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ head -3 data.th
สวัสดี
คุณคือนายตุน ตุน?
ยินดีที่ได้พบคุณ.
```

train_split ခွဲပေးတဲ့ function က အခြေခံအားဖြင့် data-frame အနေနဲ့ input ကို လက်ခံတာပါ။ ဆိုလိုတာက CSV ဖိုင်လိုမျိုးဖြစ်ရပါမယ်။ TAB နဲ့ field တစ်ခုချင်းစီကို ခြားထားတဲ့ ဖိုင်ပုံစံ ဖြစ်ရပါမယ်။  
အဲဒါကြောင့် Linux OS ရဲ့ paste ဆိုတဲ့ command ကို သုံးပြီး အထက်ပါ ဖိုင်သုံးဖိုင်ကို TAB နဲ့ ခြားပြီး တစ်ဖိုင်တည်းဖြစ်အောင် ပေါင်းပေးဖို့အတဝက် အောက်ပါအတိုင်း command ပေးရအောင်။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ paste ./data.en ./data.my ./data.th > ./data.tsv
```

အဲဒါဆိုရင်တော့ လိုချင်တဲ့ CSV ဖိုင် ဖြစ်သွားတာကို အောက်ပါအတိုင်း တွေ့ရပါလိမ့်မယ်။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ head -3 data.tsv
Hello	မင်္ဂလာပါ ။	สวัสดี
Are you Mr.Tun Tun ?	ခင်ဗျား က မစ္စတာ ထွန်းထွန်း ဖြစ် ပါ သလား ။	คุณคือนายตุน ตุน?
Nice to meet you .	ခင်ဗျား ကို တွေ့ ရတာ ဝမ်းသာ ပါ တယ် ။	ยินดีที่ได้พบคุณ.
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$
```


split-train-test.py ဖိုင်ကို လက်ရှိ path အောက်ကို download လုပ်ရအောင်...  
အဲဒါကိုလည်း GitHub ရဲ့ path (raw တော့ ဖြစ်ရမယ်) ကိုသိရင် အောက်ပါအတိုင်း Linux command တစ်ခုဖြစ်တဲ့ wget နဲ့ အလွယ်တကူ download လုပ်ယူလို့ ရပါလိမ့်မယ်။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ wget https://raw.githubusercontent.com/ye-kyaw-thu/tools/master/python/split-train-test.py
--2022-02-13 13:32:06--  https://raw.githubusercontent.com/ye-kyaw-thu/tools/master/python/split-train-test.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4905 (4.8K) [text/plain]
Saving to: ‘split-train-test.py’

split-train-test.py                   100%[=========================================================================>]   4.79K  --.-KB/s    in 0s      

2022-02-13 13:32:07 (30.9 MB/s) - ‘split-train-test.py’ saved [4905/4905]

```

split မလုပ်ခင်မှာက လက်ရှိ path မှာ ရှိနေတဲ့ ဖိုင်တွေက အောက်ပါအတိုင်းပါ။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ ls
data.en  data.my  data.th  data.tsv  split-train-test.py
```

split လုပ်ကြည့်ချင်ရင် အောက်ပါအတိုင်း command ပေးပါ။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ python ./split-train-test.py
```

split လုပ်ပြီးသွားတဲ့ အခါမှာတော့ "train-test_data/" ဆိုတဲ့ folder ကိုလည်း မြင်ရပါလိမ့်မယ်။  
```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ ls -F
data.en*  data.my*  data.th*  data.tsv*  split-train-test.py*  train-test_data/
```

အဲဒီ ဖိုလ်ဒါထဲမှာ ဘာဖိုင်တွေ ရှိသလဲ ဆိုတာကို tree command နဲ့ ခေါ်ကြည့်ရအောင်...  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ tree ./train-test_data/
./train-test_data/
├── test.tsv
└── train.tsv

0 directories, 2 files
```

split လုပ်ပြီး ထွက်လာတဲ့ training ဖိုင်နဲ့ test ဖိုင်တွေရဲ့ file size တွေကိုလည်း လေ့လာကြည့်ရအောင်...  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ wc ./train-test_data/{train,test}.tsv
  11795  374694 5553973 ./train-test_data/train.tsv
   2783   88174 1297096 ./train-test_data/test.tsv
  14578  462868 6851069 total
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$
```

## 30. [split-train-valid-test.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/split-train-valid-test.py)   

ဒီတစ်ခါတော့ ပုံမှန် Statistical Machine Translation, Neural Machine Translation မှာ သုံးတဲ့ပုံစံဖြစ်တဲ့ training, validation, test ဒေတာခွဲတာကို လုပ်ဖို့အတွက် ရည်ရွယ်ပြီး ရေးပြထားတာပါ။  
အထက်က Python script နံပါတ် 30 နဲ့ အခြေခံအားဖြင့်က တူပါတယ်။ အဓိက မတူတာက validation set ပါ ပါလာလို့ train_test_split() function ကို နှစ်ခါ ခေါ်သုံးထားတာပါပဲ။  

parallel corpus က အောက်ပါအတိုင်း English-Myanmar-Thai ရှိတယ်လို့ ဆိုကြပါစို့...  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ head -5 ./data.tsv
Hello	မင်္ဂလာပါ ။	สวัสดี
Are you Mr.Tun Tun ?	ခင်ဗျား က မစ္စတာ ထွန်းထွန်း ဖြစ် ပါ သလား ။	คุณคือนายตุน ตุน?
Nice to meet you .	ခင်ဗျား ကို တွေ့ ရတာ ဝမ်းသာ ပါ တယ် ။	ยินดีที่ได้พบคุณ.
My name is Dr.Aung .	ကျွန်တော့် နာမည် ဒေါက်တာ အောင် ဖြစ် ပါ တယ် ။	ฉันชื่อ หมออ๋อง
I am one of the junior doctors in the department .	ကျွန်တော် ဒီ ဌာန က ဆရာဝန် အငယ် တစ်ယောက် ဖြစ် ပါ တယ် ။	ฉันเป็นหนึ่งในแพทย์รุ่นน้องในแผนก
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$
```

Python script က ကိုယ်အလုပ်လုပ်မယ့် path မှာ မရှိသေးရင် Github link ကို wget command ကို pass လုပ်ပြီး download လုပ်ယူလို့ ရပါတယ်။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ wget https://raw.githubusercontent.com/ye-kyaw-thu/tools/master/python/split-train-valid-test.py
--2022-02-13 14:13:45--  https://raw.githubusercontent.com/ye-kyaw-thu/tools/master/python/split-train-valid-test.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7138 (7.0K) [text/plain]
Saving to: ‘split-train-valid-test.py’

split-train-valid-test.py             100%[=========================================================================>]   6.97K  --.-KB/s    in 0s      

2022-02-13 14:13:45 (35.8 MB/s) - ‘split-train-valid-test.py’ saved [7138/7138]
```

run မယ်။  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ python ./split-train-valid-test.py 
```

output အနေနဲ့ ထွက်လာတဲ့ train-valid-test_data/ ဆိုတဲ့ folder ထဲမှာ ရလာမယ့် ဖိုင်တွေကို ကြည့်ကြည့်ရအောင်...  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ tree ./train-valid-test_data/
./train-valid-test_data/
├── test.tsv
├── train.tsv
└── valid.tsv

0 directories, 3 files
```

file size တွေကိုလည်း စစ်ဆေးကြည့် ရအောင်...  

```
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$ wc ./train-valid-test_data/{train,valid,test}.tsv
  11795  374694 5553973 ./train-valid-test_data/train.tsv
   1392   44442  652079 ./train-valid-test_data/valid.tsv
   1392   43736  645074 ./train-valid-test_data/test.tsv
  14579  462872 6851126 total
(base) ye@:/media/ye/project2/students/mya-ei-san/exercise/12Feb2022/corpus/split-eg/4github$
```

ဒီပရိုဂရမ်က အသုံးဝင်ပါလိမ့်မယ်။ ကိုယ်တိုင်လည်း ရေးနိုင်အောင် ကြိုးစားကြပါလို့...  


## Reference

- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html
- https://morioh.com/p/a6ef01110316?f=5c21fb01c16e2556b555ab32&fbclid=IwAR1z5bVfqVf2kZYTZksqM3lkMV6HRKQwRyzkGrFkeAdyA1UUP0mcTay8A3M

## 37. [syl2freq.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2freq.py) 

input ဖိုင်က အောက်ပါအတိုင်း  

```
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ cat eg-corpus.txt 
နေကောင်း တယ် နော်
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း အောင် နေ ပါ နော်
အခု အလုပ် လုပ် နေ တယ်

```

syllabe ဖြတ်ပြီးတော့ count လုပ်ကြည့်ဖို့ အတွက် အောက်ပါအတိုင်း run ပါ။  

```
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ python ./syl2freq.py ./eg-corpus.txt 
   ကောင်း  ခု  တယ်  နေ  နော်  ပါ  ဘာ  လုပ်  လဲ  သ  အ  အောင်
0       1   0    1   1     1   0   0     0   0  0  0      0
1       0   1    0   1     0   0   1     1   1  1  1      0
2       1   0    0   2     1   1   0     0   0  0  0      1
3       0   1    1   1     0   0   0     2   0  0  2      0
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$
```

## 38. [syl2tf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2tf.py)  

tf-idf ရဲ့ tf အပိုင်းကို တွက်ပြထားတာပါ။  

အထက်က 37 က python code လိုပါပဲ။ ဒီတစ်ခါတော့ count လုပ်ထားတာကို CountVectorizer ကို မသုံးတော့ပဲနဲ့ TfidfVectorizer ကို သုံးပါမယ်။ input file ကိုလည်း eg-corpus.txt ကိုပဲ သုံးပါမယ်။ ဒီတစ်ခါ ရလာတဲ့ ရလဒ်တွေကတော့ percentage နဲ့ ရလာမှာ ဖြစ်ပါတယ်။    

```
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ python ./syl2tf.py ./eg-corpus.txt 
     ကောင်း        ခု       တယ်        နေ      နော်        ပါ        ဘာ      လုပ်        လဲ         သ         အ     အောင်
0  0.250000  0.000000  0.250000  0.250000  0.250000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000
1  0.000000  0.142857  0.000000  0.142857  0.000000  0.000000  0.142857  0.142857  0.142857  0.142857  0.142857  0.000000
2  0.166667  0.000000  0.000000  0.333333  0.166667  0.166667  0.000000  0.000000  0.000000  0.000000  0.000000  0.166667
3  0.000000  0.142857  0.142857  0.142857  0.000000  0.000000  0.000000  0.285714  0.000000  0.000000  0.285714  0.000000
```

## 39. [syl2idf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2idf.py)  

ဒီတစ်ခါတော့ tf-idf ရဲ့ idf အပိုင်းတွက်တာကိုပဲ လုပ်ပြထားတာပါ။  

```
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ python ./syl2idf.py ./eg-corpus.txt 
   feature_name  idf_weights
0        ကောင်း     1.510826
1            ခု     1.510826
2           တယ်     1.510826
3            နေ     1.000000
4          နော်     1.510826
5            ပါ     1.916291
6            ဘာ     1.916291
7          လုပ်     1.510826
8            လဲ     1.916291
9             သ     1.916291
10            အ     1.510826
11        အောင်     1.916291
```

## [syl2tf-idf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2tf-idf.py) 

input ဖိုင်ထဲက မြန်မာစာ စာကြောင်းတွေကို syllable ဖြတ်ပြီးတော့ tf-idf တွက်တာကို ဥပမာအနေနဲ့ ရေးပြထားတာပါ။  
input ဖိုင်က အောက်ပါအတိုင်း  

```
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ cat eg-corpus.txt 
နေကောင်း တယ် နော်
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း အောင် နေ ပါ နော်
အခု အလုပ် လုပ် နေ တယ်
```

run ကြည့်ရင် အောက်ပါအတိုင်း output ပြပေးလိမ့်မယ်။  

```
(py3.8.10) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ python ./syl2tf-idf.py ./eg-corpus.txt 
     ကောင်း        ခု       တယ်        နေ      နော်        ပါ        ဘာ      လုပ်        လဲ         သ         အ     အောင်
0  0.539313  0.000000  0.539313  0.356966  0.539313  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000
1  0.000000  0.347852  0.000000  0.230239  0.000000  0.000000  0.441206  0.347852  0.441206  0.441206  0.347852  0.000000
2  0.378779  0.000000  0.000000  0.501420  0.378779  0.480433  0.000000  0.000000  0.000000  0.000000  0.000000  0.480433
3  0.000000  0.309520  0.309520  0.204868  0.000000  0.000000  0.000000  0.619041  0.000000  0.000000  0.619041  0.000000
```

တကယ်က အခု တင်ပေးထားတဲ့ python code လို TfidfVectorizer တစ်ခုတည်းကို import လုပ်ယူသုံးပြီး ရေးတဲ့ ပုံစံမျိုး မဟုတ်ပဲနဲ့ [syl2idf.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2idf.py)  ကိုပဲ ဝင် update လုပ်ပြီးတော့ CountVectorizer နဲ့ TfidfTransformer နှစ်ခုကိုတွဲပြီး tf-idf တွက်ခိုင်းတာလည်း လုပ်လို့ ရပါတယ်။ အဲဒီလို ရေးမယ် ဆိုရင်တော့ python code က အောက်ပါအတိုင်း ဖြစ်လိမ့်မယ်။  

```python
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import sys
import pandas as pd
import re

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Calculating syllable tf-idf by using CountVectorizer and TfidfTransformer
# Last updated: 25 Sept 2022
# How to run:
# $ python ./syl2tf-idf2.py ./eg-corpus.txt

# References
# https://github.com/gearmonkey/tfidf-python/blob/master/tfidf.py
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#:~:text=The%20formula%20that%20is%20used,document%20frequency%20of%20t%3B%20the
# https://medium.com/analytics-vidhya/demonstrating-calculation-of-tf-idf-from-sklearn-4f9526e7e78b

def sylbreak_my(line):
   myConsonant = "က-အ"
   enChar = "a-zA-Z0-9"
   otherChar = "ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
   ssSymbol = '္'
   aThat = '်'

   #Regular expression pattern for Myanmar syllable breaking
   #*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol

   BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])")
   line = line.replace(" ",'')
   line = BreakPattern.sub(" " + r"\1", line)
   line = line.strip()
   #print(line.split())
   return line.split()

with open(sys.argv[1]) as f:
    corpus = f.read().splitlines()

#Note: just dummy stop words for Myanmar, you should replaced it
my_stop_words = ['၊', '။', '၏', '၍', '၌'] 

vectorizer = CountVectorizer(tokenizer=sylbreak_my, stop_words=my_stop_words)
matrix = vectorizer.fit_transform(corpus) # this is word count vector

tfidf_transformer = TfidfTransformer()
X = tfidf_transformer.fit_transform(matrix)
#syllable_idf = pd.DataFrame({'feature_name':vectorizer.get_feature_names_out(), 'idf_weights':tfidf_transformer.idf_})
syllable_tf_idf = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(syllable_tf_idf)

```

## 41. [syl2onehot-sklearn-4teaching.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2onehot-sklearn-4teaching.py)  

syllable ဖြတ်ပြီး One-hot embedding လုပ်တာကို ဥပမာအနေနဲ့ ရေးပြထားတာပါ။ ကျောင်းသားတွေကို ရှင်းပြဖို့အတွက် သုံးခဲ့လို့ တချို့ print out လုပ်ထားတာတွေကိုပါ ထည့်ထားတဲ့ ဗားရှင်းပါ။ running output က အောက်ပါအတိုင်းပါ။  

```
(base) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ python ./syl2onehot-sklearn-4teaching.py ./eg-corpus.txt 
corpus_syl: [['နေ', 'ကောင်း', 'တယ်', 'နော်'], ['အ', 'ခု', 'ဘာ', 'လုပ်', 'နေ', 'သ', 'လဲ'], ['နေ', 'ကောင်း', 'အောင်', 'နေ', 'ပါ', 'နော်'], ['အ', 'ခု', 'အ', 'လုပ်', 'လုပ်', 'နေ', 'တယ်']]
syllables: ['နေ', 'ကောင်း', 'တယ်', 'နော်', 'အ', 'ခု', 'ဘာ', 'လုပ်', 'နေ', 'သ', 'လဲ', 'နေ', 'ကောင်း', 'အောင်', 'နေ', 'ပါ', 'နော်', 'အ', 'ခု', 'အ', 'လုပ်', 'လုပ်', 'နေ', 'တယ်']
type of syllables variable <class 'list'>
Label Encoded: [ 3  0  2  4 10  1  6  7  3  9  8  3  0 11  3  5  4 10  1 10  7  7  3  2]
corpus_syl before encoding:  [['နေ', 'ကောင်း', 'တယ်', 'နော်'], ['အ', 'ခု', 'ဘာ', 'လုပ်', 'နေ', 'သ', 'လဲ'], ['နေ', 'ကောင်း', 'အောင်', 'နေ', 'ပါ', 'နော်'], ['အ', 'ခု', 'အ', 'လုပ်', 'လုပ်', 'နေ', 'တယ်']]
Onehot Encoded Matrix:
 [[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
================
input sentence:  ['နေ', 'ကောင်း', 'တယ်', 'နော်']
[[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]]
input sentence:  ['အ', 'ခု', 'ဘာ', 'လုပ်', 'နေ', 'သ', 'လဲ']
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]
input sentence:  ['နေ', 'ကောင်း', 'အောင်', 'နေ', 'ပါ', 'နော်']
[[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]]
input sentence:  ['အ', 'ခု', 'အ', 'လုပ်', 'လုပ်', 'နေ', 'တယ်']
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

## 42. [syl2onehot-sklearn.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl2onehot-sklearn.py)  

running output က အောက်ပါအတိုင်းပါ။  

```
(base) ye@ykt-pro:/media/ye/project1/cadt/student/internship/demo/text$ python ./syl2onehot-sklearn.py ./eg-corpus.txt 
[[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]
[[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

## 43. [zawgyi2unicode.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/zawgyi2unicode.py)  

ဇော်ဂျီဖောင့်ကနေ ယူနီကုဒ်ဖောင့်အဖြစ် ပြောင်းတာက NLP သမားတွေအတွက် လုပ်ကိုလုပ်ကြရပါတယ်။ conversion က ကိုယ့်ဖာသာကိုယ်လည်း လေ့လာပြီး ပြောင်းလို့ရပေမဲ့ ဒီနေရာမှာတော့ PyICU library ကို သုံးပြီး conversion လုပ်ဖို့အတွက် python script တစ်ပုဒ် ရေးပြီး ပြောင်းပြပါမယ်။  

Python code က အောက်ပါအတိုင်းပါ ...   

```python
from icu import Transliterator
import sys

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Converting Zawgyi to Unicode Encoding
# Last updated: 1 Oct 2022
# How to run:
# If you don't have icu library, do installation: "pip install PyICU"
# $ python ./zawgyi2unicode.py ./eg-corpus-zawgyi.txt
#
# References
# https://github.com/google/myanmar-tools/blob/master/clients/python/README.rst

with open(sys.argv[1]) as f:
    corpus = []
    for line in f:
        corpus.append(line.rstrip())
#print(corpus)

for zawgyi_line in corpus:
   converter = Transliterator.createInstance('Zawgyi-my')
   uni_line = converter.transliterate(zawgyi_line)
   print(uni_line)

```

Zawgyi font နဲ့ ရိုက်ထားတဲ့ စာကြောင်းလေးကြောင်းပါတဲ့ input ဖိုင် (eg-corpus-zawgyi.txt) က အောက်ပါအတိုင်းပါ။  

```
ေနေကာင္း တယ္ ေနာ္
အခု ဘာ လုပ္ ေန သလဲ
ေနေကာင္း ေအာင္ ေန ပါ ေနာ္
အခု အလုပ္ လုပ္ ေန တယ္
```

conversion လုပ်ကြည့်ရအောင် ...  

```
(base) ye@ykt-pro:/media/ye/project1/4github/zawgyi2unicode$ python ./zawgyi2unicode.py ./eg-corpus-zawgyi.txt 
နေကောင်း တယ် နော်
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း အောင် နေ ပါ နော်
အခု အလုပ် လုပ် နေ တယ်
(base) ye@ykt-pro:/media/ye/project1/4github/zawgyi2unicode$
```

## 44. [zawgyi2unicode-syl.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/zawgyi2unicode-syl.py)  

Zawgyi ကနေ Unicode encoding အဖြစ် ပြောင်းပြီးတော့ syllable unit ဖြတ်ပေးတဲ့ Python code ပါ။ အထက်က ပရိုဂရမ်နံပါတ် 44 ကိုပဲ update လုပ်ထားတာပါ။  

```
$ python ./zawgyi2unicode-syl.py ./eg-corpus-zawgyi.txt 
နေ ကောင်း တယ် နော်
အ ခု ဘာ လုပ် နေ သ လဲ
နေ ကောင်း အောင် နေ ပါ နော်
အ ခု အ လုပ် လုပ် နေ တယ်
```

## 46. [make-edit-error.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/make-edit-error.py)  

Demo running with a Khmer small dictionary that contained only 5 words.  

```
ye@lst-gpu-3090:~/exp/kh-spell/data/code$ python3 ./make-edit-error.py kh-input.txt 1
ស្រូវនាងក្រុង    ស្រូវនាងក្ររង
សហគាមី   សហគមាី
ពានព្រះឈុត       ពានពរ្ះឈុត
ប្រទាលប្រហោង     ប្រាទលប្រហោង
រន្ទា    ន្ទា
ល្គាយ    ល្គយយ
ផាង      ផផង
ជ្រែះ    ជ្រះែ
អក្ខបាដ          អក្ខបដ
ទាសីទាសា         ទាសីាទាសា
```

```
ye@lst-gpu-3090:~/exp/kh-spell/data/code$ python3 ./make-edit-error.py kh-input.txt 2
ស្រូវនាងក្រុង    សង្រូវនាងក្្រុង
សហគាមី   ហហហគាមី
ពានព្រះឈុត       ពានពរ្ះុត
ប្រទាលប្រហោង     ប្ទរាលបោរហោង
រន្ទា    រន្
ល្គាយ    ាល្គយា
ផាង      ផាងផ
ជ្រែះ    ជ្ រះ
អក្ខបាដ          ដកដ្ខបាដ
ទាសីទាសា         ទាសីទាសា
```

```
ye@lst-gpu-3090:~/exp/kh-spell/data/code$ python3 ./make-edit-error.py kh-input.txt r
ស្រូវនាងក្រុង    ស្រូវនាក្រុង
សហគាមី   សហគមគមី
ពានព្រះឈុត       ពានព្រុឈត
ប្រទាលប្រហោង     ប្រ្ាលប្រ្ហោង
រន្ទា    ្រនទា
ល្គាយ    ល្គាគ
ផាង      ផ ាង
ជ្រែះ    រ្រែះ
អក្ខបាដ          អក្ខាបដ
ទាសីទាសា         ទាសីទាាា
ye@lst-gpu-3090:~/exp/kh-spell/data/code$
```

Demo running with a 5 words Myanmar dictionary.  

```
ye@lst-gpu-3090:~/exp/kh-spell/data/code$ python3 ./make-edit-error.py my-input.txt 1
ပြားပြားဝပ်      ပြားပြးာဝပ်
ပုစွန်ဆိတ်       ပုွန်ဆိတ်
ကျွဲမြီးတို      ကွဲမြီးတို
ဝေဿန္တရာ         ဝေဿနန္တရာ
အယူခံ    အယူံခ
```

```
ye@lst-gpu-3090:~/exp/kh-spell/data/code$ python3 ./make-edit-error.py my-input.txt 2
ပြားပြားဝပ်      ပြားပြားဝပ်
ပုစွန်ဆိတ်       ပုတွန်ဆ်ိတ်
ကျွဲမြီးတို      ကျွွဲမြီးတိ
ဝေဿန္တရာ         ဝေဿဿန္တာ
အယူခံ    အူူယခံ
```

```
ye@lst-gpu-3090:~/exp/kh-spell/data/code$ python3 ./make-edit-error.py my-input.txt r
ပြားပြားဝပ်      ပြားပာြးဝပပ်
ပုစွန်ဆိတ်       ပုစွန်နဆိတ်
ကျွဲမြီးတို      ကျိွဲမြီးတြို
ဝေဿန္တရာ         ဝေဿန္ရာ
အယူခံ    အယူံခ
```

## 47. [8eval.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/8eval.py)  

Machine translation experiment တွေ ကိုလုပ်တဲ့အခါမှာ မော်ဒယ်တွေက ဘယ်လောက် ကောင်းမကောင်းကို test dataset နဲ့ အနည်းဆုံး BLEU score metric ကိုသုံးပြီး evaluation လုပ်ကြရပါတယ်။ သို့သော် မြန်မာစာ၊ ဂျပန်စာလို မျိုးအတွက်က word order အပြောင်းအလဲကိစ္စတွေပါရှိလို့ BLEU score တစ်ခုတည်းကြည့်ယုံနဲ့ မလုံလောက်ပါဘူး။ အဲဒါကြောင့် ကျောင်းသားတွေကို BLEU score အပြင် RIBES score, chrF++ score နဲ့ တိုင်းခိုင်းတာတွေ လုပ်ပြီးတော့၊ error analysis အသေးစိတ်လုပ်ဖို့အတွက်လည်း SCLITE toolkit ကို သုံးပြီး WER score တွက်ထုတ်ခိုင်းရပါတယ်။ စိတ်ကူးပေါက်လာတာနဲ့ NLTK library လို installation လုပ်ရတာလွယ်တာမျိုးနဲ့ evaluation metric ရှစ်မျိုးကို တွက်ထုတ်ပေးဖို့ code ရေးဖြစ်ခဲ့ပါတယ်။ ပေးလိုက်တဲ့ reference, hypothesis (မော်ဒယ်က ထွက်လာတဲ့ output) ကို ယူပြီး BLEU, RIBES, chrF++, NIST, WER, GLEU, TER, ROUGE စုစုပေါင်း ၈မျိုးနဲ့ evaluation score တွေကို တွက်ထုတ်ပေးပါလိမ့်မယ်။ Reference, hypothesis ကိုလည်း sentence level ရော corpus level ရော နှစ်မျိုးစလုံးကို လက်ခံပေးနိုင်မှာမို့ အသုံးဝင်ပါလိမ့်မယ်။  

Sentence level အတွက် example running ကတော့ အောက်ပါအတိုင်းပါ။  

```
python 8eval.py --level sentence --reference "နေ ကောင်း လား" --hypothesis "နေ ကောင်း တယ်"
Sentence BLEU score: 0.21177974141341938
Sentence RIBES score: 0.9036020036098448
Sentence chrF++ score: 0.6317279942279942
Sentence NIST score: 1.0566416671474375
Sentence WER score: 0.23076923076923078
Sentence GLEU score: 0.5
Sentence TER score: 0.23076923076923078
Sentence ROUGE scores: [{'rouge-1': {'r': 0.6666666666666666, 'p': 0.6666666666666666, 'f': 0.6666666616666668}, 'rouge-2': {'r': 0.5, 'p': 0.5, 'f': 0.4999999950000001}, 'rouge-l': {'r': 0.6666666666666666, 'p': 0.6666666666666666, 'f': 0.6666666616666668}}]
```

Corpus level အတွက် example running ကတော့ အောက်ပါအတိုင်းပါ။  

```
type ref.txt
နေကောင်း လား
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း ပါ စေ
မြန်မြန် သွား နော်
သွား ပြီ လား
သွား ပါ ပြီ
```

```
type hyp.txt
နေကောင်း ရဲ့ လား
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း ပါ ပြီ
မြန်မြန် သွား
သွား ပြီ လား
သွား ပြီ
```

```
python 8eval.py --level corpus --reference ref.txt --hypothesis hyp.txt
Corpus BLEU score: 0.5102547701105773
Corpus RIBES score: 0.7930722386200673
Corpus chrF++ score: 0.7749542696450177
Corpus NIST score: 3.3797203595001917
Corpus WER score: 0.2222222222222222
Corpus GLEU score: 0.6818181818181818
Corpus TER score: 0.24999999999999997
Average Corpus ROUGE scores: {'rouge-1': {'r': 0.8333333333333334, 'p': 0.8888888888888888, 'f': 0.8444444395444446}, 'rouge-2': {'r': 0.5, 'p': 0.5833333333333334, 'f': 0.527777774537037}, 'rouge-l': {'r': 0.8333333333333334, 'p': 0.8888888888888888, 'f': 0.8444444395444446}}
```

## 48. [soundex-metaphone.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/soundex-metaphone.py)  

Soundex ရဲ့ patent ကတော့ 1918, 1922 က တင်ထားတာမို့လို့ တော်တော်ကြာပြီဖြစ်တဲ့ algorithm ပါပဲ။ Phonetic algorithm ဖြစ်ပြီး အင်္ဂလိပ်နာမည်တွေကို ရှာဖွေတဲ့အခါမှာ စာလုံးပေါင်းတာကွဲပေမဲ့ အသံတူ (သို့) အသံဆင်တူတဲ့ နာမည်တွေကိုလည်း ဆွဲထုတ်ယူနိုင်ဖို့ အတွက် အဓိကသုံးပါတယ်။ Robert C. Russell နဲ့ Margaret King Odell က တင်ခဲ့တဲ့ proposal ပါ။ Metaphone ကတော့ Soundex algorithm ကို အခြေခံပြီး ပိုကောင်းအောင် လုပ်ထားတဲ့ phonetic algorithm တစ်ခုပါ။ Lawrence Philips က 1990 မှာ proposal တင်ခဲ့တာ ဖြစ်ပါတယ်။  

[soundex-metaphone.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/soundex-metaphone.py) ကတော့ ပေးလိုက်တဲ့ အင်္ဂလိပ်စာလုံးတွေကို Soundex သို့မဟုတ် Metaphone code တွေအဖြစ် ပြောင်းပေးတဲ့ Python script ပါ။ ပထမဆုံး run သူတွေအတွက် အဆင်ပြေအောင်လို့ running demo ကတော့ အောက်ပါအတိုင်းပါ  

```
>type en-word.txt
car
telephone
English
Myanmar
John
```

```
>python soundex-metaphone.py -f en-word.txt -c "soundex"
C600
T415
E524
M560
J500
```

```
>python soundex-metaphone.py -f en-word.txt -c "metaphone"
('KR', '')
('TLFN', '')
('ANKLX', 'ANLX')
('MNMR', '')
('JN', 'AN')
 ```

## 49. [7sim.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/7sim.py)  

Running example က အောက်ပါအတိုင်းပါ။  
စာကြောင်း နှစ်ကြောင်းအတွက် similarity score တွေ တွက်ကြည့်ချင်တယ် ဆိုရင် ...  

```
python 7sim.py -m jaccard "သမီးတော်" "သမားတော်"
jaccard: 0.7777777777777778
```

ဒီတစ်ခါတော့ Levenshtein score တွက်ကြည့်တာပါ။  

```
>python 7sim.py -m levenshtein "သမီးတော်" "သမားတော်"
levenshtein: 1
```

LCS ration တွက်ကြည့်တဲ့ ဥပမာ ...  

```
>python 7sim.py -m lcs_ratio "သမီးတော်" "သမားတော်"
lcs_ratio: 0.875
```

Similarity score ကို ၇မျိုးစလုံးနဲ့ တွက်ကြည့်တဲ့ ဥပမာ ...  

```
>python 7sim.py -m all "သမီးတော်" "သမားတော်"
levenshtein: 1
jaro_winkler: 0.9333333333333333
cosine: 0.875
dices_coefficient: 0.875
jaccard: 0.7777777777777778
lcs_ratio: 0.875
sorensen_dice_coefficient: 0.875
```

Reference နဲ့ Hypothesis ဖိုင်နှစ်ဖိုင်ကို သုံးပြီး တွက်တဲ့ ဥပမာက အောက်ပါအတိုင်းပါ။  

```
>type ref.txt
နေကောင်း လား
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း ပါ စေ
မြန်မြန် သွား နော်
သွား ပြီ လား
သွား ပါ ပြီ
```

```
>type hyp.txt
နေကောင်း ရဲ့ လား
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း ပါ ပြီ
မြန်မြန် သွား
သွား ပြီ လား
သွား ပြီ
```

```
>python 7sim.py -m all ref.txt hyp.txt
levenshtein: 14
jaro_winkler: 0.8911530972374345
cosine: 0.9326431430741515
dices_coefficient: 0.9325842696629213
jaccard: 0.8736842105263158
lcs_ratio: 0.9101123595505618
sorensen_dice_coefficient: 0.9325842696629213
```

```
>python 7sim.py --help
usage: 7sim.py [-h] [-m MEASUREMENT] text1 text2

String similarity measurements

positional arguments:
  text1                 First text string or file
  text2                 Second text string or file

optional arguments:
  -h, --help            show this help message and exit
  -m MEASUREMENT, --measurement MEASUREMENT
                        String similarity measurement to use: levenshtein, jaro_winkler, cosine,
                        dices_coefficient, jaccard, lcs_ratio, sorensen_dice_coefficient
```

## 50. [abugida.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/abugida.py)  

ဒီ ပရိုဂရမ်က မြန်မာ ဘာသာစကားအပါအဝင် ထိုင်း၊ ကမာ၊ လာအို စတဲ့ Abugida စနစ် ဘာသာစကားတွေမှာ တူညီတဲ့ writing system ရှိတယ် ဆိုတာကို ကျောင်းသားတွေကို ပြဖို့အတွက် ရေးခဲ့တာ ဖြစ်ပါတယ်။ ဥပမာ အနေနဲ့ နှိုင်းယှဉ်ပြီး လေ့လာနိုင်အောင် နံပါတ်၊ ဗျည်း နဲ့ သရ စာလုံးတွေကို ရိုက်ထုတ်ပြထားတာဖြစ်ပါတယ်။ ဘာသာစကား တစ်ခုစီမှာ ပါဝင်တဲ့ စာလုံး အားလုံးပါဝင်တာတော့ မဟုတ်ပါဘူး။ အဲဒါကြောင့် လိုအပ်ရင် လက်ရှိ ပရိုဂရမ်မှာ ထားထားတဲ့ Unicode range ကို ပြင်သုံးပါ။ Running example တချို့က အောက်ပါအတိုင်းပါ။  

help screen ခေါ်ကြည့်ရင် ...  

```
python abugida.py -h
usage: abugida.py [-h] [-a] [-l LANGUAGE] [-g GROUP]

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Print all characters for each language
  -l LANGUAGE, --language LANGUAGE
                        Print characters for one language. Available languages are: my (Burmese), th
                        (Thai), km (Khmer), lo (Laos), hi (Hindi), mr (Marathi), bn (Bengali), si
                        (Sinhala), ml (Malayalam), ta (Tamil), te (Telugu), kn (Kannada), bl
                        (Balinese), jv (Javanese), sd (Sundanese), as (Assamese), gu (Gujarati), pa
                        (Gurmukhi), or (Odia), bo (Tibetan)
  -g GROUP, --group GROUP
                        Print characters for a group of languages. Available groups are: ni (Assamese,
                        Bengali, Hindi, Gujarati, Gurmukhi, Odia, Tibetan), si (Sinhala, Malayalam,
                        Tamil, Telugu, Kannada), m (Burmese, Khmer, Thai, Laos), t (Balinese, Javanese,
                        Sundanese), Here, ni for Northern Indian languages, si for Southern Indian
                        languages, m for SouthEast Asian, mainland languages and t for SouthEase Asian,
                        maritime languages
```

Northern Indian Abugida  ဘာသာစကားတွေကိုပဲ print လုပ်စေချင်ရင် ...  

```
python abugida.py -g ni

Language: Assamese

Numbers:
০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮
Consonants:
ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন ঩ প ফ ব ভ ম য র ঱ ল ঳ ঴ ঵ শ ষ স
Vowels:
অ আ ই ঈ উ ঊ ঋ ঌ ঍ ঎ এ ঐ ঑ ঒ ও


Language: Bengali

Numbers:
০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮
Consonants:
ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন ঩ প ফ ব ভ ম য র ঱ ল ঳ ঴ ঵ শ ষ স
Vowels:
অ আ ই ঈ উ ঊ ঋ ঌ ঍ ঎ এ ঐ ঑ ঒ ও


Language: Hindi

Numbers:
० १ २ ३ ४ ५ ६ ७ ८
Consonants:
क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न ऩ प फ ब भ म य र ऱ ल ळ ऴ व श ष स
Vowels:
अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ ए ऐ ऑ ऒ ओ


Language: Gujarati

Numbers:
૦ ૧ ૨ ૩ ૪ ૫ ૬ ૭ ૮
Consonants:
ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન ઩ પ ફ બ ભ મ ય ર ઱ લ ળ ઴ વ શ ષ સ
Vowels:
અ આ ઇ ઈ ઉ ઊ ઋ ઌ ઍ ઎ એ ઐ ઑ ઒ ઓ


Language: Gurmukhi

Numbers:
੦ ੧ ੨ ੩ ੪ ੫ ੬ ੭ ੮
Consonants:
ਕ ਖ ਗ ਘ ਙ ਚ ਛ ਜ ਝ ਞ ਟ ਠ ਡ ਢ ਣ ਤ ਥ ਦ ਧ ਨ ਩ ਪ ਫ ਬ ਭ ਮ ਯ ਰ ਱ ਲ ਲ਼ ਴ ਵ ਸ਼ ਷ ਸ
Vowels:
ਅ ਆ ਇ ਈ ਉ ਊ ਋ ਌ ਍ ਎ ਏ ਐ ਑ ਒ ਓ


Language: Odia

Numbers:
୦ ୧ ୨ ୩ ୪ ୫ ୬ ୭ ୮
Consonants:
କ ଖ ଗ ଘ ଙ ଚ ଛ ଜ ଝ ଞ ଟ ଠ ଡ ଢ ଣ ତ ଥ ଦ ଧ ନ ଩ ପ ଫ ବ ଭ ମ ଯ ର ଱ ଲ ଳ ଴ ଵ ଶ ଷ ସ
Vowels:
ଅ ଆ ଇ ଈ ଉ ଊ ଋ ଌ ଍ ଎ ଏ ଐ ଑ ଒ ଓ


Language: Tibetan

Numbers:
༠ ༡ ༢ ༣ ༤ ༥ ༦ ༧ ༨
Consonants:
ཀ ཁ ག གྷ ང ཅ ཆ ཇ ཈ ཉ ཊ ཋ ཌ ཌྷ ཎ ཏ ཐ ད དྷ ན པ ཕ བ བྷ མ ཙ ཚ ཛ ཛྷ ཝ ཞ ཟ འ ཡ ར ལ ཤ ཥ ས ཧ ཨ ཀྵ ཪ ཫ
Vowels:
ི ཱི ུ ཱུ ྲྀ ཷ ླྀ ཹ ེ ཻ ོ ཽ ཾ ཿ
```

language တစ်ခုချင်းစီကိုပဲ ရိုက်ထုတ်စေချင်ရင် -l or --language ဆိုတဲ့ option ကို သုံးပါ ...  

```
python abugida.py -l my

Language: Burmese

Numbers:
၀ ၁ ၂ ၃ ၄ ၅ ၆ ၇ ၈ ၉
Consonants:
က ခ ဂ ဃ င စ ဆ ဇ ဈ ဉ ည ဋ ဌ ဍ ဎ ဏ တ ထ ဒ ဓ န ပ ဖ ဗ ဘ မ ယ ရ လ ဝ သ ဟ ဠ အ
Vowels:
ါ ာ ိ ီ ု
```

Abugida ဘာသာစကား အားလုံးကို ရိုက်ထုတ်ပေးစေချင်ရင်တော့ -a or -all option ကို သုံးလို့ ရပါတယ်။ ဒီနေရာမှာတော့ running output screen ကို မပြတော့ဘူး။  

## 52. [video_augment.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/video_augment.py)  

CADT မှာ တစ်နှစ်ခန့် လူကိုယ်တိုင် သွားလိုက်ပြန်လိုက် လုပ်ပြီး Visiting Professor လုပ်ခဲ့တဲ့ အလုပ်ရဲ့ အဆက်အနေနဲ့ ITC တက္ကသိုလ်က နောက်ဆုံးနှစ် အင်ဂျင်နီယာ ကျောင်းသား ၅ယောက်ကို undergrad thesis ရေးနိုင်ဖို့အတွက် အပတ်စဉ် seminar လုပ်ပေးပြီး သင်ပေးစရာရှိတာတွေကို သင်ပေးနေဖြစ်တယ်။ ကျောင်းသား သုံးယောက်နဲ့က Cambodia Sign Language Video Recognition ပရောဂျက်အတွက် corpus အသစ်တစ်ခု ဆောက်ဖြစ်ခဲ့တယ်။ ထုံးစံအတိုင်း ဗီဒီယို ဒေတာက class တစ်ခုကို sign language ဗီဒီယို တစ်ဖိုင်ရဖို့တောင် တော်တော် ကြိုးစားရတာလေ။ အဲဒါကြောင့် လက်ရှိ ရှိနေတဲ့ ဗီဒီယို ဒေတာတွေကို data augmentation လုပ်ဖို့ ကျောင်းသားတွေကို အကြံပေးခဲ့တယ်။ အဲဒီအတွက် demo code အဖြစ် ရေးပြထားတဲ့ python script ပါ။  

Running example ကတော့ အောက်ပါအတိုင်းပါ။  
အရင်ဆုံး လိုအပ်တဲ့ library တွေရှိတဲ့ Anaconda environment ထဲကို ဝင်ပါတယ်။  

```
(base) rnd@gpu:~/demo/vr$ conda activate sl-vr
```

1v/ လို့ နာမည်ပေးထားတဲ့ ဖိုလ်ဒါအောက်မှာ ရှိတဲ့ ဗီဒီယိုဖိုင် တစ်ဖိုင်ကို တည်ပြီး နမူနာအနေနဲ့ augmentation လုပ်ပြပါမယ်။  

```
(base) rnd@gpu:~/demo/vr/1v$ ls
ខាំ.mp4
```

temporal augmentation ဆိုတာကတော့ လှုပ်ရှားမှုကို နှေးအောင်၊ မြန်အောင် လုပ်တာမျိုးပါ။  

```
(sl-vr) rnd@gpu:~/demo/vr$ time python ./video_augment.py --input_folder ./1v/ --output_folder ./1v/temporal/ --augment temporal

real    0m7.612s
user    0m6.764s
sys     0m0.471s
```

spatial augmentation ကိုလည်း အလွယ် ဒေါင်လိုက် shift လုပ်တာကို လုပ်ပြထားတယ်လို့ ထင်တယ်။  

```
(sl-vr) rnd@gpu:~/demo/vr$ time python ./video_augment.py --input_folder ./1v/ --output_folder ./1v/spatial/ --augment spatial

real    0m6.273s
user    0m8.083s
sys     0m1.432s
```

noise ကိုလည်း မြင်သာအောင် weight များများပေးပြီး ဥပမာ လုပ်ပြထားပါတယ်။ မဟုတ်ရင် လူမျက်စိနဲ့ ကြည့်ရင် မသိသာတာမျိုးလည်း ဖြစ်တတ်လို့။   

```
(sl-vr) rnd@gpu:~/demo/vr$ time python ./video_augment.py --input_folder ./1v/ --output_folder ./1v/noise/ --augment noise

real    0m39.320s
user    0m33.797s
sys     0m5.597s
```

ဒီတစ်ခေါက်တော့ brightness, contrast ကို ကစားထားတာပါ။  

```
(sl-vr) rnd@gpu:~/demo/vr$ time python ./video_augment.py --input_folder ./1v/ --output_folder ./1v/brightness_contrast/ --augment brightness_contrast

real    0m21.550s
user    0m15.165s
sys     0m6.995s
(sl-vr) rnd@gpu:~/demo/vr$
```

ဒီနေရာမှာ တစ်ခု သတိထားရမှာက augmented video တွေကို original video ရှိတဲ့ ဖိုလ်ဒါမှာပဲ output လုပ်ရင် နောက်ထပ် augmentation တစ်မျိုးထပ် run တဲ့အခါမှာ အဲဒီ 1v/ folder အောက်မှာ ရှိသမျှဖိုင်ကို ဝင် augmentation လုပ်သွားမှာမို့လို့ အခု နမူနာ လုပ်ပြထားသလို augmentation method တစ်မျိုးကို ဖိုလ်ဒါတစ်ခုစီမှာ ခွဲလုပ်တာက ဘယ်လိုပြောင်းလဲသွားသလဲ ဆိုတာကို လေ့လာဖို့အတွက် ပိုအဆင်ပြေပါလိမ့်မယ်။ မဟုတ်ရင် temporal-spatial, temporal-spatial-noise စတဲ့ combination output တွေ ထွက်လာမှာမို့လို့ ...  

## 53. [mk-video-class.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk-video-class.py)  

Augmented လုပ်ထားတဲ့ Cambodian Sign Language ဗီဒီယိုဖိုင်တွေက အောက်ပါအတိုင်း ရှိနေတယ်။  

```
(base) rnd@gpu:~/demo/vr$ tree videos
videos
├── brightness_contrast
│   ├── ខាំ-brightness_contrast.mp4
│   ├── ខាត-brightness_contrast.mp4
│   ├── ខួរក្បាល-brightness_contrast.mp4
│   ├── ខេត្តព្រះសីហនុ -brightness_contrast.mp4
│   ├── ខេត្តមណ្ឌលគិរី -brightness_contrast.mp4
│   ├── ខែ-brightness_contrast.mp4
│   ├── ខែ្ស -brightness_contrast.mp4
│   ├── ខោ-brightness_contrast.mp4
│   ├── ខ្ជិល-brightness_contrast.mp4
│   ├── ខ្ទង់-brightness_contrast.mp4
│   ├── ខ្ទង់រយ-brightness_contrast.mp4
│   ├── ខ្ទង់រាយ-brightness_contrast.mp4
│   ├── ខ្ទឹម-brightness_contrast.mp4
│   ├── ខ្មែរ-brightness_contrast.mp4
│   ├── ខ្មៅ-brightness_contrast.mp4
│   └── ខ្លី-brightness_contrast.mp4
├── noise
│   ├── ខាំ-noise.mp4
│   ├── ខាត-noise.mp4
│   ├── ខួរក្បាល-noise.mp4
│   ├── ខេត្តព្រះសីហនុ -noise.mp4
│   ├── ខេត្តមណ្ឌលគិរី -noise.mp4
│   ├── ខែ-noise.mp4
│   ├── ខែ្ស -noise.mp4
│   ├── ខោ-noise.mp4
│   ├── ខ្ជិល-noise.mp4
│   ├── ខ្ទង់-noise.mp4
│   ├── ខ្ទង់រយ-noise.mp4
│   ├── ខ្ទង់រាយ-noise.mp4
│   ├── ខ្ទឹម-noise.mp4
│   ├── ខ្មែរ-noise.mp4
│   ├── ខ្មៅ-noise.mp4
│   └── ខ្លី-noise.mp4
├── spatial
│   ├── ខាំ-spatial.mp4
│   ├── ខាត-spatial.mp4
│   ├── ខួរក្បាល-spatial.mp4
│   ├── ខេត្តព្រះសីហនុ -spatial.mp4
│   ├── ខេត្តមណ្ឌលគិរី -spatial.mp4
│   ├── ខែ-spatial.mp4
│   ├── ខែ្ស -spatial.mp4
│   ├── ខោ-spatial.mp4
│   ├── ខ្ជិល-spatial.mp4
│   ├── ខ្ទង់-spatial.mp4
│   ├── ខ្ទង់រយ-spatial.mp4
│   ├── ខ្ទង់រាយ-spatial.mp4
│   ├── ខ្ទឹម-spatial.mp4
│   ├── ខ្មែរ-spatial.mp4
│   ├── ខ្មៅ-spatial.mp4
│   └── ខ្លី-spatial.mp4
├── temporal
│   ├── ខាំ-temporal.mp4
│   ├── ខាត-temporal.mp4
│   ├── ខួរក្បាល-temporal.mp4
│   ├── ខេត្តព្រះសីហនុ -temporal.mp4
│   ├── ខេត្តមណ្ឌលគិរី -temporal.mp4
│   ├── ខែ-temporal.mp4
│   ├── ខែ្ស -temporal.mp4
│   ├── ខោ-temporal.mp4
│   ├── ខ្ជិល-temporal.mp4
│   ├── ខ្ទង់-temporal.mp4
│   ├── ខ្ទង់រយ-temporal.mp4
│   ├── ខ្ទង់រាយ-temporal.mp4
│   ├── ខ្ទឹម-temporal.mp4
│   ├── ខ្មែរ-temporal.mp4
│   ├── ខ្មៅ-temporal.mp4
│   └── ខ្លី-temporal.mp4
├── ខាំ.mp4
├── ខាត.mp4
├── ខួរក្បាល.mp4
├── ខេត្តព្រះសីហនុ .mp4
├── ខេត្តមណ្ឌលគិរី .mp4
├── ខែ.mp4
├── ខែ្ស .mp4
├── ខោ.mp4
├── ខ្ជិល.mp4
├── ខ្ទង់.mp4
├── ខ្ទង់រយ.mp4
├── ខ្ទង់រាយ.mp4
├── ខ្ទឹម.mp4
├── ខ្មែរ.mp4
├── ខ្មៅ.mp4
└── ខ្លី.mp4

4 directories, 80 files
(base) rnd@gpu:~/demo/vr$
```

လုပ်ချင်တာက basename တူတာတွေအားလုံးကို ဖိုင်ဒါတစ်ခုအောက်ထဲမှာ သိမ်းချင်တယ်လေ။ အဲဒါမှ ၅ဖိုင် ကို class တစ်ခုအနေနဲ့ သတ်မှတ်ပြီးတော့ video recognition မော်ဒယ်ဆောက်နိုင်မှာပေါ့။ အဲဒီအတွက် mk-video-class.py ကို ရေးခဲ့တာပါ။ Example running လုပ်ပြရရင် အောက်ပါအတိုင်းပါ။  

--help နဲ့ helpscreen ခေါ်ကြည့်လို့ ရတယ်။  

```
(base) rnd@gpu:~/demo/vr$ python ./mk-video-class.py --help
usage: mk-video-class.py [-h] [-i] base_dir output_folder

Sort files into class directories.

positional arguments:
  base_dir       The directory containing the files to sort.
  output_folder  The directory to output the class directories to.

optional arguments:
  -h, --help     show this help message and exit
  -i, --index    Use indexed class names instead of the original names.
(base) rnd@gpu:~/demo/vr$
```

Run တဲ့အခါမှာ --index option ကို ထည့်ပြီးတော့ မ run ရင်လည်း ရတယ်။  
ဒီနေရာမှာ videos ဆိုတာက အထက်မှာ ပြခဲ့တဲ့ augmented ဗီဒီယိုဖိုင်တွေရှိတဲ့ ဖိုလ်ဒါပါ။  
data ဆိုတဲ့ ဖိုလ်ဒါကတော့ output folder path ပါ။  

```
(base) rnd@gpu:~/demo/vr$ (base) rnd@gpu:~/demo/vr$ time python ./mk-video-class.py videos data

real    0m0.733s
user    0m0.096s
sys     0m0.636s
```

တကယ်လို့ --index or -i option ကို ထည့်ပြီးတော့ run တာ မဟုတ်ရင်တော့ ကမ္ဘောဒီးယား basename တွေနဲ့ပဲ class folder တွေ ဆောက်ပေးသွားလိမ့်မယ်။  

```
(base) rnd@gpu:~/demo/vr$ (base) rnd@gpu:~/demo/vr$ tree data
data
├── ខាំ
│   ├── ខាំ-brightness_contrast.mp4
│   ├── ខាំ.mp4
│   ├── ខាំ-noise.mp4
│   ├── ខាំ-spatial.mp4
│   └── ខាំ-temporal.mp4
├── ខាត
│   ├── ខាត-brightness_contrast.mp4
│   ├── ខាត.mp4
│   ├── ខាត-noise.mp4
│   ├── ខាត-spatial.mp4
│   └── ខាត-temporal.mp4
├── ខួរក្បាល
│   ├── ខួរក្បាល-brightness_contrast.mp4
│   ├── ខួរក្បាល.mp4
│   ├── ខួរក្បាល-noise.mp4
│   ├── ខួរក្បាល-spatial.mp4
│   └── ខួរក្បាល-temporal.mp4
├── ខេត្តព្រះសីហនុ
│   ├── ខេត្តព្រះសីហនុ -brightness_contrast.mp4
│   ├── ខេត្តព្រះសីហនុ .mp4
│   ├── ខេត្តព្រះសីហនុ -noise.mp4
│   ├── ខេត្តព្រះសីហនុ -spatial.mp4
│   └── ខេត្តព្រះសីហនុ -temporal.mp4
├── ខេត្តមណ្ឌលគិរី
│   ├── ខេត្តមណ្ឌលគិរី -brightness_contrast.mp4
│   ├── ខេត្តមណ្ឌលគិរី .mp4
│   ├── ខេត្តមណ្ឌលគិរី -noise.mp4
│   ├── ខេត្តមណ្ឌលគិរី -spatial.mp4
│   └── ខេត្តមណ្ឌលគិរី -temporal.mp4
├── ខែ
│   ├── ខែ-brightness_contrast.mp4
│   ├── ខែ.mp4
│   ├── ខែ-noise.mp4
│   ├── ខែ-spatial.mp4
│   ├── ខែ-temporal.mp4
│   ├── ខែ្ស -brightness_contrast.mp4
│   ├── ខែ្ស .mp4
│   ├── ខែ្ស -noise.mp4
│   ├── ខែ្ស -spatial.mp4
│   └── ខែ្ស -temporal.mp4
├── ខែ្ស
│   ├── ខែ្ស -brightness_contrast.mp4
│   ├── ខែ្ស .mp4
│   ├── ខែ្ស -noise.mp4
│   ├── ខែ្ស -spatial.mp4
│   └── ខែ្ស -temporal.mp4
├── ខោ
│   ├── ខោ-brightness_contrast.mp4
│   ├── ខោ.mp4
│   ├── ខោ-noise.mp4
│   ├── ខោ-spatial.mp4
│   └── ខោ-temporal.mp4
├── ខ្ជិល
│   ├── ខ្ជិល-brightness_contrast.mp4
│   ├── ខ្ជិល.mp4
│   ├── ខ្ជិល-noise.mp4
│   ├── ខ្ជិល-spatial.mp4
│   └── ខ្ជិល-temporal.mp4
├── ខ្ទង់
│   ├── ខ្ទង់-brightness_contrast.mp4
│   ├── ខ្ទង់.mp4
│   ├── ខ្ទង់-noise.mp4
│   ├── ខ្ទង់-spatial.mp4
│   ├── ខ្ទង់-temporal.mp4
│   ├── ខ្ទង់រយ-brightness_contrast.mp4
│   ├── ខ្ទង់រយ.mp4
│   ├── ខ្ទង់រយ-noise.mp4
│   ├── ខ្ទង់រយ-spatial.mp4
│   ├── ខ្ទង់រយ-temporal.mp4
│   ├── ខ្ទង់រាយ-brightness_contrast.mp4
│   ├── ខ្ទង់រាយ.mp4
│   ├── ខ្ទង់រាយ-noise.mp4
│   ├── ខ្ទង់រាយ-spatial.mp4
│   └── ខ្ទង់រាយ-temporal.mp4
├── ខ្ទង់រយ
│   ├── ខ្ទង់រយ-brightness_contrast.mp4
│   ├── ខ្ទង់រយ.mp4
│   ├── ខ្ទង់រយ-noise.mp4
│   ├── ខ្ទង់រយ-spatial.mp4
│   └── ខ្ទង់រយ-temporal.mp4
├── ខ្ទង់រាយ
│   ├── ខ្ទង់រាយ-brightness_contrast.mp4
│   ├── ខ្ទង់រាយ.mp4
│   ├── ខ្ទង់រាយ-noise.mp4
│   ├── ខ្ទង់រាយ-spatial.mp4
│   └── ខ្ទង់រាយ-temporal.mp4
├── ខ្ទឹម
│   ├── ខ្ទឹម-brightness_contrast.mp4
│   ├── ខ្ទឹម.mp4
│   ├── ខ្ទឹម-noise.mp4
│   ├── ខ្ទឹម-spatial.mp4
│   └── ខ្ទឹម-temporal.mp4
├── ខ្មែរ
│   ├── ខ្មែរ-brightness_contrast.mp4
│   ├── ខ្មែរ.mp4
│   ├── ខ្មែរ-noise.mp4
│   ├── ខ្មែរ-spatial.mp4
│   └── ខ្មែរ-temporal.mp4
├── ខ្មៅ
│   ├── ខ្មៅ-brightness_contrast.mp4
│   ├── ខ្មៅ.mp4
│   ├── ខ្មៅ-noise.mp4
│   ├── ខ្មៅ-spatial.mp4
│   └── ខ្មៅ-temporal.mp4
└── ខ្លី
    ├── ខ្លី-brightness_contrast.mp4
    ├── ខ្លី.mp4
    ├── ខ្លី-noise.mp4
    ├── ខ្លី-spatial.mp4
    └── ខ្លី-temporal.mp4

16 directories, 95 files
(base) rnd@gpu:~/demo/vr$
```

တကယ်လို့ --index option နဲ့ run မယ် ဆိုရင်တော့ class နာမည်တွေကို 1, 2, 3 အသီးသီး ပေးသွားမှာမို့ command line environment မှာ လုပ်ရကိုင်ရတာ ပိုလွယ်ကူတာပေါ့။    

```
(base) rnd@gpu:~/demo/vr$ time python ./mk-video-class.py videos class --index

real    0m1.459s
user    0m0.108s
sys     0m0.676s
(base) rnd@gpu:~/demo/vr$
```

--index option နဲ့ run ပြီး ထွက်လာမယ့် output ကတော့ အောက်ပါအတိုင်းပါ။  

```
(base) rnd@gpu:~/demo/vr$ tree class
class
├── 1
│   ├── ខេត្តមណ្ឌលគិរី -brightness_contrast.mp4
│   ├── ខេត្តមណ្ឌលគិរី .mp4
│   ├── ខេត្តមណ្ឌលគិរី -noise.mp4
│   ├── ខេត្តមណ្ឌលគិរី -spatial.mp4
│   └── ខេត្តមណ្ឌលគិរី -temporal.mp4
├── 10
│   ├── ខ្មៅ-brightness_contrast.mp4
│   ├── ខ្មៅ.mp4
│   ├── ខ្មៅ-noise.mp4
│   ├── ខ្មៅ-spatial.mp4
│   └── ខ្មៅ-temporal.mp4
├── 11
│   ├── ខ្ទឹម-brightness_contrast.mp4
│   ├── ខ្ទឹម.mp4
│   ├── ខ្ទឹម-noise.mp4
│   ├── ខ្ទឹម-spatial.mp4
│   └── ខ្ទឹម-temporal.mp4
├── 12
│   ├── ខ្មែរ-brightness_contrast.mp4
│   ├── ខ្មែរ.mp4
│   ├── ខ្មែរ-noise.mp4
│   ├── ខ្មែរ-spatial.mp4
│   └── ខ្មែរ-temporal.mp4
├── 13
│   ├── ខ្ទង់-brightness_contrast.mp4
│   ├── ខ្ទង់.mp4
│   ├── ខ្ទង់-noise.mp4
│   ├── ខ្ទង់-spatial.mp4
│   ├── ខ្ទង់-temporal.mp4
│   ├── ខ្ទង់រយ-brightness_contrast.mp4
│   ├── ខ្ទង់រយ.mp4
│   ├── ខ្ទង់រយ-noise.mp4
│   ├── ខ្ទង់រយ-spatial.mp4
│   ├── ខ្ទង់រយ-temporal.mp4
│   ├── ខ្ទង់រាយ-brightness_contrast.mp4
│   ├── ខ្ទង់រាយ.mp4
│   ├── ខ្ទង់រាយ-noise.mp4
│   ├── ខ្ទង់រាយ-spatial.mp4
│   └── ខ្ទង់រាយ-temporal.mp4
├── 14
│   ├── ខ្ទង់រាយ-brightness_contrast.mp4
│   ├── ខ្ទង់រាយ.mp4
│   ├── ខ្ទង់រាយ-noise.mp4
│   ├── ខ្ទង់រាយ-spatial.mp4
│   └── ខ្ទង់រាយ-temporal.mp4
├── 15
│   ├── ខួរក្បាល-brightness_contrast.mp4
│   ├── ខួរក្បាល.mp4
│   ├── ខួរក្បាល-noise.mp4
│   ├── ខួរក្បាល-spatial.mp4
│   └── ខួរក្បាល-temporal.mp4
├── 16
│   ├── ខាត-brightness_contrast.mp4
│   ├── ខាត.mp4
│   ├── ខាត-noise.mp4
│   ├── ខាត-spatial.mp4
│   └── ខាត-temporal.mp4
├── 2
│   ├── ខេត្តព្រះសីហនុ -brightness_contrast.mp4
│   ├── ខេត្តព្រះសីហនុ .mp4
│   ├── ខេត្តព្រះសីហនុ -noise.mp4
│   ├── ខេត្តព្រះសីហនុ -spatial.mp4
│   └── ខេត្តព្រះសីហនុ -temporal.mp4
├── 3
│   ├── ខែ្ស -brightness_contrast.mp4
│   ├── ខែ្ស .mp4
│   ├── ខែ្ស -noise.mp4
│   ├── ខែ្ស -spatial.mp4
│   └── ខែ្ស -temporal.mp4
├── 4
│   ├── ខែ-brightness_contrast.mp4
│   ├── ខែ.mp4
│   ├── ខែ-noise.mp4
│   ├── ខែ-spatial.mp4
│   ├── ខែ-temporal.mp4
│   ├── ខែ្ស -brightness_contrast.mp4
│   ├── ខែ្ស .mp4
│   ├── ខែ្ស -noise.mp4
│   ├── ខែ្ស -spatial.mp4
│   └── ខែ្ស -temporal.mp4
├── 5
│   ├── ខោ-brightness_contrast.mp4
│   ├── ខោ.mp4
│   ├── ខោ-noise.mp4
│   ├── ខោ-spatial.mp4
│   └── ខោ-temporal.mp4
├── 6
│   ├── ខាំ-brightness_contrast.mp4
│   ├── ខាំ.mp4
│   ├── ខាំ-noise.mp4
│   ├── ខាំ-spatial.mp4
│   └── ខាំ-temporal.mp4
├── 7
│   ├── ខ្លី-brightness_contrast.mp4
│   ├── ខ្លី.mp4
│   ├── ខ្លី-noise.mp4
│   ├── ខ្លី-spatial.mp4
│   └── ខ្លី-temporal.mp4
├── 8
│   ├── ខ្ជិល-brightness_contrast.mp4
│   ├── ខ្ជិល.mp4
│   ├── ខ្ជិល-noise.mp4
│   ├── ខ្ជិល-spatial.mp4
│   └── ខ្ជិល-temporal.mp4
├── 9
│   ├── ខ្ទង់រយ-brightness_contrast.mp4
│   ├── ខ្ទង់រយ.mp4
│   ├── ខ្ទង់រយ-noise.mp4
│   ├── ខ្ទង់រយ-spatial.mp4
│   └── ខ្ទង់រយ-temporal.mp4
└── index.txt

16 directories, 96 files
(base) rnd@gpu:~/demo/vr$
```

## 54. [mk-video-class-for-sentence.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mk-video-class-for-sentence.py)  

အထက်က mk-video-class.py နဲ့ အတူတူပါပဲ။ ဒီတစ်ခါတော့ label တွေက စာကြောင်းတွေ ဖြစ်သွားလို့ ပိုရှည်လာပါလိမ့်မယ်။ အဲဒီအပြင် ဗီဒီရိုကို ရိုက်တဲ့အခါမှာ signer တွေက Cambodian Sign Language တစ်မျိုးတည်း ဆိုလိုတာက sign တစ်မျိုးတည်းကိုပဲ နှစ်ခါ၊ သုံးခါ ရိုက်တာမျိုးတွေ ရှိပါတယ်။ အဲဒီအတွက်ကို ဖိုင်နာမည်မှာ (1), (2), (3), (4) စတာတွေ ပါလာပါတယ်။ အခု Python script နံပါတ် ၅၄ က အဲဒီ ကိစ္စကို ဖြေရှင်းဖို့အတွက် ပြင်ရေးထားတာပါ။ ဆိုလိုတာက နံပါမှာ (1), (2), (3), (4) တွေ ပါလာရင်လည်း ဖိုင်နာမည်တူရင် class တစ်ခုတည်းအောက်မှာ ထားဖို့အတွက် RE ကို အဓိက ဝင်ပြင်ထားတာပါ။

Running example တချို့ကို ဥပမာအနေနဲ့ ထည့်ပေးထားလိုက်မယ်။  
coding လုပ်စဉ်မှာ ထုံးစံအတိုင်း example ဖိုင်တချို့ ကိုပဲ ထည့်ပြီး သွားပါမယ်။ မဟုတ်ရင် ကြာနေမှာမို့ ...  

အောက်ပါ video folder ကို ဥပမာအနေနဲ့ သုံးပြီး run ပြမယ်။  

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/sent$ ls
 brightness_contrast
 noise
 spatial
 temporal
'មនុស្សម្នាក់បានបាក់ដៃ(2).mp4'
'មនុស្សម្នាក់បានបាក់ដៃ(3).mp4'
'មនុស្សម្នាក់បានបាក់ដៃ(4).mp4'
'មនុស្សម្នាក់បានរងរបួស(1).mp4'
 មនុស្សម្នាក់បានរងរបួស.mp4
'មានតែអ្នកយាមអ្នកជំងឺម្នាក់ប៉ុណ្ណោះដែលនឹងត្រូវបានអនុញ្ញាតឱ្យស្នាក់នៅពេលយប់(1).mp4'
 មានតែអ្នកយាមអ្នកជំងឺម្នាក់ប៉ុណ្ណោះដែលនឹងត្រូវបានអនុញ្ញាតឱ្យស្នាក់នៅពេលយប់.mp4
 ហែលទឹក.mp4
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (1).mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (2).mp4'
'អ្នកបានបាក់ជើង (1).mp4'
'អ្នកបានបាក់ជើង (2).mp4'
'អ្នកបានបាក់ដៃ (1).mp4'
'អ្នកបានបាក់ដៃ (2).mp4'
'ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត(1).mp4'
 ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត.mp4
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/sent$
```

--index option မပါပဲ run ရင် အောက်ပါအတိုင်း class name တွေ သို့မဟုတ် class folder တွေကို ရလာပါလိမ့်မယ်။  

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing$ ls class
 មនុស្សម្នាក់បានបាក់ដៃ                                         'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ'
 មនុស្សម្នាក់បានរងរបួស                                          អ្នកបានបាក់ជើង
 មានតែអ្នកយាមអ្នកជំងឺម្នាក់ប៉ុណ្ណោះដែលនឹងត្រូវបានអនុញ្ញាតឱ្យស្នាក់នៅពេលយប់   អ្នកបានបាក់ដៃ
 ហែលទឹក                                                     ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing$
```

class folder တစ်ခုအောက်ကို ဝင်ကြည့်ရင် original video ဖိုင်ကိုရော augmented လုပ်ထားတဲ့ ဗီဒီယိုဖိုင်တွေကိုကော ပြီးတော့ (1), (2), (3), စသည်ဖြင့် ခွဲထားတဲ့ ဖိုင်နာမည်တူတွေရော အတူတူ စုပေးထားတာကို တွေ့ရပါလိမ့်မယ်။  

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing$ cd class
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/class$ cd ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/class/ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត$ ls
'ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត(1)-brightness_contrast.mp4'   ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត-brightness_contrast.mp4
'ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត(1).mp4'                       ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត.mp4
'ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត(1)-noise.mp4'                 ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត-noise.mp4
'ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត(1)-spatial.mp4'               ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត-spatial.mp4
'ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត(1)-temporal.mp4'              ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត-temporal.mp4
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/class/ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត$
```

--inded ထည့်ပြီး run ရင်တော့ class name တွေကို 1, 2, 3 စသည်ဖြင့် index လုပ်ပြီးသိမ်းပေးသွားပါလိမ့်မယ်။   

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing$ python mk-video-class-for-sentence.py sent label --index
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing$ cd label
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$ ls
1  2  3  4  5  6  7  8  index.txt
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$
```

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$ cat index.txt
អ្នកបានបាក់ជើង : 1
អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ : 2
ហែលទឹក : 3
មនុស្សម្នាក់បានបាក់ដៃ : 4
មនុស្សម្នាក់បានរងរបួស : 5
មានតែអ្នកយាមអ្នកជំងឺម្នាក់ប៉ុណ្ណោះដែលនឹងត្រូវបានអនុញ្ញាតឱ្យស្នាក់នៅពេលយប់ : 6
អ្នកបានបាក់ដៃ : 7
ឱ្យគាត់នៅស្ងៀមបែបនេះបន្តទៀត : 8
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$
```

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$ ls 1
'អ្នកបានបាក់ជើង (1)-brightness_contrast.mp4'  'អ្នកបានបាក់ជើង (2)-brightness_contrast.mp4'
'អ្នកបានបាក់ជើង (1).mp4'                      'អ្នកបានបាក់ជើង (2).mp4'
'អ្នកបានបាក់ជើង (1)-noise.mp4'                'អ្នកបានបាក់ជើង (2)-noise.mp4'
'អ្នកបានបាក់ជើង (1)-spatial.mp4'              'អ្នកបានបាក់ជើង (2)-spatial.mp4'
'អ្នកបានបាក់ជើង (1)-temporal.mp4'             'អ្នកបានបាក់ជើង (2)-temporal.mp4'
```

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$ ls 2
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (1)-brightness_contrast.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (1).mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (1)-noise.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (1)-spatial.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (1)-temporal.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (2)-brightness_contrast.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (2).mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (2)-noise.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (2)-spatial.mp4'
'អាចចាប់ពីម៉ោង1000ព្រឹក នៅថ្ងៃសៅរ៍ និង ថ្ងៃអាទិត្យ (2)-temporal.mp4'
```

```
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$ ls 3
ហែលទឹក-brightness_contrast.mp4  ហែលទឹក.mp4  ហែលទឹក-noise.mp4  ហែលទឹក-spatial.mp4  ហែលទឹក-temporal.mp4
(sl-vr) rnd@gpu:~/demo/vr/exp/sentence/preprocessing/label$
```

## 55. [m4v_to_mp4.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/m4v_to_mp4.py)  

Cambodian Sign Language (CSL) ဒေတာတွေကို ပြင်ဆင်တဲ့အခါမှာ mp4 ဖိုင်တွေရော၊ m4v ဖိုင်တွေရော ရောပါနေတာမို့ mp4 format အဖြစ် ပြောင်းဖို့ preprocessing အလုပ်တစ်ခု က မထင်မှတ်ပဲ ဝင်လာပါတယ်။ m4v video ဖိုင်တွေက Apple OS မှာ သုံးတဲ့ format ပါ။ ဒီ m4v_to_mp4.py က m4v တွေ့ရင် mp4 ပြောင်းပြီး output folder ထဲမှာ သိမ်းဆည်းပေးမယ်။ တကယ်လို့ mp4 ဖိုင်ကိုပဲ တွေ့ရင်တော့ အဲဒီဖိုင်ကို output folder ဆီကို copy ကူးပေးပါလိမ့်မယ်။  

## Check m4v Files

mp4 ဖိုင်တွေကတော့ ပိုများတယ်။  

```
(base) rnd@gpu:~/demo/vr/exp/word/Words$ ls *.mp4 | wc
   1572    1628   37384
(base) rnd@gpu:~/demo/vr/exp/word/Words$
```

အဲဒီ ဖိုလ်ဒါအောက်မှာပဲ m4v ဖိုင်တွေလည်း အောက်ပါအတိုင်း ရောပါနေတယ်။  

```
(base) rnd@gpu:~/demo/vr/exp/word/Words$ ls *.m4v
 ចក.m4v           ញញឹម.m4v       ទឹកត្រី.m4v     បាយ័ន.m4v           មុង.m4v       វិទ្យាសាស្ត្រ.m4v   សាវម៉ាវ.m4v
 ចង្កូម.m4v         ដប.m4v        ទេសចរណ៍.m4v   ប៉ោងប៉ោង.m4v         មេសា.m4v     សកម្មភាព.m4v     សិល្បៈ.m4v
 ចង្វាក់.m4v       'ដាំ(ស្ល).m4v'   ធូលី.m4v       ប្រពៃណី.m4v          យប់មិញ.m4v     សង់ទីម៉ែត.m4v      សិស្ស.m4v
 ចម្លីយ.m4v         ដេស៊ីម៉ែត.m4v    ធ្នូ.m4v       ផឹក.m4v             រងចាំ.m4v     សត្រូវ.m4v        សុខ.m4v
 ច្រាសដុសធ្មេញ.m4v   តុ.m4v         នំ.m4v        ផ្លែក្រូច.m4v         រត់.m4v       សត្វ.m4v
 ឆ្នាំង.m4v         ត្បូង.m4v       និមន្ត.m4v     ពុទ្ធសករាជ.m4v       រមិលគុណ.m4v   'ស(ពណ៌).m4v'
 ជ័រលុប.m4v         ថ្មកែវ.m4v     បទ.m4v       ព្រះបរមរាជវាំង.m4v   រោងចក្រ.m4v   សមាសធាតុ.m4v
 ជិតស្និទ្ធិ.m4v       ថ្លៃ.m4v       បាគង.m4v     ភាគបែង.m4v         ល្ហុង.m4v      សាគរ.m4v
 ឈឺក្បាល.m4v        ទឹកខ្មៅ.m4v     បាពួន.m4v     មង្ឈុត.m4v           វិច្ឆិកា.m4v    សារ.m4v
(base) rnd@gpu:~/demo/vr/exp/word/Words$ ls *.m4v | wc
     58      58    1332
(base) rnd@gpu:~/demo/vr/exp/word/Words$
```

## --help

```
(base) rnd@gpu:~/demo/vr/exp/word$ python m4v_to_mp4.py --help
usage: m4v_to_mp4.py [-h] [--input INPUT] [--output OUTPUT]

Convert m4v videos to mp4.

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    Input folder path
  --output OUTPUT  Output folder path
(base) rnd@gpu:~/demo/vr/exp/word$
```

## Example Running

```
(base) rnd@gpu:~/demo/vr/exp/word$ time python m4v_to_mp4.py --input Words --output allmp4
...
...
...
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'Words/ត្បូង.m4v':
  Metadata:
    major_brand     : mp42
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    creation_time   : 2019-03-06T07:33:36.000000Z
    encoder         : HandBrake 1.2.2 2019022300
  Duration: 00:00:03.61, start: 0.000000, bitrate: 496 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, smpte170m/bt709/bt709), 960x720 [SAR 4:3 DAR 16:9], 329 kb/s, 29.97 fps, 29.97 tbr, 90k tbn, 180k tbc (default)
    Metadata:
      creation_time   : 2019-03-06T07:33:36.000000Z
      handler_name    : VideoHandler
    Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 155 kb/s (default)
    Metadata:
      creation_time   : 2019-03-06T07:33:36.000000Z
      handler_name    : SoundHandler
Output #0, mp4, to 'allmp4/ត្បូង.mp4':
  Metadata:
    major_brand     : mp42
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf58.29.100
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, smpte170m/bt709/bt709), 960x720 [SAR 4:3 DAR 16:9], q=2-31, 329 kb/s, 29.97 fps, 29.97 tbr, 90k tbn, 90k tbc (default)
    Metadata:
      creation_time   : 2019-03-06T07:33:36.000000Z
      handler_name    : VideoHandler
    Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 155 kb/s (default)
    Metadata:
      creation_time   : 2019-03-06T07:33:36.000000Z
      handler_name    : SoundHandler
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
frame=  108 fps=0.0 q=-1.0 Lsize=     219kB time=00:00:03.56 bitrate= 502.6kbits/s speed=3.88e+03x
video:145kB audio:68kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 2.434549%
Total no. of successfully converted m4v files: 58

real    0m54.499s
user    0m4.515s
sys     0m4.643s
```

m4v ဖိုင် စုစုပေါင်း ၅၈ ဖိုင်စလုံးကို convert လုပ်ပေးသွားတာကို တွေ့ရပါလိမ့်မယ်။  

## Check the Output Folder

output folder ထဲမှာ m4v ဖိုင်တွေရှိသလား ဆိုတာကို စစ်ကြည့်ရင် မရှိတာကို အောက်ပါအတိုင်း တွေ့ရပါလိမ့်မယ်။  

```
(base) rnd@gpu:~/demo/vr/exp/word/allmp4$ ls *.m4v
ls: cannot access '*.m4v': No such file or directory
```

mp4 ဖိုင်စုစုပေါင်းက အောက်ပါအတိုင်း ...  

```
(base) rnd@gpu:~/demo/vr/exp/word/allmp4$ ls *.mp4 | wc
   1629    1685   38696
(base) rnd@gpu:~/demo/vr/exp/word/allmp4$
```

Video ဖိုင်တွေကို သိမ်းထားတဲ့ folder တွေမှာ hidden file တွေရှိတတ်တာကိုလည်း မမေ့ပါနဲ့ ... 

```
(base) rnd@gpu:~/demo/vr/exp/word/Words$ find . -not -name "*.m4v" -not -name "*.mp4" -type f
./.DS_Store
(base) rnd@gpu:~/demo/vr/exp/word/Words$
```

## 56. [mov_to_mp4.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/mov_to_mp4.py)  

အထက်က m4v_to_mp4.py နဲ့ အတူတူပါပဲ။ ဒီတစ်ခါတော့ mov ကနေ mp4 ကို ပြောင်းဖို့အတွက် သုံးခဲ့တာပါ။  
Running example က အောက်ပါအတိုင်းပါ။  

```
(base) rnd@gpu:~/demo/vr/exp/sentence$ time python mov_to_mp4.py --input Sentences --output allmp4
...
...
...
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'Sentences/ធុងទឹក.mov':
  Metadata:
    major_brand     : qt
    minor_version   : 0
    compatible_brands: qt
    creation_time   : 2023-03-15T07:11:45.000000Z
    com.apple.quicktime.artwork: {"data":{"edittime":10,"infoStickerId":"","musicId":"","os":"mac","product":"vicut","stickerId":"","videoEffectId":"","videoId":"9d7f18ae-124e-48fa-bc51-bad3c59db7df","videoParams":{"be":0,"ef":0,"ft":0,"ma":0,"me":0,"mu":0,"re":0,"sp":0,"st":0,"te":0,"tx
  Duration: 00:00:04.73, start: 0.000000, bitrate: 14718 kb/s
    Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1920x1080, 14615 kb/s, 30 fps, 30 tbr, 600 tbn, 1200 tbc (default)
    Metadata:
      creation_time   : 2023-03-15T07:11:45.000000Z
      handler_name    : Core Media Video
      encoder         : H.264
    Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 94 kb/s (default)
    Metadata:
      creation_time   : 2023-03-15T07:11:45.000000Z
      handler_name    : Core Media Audio
Output #0, mp4, to 'allmp4/ធុងទឹក.mp4':
  Metadata:
    major_brand     : qt
    minor_version   : 0
    compatible_brands: qt
    com.apple.quicktime.artwork: {"data":{"edittime":10,"infoStickerId":"","musicId":"","os":"mac","product":"vicut","stickerId":"","videoEffectId":"","videoId":"9d7f18ae-124e-48fa-bc51-bad3c59db7df","videoParams":{"be":0,"ef":0,"ft":0,"ma":0,"me":0,"mu":0,"re":0,"sp":0,"st":0,"te":0,"tx
    encoder         : Lavf58.29.100
    Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1920x1080, q=2-31, 14615 kb/s, 30 fps, 30 tbr, 19200 tbn, 600 tbc (default)
    Metadata:
      creation_time   : 2023-03-15T07:11:45.000000Z
      handler_name    : Core Media Video
      encoder         : H.264
    Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 94 kb/s (default)
    Metadata:
      creation_time   : 2023-03-15T07:11:45.000000Z
      handler_name    : Core Media Audio
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
frame=  142 fps=0.0 q=-1.0 Lsize=    8506kB time=00:00:04.71 bitrate=14787.7kbits/s speed=79.3x
video:8445kB audio:55kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.075300%
Total no. of successfully converted mov files: 247

real    9m3.096s
user    0m13.782s
sys     0m32.286s
```

mov ဖိုင် စုစုပေါင်း 247 ဖိုင်ကို mp4 encoding အဖြစ် ပြောင်းပေးသွားတာကို တွေ့ရပါလိမ့်မယ်။  
ပြောင်းပြီးသွားတဲ့ အခါမှာတော့ sentence level CSL ဗီဒီယိုဖိုင်တွေက စုစုပေါင်း 1035 ဖိုင် ရှိတာကို အောက်ပါအတိုင်း တွေ့ရပါတယ်။  

```
(base) rnd@gpu:~/demo/vr/exp/sentence/allmp4$ ls *.mp4 | wc
   1035    1464   83908
(base) rnd@gpu:~/demo/vr/exp/sentence/allmp4$
```

## 57. [jiwer_wer_mer_wil.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/jiwer_wer_mer_wil.py)  

Automatic Speech Recognition (ASR) system တစ်ခု သို့မဟုတ် မော်ဒယ် တစ်ခုရဲ့ performance ကို ပုံမှန်အားဖြင့် edit-distance ကိုအခြေခံပြီးတွက်တဲ့ Word Error Rate (WER) ကိုပဲ သုံးပြီးတော့ evaluation လုပ်ကြပါတယ်။ သို့သော် ကျောင်းသားတွေအနေနဲ့က Match Error Rate (MER) နဲ့ Word Information Lost (WIL) evaluation metric တွေကိုလည်း သိထားသင့်တယ်။  

- Match Error Rate (MER): This metric also evaluates the performance of an ASR system. The MER value indicates the percentage of words that were incorrectly predicted and inserted. A lower MER value indicates better performance, with a MER of 0 being perfect. The formula for it is `MER = (S + D + I) / (N + I)` where `S` is the number of substitutions, `D` is the number of deletions, `I` is the number of insertions, and `N` is the number of words in the reference.
  
- Word Information Lost (WIL): This metric indicates the percentage of words that were incorrectly predicted between a set of ground-truth sentences and a set of hypothesis sentences. A lower WIL indicates better performance, with a WIL of 0 being perfect. The formula for it is `WIL = 1 - (C/N) + (C/P)` where `C` is the number of correct words, `N` is the number of words in the reference, and `P` is the number of words in the prediction.

တွက်ချက်ပုံ အသေးစိတ်က [ဒီစာတမ်း](https://www.isca-speech.org/archive_v0/archive_papers/interspeech_2004/i04_2765.pdf) ကို ဖတ်ပါ။  

Running လုပ်ပုံလုပ်နည်းက အောက်ပါအတိုင်း။  

```
python jiwer_wer_mer_wil2.py -s "ye kyaw thu" "thu ye kyaw"
WER: 0.6666666666666666
MER: 0.5
WIL: 0.5555555555555556
```

တကယ် experiment တွေကို လုပ်ကြတဲ့အခါမှာတော့ စာကြောင်းရေ တစ်ထောင်၊ ၅ထောင် စသည်ဖြင့် test data ထားပြီးလုပ်ကြတာမို့ ဖိုင်အနေနဲ့ ပရိုဂရမ်ကို pass လုပ်ပေးတာက ပိုအဆင်ပြေပါလိမ့်မယ်။  

```
>type ref.txt
နေကောင်း လား
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း ပါ စေ
မြန်မြန် သွား နော်
သွား ပြီ လား
သွား ပါ ပြီ
```

```
>type hyp.txt
နေကောင်း ရဲ့ လား
အခု ဘာ လုပ် နေ သလဲ
နေကောင်း ပါ ပြီ
မြန်မြန် သွား 
သွား ပြီ လား
သွား ပြီ
```

```
>python jiwer_wer_mer_wil.py -f ref.txt hyp.txt
WER: 0.21052631578947367
MER: 0.2
WIL: 0.2514619883040936
```

## 58. [passphrase_generator.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/passphrase_generator.py)  

passphrase generation ဆိုတာက password တွေကို automatic ထုတ်တဲ့ နည်းလမ်းတစ်ခုပါ။  
အဲဒီ method က လွယ်ပေမဲ့ လက်တွေ့ မြန်မာစာ စာလုံးတွေနဲ့ ထုတ်ကြည့်တဲ့အခါမှာ ဘယ်လိုနေသလဲ ဆိုတာကို သိချင်လို့ စမ်းကြည့်ဖို့အတွက် ရေးခဲ့တဲ့ code ပါ။  

ပရိုဂရမ်ကို သုံးပုံသုံးနည်းက အောက်ပါအတိုင်းပါ။  

```
(base) C:\Users\ye\.spyder-py3>python passphrase_generator.py --help
usage: passphrase_generator.py [-h] [-n NUM_WORDS] [-s] wordlist

Generate a passphrase from a list of words.

positional arguments:
  wordlist              The file name of the word list.

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_WORDS, --num_words NUM_WORDS
                        The number of words in the passphrase (default: 3).
  -s, --space           Include spaces between words.
```

အဘိဓာန်အသေးလေးနဲ့ ပဲ test လုပ်ပြမယ်။  

```
(base) C:\Users\ye\.spyder-py3>type word-my.txt
ကျောင်းသား
ဆရာ
မိဘ
သမီး
မြန်မာ
တက္ကသိုလ်
တိရစ္ဆာန်
လူ
အုန်းသီး
သရက်သီး
```

```
(base) C:\Users\ye\.spyder-py3>python passphrase_generator.py word-my.txt
ကျောင်းသားအုန်းသီးမြန်မာ
```

```
(base) C:\Users\ye\.spyder-py3>python passphrase_generator.py word-my.txt -s
လူ သရက်သီး တက္ကသိုလ်
```

```
(base) C:\Users\ye\.spyder-py3>python passphrase_generator.py word-my.txt -s -n 2
တိရစ္ဆာန် အုန်းသီး
```

```
(base) C:\Users\ye\.spyder-py3>python passphrase_generator.py word-my.txt -s -n 3
လူ တက္ကသိုလ် တိရစ္ဆာန်
```

```
(base) C:\Users\ye\.spyder-py3>python passphrase_generator.py word-my.txt -n 3
သရက်သီးလူကျောင်းသား
```

## 59. [rule_based_password_gen.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/rule_based_password_gen.py)  

Rule-based password ဆိုတာကလည်း password တွေကို အော်တိုမစ်တစ် ထုတ်လို့ရတဲ့ နည်းလမ်းတစ်ခုပါ။ Rule ကို ဒီဇိုင်းလုပ်ထားတဲ့အပေါ်ကိုမူတည်ပြီးတော့ hacker တွေအနေနဲ့ ဖြေရတာ ခက်တဲ့ အပိုင်းတွေ ရှိပါတယ်။  
ဒီ ပရိုဂရမ်ကတော့ မြန်မာစာအတွက် အလွယ်စမ်းထားကြည့်တာပါ။  

```
(base) C:\Users\ye\.spyder-py3>python ./rule_based_password_gen.py --help
usage: rule_based_password_gen.py [-h] [-s SYLLABLE] [-n NUMBER] [-e EXTRA] -r RULE

Generate a rule-based password.

optional arguments:
  -h, --help            show this help message and exit
  -s SYLLABLE, --syllable SYLLABLE
                        The file name for the syllable list (default: syllable.txt).
  -n NUMBER, --number NUMBER
                        The file name for the number list (default: number.txt).
  -e EXTRA, --extra EXTRA
                        The file name for the special characters list (default: extra.txt).
  -r RULE, --rule RULE  The rule for generating the password, for example "s+e+n+n".
```

```
(base) C:\Users\ye\.spyder-py3>python ./rule_based_password_gen.py -s syllable.txt -n number.txt -e extra.txt -r snsne
ကာ၃ကာ၅g

```

```
(base) C:\Users\ye\.spyder-py3>python ./rule_based_password_gen.py -s syllable.txt -n number.txt -e extra.txt -r sen
ကားg၅
```

```
(base) C:\Users\ye\.spyder-py3>python ./rule_based_password_gen.py -r se
ကd
```

```
(base) C:\Users\ye\.spyder-py3>python ./rule_based_password_gen.py -r sen
ကော်e၀
```

```
(base) C:\Users\ye\.spyder-py3>python ./rule_based_password_gen.py -r nsnseses
၀ကု၇ခါeခeခု
```

test-run လုပ်ဖို့အတွက် သုံးခဲ့တဲ့ ယာယီအဘိဓာန်တွေကတော့ အောက်ပါအတိုင်းပါ။  

```
type syllable.txt
က
ကာ
ကိ
ကီ
ကု
ကူ
ကေ
ကဲ
ကော့
ကော်
ကံ
ကား
ခ
ခါ
ခိ
ခီ
ခု
ခူ
ခေ
ခဲ
ခေါ့
ခေါ်
ခံ
ခါး
```

```
type number.txt
၁
၂
၃
၄
၅
၆
၇
၈
၉
၀
```

```
type extra.txt
a
b
c
d
e
f
g
```

## 60. [MOS_eval.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/MOS_eval.py)  

TTS model တွေကို Mean Opinion Score (MOS) သုံးပြီး subjective evaluation လုပ်လေ့ရှိတယ်။ TTS model က ထုတ်ပေးထားတဲ့ synthesized speech file တွေကို native speaker က နားထောင်ပြီး 1 to 5 scale နဲ့ evaluation လုပ်သွားတဲ့ ပုံစံပါ။ ဒီ python script မှာတော့ ဖိုင်တစ်ဖိုင်ကို သုံးခါအထိ နားထောင်ခွင့် ပေးထားတယ်။ ဒါကလည်း လက်တွေ့ user-study လုပ်တဲ့ အခါမှာ လိုအပ်တယ်။ တစ်ခေါက်ပဲ play လုပ်ရင် အာရုံမစိုက်လိုက်နိုင်လို့ မကြားလိုက်နိုင်တဲ့ အပိုင်းတွေလည်း ရှိသွားနိုင်လို့။ အထူးသဖြင့် ရှည်တဲ့ စာကြောင်းတွေကို TTS လုပ်ထားတဲ့ အခါမျိုးမှာ ဆိုရင် ပိုလိုအပ်လို့...   

--help ဆိုတဲ့ option နဲ့ help ခေါ်ကြည့်ပါ။  

```
(base) C:\Users\ye\.spyder-py3>python ./MOS_eval1.py --help
C:\Users\ye\Anaconda3\lib\site-packages\pydub\utils.py:170: RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
  warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
usage: MOS_eval1.py [-h] audio_folder log_folder

MOS Evaluation Program

positional arguments:
  audio_folder  Path to the audio folder
  log_folder    Path to the log folder

optional arguments:
  -h, --help    show this help message and exit

(base) C:\Users\ye\.spyder-py3>
```

wavefiles\ ဆိုတဲ့ ဖိုလ်ဒါအောက်မှာ example running အတွက် အသံဖိုင် သုံးဖိုင်ကို သိမ်းထားတယ်။  
log\ ဆိုတဲ့ ဖိုလ်ဒါက output folder ပါ။ မရှိရင် ပရိုဂရမ်က create လုပ်ပေးလိမ့်မယ်။  

Example running က အောက်ပါအတိုင်းပါ။  

```
(base) C:\Users\ye\.spyder-py3>python MOS_eval1.py wavefiles log
C:\Users\ye\Anaconda3\lib\site-packages\pydub\utils.py:170: RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
  warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
Enter your name: Ye Kyaw Thu
Enter your age: 13
Enter your sex: Male
Enter your native language: Burmese
Enter your second language: Japanese
Enter other languages you understand well (comma-separated): English, Rakhine
Welcome to the MOS evaluation!
You will listen to the synthesized speech and rate its quality.
Please rate each speech sample on a scale of 1-5.
Press 'Q' to quit the evaluation.

Speech Sample: wavefiles\221222_0276S1.wav
Do you want to replay the audio? (Y/N): Y
Do you want to replay the audio? (Y/N): Y
Rate the speech quality on a scale of 1-5 (1: Bad, 5: Excellent): 3

Speech Sample: wavefiles\221222_0275S1.wav
Do you want to replay the audio? (Y/N): N
Rate the speech quality on a scale of 1-5 (1: Bad, 5: Excellent): 5

Speech Sample: wavefiles\221222_0278S1.wav
Do you want to replay the audio? (Y/N): N
Rate the speech quality on a scale of 1-5 (1: Bad, 5: Excellent): 5

Evaluation log saved as: log\mos_evaluation_log_2023-06-22_19-22-33.txt
```

ထွက်လာမယ့် log ဖိုင်ကိုလည်း ဝင်ကြည့်ကြရအောင်။  

```
(base) C:\Users\ye\.spyder-py3>cd log

(base) C:\Users\ye\.spyder-py3\log>dir
 Volume in drive C has no label.
 Volume Serial Number is 9C54-A208

 Directory of C:\Users\ye\.spyder-py3\log

06/22/2023  07:22 PM    <DIR>          .
06/22/2023  07:22 PM    <DIR>          ..
06/22/2023  07:22 PM               412 mos_evaluation_log_2023-06-22_19-22-33.txt
               1 File(s)            412 bytes
               2 Dir(s)  27,005,231,104 bytes free
```

Log ဖိုင်ထဲမှာတော့ အောက်ပါအတိုင်း User information နဲ့ evaluation score တွေကို သိမ်းပေးထားလိမ့်မယ်။  

```
MOS Evaluation Log
Date: 2023-06-22_19-22-33

User Information:
Name: Ye Kyaw Thu
Age: 13
Sex: Male
Native Language: Burmese
Second Language: Japanese
Other Languages: English, Rakhine

Scores:
Audio File: wavefiles\221222_0276S1.wav
Score: 3

Audio File: wavefiles\221222_0275S1.wav
Score: 5

Audio File: wavefiles\221222_0278S1.wav
Score: 5

Total Audio Files: 3
Average MOS Score: 4.33

```

## 61. [spacy_pos_ner.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/spacy_pos_ner.py)   

လက်တွေ့ မြန်မာစာအတွက် NLP corpus development လုပ်တဲ့အခါမှာ တခြားဘာသာစကားတွေမှာ ဘယ်လို POS tagging လုပ်ကြသလဲ၊ NER Tagging လုပ်ကြသလဲ ဆိုတာကိုလည်း လေ့လာကြရပါတယ်။ ငါ့အတွက်တော့ အင်္ဂလိပ်စာနဲ့ ဂျပန်စာကို အဓိက မှီငြမ်းဖြစ်ခဲ့ပါတယ်။ ဒီ ပရိုဂရမ်က Spacy library ကို သုံးပြီးတော့ အင်္ဂလိပ်စာ စာကြောင်းတွေကို POS tagging, NER tagging လုပ်ဖို့အတွက် စမ်းရေးထားတာ ဖြစ်ပါတယ်။   

အင်္ဂလိပ်စာ စာကြောင်း သုံးကြောင်း copy/paste လုပ်ထားတဲ့ ဖိုင်ကို သုံးပြီး လက်တွေ့ run ပြပါမယ်။  

```
> type en-sentence.txt
Two international key players in the area of computational linguistics, the ELRA Language Resources Association (ELRA) and the International Committee on Computational Linguistics (ICCL), are joining forces to organize the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024) to be held in Torino, Italy on 20-25 May, 2024.

The 18th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP 2023) and The International Conference on Artificial Intelligence and Internet of Things (AIoT 2023) is a joint conference organized by Artificial Intelligence Association of Thailand (AIAT) and Rajamangala University of Technology Thanyaburi (RMUTT), to be held on November 27-29, 2023 in Bangkok, Thailand.

The iSAI-NLP-AIoT 2023 conference aims to facilitate technology and knowledge exchange among international researchers/scholars in the field of artificial intelligence and natural language processing, by covering a broad range of research topics in machine learning, data analytics, robotics, Internet of Things, embedded systems, signal, image speech processing, smart technology and security.
```

`python spacy_pos_ner.py -i en-sentence.txt -t pos -f left-to-right` ဆိုတဲ့ command ပေးပြီးတော့ POS tagging လုပ်ကြည့်ရင်  ...  

```text
Two/NUM international/ADJ key/ADJ players/NOUN in/ADP the/DET area/NOUN of/ADP computational/ADJ linguistics/NOUN ,/PUNCT the/DET ELRA/PROPN Language/PROPN Resources/PROPN Association/PROPN (/PUNCT ELRA/PROPN )/PUNCT and/CCONJ the/DET International/PROPN Committee/PROPN on/ADP Computational/PROPN Linguistics/PROPN (/PUNCT ICCL/PROPN )/PUNCT ,/PUNCT are/AUX joining/VERB forces/NOUN to/PART organize/VERB the/DET 2024/NUM Joint/PROPN International/PROPN Conference/PROPN on/ADP Computational/PROPN Linguistics/PROPN ,/PUNCT Language/PROPN Resources/PROPN and/CCONJ Evaluation/PROPN (/PUNCT LREC/PROPN -/PUNCT COLING/PROPN 2024/NUM )/PUNCT to/PART be/AUX held/VERB in/ADP Torino/PROPN ,/PUNCT Italy/PROPN on/ADP 20/NUM -/SYM 25/NUM May/PROPN ,/PUNCT 2024/NUM ./PUNCT
The/DET 18th/ADJ International/PROPN Joint/PROPN Symposium/PROPN on/ADP Artificial/PROPN Intelligence/PROPN and/CCONJ Natural/PROPN Language/PROPN Processing/PROPN (/PUNCT iSAI/NOUN -/NOUN NLP/PROPN 2023/NUM )/PUNCT and/CCONJ The/DET International/PROPN Conference/PROPN on/ADP Artificial/PROPN Intelligence/PROPN and/CCONJ Internet/PROPN of/ADP Things/PROPN (/PUNCT AIoT/PROPN 2023/NUM )/PUNCT is/AUX a/DET joint/ADJ conference/NOUN organized/VERB by/ADP Artificial/PROPN Intelligence/PROPN Association/PROPN of/ADP Thailand/PROPN (/PUNCT AIAT/PROPN )/PUNCT and/CCONJ Rajamangala/PROPN University/PROPN of/ADP Technology/PROPN Thanyaburi/PROPN (/PUNCT RMUTT/PROPN )/PUNCT ,/PUNCT to/PART be/AUX held/VERB on/ADP November/PROPN 27/NUM -/SYM 29/NUM ,/PUNCT 2023/NUM in/ADP Bangkok/PROPN ,/PUNCT Thailand/PROPN ./PUNCT
The/DET iSAI/PROPN -/PUNCT NLP/PROPN -/PUNCT AIoT/PROPN 2023/NUM conference/NOUN aims/VERB to/PART facilitate/VERB technology/NOUN and/CCONJ knowledge/NOUN exchange/NOUN among/ADP international/ADJ researchers/NOUN //SYM scholars/NOUN in/ADP the/DET field/NOUN of/ADP artificial/ADJ intelligence/NOUN and/CCONJ natural/ADJ language/NOUN processing/NOUN ,/PUNCT by/ADP covering/VERB a/DET broad/ADJ range/NOUN of/ADP research/NOUN topics/NOUN in/ADP machine/NOUN learning/NOUN ,/PUNCT data/NOUN analytics/NOUN ,/PUNCT robotics/NOUN ,/PUNCT Internet/NOUN of/ADP Things/PROPN ,/PUNCT embedded/VERB systems/NOUN ,/PUNCT signal/NOUN ,/PUNCT image/NOUN speech/NOUN processing/NOUN ,/PUNCT smart/ADJ technology/NOUN and/CCONJ security/NOUN ./PUNCT
```

ဒီတစ်ခါတော့ NER tagging လုပ်ကြည့်ရအောင်။  
`python spacy_pos_ner.py -i en-sentence.txt -t ner -f left-to-right`   

```
Two/CARDINAL international/O key/O players/O in/O the/O area/O of/O computational/O linguistics/O ,/O the/ORG ELRA/ORG Language/ORG Resources/ORG Association/ORG (/O ELRA/ORG )/O and/O the/ORG International/ORG Committee/ORG on/ORG Computational/ORG Linguistics/ORG (/O ICCL/ORG )/O ,/O are/O joining/O forces/O to/O organize/O the/O 2024/DATE Joint/EVENT International/EVENT Conference/EVENT on/EVENT Computational/EVENT Linguistics/EVENT ,/EVENT Language/EVENT Resources/EVENT and/EVENT Evaluation/EVENT (/O LREC/O -/O COLING/O 2024/O )/O to/O be/O held/O in/O Torino/GPE ,/O Italy/GPE on/O 20/DATE -/DATE 25/DATE May/DATE ,/DATE 2024/DATE ./O
The/O 18th/ORDINAL International/EVENT Joint/EVENT Symposium/EVENT on/EVENT Artificial/EVENT Intelligence/EVENT and/EVENT Natural/EVENT Language/EVENT Processing/EVENT (/O iSAI/O -/O NLP/O 2023/O )/O and/O The/LAW International/LAW Conference/LAW on/LAW Artificial/LAW Intelligence/LAW and/LAW Internet/LAW of/LAW Things/LAW (/O AIoT/O 2023/O )/O is/O a/O joint/O conference/O organized/O by/O Artificial/ORG Intelligence/ORG Association/ORG of/ORG Thailand/ORG (/O AIAT/O )/O and/O Rajamangala/ORG University/ORG of/ORG Technology/ORG Thanyaburi/ORG (/O RMUTT/ORG )/O ,/O to/O be/O held/O on/O November/DATE 27/DATE -/DATE 29/DATE ,/O 2023/DATE in/O Bangkok/GPE ,/O Thailand/GPE ./O
The/O iSAI/O -/O NLP/O -/O AIoT/O 2023/O conference/O aims/O to/O facilitate/O technology/O and/O knowledge/O exchange/O among/O international/O researchers/O //O scholars/O in/O the/O field/O of/O artificial/O intelligence/O and/O natural/O language/O processing/O ,/O by/O covering/O a/O broad/O range/O of/O research/O topics/O in/O machine/O learning/O ,/O data/O analytics/O ,/O robotics/O ,/O Internet/O of/O Things/O ,/O embedded/O systems/O ,/O signal/O ,/O image/O speech/O processing/O ,/O smart/O technology/O and/O security/O ./O
```

စာကြောင်းနဲ့ tag တွေကို သပ်သပ်စီ ခွဲထုတ်ပြီးတော့ parallel data အနေနဲ့ ယူချင်ရင်တော့ -to (tag only) ဆိုတဲ့ option နဲ့ run ပါ။  
`python spacy_pos_ner.py -i en-sentence.txt -t pos -f left-to-right -to`  

```
NUM ADJ ADJ NOUN ADP DET NOUN ADP ADJ NOUN PUNCT DET PROPN PROPN PROPN PROPN PUNCT PROPN PUNCT CCONJ DET PROPN PROPN ADP PROPN PROPN PUNCT PROPN PUNCT PUNCT AUX VERB NOUN PART VERB DET NUM PROPN PROPN PROPN ADP PROPN PROPN PUNCT PROPN PROPN CCONJ PROPN PUNCT PROPN PUNCT PROPN NUM PUNCT PART AUX VERB ADP PROPN PUNCT PROPN ADP NUM SYM NUM PROPN PUNCT NUM PUNCT
DET ADJ PROPN PROPN PROPN ADP PROPN PROPN CCONJ PROPN PROPN PROPN PUNCT NOUN NOUN PROPN NUM PUNCT CCONJ DET PROPN PROPN ADP PROPN PROPN CCONJ PROPN ADP PROPN PUNCT PROPN NUM PUNCT AUX DET ADJ NOUN VERB ADP PROPN PROPN PROPN ADP PROPN PUNCT PROPN PUNCT CCONJ PROPN PROPN ADP PROPN PROPN PUNCT PROPN PUNCT PUNCT PART AUX VERB ADP PROPN NUM SYM NUM PUNCT NUM ADP PROPN PUNCT PROPN PUNCT
DET PROPN PUNCT PROPN PUNCT PROPN NUM NOUN VERB PART VERB NOUN CCONJ NOUN NOUN ADP ADJ NOUN SYM NOUN ADP DET NOUN ADP ADJ NOUN CCONJ ADJ NOUN NOUN PUNCT ADP VERB DET ADJ NOUN ADP NOUN NOUN ADP NOUN NOUN PUNCT NOUN NOUN PUNCT NOUN PUNCT NOUN ADP PROPN PUNCT VERB NOUN PUNCT NOUN PUNCT NOUN NOUN NOUN PUNCT ADJ NOUN CCONJ NOUN PUNCT
```

NER tag တွေပဲ လိုချင်တဲ့အခါအတွက်က ...   
`python spacy_pos_ner.py -i en-sentence.txt -t ner -f left-to-right -to`  

```
CARDINAL O O O O O O O O O O ORG ORG ORG ORG ORG O ORG O O ORG ORG ORG ORG ORG ORG O ORG O O O O O O O O DATE EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT O O O O O O O O O O GPE O GPE O DATE DATE DATE DATE DATE DATE O
O ORDINAL EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT EVENT O O O O O O O LAW LAW LAW LAW LAW LAW LAW LAW LAW LAW O O O O O O O O O O ORG ORG ORG ORG ORG O O O O ORG ORG ORG ORG ORG O ORG O O O O O O DATE DATE DATE DATE O DATE O GPE O GPE O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
```

CRF လိုမော်ဒယ် ဆောက်ဖို့အတွက် ဆိုရင် tag တွေကို column format အနေနဲ့ print ထုတ်ချင်တဲ့ အခါမျိုးလည်း ရှိပါတယ်။ အဲဒီအတွက်က -f သို့မဟုတ် --format ဆိုတဲ့ option ကို column ဆိုပြီး ပြောင်းပေးပါ။  

```
(base) C:\Users\801680\.spyder-py3>python spacy_pos_ner.py -i en-sentence.txt -t ner -f column -to
CARDINAL
O
O
O
O
O
O
O
O
O
O
ORG
ORG
ORG
ORG
ORG
O
ORG
O
O
ORG
ORG
ORG
ORG
ORG
ORG
O
ORG
O
O
O
O
O
O
O
O
DATE
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
O
O
O
O
O
O
O
O
O
O
GPE
O
GPE
O
DATE
DATE
DATE
DATE
DATE
DATE
O

O
ORDINAL
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
EVENT
O
O
O
O
O
O
O
LAW
LAW
LAW
LAW
LAW
LAW
LAW
LAW
LAW
LAW
O
O
O
O
O
O
O
O
O
O
ORG
ORG
ORG
ORG
ORG
O
O
O
O
ORG
ORG
ORG
ORG
ORG
O
ORG
O
O
O
O
O
O
DATE
DATE
DATE
DATE
O
DATE
O
GPE
O
GPE
O

O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
```

-to (tag only) ဆိုတဲ့ option ကို ဖြုတ်လိုက်ရင်တော့ word/tag ဆိုတဲ့ ပုံစံနဲ့ စာလုံးကော tag ကော နှစ်မျိုးတွဲရပါလိမ့်မယ်။   
`python spacy_pos_ner.py -i en-sentence.txt -t ner -f column`  

```
Two/CARDINAL
international/O
key/O
players/O
in/O
the/O
area/O
of/O
computational/O
linguistics/O
,/O
the/ORG
ELRA/ORG
Language/ORG
Resources/ORG
Association/ORG
(/O
ELRA/ORG
)/O
and/O
the/ORG
International/ORG
Committee/ORG
on/ORG
Computational/ORG
Linguistics/ORG
(/O
ICCL/ORG
)/O
,/O
are/O
joining/O
forces/O
to/O
organize/O
the/O
2024/DATE
Joint/EVENT
International/EVENT
Conference/EVENT
on/EVENT
Computational/EVENT
Linguistics/EVENT
,/EVENT
Language/EVENT
Resources/EVENT
and/EVENT
Evaluation/EVENT
(/O
LREC/O
-/O
COLING/O
2024/O
)/O
to/O
be/O
held/O
in/O
Torino/GPE
,/O
Italy/GPE
on/O
20/DATE
-/DATE
25/DATE
May/DATE
,/DATE
2024/DATE
./O

The/O
18th/ORDINAL
International/EVENT
Joint/EVENT
Symposium/EVENT
on/EVENT
Artificial/EVENT
Intelligence/EVENT
and/EVENT
Natural/EVENT
Language/EVENT
Processing/EVENT
(/O
iSAI/O
-/O
NLP/O
2023/O
)/O
and/O
The/LAW
International/LAW
Conference/LAW
on/LAW
Artificial/LAW
Intelligence/LAW
and/LAW
Internet/LAW
of/LAW
Things/LAW
(/O
AIoT/O
2023/O
)/O
is/O
a/O
joint/O
conference/O
organized/O
by/O
Artificial/ORG
Intelligence/ORG
Association/ORG
of/ORG
Thailand/ORG
(/O
AIAT/O
)/O
and/O
Rajamangala/ORG
University/ORG
of/ORG
Technology/ORG
Thanyaburi/ORG
(/O
RMUTT/ORG
)/O
,/O
to/O
be/O
held/O
on/O
November/DATE
27/DATE
-/DATE
29/DATE
,/O
2023/DATE
in/O
Bangkok/GPE
,/O
Thailand/GPE
./O

The/O
iSAI/O
-/O
NLP/O
-/O
AIoT/O
2023/O
conference/O
aims/O
to/O
facilitate/O
technology/O
and/O
knowledge/O
exchange/O
among/O
international/O
researchers/O
//O
scholars/O
in/O
the/O
field/O
of/O
artificial/O
intelligence/O
and/O
natural/O
language/O
processing/O
,/O
by/O
covering/O
a/O
broad/O
range/O
of/O
research/O
topics/O
in/O
machine/O
learning/O
,/O
data/O
analytics/O
,/O
robotics/O
,/O
Internet/O
of/O
Things/O
,/O
embedded/O
systems/O
,/O
signal/O
,/O
image/O
speech/O
processing/O
,/O
smart/O
technology/O
and/O
security/O
./O
```

## 62. [spacy_pos_dep_jp.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/spacy_pos_dep_jp.py)  

ဒီတစ်ခါတော့ ဂျပန်စာကြောင်းတွေအတွက် Spacy library ကို သုံးပြီး POS နဲ့ Dependency tagging နှစ်မျိုးကို လုပ်ကြည့်ထားတာပါ။ သိရသလောက် NER ကို Spacy library က support လုပ်မထားလို့ နှစ်မျိုးကိုပဲ စမ်းကြည့်ခဲ့တယ်။   

NHK site ကနေ ကော်ပီယူထားတဲ့ စာကြောင်း သုံးကြောင်းကို input ဖိုင်အနေနဲ့ သိမ်းထားပြီး testing လုပ်ခဲ့တယ်။  

```
NHKが海外配信に利用している衛星を直接受信することで、1日およそ5時間、ニュースを中心に日本語の番組を無料で視聴できます。
衛星からの直接受信により無料で視聴できる、ノンスクランブル時間帯の番組表です。
一部の番組はインターネットで視聴できます。
```

POS Tagging ...  

```
python spacy_pos_dep_jp.py -i jp-sentence.txt -t pos -f left-to-right
NHK/PROPN が/ADP 海外/NOUN 配信/NOUN に/ADP 利用/VERB し/AUX て/SCONJ いる/VERB 衛星/NOUN を/ADP 直接/ADV 受信/VERB する/AUX こと/NOUN で/AUX 、/PUNCT 1/NUM 日/NOUN およそ/NOUN 5/NUM 時間/NOUN 、/PUNCT ニュース/NOUN を/ADP 中心/NOUN に/ADP 日本/PROPN 語/NOUN の/ADP 番組/NOUN を/ADP 無料/NOUN で/ADP 視聴/VERB でき/AUX ます/AUX 。/PUNCT
衛星/NOUN から/ADP の/ADP 直接/ADV 受信/NOUN に/ADP より/VERB 無料/NOUN で/ADP 視聴/VERB できる/AUX 、/PUNCT ノンスクランブル/NOUN 時間/NOUN 帯/NOUN の/ADP 番組/NOUN 表/NOUN です/AUX 。/PUNCT
一部/NOUN の/ADP 番組/NOUN は/ADP インターネット/NOUN で/ADP 視聴/VERB でき/AUX ます/AUX 。/PUNCT
```

Dependency parsing ...  

```
python spacy_pos_dep_jp.py -i jp-sentence.txt -t dep -f left-to-right
NHK/nsubj が/case 海外/compound 配信/obl に/case 利用/acl し/aux て/mark いる/fixed 衛星/obj を/case 直接/advmod 受信/acl する/aux こと/advcl で/cop 、/punct 1/nummod 日/nmod およそ/compound 5/nummod 時間/obl  、/punct ニュース/obj を/case 中心/obl に/case 日本/compound 語/nmod の/case 番組/obj を/case 無料/obl で/case 視聴/ROOT でき/aux ます/aux 。/punct
衛星/obl から/case の/case 直接/advmod 受信/obl に/case より/fixed 無料/obl で/case 視聴/acl できる/aux  、/punct ノンスクランブル/compound 時間/compound 帯/nmod の/case 番組/compound 表/ROOT です/cop 。/punct
一部/nmod の/case 番組/nsubj は/case インターネット/obl で/case 視聴/ROOT でき/aux ます/aux 。/punct
```

အထက်က အင်္ဂလိပ်စာ ပရိုဂရမ်လိုပါပဲ။ Tag တွေချည်းပဲ ဆွဲထုတ်တွေလည်း ရပါတယ်။  

```
python spacy_pos_dep_jp.py -i jp-sentence.txt -t dep -f left-to-right -to
nsubj case compound obl case acl aux mark fixed obj case advmod acl aux advcl cop punct nummod nmod compound nummod obl punct obj case obl case compound nmod case obj case obl case ROOT aux aux punct
obl case case advmod obl case fixed obl case acl aux punct compound compound nmod case compound ROOT cop punct
nmod case nsubj case obl case ROOT aux aux punct
```

Column format အနေနဲ့တော့ လုပ်မပြတော့ဘူး။  
ပြီးတော့ output ဖိုင်အနေနဲ့လည်း သိမ်းလို့ ရပါတယ်။  

```
python spacy_pos_dep_jp.py -i jp-sentence.txt -t dep -f left-to-right -to -o output.txt
```

## 63. [spacy_pos_ner_dep_zh.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/spacy_pos_ner_dep_zh.py)  

အထက်က ပရိုဂရမ် နှစ်ပုဒ်လိုပါပဲ။ ဒီ script ကတော့ တရုပ်စာကြောင်းတွေကို POS tagging, NER tagging နဲ့ Dependency parsing လုပ်ဖို့အတွက် အသုံးဝင်ပါလိမ့်မယ်။  

အရင်ဆုံး POS tagging ကို လုပ်ကြည့်ရအောင်ပါ။  

```
python spacy_pos_ner_dep_zh.py -i zh-sentence.txt -t pos -f left-to-right
“/PUNCT 泰坦/ADJ ”/PUNCT 潜水器/NOUN 失联/VERB ：/PUNCT 探索/VERB 泰坦尼克号/NOUN 残骸/NOUN 要/VERB 冒多/VERB 大/VERB 的/PART 风险/NOUN ？/PUNCT

我/PRON 喜欢/VERB 中国/PROPN 功夫/NOUN 。/PUNCT

你好/VERB 吗/PART ？/PUNCT
我/PRON 的/PART 老朋友/NOUN
```

ဒီတစ်ခါတော့ NER tagging လုပ်မယ်။  

```
python spacy_pos_ner_dep_zh.py -i zh-sentence.txt -t ner -f left-to-right
“/O 泰坦/O ”/O 潜水器/O 失联/O ：/O 探索/O 泰坦尼克号/O 残骸/O 要/O 冒多/O 大/O 的/O 风险/O ？/O
/O 我/O 喜欢/O 中国/GPE 功夫/O 。/O
/O 你好/O 吗/O ？/O 我/O 的/O 老朋友/O
```

Chinese အတွက်က Spacy library က POS/NER/Depedency parsing သုံးမျိုးစလုံးကို support လုပ်ပါတယ်။ Dependency parsing ကို လုပ်ရင် အောက်ပါလိုမျိုး Output ကို ရလိမ့်မယ်။  

```
python spacy_pos_ner_dep_zh.py -i zh-sentence.txt -t dep -f left-to-right
“/punct 泰坦/amod ”/punct 潜水器/nsubj 失联/ROOT ：/punct 探索/conj 泰坦尼克号/compound:nn 残骸/dobj 要/xcomp 冒多/ccomp 大/amod 的/mark 风险/dobj ？/punct

我/nsubj 喜欢/ROOT 中国/nmod:assmod 功夫/dobj 。/punct

你好/dep 吗/discourse ？/ROOT
我/nmod:assmod 的/case 老朋友/ROOT
```

64. [nltk-lm.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/nltk-lm.py)

NLTK library က တကယ့် professional language model ဆောက်တဲ့ library မဟုတ်ပေမဲ့ ဥပမာ အနေနဲ့ python code နဲ့ရေးပြထားတာပါ။  

2gram LM building ...  

```
python .\nltk-lm.py -c .\corpus\mypos.txt -s .\corpus\stopwords.txt -n 2 -o .\corpus\mypos.2gram.txt -sm 1
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Most common 2-grams:  [(('ပါ', 'တယ်'), 3522), (('ဖြစ်', 'သည်'), 1416), (('ခဲ့', 'သည်'), 1286), (('တစ်', 'ခု'), 1066), (('ပေး', 'ပါ'), 1059)]
```

10 lines of .\corpus\mypos.2gram.txt ...   

```
('၁၉၆၂', 'ခုနှစ်') 23
('ခုနှစ်', 'ခန့်မှန်း') 2
('ခန့်မှန်း', 'သန်းခေါင်စာရင်း') 2
('သန်းခေါင်စာရင်း', 'အရ') 6
('အရ', 'လူဦးရေ') 7
('လူဦးရေ', '၁၁၅၉၃၁') 1
('၁၁၅၉၃၁', 'ယောက်') 1
('ယောက်', 'ရှိ') 46
('ရှိ', 'သည်') 668
('လူ', 'တိုင်း') 53
```

10 lines of .\corpus\mypos.2gram.txt ...   

```
('ထမင်းဟင်း', 'ချက်') 1
('တဝက်', 'စီ') 1
('ဇူလိုင်', '၁၄') 1
('မယ့်', 'us') 1
('us', '123') 1
('123', 'မှာ') 1
('ကား', 'မှ') 1
('မှ', 'ကားဘီး') 1
('ကားဘီး', 'ကို') 1
('အလွန်တရာ', 'ပြည့်ကျပ်') 1
```

ဒီတစ်ခါတော့ text file format နဲ့ သိမ်းတာမဟုတ်ပဲ binary format နဲ့ language model ဖိုင်ကို သိမ်ပါမယ်။ အဲဒီအတွက်က -b ဆိုတဲ့ command line argument ကို သုံးပါ။  

```
python .\nltk-lm.py -c .\corpus\mypos.txt -s .\corpus\stopwords.txt -n 2 -o .\corpus\mypos.2gram.bin -sm 1 -b
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Most common 2-grams:  [(('ပါ', 'တယ်'), 3522), (('ဖြစ်', 'သည်'), 1416), (('ခဲ့', 'သည်'), 1286), (('တစ်', 'ခု'), 1066), (('ပေး', 'ပါ'), 1059)]
```

3gram model building with text file format ...  

```
python .\nltk-lm.py -c .\corpus\mypos.txt -s .\corpus\stopwords.txt -n 3 -o .\corpus\mypos.3gram.txt -sm 1
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Most common 3-grams:  [(('ချင်', 'ပါ', 'တယ်'), 490), (('ရ', 'ပါ', 'တယ်'), 334), (('ပေး', 'နိုင်', 'မလား'), 267), (('လို့', 'ရ', 'မလား'), 265), (('ရှိ', 'ပါ', 'တယ်'), 259)]
```

3gram LM ဖိုင်ရဲ့ ထိပ်ဆုံး ၁၀ကြောင်းက အောက်ပါအတိုင်း ...   

```
('၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း') 2
('ခုနှစ်', 'ခန့်မှန်း', 'သန်းခေါင်စာရင်း') 2
('ခန့်မှန်း', 'သန်းခေါင်စာရင်း', 'အရ') 2
('သန်းခေါင်စာရင်း', 'အရ', 'လူဦးရေ') 1
('အရ', 'လူဦးရေ', '၁၁၅၉၃၁') 1
('လူဦးရေ', '၁၁၅၉၃၁', 'ယောက်') 1
('၁၁၅၉၃၁', 'ယောက်', 'ရှိ') 1
('ယောက်', 'ရှိ', 'သည်') 4
('လူ', 'တိုင်း', 'တွင်') 19
('တိုင်း', 'တွင်', 'သင့်မြတ်') 1
```

3gram LM ဖိုင်ရဲ့ နောက်ဆုံး ၁၀ကြောင်းက အောက်ပါအတိုင်း ...  

```
('ပါ', 'ဟုတ်', 'လား') 1
('ကား', 'မှ', 'ကားဘီး') 1
('မှ', 'ကားဘီး', 'ကို') 1
('ကားဘီး', 'ကို', 'ဖြုတ်') 1
('ကို', 'ဖြုတ်', 'လိုက်') 1
('ဖြုတ်', 'လိုက်', 'သည်') 1
('ဘူတာရုံ', 'က', 'အလွန်တရာ') 1
('က', 'အလွန်တရာ', 'ပြည့်ကျပ်') 1
('အလွန်တရာ', 'ပြည့်ကျပ်', 'နေ') 1
('ပြည့်ကျပ်', 'နေ', 'သည်') 1
```

ဒီတစ်ခါတော့ 3gram model ကိုပဲ binary file format နဲ့ ဆောက်ခိုင်းကြည့်မယ်  

```
python .\nltk-lm.py -c .\corpus\mypos.txt -s .\corpus\stopwords.txt -n 3 -o .\corpus\mypos.3gram.bin -sm 1 -b
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Most common 3-grams:  [(('ချင်', 'ပါ', 'တယ်'), 490), (('ရ', 'ပါ', 'တယ်'), 334), (('ပေး', 'နိုင်', 'မလား'), 267), (('လို့', 'ရ', 'မလား'), 265), (('ရှိ', 'ပါ', 'တယ်'), 259)]
```

လက်ရှိ folder အောက်ကို ကြည့်ရအောင် ...  

```
dir .\corpus
 Volume in drive C has no label.
 Volume Serial Number is 9C54-A208

 Directory of C:\Users\ye\.spyder-py3\corpus

06/26/2023  06:33 PM    <DIR>          .
06/26/2023  06:33 PM    <DIR>          ..
06/26/2023  06:24 PM         4,510,660 mypos.2gram.bin
06/26/2023  05:54 PM         7,361,805 mypos.2gram.txt
06/26/2023  06:33 PM        13,077,276 mypos.3gram.bin
06/26/2023  06:28 PM        18,029,201 mypos.3gram.txt
06/26/2023  04:12 PM         7,347,011 mypos.txt
06/26/2023  04:56 PM                61 stopwords.txt
               6 File(s)     50,326,014 bytes
               2 Dir(s)  28,262,445,056 bytes free
```		   
			   
## 65. [nltk-lm-predict.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/nltk-lm-predict.py)  

Language model (LM) က ခုချိန်ခါမှာ ဆိုရင် ChatGPT ရဲ့ ကျေးဇူးကြောင့် CS, IT နဲ့ ဆိုင်တဲ့သူ မဟုတ်ရင်တောင်မှ ကြားဖူးနေကြလောက်ပါပြီ။ ဟုတ်တယ် LM ကို သုံးပြီး NLP downstream task တွေ အမျိုးမျိုး လုပ်လို့ ရပါတယ်။ သို့သော် အဲဒီလိုလုပ်နိုင်ဖို့အတွက်က ဒေတာတွေက တကယ့်ကို အများကြီး လိုအပ်ပါတယ်။ ဒီ nltk-lm-predict.py ပရိုဂရမ်ကတော့ အထက်က nltk-lm.py နဲ့ ဆောက်ထားခဲ့တဲ့ LM နှစ်မျိုး (2gram, 3gram) ကို သုံးပြီးတော့ input ပေးလိုက်တဲ့ စာကြောင်းအပေါ်မူတည်ပြီးတော့ နောက်ဆက်တွဲ ဖြစ်လာနိုင်တဲ့ စကားလုံး (word) ကို ခန့်မှန်းတဲ့ အလုပ်ကို ဒီမို လုပ်ပြထားတာပါ။ အင်္ဂလိပ်လိုဆိုရင်တော့ next word prediction ပေါ့။ လက်ရှိ ဒီမို လုပ်ဖို့အတွက် သုံးခဲ့တဲ့ ဒေတာက myPOS မို့လို့ training ဒေတာက စုစုပေါင်း စာကြောင်းရေ လေးသောင်း သုံးထောင်ကျော်ပဲ ရှိပါတယ်။ အဲဒါကြောင့် LM အနေနဲ့ဆိုရင် ဒေတာက နည်းတယ်လို့ ပြောလို့ ရပါတယ်။ ဘာပဲဖြစ်ဖြစ် လက်တွေ့လုပ်ပြလိုက်မှ မြင်သာတာမို့ ...  

အရင်ဆုံး 2gram model ကို သုံးပြီးတော့ ရိုက်ထည့်လိုက်တဲ့ စာကြောင်းရဲ့ နောက်မှာ ဘယ်လို စာလုံးမျိုးဖြစ်နိုင်တယ်လို့ ခန့်မှန်းပေးတာကို လေ့လာကြည့်ကြရအောင် ...  

```
python nltk-lm-predict.py -m .\corpus\mypos.2gram.bin
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Language model loaded successfully.
Enter a sentence or phrase (or press 'q' to quit): နေကောင်း ရဲ့
Next possible words: ['လား', 'အိတ်', 'နာမည်', 'လက်မှတ်', 'စကား']
Enter a sentence or phrase (or press 'q' to quit): ဗိုက်
Next possible words: ['မ', 'အရမ်း', 'က', 'ကို', 'ထဲ']
Enter a sentence or phrase (or press 'q' to quit): မြန်မြဏ္ တွါ။ ဦှ
Next possible words: ['<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း', 'သန်းခေါင်စာရင်း']
Enter a sentence or phrase (or press 'q' to quit): ကျောင်းသား များ
Next possible words: ['ကို', 'သည်', 'နှင့်', 'တွင်', 'ဖြစ်']
Enter a sentence or phrase (or press 'q' to quit): စိတ်ဝင်စား
Next possible words: ['စရာ', 'တယ်', 'ဖို့', 'မှု', 'ဖွယ်']
Enter a sentence or phrase (or press 'q' to quit): အဲဒီ အချိန် ကို
Next possible words: ['သွား', 'မ', 'လည်း', 'တွေ့', 'ဘယ်']
Enter a sentence or phrase (or press 'q' to quit): ဘယ်လို တေးဂီတ
Next possible words: ['ကို', 'များ', 'မျိုး', 'က', 'အမျိုးအစား']
Enter a sentence or phrase (or press 'q' to quit): ရန်ကုန် နှင့်
Next possible words: ['ပတ်သက်', 'အခြား', 'မြန်မာ', 'တစ်', 'တူ']
Enter a sentence or phrase (or press 'q' to quit):
```

ဒီတစ်ခါတော့ 3gram LM ကို သုံးပြီး next word prediction ကို လုပ်ကြည့်ပါမယ်။  

```
python nltk-lm-predict.py -m .\corpus\mypos.3gram.bin
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Language model loaded successfully.
Enter a sentence or phrase (or press 'q' to quit): ဂျီဒီပီ
Next possible words: ['ကို', '၏', 'သည်', 'ကိန်းဂဏန်း', 'တက်']
Enter a sentence or phrase (or press 'q' to quit): ဈေး က
Next possible words: ['တော့', 'များ', 'ဘာ', 'လည်း', 'ဝယ်']
Enter a sentence or phrase (or press 'q' to quit): ဘူတာရုံ က
Next possible words: ['ဘယ်', 'နေ', 'ဘာ', 'တောင်', 'ယာဉ်စီးခ']
Enter a sentence or phrase (or press 'q' to quit): ရန်ကုန် နှင့်
Next possible words: ['အခြား', 'မန္တလေး', 'နိုင်ငံ', 'ပဲခူး', 'တိုက်ရိုက်']
Enter a sentence or phrase (or press 'q' to quit): မျှော်လင့်ချက် က
Next possible words: ['<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း', 'သန်းခေါင်စာရင်း']
Enter a sentence or phrase (or press 'q' to quit): သော့
Next possible words: ['ကို', '</s>', 'များ', 'ပါ', 'ရှိ']
Enter a sentence or phrase (or press 'q' to quit): မင်း ဘာ
Next possible words: ['ဖြစ်', 'စား', 'လုပ်', 'လို့', 'လို']
Enter a sentence or phrase (or press 'q' to quit): ငါ့ အမ
Next possible words: ['ကြီး', '<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း']
Enter a sentence or phrase (or press 'q' to quit): ကျွန်တော့ သဘော
Next possible words: ['<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း', 'သန်းခေါင်စာရင်း']
Enter a sentence or phrase (or press 'q' to quit): စစ်ဆေး
Next possible words: ['ပေး', 'ကြည့်', 'မှု', 'ပါ', 'ပြီး']
Enter a sentence or phrase (or press 'q' to quit): q
```

ဒီ Python script က text file format LM ဖိုင်ကိုလည်း support လုပ်ပါတယ်။  

```
python nltk-lm-predict.py -m .\corpus\mypos.3gram.bin
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Language model loaded successfully.
Enter a sentence or phrase (or press 'q' to quit): မင်း ကို
Next possible words: ['ပြော', 'ကြည့်', 'ပါ', 'မ', 'ပဲ']
Enter a sentence or phrase (or press 'q' to quit): ကောင်မလေး
Next possible words: ['က', 'နဲ့', 'ကို', 'ရှိ', 'တွေ']
Enter a sentence or phrase (or press 'q' to quit): ကောင်မလေး ရဲ့
Next possible words: ['<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း', 'သန်းခေါင်စာရင်း']
Enter a sentence or phrase (or press 'q' to quit): ကန့်သတ်
Next possible words: ['ထား', 'ချုပ်ချယ်', 'ချက်', 'ခြင်း', 'သည့်']
Enter a sentence or phrase (or press 'q' to quit): အားလပ်ခွင့်
Next possible words: ['ခံစားပိုင်ခွင့်', '<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း']
Enter a sentence or phrase (or press 'q' to quit): အာဂုံဆောင်
Next possible words: ['အလွတ်ကျက်', '<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း']
Enter a sentence or phrase (or press 'q' to quit): မီးဖွား
Next possible words: ['ဖို့', 'ထုံးတမ်း', '<s>', '၁၉၆၂', 'ခုနှစ်']
Enter a sentence or phrase (or press 'q' to quit): ခေါင်းလောင်း ကို
Next possible words: ['အချိန်', '<s>', '၁၉၆၂', 'ခုနှစ်', 'ခန့်မှန်း']
Enter a sentence or phrase (or press 'q' to quit): ဆယ့်ငါး
Next possible words: ['မိနစ်', '</s>', '<s>', '၁၉၆၂', 'ခုနှစ်']
Enter a sentence or phrase (or press 'q' to quit): လည်
Next possible words: ['တာ', 'ချင်', 'စရာ', 'နိုင်', 'ဖို့']
Enter a sentence or phrase (or press 'q' to quit): ရွှေတိဂုံ
Next possible words: ['စေတီတော်', 'ဘုရား', 'စေတီ', 'လို့', 'စေတီတော်မြတ်']
Enter a sentence or phrase (or press 'q' to quit): ဝန်ဆောင်
Next possible words: ['မှု', 'ပေး', 'တဲ့', 'ခ', 'ထူထောင်']
Enter a sentence or phrase (or press 'q' to quit): ထောက်ခံ
Next possible words: ['ပေး', 'မှု', 'သူ', 'အားပေး', 'ခဲ့']
Enter a sentence or phrase (or press 'q' to quit): နာနတ်သီး
Next possible words: ['</s>', 'ကို', 'စား', 'ဖျော်ရည်', 'ဒါမှမဟုတ်']
Enter a sentence or phrase (or press 'q' to quit): စပျစ်ရည်
Next possible words: ['နည်းနည်း', 'ထည့်', '<s>', '၁၉၆၂', 'ခုနှစ်']
Enter a sentence or phrase (or press 'q' to quit): ဘူမိဗေဒ
Next possible words: ['ပညာရှင်', 'ကို', 'တိုင်းတာ', 'ပညာရပ်', 'သည်']
Enter a sentence or phrase (or press 'q' to quit): ကြိုးကြိုးစားစား
Next possible words: ['လုပ်', 'စာကျက်', 'အလုပ်', 'စာ', 'နဲ့']
Enter a sentence or phrase (or press 'q' to quit): q
```

ဒီ nltk-lm.py နဲ့ nltk-lm-predict ပရိုဂရမ်နှစ်ပုဒ်ကနေ language model ရဲ့ အသုံးဝင်ပုံကို ခန့်မှန်းလို့ ရမယ်လို့ ထင်ပါတယ်။ ဒေတာအများကြီးကို သုံးပြီးတော့ LLM (Large Language Model) ဆောက်နိုင်ရင်တော့ intelligent လို့ ဆိုလို့ရတဲ့ အပိုင်းအထိ ဖြစ်လာတယ်။ လက်ရှိ ChatGPT က ဥပမာ တစ်ခုပါပဲ။ အဲဒါကြောင့် languagem modeling နဲ့ ပတ်သက်တဲ့ သုတေသနကလည်း စိတ်ဝင်စားဖို့ ကောင်းပါတယ်။   

## 66. [format_conversion.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/format_conversion.py)  

NLP သမားတွေဆိုရင်တော့ သိပြီးသားဖြစ်ပါလိမ့်မယ်။ ဒေတာ format တွေကို left-to-right ရေးတဲ့ ပုံစံကနေ top-down သို့မဟုတ် column အလိုက်ရေးတဲ့ ပုံစံကို ပြောင်းကြရတာကို။ အထူးသဖြင့် CRF လိုမော်ဒယ်မျိုး training လုပ်ဖို့အတွက် ဆိုရင်ပေါ့။ ထိုနည်းလည်းကောင်း CRF model နဲ့ testing လုပ်ပြီး ရလာတဲ့ column format ဒေတာဖိုင်တွေကိုလည်း ပုံမှန်အတိုင်း left-to-right ရေးတဲ့ပုံစံအဖြစ် ပြောင်းကြရတာကို။ ဒီ python script က အဲဒီအလုပ်အတွက် ရေးထားတာပါ။  

မသုံးခင်မှာ၊ အရင်ဆုံး -h, --help နဲ့ help screen ခေါ်ကြည့်ပါ။  

```
python format_conversion.py --help
usage: format_conversion.py [-h] -f {top-down,left-to-right} input_file output_file

Convert between CRF and left-to-right formats.

positional arguments:
  input_file            Path to the input file
  output_file           Path to the output file

optional arguments:
  -h, --help            show this help message and exit
  -f {top-down,left-to-right}, --format {top-down,left-to-right}
                        Format of the output file
```

NER tagging လုပ်ထားတဲ့ corpus အသေးလေးနဲ့ test-run လုပ်ပြမယ်။  
Filename က small-ner.txt ပါ။ စုစုပေါင်း စာကြောင်းရေ ၃၀ပါ။  

```
မြန်မာ/S-NOP တို့/O သည်/O ခရစ်/B-DATE ၁၁/I-DATE ရာစုနှစ်/E-DATE မှ/O စ/O ၍/O ဗုဒ္ဓ/S-REL သာသနာ/O ကို/O လက်ခံ/O ခဲ့/O ၍/O မည်/O သည့်/O ကိစ္စ/O မဆို/O ဗုဒ္ဓ/S-REL သာသနာ/O ကို/O ထိပ်တန်း/O က/O ထား/O ၍/O စဉ်းစား/O ဆောင်ရွက်/O သော/O ဓလေ့/O ကို/O ရ/O ခဲ့/O ပါ/O သည်/O ။/O
ဘူမိဗေဒ/O ပညာရပ်/O ၏/O ဘာသာရပ်/O ခွဲ/O များ/O ကား/O အောက်/O ပါ/O အတိုင်း/O ပင်/O ဖြစ်/O ၏/O ။/O
အဲဒါ/O ကြောင့်/O တစ်/S-NUM ယောက်/O လောက်/O နားလည်/O ရင်/O တခါတည်း/O မုဒိတာ/O အများကြီး/O ဖြစ်/O တယ်/O ။/O
ငှက်/O ကျောရိုး/O အဆစ်/O များ/O သည်/O ပေါင်းစပ်/O နေ/O သဖြင့်/O ကျောရိုး/O သည်/O မြီးထူးရိုး/O နှင့်/O လည်း/O နီးကပ်/O စွာ/O ဆက်စပ်/O တည်ရှိ/O သည်/O ။/O
ယင်း/O ကိစ္စ/O ကြောင့်/O ခရစ်ယာန်/S-REL လူနည်းစု/O များ/O ဖြစ်/O ကြ/O သည့်/O ကချင်/S-NOP ၊/O ကရင်/S-NOP တို့/O နှင့်/O သွေးကွဲ/O စေ/O ခဲ့/O သည်/O ။/O
အားလုံး/O ကို/O ဟန်ချက်/O ညီညီ/O လျှောက်/O နိုင်/O ရင်/O နောင်တော်/O တို့/O အတွက်/O enjoy/O uni/O life/O ပေါ့/O ။/O
သုတေသန/O တွေ/O လုပ်/O တယ်/O ။/O
သို့သော်လည်း/O ဒဏ်ခတ်/O ပိတ်ဆို့/O မှု/O တွင်/O ပါ/O သော/O ဂယ်ပေါက်/O အားနည်း/O ချက်/O များ/O ကြောင့်/O အချို့/O အနောက်/O နိုင်ငံ/O ရေနံ/O ကုမ္ပဏီ/O ကြီး/O များ/O လုပ်ငန်း/O များ/O ဆက်လက်/O လုပ်ကိုင်/O လျက်/O ရှိ/O ပြီး/O အာရှ/S-LOC စီးပွား/O ရေး/O လုပ်ငန်း/O များ/O က/O လည်း/O ဆက်လက်/O ရင်းနှီးမြှုပ်နှံ/O လျက်/O ရှိ/O သည်/O ။/O
နိဒါန်း/O က/O မွေးဖွား/O ခြင်း/O ။/O
ထို့ကြောင့်/O လည်း/O ပလောပီနံ/O သို့/O ရောက်/O ၍/O များမကြာမီ/O အသက်/O ၁၉/S-NUM နှစ်/O အရွယ်/O တွင်/O မြန်မာ/B-GPE ပြည်/E-GPE သို့/O ပြန်လည်/O ရောက်/O ရှိ/O လာ/O ပြန်/O ကာ/O ရှေးဦးစွာ/O ငယ်/O ဆရာ/O ငယ်/O ကျောင်း/O ဖြစ်/O သော/O ဖာသာရ်-ဝဲလဝါး/S-PER ၏/O အာ/B-LOC -/O စီ/I-LOC -/O အင်မ်/I-LOC ကျောင်း/E-LOC တွင်/O ပင်/O ဆရာ/O အဖြစ်/O ခန့်ထား/O ချီးမြှင့်/O ခြင်း/O ခံ/O ရ/O သည်/O ။/O
တစ်ဆယ့်နှစ်/B-DATE ရာစုနှစ်/E-DATE တွင်/O အာဖဂန်/S-NOP တို့/O သည်/O ဝင်ရောက်/O လာ/O ပြန်/O ၍/O နောက်ဆုံး/O တွင်/O အိန္ဒိယ/B-LOC မြောက်/I-LOC ပိုင်း/I-LOC နှင့်/I-LOC တောင်/I-LOC ပိုင်း/E-LOC ကို/O ပါ/O ယင်း/O တို့/O သိမ်းသွင်း/O နိုင်/O ခဲ့/O သည်/O ။/O
အလွန်/O မြင့်မား/O သော/O ကျောက်တောင်စောက်/O များ/O တွင်/O ဥဥ/O လေ့/O ရှိ/O ကြ/O သည့်/O ပင်လယ်ငှက်/O များ/O စွာ/O တို့/O သည်/O တစ်/O မြုံ/O တွင်/O တစ်/S-NUM လုံး/O ချင်း/O သာ/O ဥ/O လေ့/O ရှိ/O ကြ/O ၍/O လူ/O တို့/O လိုက်လံ/O ပစ်ခတ်/O လေ့/O ရှိ/O သော/O ရေကြက်/O ကဲ့သို့/O ငှက်/O မျိုး/O တို့/O တွင်/O ဖျက်ဆီး/O မည့်/O ရန်သူ/O ပေါများ/O သဖြင့်/O တစ်/O မြုံ/O လျှင်/O ဥ/O ပေါင်း/O ၁ဝ/S-NUM လုံး/O မှ/O အလုံး/O ၂ဝ/S-NUM အထိ/O ဥဥ/O တတ်/O ကြ/O သည်/O ။/O
အလာဂျီ/O ရ/O ရင်/O ၂/S-NUM မျိုး/O ဖြစ်/O မယ်/O ။/O
ဒီ/O အိတ်/O ပြ/O ပေး/O ပါ/O ။/O
မေခိုင်/S-PER တို့/O မွေးဖွား/O ကြီးပြင်း/O နေထိုင်/O ခဲ့/O ရာ/O တောင်ကြီး/S-GPE က/O အဖေ့/O ဆွေမျိုး/O များ/O ရောက်/O လာ/O လျှင်/O ၊/O မြင်းခြံ/S-GPE က/O အမေ့/O ဆွေ/O မျိုး/O များ/O ရောက်/O လာ/O လျှင်/O တော့/O တညီတညာ/O ကျဉ်းမြောင်း/O သေးငယ်/O သည့်/O အိမ်ကလေး/O များ/O ကို/O မ/O နေ/O နိုင်/O ပါ/O ဘူး/O ဆို/O တတ်/O ကြ/O သည်/O ။/O
Website/O တစ်/O ခု/O ကို/O ကျွန်တော်/O တို့/O ဖွင့်/O လိုက်/O ချိန်/O တွင်/O Browser/O ထဲ/O တွင်/O မြင်/O နေ/O ရ/O သော/O Web/O Page/O တစ်/O ခု/O လုံး/O သည်/O Client-side/O ဖြစ်/O သည်/O ။/O
နား/O ထဲ/O က/O နေ/O ခပ်ပြစ်ပြစ်/O အရည်/O တွေ/O ဆင်း/O မယ်/O ။/O
အဲဒီ/O မိခင်/O ဟာ/O ည/S-TIME ည/S-TIME အိပ်မက်/O ဆိုး/O တွေ/O မက်/O ရင်း/O သောက/O များ/O တတ်/O တဲ့/O မိခင်/O မျိုး/O လား/O ၊/O သား/O လေး/O ဘေးရန်/O ကင်း/O စေ/O ဖို့/O အမြဲ/O ဆုတောင်း/O နေ/O တတ်/O တဲ့/O မိခင်/O မျိုး/O လား/O ။/O
မွတ်စလင်/S-REL များ/O အတွက်/O နေ့စဉ်/O ဘဝ/O တွင်/O ထို/O ဆွန္နသ်/O နှင့်/O ဟဒီးဆ်/O များ/O ကို/O လိုက်နာ/O ကျင့်သုံး/O ရန်/O အရေးကြီး/O လေ/O သည်/O ။/O
သွေး/O တွင်း/O မဂ္ဂနီဆီယမ်/O ဓာတ်/O နည်း/O ခြင်း/O ၊/O မူးဝေ/O ထိုင်းမှိုင်း/O ခြင်း/O ၊/O စိတ်/O ရှုပ်ထွေး/O ခြင်း/O ၊/O နှလုံးခုန်/O မြန်/O ခြင်း/O ၊/O မ/O မှန်/O ခြင်း/O ၊/O ကြွက်သား/O များ/O အကြောဆွဲ/O ခြင်း/O ၊/O ဂဏှာမငြိမ်/O ဖြစ်/O ခြင်း/O ၊/O ကြွက်သား/O များ/O အားနည်း/O ခြင်း/O ၊/O ချောင်းဆိုး/O ခြင်း/O ၊/O လည်ချောင်း/O ထဲ/O တစ်ဆို့ဆို့/O ခံစား/O ရ/O ခြင်း/O ၊/O တက်/O ခြင်း/O ။/O
လူ/O တစ်/O ယောက်/O ၊/O အဖွဲ့အစည်း/O တစ်/O ခု/O အနေနဲ့/O လူထု/O ရဲ့/O အမြင်/O မှာ/O ဘယ်လို/O ပုံရိပ်/O ပေါ်/O စေ/O ချင်/O သလဲ/O ဆို/O ပြီး/O တည်ဆောက်/O တာ/O ကို/O PR/O လုပ်/O တယ်/O လို့/O ခေါ်/O ပါ/O တယ်/O ။/O
အမေရိကန်/S-GPE ၃၃/B-NUM သန်း/E-NUM မှာ/O ဖြစ်/O နေ/O ကြ/O ရ/O တယ်/O ။/O
လက်တွေ့/O သင်ယူ/O ရ/O သော/O အချိန်ကာလ/O များ/O မှာ/O အထက်တန်း/O ပညာ/O နှင့်/O ဗဟုသုတ/O များ/O ကို/O စနစ်တကျ/O ပို့ချ/O ရာ/O ကျောင်း/O ကြီး/O များ/O ကို/O တက္ကသိုလ်/O ဟု/O ခေါ်/O သည်/O ။/O
လမ်းဘက်/O က/O လည်း/O အမြန်/O ပြင်/O လေ့/O မ/O ရှိ/O ။/O
မြို့တော်/O ၏/O နေရာ/O တော်တော်/O များများ/O သည်/O ဆောက်လုပ်/O နေ/O ဆဲ/O ဖြစ်/O ပြီး/O ၂၀၁၂/B-DATE ခုနှစ်/E-DATE ဝန်းကျင်/O တွင်/O အပြီးသတ်/O မည်/O ဖြစ်/O သည်/O ။/O
တစ်/S-NUM ယောက်/O တည်း/O ခရီးသွား/O နေ/O ပါ/O တယ်/O ။/O
ကျွန်တော်/O လည်း/O ဒီ/O အတိုင်း/O ပဲ/O ထင်/O တယ်/O
မြင်းခြံ/B-GPE ခရိုင်/E-GPE အလုပ်သမား/B-ORG သမဂ္ဂ/E-ORG နှင့်/I-ORG လယ်သမား/B-ORG သမဂ္ဂ/E-ORG တို့/O တွင်/O အလုပ်အမှုဆောင်/O အဖြစ်/O ဆောင်ရွက်/O ရင်း/O ဖြူး/B-GPE မြို့/E-GPE တွင်/O ကျင်းပ/O သည့်/O မြန်မာ/B-ORG နိုင်ငံ/I-ORG လုံး/I-ORG ဆိုင်ရာ/I-ORG ဖြူး/I-ORG လယ်သမား/I-ORG ကွန်ဂရက်/E-ORG ကြီး/O သို့/O မြင်းခြံ/B-GPE ခရိုင်/E-GPE ကိုယ်စားလှယ်/O အဖြစ်/O တက်ရောက်/O ခဲ့/O သည်/O ။/O
မနေ့/S-DATE က/O တော့/O ရွှေစင့်/S-PER ကို/O အကြံဉာဏ်/O တောင်း/O သည့်/O အနေနှင့်/O ဖွင့်ဟ/O ပြော/O ပြ/O ဖြစ်/O လိုက်/O သည်/O မို့/O သည်/O နေ့/O အားလုံး/O သိ/O နေ/O ပြီ/O ။/O
ကျောက်စာ/O အဦး/O ပိုင်း/O တွင်/O ဝါဆို/S-DATE လ/E-DATE ကို/O မ္လယ်တာ/S-DATE ဟူ၍/O လည်းကောင်း/O ၊/O မြွယ်တာ/S-DATE ဟူ၍/O လည်းကောင်း/O ရေး/O သည်/O ။/O
```

left-to-right ကနေ column format အဖြစ် ပြောင်းမယ် ဆိုရင် အောက်ပါအတိုင်း။  

```
python format_conversion.py .\small-ner.txt .\top-down.txt -f top-down
```

format ပြောင်းပြီးထွက်လာတဲ့ top-down.txt ဖိုင်က အောက်ပါပုံစံအတိုင်း ပါ။ အကုန် ရိုက်မပြပဲ စာကြောင်း တချို့ပဲ ဥပမာအနေနဲ့ ပြထားလိုက်မယ်။  

```
မြန်မာ	S-NOP
တို့	O
သည်	O
ခရစ်	B-DATE
၁၁	I-DATE
ရာစုနှစ်	E-DATE
မှ	O
စ	O
၍	O
ဗုဒ္ဓ	S-REL
သာသနာ	O
ကို	O
လက်ခံ	O
ခဲ့	O
၍	O
မည်	O
သည့်	O
ကိစ္စ	O
မဆို	O
ဗုဒ္ဓ	S-REL
သာသနာ	O
ကို	O
ထိပ်တန်း	O
က	O
ထား	O
၍	O
စဉ်းစား	O
ဆောင်ရွက်	O
သော	O
ဓလေ့	O
ကို	O
ရ	O
ခဲ့	O
ပါ	O
သည်	O
။	O
	
ဘူမိဗေဒ	O
ပညာရပ်	O
၏	O
ဘာသာရပ်	O
ခွဲ	O
များ	O
ကား	O
အောက်	O
ပါ	O
အတိုင်း	O
ပင်	O
ဖြစ်	O
၏	O
။	O
	
အဲဒါ	O
ကြောင့်	O
တစ်	S-NUM
...
...
...
```

CRF format သို့မဟုတ် column format ကနေ left-to-right format ကို ပြောင်းချင်ရင်တော့ အောက်ပါအတိုင်း run ပါ။  

```
python format_conversion.py .\top-down.txt .\left-to-right.txt -f left-to-right
```

output file ဖြစ်တဲ့ left-to-right.txt ဖိုင်ကတော့ ...  

```
မြန်မာ/S-NOP တို့/O သည်/O ခရစ်/B-DATE ၁၁/I-DATE ရာစုနှစ်/E-DATE မှ/O စ/O ၍/O ဗုဒ္ဓ/S-REL သာသနာ/O ကို/O လက်ခံ/O ခဲ့/O ၍/O မည်/O သည့်/O ကိစ္စ/O မဆို/O ဗုဒ္ဓ/S-REL သာသနာ/O ကို/O ထိပ်တန်း/O က/O ထား/O ၍/O စဉ်းစား/O ဆောင်ရွက်/O သော/O ဓလေ့/O ကို/O ရ/O ခဲ့/O ပါ/O သည်/O ။/O
ဘူမိဗေဒ/O ပညာရပ်/O ၏/O ဘာသာရပ်/O ခွဲ/O များ/O ကား/O အောက်/O ပါ/O အတိုင်း/O ပင်/O ဖြစ်/O ၏/O ။/O
အဲဒါ/O ကြောင့်/O တစ်/S-NUM ယောက်/O လောက်/O နားလည်/O ရင်/O တခါတည်း/O မုဒိတာ/O အများကြီး/O ဖြစ်/O တယ်/O ။/O
...
...
...
```

## 67. [format_conversion_with_error_check.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/format_conversion_with_error_check.py)  

Corpus တစ်ခုကို development လုပ်တဲ့အခါမှာ tagging လုပ်တဲ့သူက များရင်များသလို error တွေ ရှိတတ်ပါတယ်။ ဒီပရိုဂရမ်က NER corpus development လုပ်နေစဉ်မှာ ဖြစ်တတ်တဲ့ tagging အမှား (ဒီနေရာမှာ အမှားဆိုတာက typing အမှားကြောင့် word နဲ့ tag နဲ့ ပူးသွားတာမျိုး၊ tag နာမည်က defined လုပ်ထားတဲ့အတိုင်း အတိအကျမတူတဲ့ အမှားမျိုးကို ဆိုလို) တွေကို စစ်ဆေးဖို့အတွက် ရေးခဲ့ပါတယ်။   

Error checking for test-NER corpus (crf or top-down format):  

```
\crf>python ..\..\..\..\format_conversion_with_error_check2.py test.ner tmp.out -f left-to-right -l labels.txt -e tmp-error.out -d " "
Found 28 lines with format errors. Details are written to 'tmp-error.out' if provided.
```

စစ်ဆေးပြီး CRF format နဲ့ ပြင်ဆင်ထားတဲ့ corpus ထဲမှာ အမှားတွေကို တွေ့လို့ tmp-error.out ဆိုတဲ့ ဖိုင်မှာ ရေးပေးပါလိမ့်မယ်။ အဲဒီ ဖိုင်ထဲမှာတော့ အောက်ပါလိုမျိုး အမှားတွေကို တွေ့ရပါလိမ့်မယ်။  

```
Sentence 73, Token 1883: အက်ဥပဒေ S-lAW
Sentence 90, Token 2363: ဖွံ့ဖြိုး o
Sentence 102, Token 2716: ။ O​
Sentence 169, Token 4159: ။ Oဒါ
Sentence 192, Token 4702: ။ Oသတ်မှတ်
Sentence 252, Token 5913: ။ Oရေတွင်း
Sentence 473, Token 11324: ရေး Oအဖွဲ့အစည်း
Sentence 655, Token 15148: မစ္စတာ B-PRE
Sentence 1091, Token 25139: အဖွဲ့အစည်း Oမနုဿဗေဒ
Sentence 1135, Token 26054: မင်း E-MER
Sentence 1157, Token 26581: ။ Oကျွန်မ
Sentence 1246, Token 28440: ။ O​
Sentence 1325, Token 30189: မယ် o
Sentence 1376, Token 31420: ။ O​
Sentence 1398, Token 31853: ။ Oသင်တန်း
Sentence 1483, Token 34014: ။ O​
Sentence 1610, Token 36979: ၁၂ဝ S-NUMD
Sentence 1632, Token 37518: ကျောင်း E-LOCနှင့်
Sentence 1652, Token 38000: ဖိုးဆင် s-PER
Sentence 1669, Token 38432: ရန်ကုန် B-FACTION
Sentence 1669, Token 38433: တက္ကသိုလ် I-FACTION
Sentence 1669, Token 38434: စာကြည့်တိုက် E-FACTION
Sentence 1700, Token 39223: ။ Oအညို
Sentence 1831, Token 42191: ငွေကြေး S-O
Sentence 1834, Token 42285: CB B-PROUDCT
Sentence 1869, Token 43145: ။ Oမယ်လ်ဗင်
Sentence 1953, Token 45128: King E-DENT
Sentence 1982, Token 45745: ။ Oသို့သော်လည်း
```

Error checking for test-NER corpus (left-to-right format):  

```
\ltor>python ..\..\..\..\format_conversion_with_error_check2.py test.ner tmp.out -f top-down -l labels.txt -e tmp-error.out -d "/"
Found 73 lines with format errors. Details are written to 'tmp-error.out' if provided.
```

စစ်ဆေးပြီး left-to-right format နဲ့ ရိုက်ထားတဲ့ corpus ထဲမှာ အမှားတွေကို တွေ့လို့ tmp-error.out ဆိုတဲ့ ဖိုင်မှာ ရေးပေးပါလိမ့်မယ်။ အဲဒီ ဖိုင်ထဲမှာတော့ အောက်ပါလိုမျိုး အမှားတွေကို တွေ့ရပါလိမ့်မယ်။  


```
Sentence 66, Token 17: //O
Sentence 73, Token 11: အက်ဥပဒေ/S-lAW
Sentence 90, Token 4: ဖွံ့ဖြိုး/o
Sentence 102, Token 14: ။/O​
Sentence 111, Token 9: /O
Sentence 141, Token 3: /O
Sentence 141, Token 8: /O
Sentence 162, Token 28: /O
Sentence 162, Token 29: /O
Sentence 169, Token 2: ။/Oဒါ/O
Sentence 186, Token 4: /O
Sentence 186, Token 24: /O
Sentence 192, Token 2: ။/Oသတ်မှတ်/O
Sentence 233, Token 4: /O
Sentence 252, Token 12: ။/Oရေတွင်း/O
Sentence 334, Token 2: /O
Sentence 344, Token 6: /O
Sentence 469, Token 55: သလဲ
Sentence 473, Token 47: ရေး/Oအဖွဲ့အစည်း/O
Sentence 479, Token 7: /O
Sentence 586, Token 3: /O
Sentence 615, Token 4: /O
Sentence 650, Token 34: /O
Sentence 651, Token 1: ဒီလောက်
Sentence 655, Token 1: မစ္စတာ/B-PRE
Sentence 664, Token 3: တယ်
Sentence 790, Token 8: ရဲဘော်
Sentence 802, Token 33: /O
Sentence 855, Token 8: လေ
Sentence 862, Token 11: /O
Sentence 927, Token 9: ပါဦး
Sentence 1026, Token 13: /O
Sentence 1068, Token 5: လေ
Sentence 1091, Token 12: အဖွဲ့အစည်း/Oမနုဿဗေဒ/O
Sentence 1135, Token 2: မင်း/E-MER
Sentence 1143, Token 8: /O
Sentence 1157, Token 4: ။/Oကျွန်မ/O
Sentence 1198, Token 7: လဲ
Sentence 1211, Token 34: /O
Sentence 1246, Token 9: ။/O​/O
Sentence 1325, Token 3: မယ်/o
Sentence 1343, Token 5: /O
Sentence 1376, Token 48: ။/O​
Sentence 1398, Token 2: ။/Oသင်တန်း/O
Sentence 1480, Token 5: ပေါ်ထွန်း
Sentence 1483, Token 15: ။/O​
Sentence 1610, Token 3: ၁၂ဝ/S-NUMD
Sentence 1632, Token 7: ကျောင်း/E-LOCနှင့်/O
Sentence 1632, Token 14: /O
Sentence 1632, Token 17: /O
Sentence 1652, Token 2: ဖိုးဆင်/s-PER
Sentence 1667, Token 24: /O
Sentence 1669, Token 7: ရန်ကုန်/B-FACTION
Sentence 1669, Token 8: တက္ကသိုလ်/I-FACTION
Sentence 1669, Token 9: စာကြည့်တိုက်/E-FACTION
Sentence 1669, Token 18: /O
Sentence 1679, Token 41: /O
Sentence 1680, Token 9: /O
Sentence 1680, Token 18: /O
Sentence 1700, Token 7: ။/Oအညို/O
Sentence 1749, Token 44: မယ်
Sentence 1831, Token 1: ငွေကြေး/S-O
Sentence 1834, Token 36: CB/B-PROUDCT
Sentence 1869, Token 4: ။/Oမယ်လ်ဗင်/S-GPE
Sentence 1882, Token 33: ။/O/O
Sentence 1897, Token 14: /O
Sentence 1951, Token 43: တယ်
Sentence 1953, Token 5: King/E-DENT
Sentence 1969, Token 5: /O
Sentence 1982, Token 10: ။/Oသို့သော်လည်း/O
Sentence 1983, Token 18: လား
Sentence 1990, Token 35: /O
Sentence 1990, Token 37: /O
```

ဒီတစ်ခါတော့ format မှန်အောင် ပြင်ဆင်ပြီး ရိုက်ထည့်ထားတဲ့ NER corpus အသေးလေးနဲ့ format change တာကို လုပ်ပြပါမယ်။ 
CRF format NER corpus အသေးလေးက အောက်ပါအတိုင်းပါ။  

```
ဟုတ်ကဲ့ O
။ O
ဒါ O
က O
တိုကျို S-GPE
အနီး O
မှာ O
ရှိ O
တဲ့ O
ဆိပ်ကမ်း O
မြို့ O
ကြီး O
ပါ O
၊ O
 
အနာ O
ရဲ့​ O
ဘေး O
ပတ်​လည် O
မှာ O
ရောင် O
ပြီး O
မြင့်တက် O
လာ O
ပါ O
တယ် O
။ O
ရေတွင်း O
နှုတ်​ခမ်း O
ပုံစံ O
ဖြစ် O
လာ O
တာ O
ပါ O
။ O
 
ပက် O
နှင့် O
ကလေး O
သူငယ် O
များ O
ကို O
ကယ်ဆယ် O
ရေး O
အဖွဲ့အစည်း O
တို့ O
ဖြစ် O
သည် O
။ O
 
သို့မဟုတ် O
လူ့ O
အဖွဲ့အစည်း O
မနုဿဗေဒ O
ဘာသာရပ် O
နှင့် O
ဆက်စပ် O
လျက် O
ရှိ O
နေ O
ပြန် O
ပေ O
သည် O
။ O
 
မင်္ဂလာ O
ပါ O
ဆရာ O
။ O
ကျွန်မ O
ကလေး O
နှာစေး O
တာ O
တော်တော် O
ဆိုး O
နေ O
လို့ O
ပါ O
ဆရာ O
။ O
 
၉ O
။ O
သင်တန်း O
တက်ရောက် O
ခွင့် O
ရရှိ O
သူ O
များ O
သည် O
သင်တန်း O
ပြီးစီး O
အောင် O
တက်ရောက် O
ရ O
မည် O
။ O
 
၁၉၂၄ S-DATE
တွင် O
ရန်ကုန် B-GPE
မြို့ E-GPE
အမျိုးသား B-LOC
အထက်တန်း I-LOC
ကျောင်း E-LOC
နှင့် O
မြို့မ B-LOC
အမျိုးသား I-LOC
အထက်တန်း I-LOC
ကျောင်း E-LOC
တို့ O
တွင် O
ပညာ O
သင်ကြား O
ခဲ့ O
သည် O
။ O
 
၄င်း O
နောက် O
အဖတ် O
ကွာကျ O
လာ O
မည် O
။ O
အညို O
အမည်း O
စက် O
များ O
အဖြစ် O
ကျန် O
ခဲ့ O
တတ် O
သည် O
။ O
```

ပထမဆုံး crf to left-to-right ကို ပြောင်းမယ်။  

```
format_conversion_with_error_check2.py tmp.out.crf tmp.out.ltr -f left-to-right -l labels.txt -d " " -e tmp-error.out
```

ဒီနေရာမှာ -f left-to-right ဆိုတာက target output ဖိုင်ရဲ့ format ကို ဆိုလိုတာပါ။ ဆန့်ကျင်ဘက်အနေနဲ့ -d or --delimiter ဆိုတဲ့ option ကတော့ input corpus မှာသုံးထားတဲ့ delimiter ကို ဆိုလိုတာပါ။   

Input Corpus မှာက error မရှိလို့ tmp.out.ltr ဆိုတဲ့ ဖိုင်မှာ left-to-right format နဲ့ အောက်ပါအတိုင်း ရေးပေးထားတာကို တွေ့ရပါလိမ့်မယ်။  

```
ဟုတ်ကဲ့/O ။/O ဒါ/O က/O တိုကျို/S-GPE အနီး/O မှာ/O ရှိ/O တဲ့/O ဆိပ်ကမ်း/O မြို့/O ကြီး/O ပါ/O ၊/O
အနာ/O ရဲ့​/O ဘေး/O ပတ်​လည်/O မှာ/O ရောင်/O ပြီး/O မြင့်တက်/O လာ/O ပါ/O တယ်/O ။/O ရေတွင်း/O နှုတ်​ခမ်း/O ပုံစံ/O ဖြစ်/O လာ/O တာ/O ပါ/O ။/O
ပက်/O နှင့်/O ကလေး/O သူငယ်/O များ/O ကို/O ကယ်ဆယ်/O ရေး/O အဖွဲ့အစည်း/O တို့/O ဖြစ်/O သည်/O ။/O
သို့မဟုတ်/O လူ့/O အဖွဲ့အစည်း/O မနုဿဗေဒ/O ဘာသာရပ်/O နှင့်/O ဆက်စပ်/O လျက်/O ရှိ/O နေ/O ပြန်/O ပေ/O သည်/O ။/O
မင်္ဂလာ/O ပါ/O ဆရာ/O ။/O ကျွန်မ/O ကလေး/O နှာစေး/O တာ/O တော်တော်/O ဆိုး/O နေ/O လို့/O ပါ/O ဆရာ/O ။/O
၉/O ။/O သင်တန်း/O တက်ရောက်/O ခွင့်/O ရရှိ/O သူ/O များ/O သည်/O သင်တန်း/O ပြီးစီး/O အောင်/O တက်ရောက်/O ရ/O မည်/O ။/O
၁၉၂၄/S-DATE တွင်/O ရန်ကုန်/B-GPE မြို့/E-GPE အမျိုးသား/B-LOC အထက်တန်း/I-LOC ကျောင်း/E-LOC နှင့်/O မြို့မ/B-LOC အမျိုးသား/I-LOC အထက်တန်း/I-LOC ကျောင်း/E-LOC တို့/O တွင်/O ပညာ/O သင်ကြား/O ခဲ့/O သည်/O ။/O
၄င်း/O နောက်/O အဖတ်/O ကွာကျ/O လာ/O မည်/O ။/O အညို/O အမည်း/O စက်/O များ/O အဖြစ်/O ကျန်/O ခဲ့/O တတ်/O သည်/O ။/O
```

ဒီတစ်ခါတော့ left-to-right ကနေ top-down သို့မဟုတ် CRF format ကို ပြောင်းကြည့်ပါမယ်။     

```
python format_conversion_with_error_check2.py tmp.out.ltr tmp.out.crf -f top-down -l labels.txt -d "/" -e tmp-error.out
```

ထွက်လာတဲ့ top-down or CRF format ဖိုင်က အောက်ပါအတိုင်းပါ။  

```
ဟုတ်ကဲ့ O
။ O
ဒါ O
က O
တိုကျို S-GPE
အနီး O
မှာ O
ရှိ O
တဲ့ O
ဆိပ်ကမ်း O
မြို့ O
ကြီး O
ပါ O
၊ O
 
အနာ O
ရဲ့​ O
ဘေး O
ပတ်​လည် O
မှာ O
ရောင် O
ပြီး O
မြင့်တက် O
လာ O
ပါ O
တယ် O
။ O
ရေတွင်း O
နှုတ်​ခမ်း O
ပုံစံ O
ဖြစ် O
လာ O
တာ O
ပါ O
။ O
 
ပက် O
နှင့် O
ကလေး O
သူငယ် O
များ O
ကို O
ကယ်ဆယ် O
ရေး O
အဖွဲ့အစည်း O
တို့ O
ဖြစ် O
သည် O
။ O
 
သို့မဟုတ် O
လူ့ O
အဖွဲ့အစည်း O
မနုဿဗေဒ O
ဘာသာရပ် O
နှင့် O
ဆက်စပ် O
လျက် O
ရှိ O
နေ O
ပြန် O
ပေ O
သည် O
။ O
 
မင်္ဂလာ O
ပါ O
ဆရာ O
။ O
ကျွန်မ O
ကလေး O
နှာစေး O
တာ O
တော်တော် O
ဆိုး O
နေ O
လို့ O
ပါ O
ဆရာ O
။ O
 
၉ O
။ O
သင်တန်း O
တက်ရောက် O
ခွင့် O
ရရှိ O
သူ O
များ O
သည် O
သင်တန်း O
ပြီးစီး O
အောင် O
တက်ရောက် O
ရ O
မည် O
။ O
 
၁၉၂၄ S-DATE
တွင် O
ရန်ကုန် B-GPE
မြို့ E-GPE
အမျိုးသား B-LOC
အထက်တန်း I-LOC
ကျောင်း E-LOC
နှင့် O
မြို့မ B-LOC
အမျိုးသား I-LOC
အထက်တန်း I-LOC
ကျောင်း E-LOC
တို့ O
တွင် O
ပညာ O
သင်ကြား O
ခဲ့ O
သည် O
။ O
 
၄င်း O
နောက် O
အဖတ် O
ကွာကျ O
လာ O
မည် O
။ O
အညို O
အမည်း O
စက် O
များ O
အဖြစ် O
ကျန် O
ခဲ့ O
တတ် O
သည် O
။ O
```

## 68. [cut_columns.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/cut_columns.py)   

myG2P အဘိဓာန်ကို ဥပမာအနေနဲ့ သုံးပြီး လိုချင်တဲ့ column တွေကို ဆွဲထုတ်ပြပါမယ်။ myG2P အဘိဓာန်မှာရဲ့ format က အောက်ပါအတိုင်းပါ။   

```
1	...ဖြစ်စေ...ဖြစ်စေ	... ဖြစ် စေ ... ဖြစ် စေ	... hpji' sei ... hpji' sei	... pʰjɪʔ sè ... pʰjɪʔ sè
2	...ရိုး...စဉ်	... ရိုး ... စဉ်	... jou: ... sin	... jó ... sɪ̀ɴ
3	...ရိုး...စဉ်	... ရိုး ... စဉ်	... jou: ... zin	... jó ... zɪ̀ɴ
4	...လို...ငြား	... လို ... ငြား	... lou ... nja:	... lò ... ɲá
5	ကကတစ်	က က တစ်	ka. ga- di'	ka̰ gə dɪʔ
6	ကကတိုး	က က တိုး	ka. ga- dou:	ka̰ gə dó
7	ကကုသန်	က ကု သန်	ka. ku. than	ka̰ kṵ θàɴ
8	ကကုသန်	က ကု သန်	kau' ka- than	kaʊʔ kə θàɴ
9	ကကူရံ	က ကူ ရံ	ka. ku jan	ka̰ kù jàɴ
10	ကကြိုး	က ကြိုး	ka. gyou:	ka̰ dʑó
11	ကကြိုးတန်ဆာ	က ကြိုး တန် ဆာ	ka. gyou: da- za	ka̰ dʑó də zà
12	ကကြီကကြောင်လုပ်	က ကြီ က ကြောင် လုပ်	ga- gyi ga- gyaun lou'	gə dʑì gə dʑàʊɴ loʊʔ
13	ကကြီး	က ကြီး	ka. gyi:	ka̰ dʑí
14	ကကြီးထွန်	က ကြီး ထွန်	ka. gyi: htun	ka̰ dʑí tʰʊ̀ɴ
15	ကကွက်	က ကွက်	ka. gwe'	ka̰ gwɛʔ
16	ကချလာ	က ချ လာ	ka- cha- la-	kə tɕʰə là
17	ကချင်	က ချင်	ka- chin	kə tɕʰɪ̀ɴ
18	ကချေသည်	က ချေ သည်	ka. gyei dhe	ka̰ dʑè ðɛ̀
19	ကချော်ကချွတ်	က ချော် က ချွတ်	ka- cho ka- chu'	kə tɕʰɔ̀ kə tɕʰʊʔ
20	ကစဉ့်ကရဲ	က စဉ့် က ရဲ	ga- zin. ga je:	gə zɪ̰ɴ gə jɛ́
...
...
...
```

column no. 2 ကိုပဲ ဆွဲထုတ်ယူချင်တာ ဆိုရင် ...  

```
python cut_columns.py -i myg2p.txt -o dict.txt -c 2
```

အဲဒါဆိုရင် output ဖိုင်ဖြစ်တဲ့ dict.txt ဆိုတဲ့ ဖိုင်မှာ အောက်ပါအတိုင်း ရလာပါလိမ့်မယ်။  

```
...ဖြစ်စေ...ဖြစ်စေ
...ရိုး...စဉ်
...ရိုး...စဉ်
...လို...ငြား
ကကတစ်
ကကတိုး
ကကုသန်
ကကုသန်
ကကူရံ
ကကြိုး
...
...
...
```

ဒီတစ်ခါတော့ column 3 နဲ့ column 5 ကိုပဲ ဆွဲထုတ်ယူကြည့်ရအောင် ...  

```
python cut_columns.py -i myg2p.txt -o dict.txt -c 3,5
```

အောက်ပါလိုမျိုး output ကို ရလာပါလိမ့်မယ်။  

```
... ဖြစ် စေ ... ဖြစ် စေ	... pʰjɪʔ sè ... pʰjɪʔ sè
... ရိုး ... စဉ်	... jó ... sɪ̀ɴ
... ရိုး ... စဉ်	... jó ... zɪ̀ɴ
... လို ... ငြား	... lò ... ɲá
က က တစ်	ka̰ gə dɪʔ
က က တိုး	ka̰ gə dó
က ကု သန်	ka̰ kṵ θàɴ
က ကု သန်	kaʊʔ kə θàɴ
က ကူ ရံ	ka̰ kù jàɴ
က ကြိုး	ka̰ dʑó
က ကြိုး တန် ဆာ	ka̰ dʑó də zà
...
...
...
```

နောက်ဆုံး ဥပမာ အနေနဲ့ column 2 ရယ် ပြီးတော့ column 4 ကနေ 5 အထိကို ဆွဲထုတ်ယူကြည့်ရအောင် ...    

```
python cut_columns.py -i myg2p.txt -o dict.txt -c 2,4-5
```

အဲဒါဆိုရင်တော့ output ဖိုင်မှာ အောက်ပါအတိုင်း ရရှိပါလိမ့်မယ်။  

```
...ဖြစ်စေ...ဖြစ်စေ	... hpji' sei ... hpji' sei	... pʰjɪʔ sè ... pʰjɪʔ sè
...ရိုး...စဉ်	... jou: ... sin	... jó ... sɪ̀ɴ
...ရိုး...စဉ်	... jou: ... zin	... jó ... zɪ̀ɴ
...လို...ငြား	... lou ... nja:	... lò ... ɲá
ကကတစ်	ka. ga- di'	ka̰ gə dɪʔ
ကကတိုး	ka. ga- dou:	ka̰ gə dó
ကကုသန်	ka. ku. than	ka̰ kṵ θàɴ
ကကုသန်	kau' ka- than	kaʊʔ kə θàɴ
ကကူရံ	ka. ku jan	ka̰ kù jàɴ
ကကြိုး	ka. gyou:	ka̰ dʑó
ကကြိုးတန်ဆာ	ka. gyou: da- za	ka̰ dʑó də zà
ကကြီကကြောင်လုပ်	ga- gyi ga- gyaun lou'	gə dʑì gə dʑàʊɴ loʊʔ
...
...
...
```

## 69. []()    

```

```

```

```

## 70. [extract_filename_parts.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/extract_filename_parts.py)   

```
python extract_filename_parts.py -d _ -c 2 -t count -f 'F:\NECTEC\Project\MyanmarSpeech\MyanmarSpeech' -v True  
...
...
...
Processing file: 'my_9135_6838773436.wav', split parts: ['my', '9135', '6838773436'], delimiter: '_'
Processing file: 'my_9135_6874672543.wav', split parts: ['my', '9135', '6874672543'], delimiter: '_'
Processing file: 'my_9135_8132251154.wav', split parts: ['my', '9135', '8132251154'], delimiter: '_'
Processing file: 'my_9135_8216260569.wav', split parts: ['my', '9135', '8216260569'], delimiter: '_'
Processing file: 'my_9135_8800445756.wav', split parts: ['my', '9135', '8800445756'], delimiter: '_'
Processing file: 'my_9135_8984330841.wav', split parts: ['my', '9135', '8984330841'], delimiter: '_'
Processing file: 'my_9762_1332691553.wav', split parts: ['my', '9762', '1332691553'], delimiter: '_'
Processing file: 'my_9762_1375209801.wav', split parts: ['my', '9762', '1375209801'], delimiter: '_'
Processing file: 'my_9762_1545151994.wav', split parts: ['my', '9762', '1545151994'], delimiter: '_'
Processing file: 'my_9762_1798008689.wav', split parts: ['my', '9762', '1798008689'], delimiter: '_'
Processing file: 'my_9762_2206342814.wav', split parts: ['my', '9762', '2206342814'], delimiter: '_'
Processing file: 'my_9762_2946203558.wav', split parts: ['my', '9762', '2946203558'], delimiter: '_'
Processing file: 'my_9762_3152139971.wav', split parts: ['my', '9762', '3152139971'], delimiter: '_'
Processing file: 'my_9762_3320949406.wav', split parts: ['my', '9762', '3320949406'], delimiter: '_'
Processing file: 'my_9762_3455363699.wav', split parts: ['my', '9762', '3455363699'], delimiter: '_'
Processing file: 'my_9762_3890976555.wav', split parts: ['my', '9762', '3890976555'], delimiter: '_'
Processing file: 'my_9762_4183637449.wav', split parts: ['my', '9762', '4183637449'], delimiter: '_'
Processing file: 'my_9762_5699386864.wav', split parts: ['my', '9762', '5699386864'], delimiter: '_'
Processing file: 'my_9762_6066737770.wav', split parts: ['my', '9762', '6066737770'], delimiter: '_'
Processing file: 'my_9762_7115411053.wav', split parts: ['my', '9762', '7115411053'], delimiter: '_'
Processing file: 'my_9762_7662037577.wav', split parts: ['my', '9762', '7662037577'], delimiter: '_'
20
```

## 71. [sort_openslr_transcript.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/sort_openslr_transcript.py)  

[OpenSLR Myanmar Speech Data](https://openslr.org/80/) မှာတင်ပေးထားတဲ့ transcript index ဖိုင်က ကျပန်း အစီအစဉ်နဲ့ ဖြစ်နေလို့ wave ဖိုင်တွေနဲ့ parallel ဖြစ်ဖို့အတွက် sorting စီဖို့ ရေးခဲ့တဲ့ Python script ပါ။  

original filename: line_index_female.tsv ဖိုင်မှာက အောက်ပါအတိုင်း randomized အစီအစဉ်နဲ့ ဖြစ်နေတာ ...  

```
bur_7865_1250917969	ပြီးတော့ တရုတ် နဲ့လည်း ချစ်ကြည်ရင်းနှီးတဲ့ ဆက်ဆံရေး ရှိတယ်
bur_8698_6883351313	အဲ့ဒီ ဝေဖန်မှုတွေ နဲ့ ပတ်သက် လို့ ဘယ်လို တုံ့ပြန်ချင်ပါသလဲ
bur_3260_8853590661	မမီ မွေးဖွားနေတဲ့ အချိန် မှာတော့ ဘုရား ဂုဏ်တော် ကိုပဲ တောက်လျှောက် ရွတ်နေခဲ့ပါတယ်
bur_2446_1980151079	ခင်ဦးသာ နှင့် နန်းလွင်နှင်းပွင့် ပူးပေါင်း ရေးသားသည်
bur_5189_8958061789	ကြည့်ရသည်မှာ မြန်မာ နိုင်ငံ တွင် သူ့ အတွက် ခိုလှုံရာ တခု တွေ့ခဲ့ပုံ ရပါသည်
bur_6884_6350507293	မမဖွေးဖွေး နဲ့ တွေ့ရ တော့ တအား ပျော်တယ် လို့ ပြောပါတယ်
bur_5362_7563127136	အထူးသဖြင့် နိုင်ငံရေး လောက ကို စုစည်းနိုင်ခဲ့သည် ဟု ဆိုနိုင်ပါသည်
bur_7543_6156096513	ကဖင်း မပါဝင်သော ကော်ဖီ သောက်ပါ
bur_8266_0671510151	ကောလင်း မြို့နယ် ရေကြီးတာ က ဆည်ကျိုး လို့ မဟုတ်ဘူး
bur_6118_8081481703	ကျွန်မ အလုပ် ကို လေးလေးစားစား လုပ်ပါတယ်
...
...
...
```

Ascending အစီအစဉ်အတိုင်း sorting လုပ်မယ် ဆိုရင် အောက်ပါအတိုင်း run ပါ။  

```
python sort_openslr_transcript.py -i .\sorting\line_index_female.tsv -o line_index_female_sort.txt -d "\t" -s asc
```

output ဖိုင်မှာတော့ ငယ်စဉ်ကြီးလိုက် အစီအစဉ်နဲ့ စီပေးထားတာကို တွေ့ရပါလိမ့်မယ်။  

```
bur_0366_0045318711	ဆိုတော့ တယ်လီဖုန်း အော်ပရေတာ ဖြစ်လာရင် ကော ဝန်ဆောင်မှုပိုင်း က ကောင်းနိုင်ပါ့မလား
bur_0366_0096392289	ဒီ စနစ် ကို ကျင့်သုံး တော့ အကာအကွယ် ဆိုတာ လည်း မယူကြဘူး
bur_0366_0178258874	ယင်း ရုပ်ရှင် တွင် မင်းမော်ကွန်း နိုင်နိုင်း သင်ဇာဝင့်ကျော် နှင့် စံရတီမိုးမြတို့ က အဓိက ပါဝင် သရုပ်ဆောင်မည် ဖြစ်သည်
bur_0366_0235517782	ဒါကြောင့် ကျွန်မတို့ အတူတကွ ဆုတောင်းကြပါမယ်
bur_0366_0432235369	ကယန်း လူမျိုးတို့ ကို ပဒေါင် ဟု လည်း ခေါ်ဝေါ်ကြ ပြီး ကယန်း အမျိုးသမီးများ သည် လည်ပင်း တွင် ကြေးကွင်းများ ကို ရစ်ပတ် ဝတ်ဆင်ထားကြသည်
bur_0366_0445549145	အနုပညာ ဝမ်းစာ မပြည့်သေးဘဲနဲ့ လည်း မလုပ်ချင်သေးဘူး
bur_0366_0446483510	အကယ်ဒမီ ထူးချွန်ဆု ရရှိစဉ် ကာလ တွင် ငယ် စာရေးဆရာ မင်းလူ မှာ ထောင် တွင်း အကျဉ်းကျ ခံနေရချိန် ဖြစ်သည်
bur_0366_0469985799	ယုံကြည်မှု တည်ဆောက်တဲ့ အခါ လိုအပ်တဲ့ လုပ်ဆောင်ချက် လို့ သုံးသပ်ကြည့်တာပါ
bur_0366_0476333076	သူတို့ က အဲ့ဒါ စစ်ဥပဒေချုပ်ရုံး က လာကြတာ
bur_0366_0627382718	ကချင် ပြည်နယ် နှင့် ဆက်လျက် ရှိသည့် ရှမ်းပြည်နယ် တစ်စိတ်တစ်ပိုင်း လည်း ပါဝင်သည်
...
...
...
```

## 73. [dKNN.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/dKNN.py)     

Running examples are as follows:  

```
python dKNN.py -h
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
usage: dKNN.py [-h] [--mode {knn,deepknn,diffknn}] [--dataset {iris,wine}] [--epochs EPOCHS]
               [--n_layers N_LAYERS] [--n_neighbors N_NEIGHBORS]

This program provides 3 methods for classification: KNN, DeepKNN, and DiffKNN. KNN is the traditional
K-Nearest Neighbors. DeepKNN first trains a neural network on the input data, and uses the trained
model to transform the input data before applying the KNN algorithm. DiffKNN treats the K-Nearest
Neighbors process as a differentiable operation, optimizing the entire process end-to-end.

optional arguments:
  -h, --help            show this help message and exit
  --mode {knn,deepknn,diffknn}
                        The mode to run: traditional KNN, DeepKNN, or DiffKNN.
  --dataset {iris,wine}
                        The dataset to use: Iris or Wine.
  --epochs EPOCHS       The number of epochs to train for (DeepKNN only).
  --n_layers N_LAYERS   The number of layers in the neural network (DeepKNN only).
  --n_neighbors N_NEIGHBORS
                        The number of neighbors to use in KNN.
```

Running KNN ...   
the default dataset is Iris.  

```
python dKNN.py --mode knn
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: iris
Test accuracy (KNN): 1.0
Confusion matrix (KNN):
 [[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

for this time I run with Wine dataset:  

```
python dKNN.py --mode knn --dataset wine
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: wine
Test accuracy (KNN): 0.9444444444444444
Confusion matrix (KNN):
 [[14  0  0]
 [ 1 12  1]
 [ 0  0  8]]
```

diffKNN mode with Iris dataset ...  

```
python dKNN.py --mode diffknn --dataset iris
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: iris
Test accuracy (DiffKNN): 1.0
Confusion matrix (DiffKNN):
 [[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

diffKNN with Wine dataset.  
Note: we don't need hyperparameters for diffKNN approach.  

```
python dKNN.py --mode diffknn --dataset wine
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: wine
Test accuracy (DiffKNN): 0.9444444444444444
Confusion matrix (DiffKNN):
 [[14  0  0]
 [ 1 12  1]
 [ 0  0  8]]
```

For this time, running deepKNN with Wine dataset.  
Number of layers = 2 and number of epochs = 300.  

```
python dKNN.py --mode deepknn --dataset wine --n_layers 2 --epochs 300
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: wine
Test accuracy (DeepKNN): 1.0
Confusion matrix (DeepKNN):
 [[14  0  0]
 [ 0 14  0]
 [ 0  0  8]]
```

Let's play --n_layers and --epochs parameters ...  

```
python dKNN.py --mode deepknn --dataset wine --n_layers 6 --epochs 100
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: wine
Test accuracy (DeepKNN): 0.9722222222222222
Confusion matrix (DeepKNN):
 [[13  1  0]
 [ 0 14  0]
 [ 0  0  8]]
```

For this time, --n_layers = 6 and --epochs = 10 setting ...  

```
python dKNN.py --mode deepknn --dataset wine --n_layers 6 --epochs 10
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: wine
Test accuracy (DeepKNN): 0.8055555555555556
Confusion matrix (DeepKNN):
 [[12  2  0]
 [ 3 10  1]
 [ 0  1  7]]
```

## 74. [dKNN-ver2.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/dKNN-ver2.py) 

```
python dKNN-ver2.py --mode deepknn --draw_diagram
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: iris
Test accuracy (DeepKNN): 0.9666666666666667
Confusion matrix (DeepKNN):
 [[10  0  0]
 [ 0  8  1]
 [ 0  0 11]]
```

deepKNN ရဲ့ Architecture ပုံကို အောက်ပါအတိုင်း ရပါလိမ့်မယ်။  

<p align="center" width="100%">
    <img width="33%" src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/deepknn.png">
</p>

```
python dKNN-ver2.py --mode diffknn --draw_diagram
<frozen importlib._bootstrap>:228: RuntimeWarning: scipy._lib.messagestream.MessageStream size changed, may indicate binary incompatibility. Expected 56 from C header, got 64 from PyObject
Dataset: iris
Test accuracy (DiffKNN): 1.0
Confusion matrix (DiffKNN):
 [[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

diffKNN က ဘယ်လို အလုပ်လုပ်သလဲ ဆိုတာကို ရှင်းပြတဲ့ပုံကို ဆွဲပေးပါလိမ့်မယ်။  

<p align="center" width="100%">
    <img width="33%" src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/diffknn.png">
</p>

## 75. [change_sampling_rate.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/change_sampling_rate.py)  

ပေးလိုက်တဲ့ ဖိုလ်ဒါအောက်မှာ ရှိတဲ့ wave ဖိုင်တွေကို ကိုယ်လိုချင်တဲ့ sampling rate ကို ပြောင်းဖို့အတွက် ရေးခဲ့တဲ့ script ပါ။
သုံးပုံသုံးနည်းက အောက်ပါအတိုင်းပါ။

```
(tacotron2) root@500e9f8181d8:/home/ye/exp/speech_data/MyanmarSpeech# time python ./change_sampling_rate.py --input_folder ./wavs --output_folder ./wavs_22khz --target_sample_rate 22050
Successfully converted 2530 files from original sampling rate to 22050 Hz

real    5m25.370s
user    3m36.422s
sys     0m14.277s
```

Sampling လုပ်စဉ်မှာ error ရှိပြီး ပြောင်းမပေးတာမျိုးလည်း ဖြစ်နိုင်လို့ ဖိုင်အရေအတွက် ကို တိုက်စစ်ပြီး အကြမ်းစစ်တာပါ။  

```
(tacotron2) root@500e9f8181d8:/home/ye/exp/speech_data/MyanmarSpeech# ls ./wavs_22khz/*.wav | wc
   2530    2530   91080
(tacotron2) root@500e9f8181d8:/home/ye/exp/speech_data/MyanmarSpeech# ls ./wavs/*.wav | wc
   2530    2530   75900
(tacotron2) root@500e9f8181d8:/home/ye/exp/speech_data/MyanmarSpeech#
```

## 76. [check_silence.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/check_silence.py)  


အသံဒေတာရဲ့ root mean square (RMS) ကို NumPy library ကိုသုံးပြီးတွက်ထားပါတယ်။ RMS ဆိုတာက math formula အနေနဲ့ ရေးမယ် ဆိုရင်အောက်ပါအတိုင်းပါ။   

$$RMS = \sqrt{\frac{1}{N} \sum_{i=0}^{N-1} x^2[i]}$$

ဒီ formula မှာ N က sequence မှာရှိနေတဲ့ sample စုစုပေါင်း အရေအတွက်ကို ကိုယ်စားပြုပါတယ်။   
ပြီးတော့ x[i] ဆိုတာကတော့ i-th sample ရဲ့ amplitude ပါ။   

တကယ်လို့ တွက်လို့ ရလာတဲ့ RMS တန်ဖိုးက < threshold ဆိုရင် silent ဖြစ်နေတယ်လို့ ဆုံးဖြတ်တယ်။  

Running example ...  

```
python ./check_silence.py --input_folder ./test_out/
0.wav might be silent, RMS=0.00010648194071440837
1.wav might be silent, RMS=0.0
2.wav might be silent, RMS=0.0
```

## 77. [graph_lm_spellchek.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/graph_lm_spellchek.py)  


spell_err.txt ဖိုင်က အောက်ပါအတိုင်း ...  

```
ကျောင်သား
မရား
ချစသူ
ပိသာ
ဖုရား
ဆယာမား
ထမင်
ပဲပုတ်
ဉီးဉီး
မြက်မှန်
ပိဿ
မိန်းက
ချက
```

```
python ./graph_spellcheck2.py -d ./corpus/dict.txt -e ./spell_err.txt -o checked.txt -m 6 -c ./corpus/mypos.txt -n 3
```

မှားတာကို detect လုပ်ပြီး စာလုံးပေါင်း အမှန်ကို ပြင်ပေးထားတဲ့ output ကအောက်ပါအတိုင်း ...  

```
No correction found for "ကျောင်သား"
No correction found for "မရား"
No correction found for "ချစသူ"
No correction found for "ပိသာ"
No correction found for "ဖုရား"
No correction found for "ဆယာမား"
The correction for "ထမင်" is "ထမင်းဘူး"
No correction found for "ပဲပုတ်"
No correction found for "ဉီးဉီး"
No correction found for "မြက်မှန်"
The correction for "ပိဿ" is "ပိဿာ"
The correction for "မိန်းက" is "မိန်းကလေး"
The correction for "ချက" is "ချက်ချာ"
```

လက်ရှိ experiment က myG2P dictionary နဲ့ myPOS ဒေတာကို language model ဆောက်ပြီး စမ်းကြည့်ထားတာ။ လက်ရှိ ရလဒ်ထက် ပိုကောင်း စေချင်ရင်တော့ error model ကို ဆောက်ပြီး (error dictionary ကိုတော့ပြင်ရမယ်) စမ်းလို့ ရနိုင်တယ်။ သို့သော် ရလဒ်ကတော့ ဘယ်လောက်ထိ တိုးတက်လာမလဲ ဆိုတာက ပြောလို့ မရဘူး။ word level နဲ့ပဲ သွားနေတော့ ...  

## 78. [detect_language_ver1.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/detect_language_ver1.py)  

ဒီ ပရိုဂရမ်မှာ [langdetect](https://github.com/Mimino666/langdetect) ဆိုတဲ့ Python library ကို သုံးပြီး input ဖိုင်ထဲက စာကြောင်း တစ်ကြောင်းချင်းစီရဲ့ ဘာသာစကားကို detect လုပ်ပါတယ်။ ပြီးမှ တစ်ဖိုင်လုံးမှာ ပါဝင်တဲ့ ဘာသာစကား တစ်ခုခြင်းစီရဲ့ % ကို တွက်ပြီး print လုပ်ပေးတာ ဖြစ်ပါတယ်။ တစ်ခုရှိတာက ဒီ library က ကြာလည်း ကြာပါပြီ။ Original version က Java နဲ့ ရေးထားတာပါ။ Language detection လုပ်တဲ့ algorithm ကတော့ character n-gram ကိုသုံးပြီးတော့ Naive Bayse နဲ့ classification လုပ်တဲ့ ပုံစံမျိုးပါ။ Approach အသေးစိတ် ကတော့ slideshare မှာတင်ထားတဲ့ [presentation slide](https://www.slideshare.net/shuyo/language-detection-library-for-java) ကို မှီငြမ်းပါ။ အဲဒီ ဆလိုက်ထဲမှာ ဖော်ပြထားတာကတော့ သူတို့ရဲ့ experiment ရလဒ်ကနေ ဘာသာစကားပေါင်း ၄၉ ဘာသာကို 99.8% precision ရတဲ့အထိ ခွဲခြားပေးနိုင်တယ်ပါတယ်တဲ့ ...     

ဒီနည်းလမ်းကိုပဲ တကယ်ယူသုံးမယ် ဆိုရင်တော့ ဘာသာစကားအသစ်တစ်ခုကို ထပ်တိုးချင်တာ၊ သိအောင်လုပ်ချင်တာ ဆိုရင်တော့ text corpus ဖိုင်ကို ပြင်ဆင်ပြီး java program ကို run ပြီးတော့ language profile ဆိုတာကို ဆောက်ပေးရပါတယ်။ ဒီ python script မှာက ရှိပြီးသား library ကိုပဲ ယူသုံးတာမို့လို့ မြန်မာစာတို့ ခမာစာတို့ ဆိုရင် language နာမည်နဲ့တကွ classification မလုပ်ပေးနိုင်ပါဘူး။ သို့သော် တော်တော်များများသော ဘာသာစကားကို detect လုပ်ပေးနိုင်ပါလိမ့်မယ်။ ပြီးတော့ မြန်မာစာတို့လို ဘာသာစကားတွေကိုတော့ Unknown ဆိုတဲ့ အမျိုးအစားအောက်မှာ ခွဲခြားပြီး ရာခိုင်းနှုန်းကို တွက်ပေးပါလိမ့်မယ်။  

Multilingual input ဖိုင်ကို အောက်ပါအတိုင်း ပြင်ဆင်ပြီး စမ်းခဲ့ပါတယ်။  

```
မျှော်လင့် ရင်း ဝေး မ မျှော်လင့် ချင် တော့ ပါ ဘူး စိတ် ရော လူ ရော ပင်ပန်း လို့ ပါ
Please note that you should consult the latest OpenAI documentation for accurate information on how to use the GPT-4 or any later models, as APIs can change and my training only goes up until September 2021.
ထိုစဉ် ဇကာပေါက် မှ ကြေညာ ချက် ထုတ်ပြန် လိုက် သည် 😁 😁 😁
Eleventh of July, Twenty-Three.
မေး ထား တာ တွေ လည်း မ ဖြေ ဘူး ဘယ်လို လဲ
ကိုယ် တွေ က မြန်မာ ၊ အမေရိကန် က မ ဟုတ် ၊ ဥရောပ က မ ဟုတ် ပါ ။
ไม่เป็นไร
ส่วนห้องแบบตะวันตกจะบุพื้นด้วยไม้หรือพรมและมักวางโต๊ะเก้าอี้ไว้ใช้ ปัจจุบันห้องแบบตะวันตกมีมากขึ้น และผู้ที่ใช้ห้องทั้งสองแบบผสมผสานกันก็มีมากขึ้นด้วย
越南高层和中美互动频频 既要美国航母存在也要连接中国高铁
ယခု ထက် လည်း ပို ၍ ပို ၍ အောင်မြင် နိုင် ပါစေ ။
（台灣英文新聞／生活組　綜合報導）今年最受矚目的一組時尚關鍵字非「#多巴胺」莫屬，多巴胺又稱為「快樂物質」，主張在日常中加入豐富的色彩，刺激視覺產生勾起愉悅感的多巴胺。今年夏天，除了穿搭跟上流行，居家布置也不能忽略，快用顏色讓你與身邊的人都能夠獲得活力，趕走夏天疲勞症候群。
*若有性騷、性暴力事件通報或諮詢，請聯絡113婦幼保護專線，若遇狀況緊急時請直接撥打110報案專線。
¿Cómo está usted?
​អនុស្សរណៈ​នៃ​ការយោគយល់​គ្នា​នេះ​ត្រូវ​បាន​ចុះហត្ថលេខា​នៅ​ទី​ក្រុងភ្នំពេញ​រវាង​អគ្គនាយក​ធនាគារ​ជាតិ​កម្ពុជា​ ​លោក​ ​គីម​ទី​ ​កោ​ម​លី​ ​និង​អនុប្រធាន​ ​Union​Pay​ ​International​ ​លោក​ ​L​ar​r​y​ ​Wan​g​ ​ក្រោមអធិបតីភាព​ ​លោកស្រី​ ​ជា​ ​សិរី​ ​ទេសាភិបាល​រង​ធនាគារ​ជាតិ​កម្ពុជា​។​
¿Cómo estás?
¿Qué tal? 
金閣寺行きます
浴衣買います
លោកគ្រូ​ ​អ្នក​គ្រូ​ ​និង​សិស្សានុសិស្ស​ចំនួន​៣​វិទ្យាល័យ​ ​បាន​ធ្វើ​ទស្សនកិច្ច​ស្វែងយល់​ពី​គម្រោង​ ​ស្រាវជ្រាវ​បុរាណ​វិទ្យា​នៅ​បរិវេណ​វត្ត​កោះ​កែវ​ជុ​លា​មុនី​ព្រះ​ធម្មចេតិយ​ ​ក្នុង​ក្រុង​សៀមរាប​។​
```

Run ကြည့်ရင် အောက်ပါအတိုင်း detect လုပ်လို့ ရတဲ့ ဘာသာစကားတွေကို % နဲ့ ပြသပေးပါလိမ့်မယ်။  
Error တော့ မကင်းပါဘူး။ French 5.26% ဆိုတာနဲ့ Korean 5.26% ဆိုတာက classification error ပါ။  

```
python detect_language_ver1.py multi_lingual_text.txt
unknown: 36.84%
English: 10.53%
Thai: 10.53%
Chinese Simplified: 5.26%
Chinese Traditional: 5.26%
Korean: 5.26%
Spanish: 10.53%
French: 5.26%
Japanese: 10.53%
```

## 79. [detect_language_ver2.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/detect_language_ver2.py)   

Python script no. 78 မှာတုန်းက langdetect ကနေ စစ်ပြီး အောက်ပါအတိုင်း Unknown ဖြစ်တာတွေ ရှိပါတယ်။  

```python
def detect_language(text):
    try:
        lang = detect(text)
        if lang in language_codes:
            return language_codes[lang]
        else:
            return 'unknown'
    except:
        return 'unknown'
```

ဖြေရှင်းတဲ့ နည်းကတော့ အရင်ဆုံး Unicode table ရဲ့ code နံပါတ်တွေရဲ့ range တွေအလိုက် ဘာသာစကားတွေကို python dictionary ဆောက်ပြီး အောက်ပါအတိုင်း သတ်မှတ်လိုက်ပါတယ်။   

```python
language_unicode_ranges = {
    'Latin': ('\u0020', '\u007E'),
    'Latin Extended-A': ('\u0100', '\u017F'),
    'Latin Extended-B': ('\u0180', '\u024F'),
    'IPA Extensions': ('\u0250', '\u02AF'),
    'Spacing Modifier Letters': ('\u02B0', '\u02FF'),
    'Combining Diacritical Marks': ('\u0300', '\u036F'),
    'Greek and Coptic': ('\u0370', '\u03FF'),
    'Cyrillic': ('\u0400', '\u04FF'),
    'Cyrillic Supplement': ('\u0500', '\u052F'),
    'Armenian': ('\u0530', '\u058F'),
    'Hebrew': ('\u0590', '\u05FF'),
    'Arabic': ('\u0600', '\u06FF'),
    'Syriac': ('\u0700', '\u074F'),
...
...
...
    'CJK Compatibility Ideographs': ('\uF900', '\uFAFF'),
    'Alphabetic Presentation Forms': ('\uFB00', '\uFB4F'),
    'Arabic Presentation Forms-A': ('\uFB50', '\uFDFF'),
    'Variation Selectors': ('\uFE00', '\uFE0F'),
    'Vertical Forms': ('\uFE10', '\uFE1F'),
    'Combining Half Marks': ('\uFE20', '\uFE2F'),
    'CJK Compatibility Forms': ('\uFE30', '\uFE4F'),
    'Small Form Variants': ('\uFE50', '\uFE6F'),
    'Arabic Presentation Forms-B': ('\uFE70', '\uFEFF'),
    'Halfwidth and Fullwidth Forms': ('\uFF00', '\uFFEF'),
    'Specials': ('\uFFF0', '\uFFFF')
}
```

ပြီးတော့မှ detect_dominant_script ဆိုတဲ့ function ကို ဆောက်ထားပြီး unknown exception ဖြစ်တဲ့ sentence တွေကို function argument အနေနဲ့ ပေးလိုက်ပြီး ဘာသာစကား ထပ်ခွဲခြားတဲ့ အလုပ်ကို လုပ်တဲ့ ပုံစံပါ။  

```python
def detect_dominant_script(sentence):
    script_counts = Counter(detect_unicode_script(c) for c in sentence if detect_unicode_script(c) is not None)
    if not script_counts:  # The sentence does not contain any characters from known scripts
        return None
    return script_counts.most_common(1)[0][0]
```

အဲဒီလိုနည်းနဲ့ ပထမ ဗားရှင်းမှာ မသိတဲ့ မြန်မာစာတို့ ခမာဘာသာစကားတို့ကို classification လုပ်ပေးနိုင်အောင် update လုပ်ထားတဲ့ ပရိုဂရမ်ပါ။ ဒီကောင်ကိုတော့ version 2.0 အဖြစ် သတ်မှတ်ထားပါတယ်။  

```
python detect_language_ver2.py multi_lingual_text.txt
English: 10.53%
Thai: 10.53%
Chinese Simplified: 5.26%
Chinese Traditional: 5.26%
Korean: 5.26%
Spanish: 10.53%
French: 5.26%
Japanese: 10.53%
Guess, Myanmar: 26.32%
Guess, Khmer: 10.53%
```

တစ်ခု သိထားရမှာက language detection ဆိုတဲ့ problem ကလည်း တကယ့် လက်တွေ့မှာ 100% မှန်ဖို့ ဆိုတာက ခက်ပါတယ်။ ဘာကြောင့်လဲ ဆိုတော့ တချို့ Unicode နံပါတ်နဲ့ သတ်မှတ်ထားတဲ့ စာလုံးတွေကလည်း share လုပ်ပြီး သုံးတဲ့ ဘာသာစကားတွေက ရှိလို့ပါ။ ဥပမာ မြင်သာအောင် ပြောရရင် မြန်မာ ဗျည်းတချို့ ဆိုရင် စကောကရင်ကကော၊ ရှမ်းကကော သုံးပါတယ်။ တကယ်က ဒီနေရာမှာ မြင်သာအောင် မြန်မာ ဗျည်းလို့ ပြောနေပေမဲ့ ကရင်တွေ၊ ရှမ်းတွေအနေနဲ့ ကြည့်ရင် ကရင်စာလုံး၊ ရှမ်းစာလုံးပါပဲ။ အသံထွက်လည်း မတူကြပါဘူး။ ထိုနည်းလည်းကောင်း ဥရောပ ဘာသာစကားတွေမှာလည်း အဲဒီလိုမျိုး စာလုံးတွေကို ရှဲလုပ်ပြီးသုံးနေကြတဲ့ ဘာသာစကားတွေက အများကြီးပါ။ အဲဒါကြောင့် input ဖိုင်ထဲမှာ ရှိတဲ့ စာကြောင်းတွေကို အခြေခံပြီး ဘယ်ဘာသာစကားတွေက ဘယ်လောက် ရာခိုင်းနှုန်းဆိုတာကို တိတိကျကျ classification လုပ်ရတဲ့ အလုပ်က အရမ်း အလွယ်ကြီး မဟုတ်တာကိုတော့ သိထားစေချင်ပါတယ်။ နောက်တစ်ခုက detection လုပ်ပေးနိုင်တဲ့ speed ကလည်း လက်တွေ့ အလုပ်တွေမှာဆိုရင် အရေးကြီးပါတယ်။   

## 80. [embedder.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/embedder.py)   

NLP field, AI field ထဲမှာ word embedding ဆိုတာကို သိထားဖို့ အရမ်းအရေးကြီးပါတယ်။ ဘာကြောင့်လဲ ဆိုတော့ text တွေ စာကြောင်းတွေကို ကိုယ်လိုချင်တဲ့ မော်ဒယ် တစ်ခုခု မဆောက်ခင်မှာ အရင်ဆုံး embedding တစ်မျိုးမျိုးကို လုပ်ကြရတာမို့ပါ။ ပြီးတော့ ဒီ word embedding ဟာလည်း သုတေသန တစ်ခုအနေနဲ့ စိတ်ဝင်စားဖို့ ကောင်းပါတယ်။ 

ဒီ script ကို သုံးပြီး text embedding မှာ နာမည်ကြီးတဲ့၊ တကယ်လည်း အသုံးဝင်တဲ့ tf-idf, word2vec နဲ့ fasttext ဆိုတဲ့ embedding သုံးမျိုးကို လုပ်ကြည့်လို့ ရပါလိမ့်မယ်။  

Manually word segmented လုပ်ထားတဲ့ ဗမာစာ corpus information က အောက်ပါအတိုင်းပါ။  

```
(base) rnd@gpu:~/demo/ai4my/corpus$ wc segmentation-data-updated2
  213104  5342347 69130416 segmentation-data-updated2
```

shell script တစ်ပုဒ် ရေးပြီး training လုပ်ပါမယ်။  

```
(base) rnd@gpu:~/demo/ai4my$ cat run_train.sh
#!/bin/bash

# training with default parameters
time python ./embedder.py ./corpus/segmentation-data-updated2 -e tfidf
time python ./embedder.py ./corpus/segmentation-data-updated2 -e word2vec
time python ./embedder.py ./corpus/segmentation-data-updated2 -e fasttext
```

Training ...  

```
(ai4my) rnd@gpu:~/demo/ai4my$ ./run_train.sh
/home/rnd/anaconda3/envs/ai4my/lib/python3.8/site-packages/sklearn/feature_extraction/text.py:525: UserWarning: The parameter 'token_pattern' will not be used since 'tokenizer' is not None'
  warnings.warn(
TF-IDF embeddings have been saved to ./corpus/segmentation-data-updated2_tfidf.npz
TF-IDF features have been saved to ./corpus/segmentation-data-updated2_tfidf_features.json

real    0m6.928s
user    0m7.068s
sys     0m2.454s
Word2Vec model has been saved to ./corpus/segmentation-data-updated2_word2vec.model

real    0m15.679s
user    0m51.297s
sys     0m2.676s
FastText model has been saved to ./corpus/segmentation-data-updated2_fasttext.model

real    0m46.201s
user    2m38.502s
sys     0m3.190s
(ai4my) rnd@gpu:~/demo/ai4my$
```

Training က အဆင်ပြေပြေနဲ့ run လို့ ပြီးသွားရင်တော့ အောက်ပါအတိုင်း tf-idf, word2vec နဲ့ fasttext မော်ဒယ်တွေကို ရရှိပါလိမ့်မယ်။  

```
(base) rnd@gpu:~/demo/ai4my/corpus$ ls *.{model,npz} -lh
-rw-rw-r-- 1 rnd rnd 41M Jul 13 00:52 segmentation-data-updated2_fasttext.model
-rw-rw-r-- 1 rnd rnd 36M Jul 13 00:51 segmentation-data-updated2_tfidf.npz
-rw-rw-r-- 1 rnd rnd 41M Jul 13 00:51 segmentation-data-updated2_word2vec.model
```

မော်ဒယ်ဖိုင်တွေ အပြင် တခြား အောက်ပါ output ဖိုင်တွေကိုလည်း save လုပ်ပေးပါလိမ့်မယ်။  
ဒီနေရာမှာ၊ .npy ဖိုင်ကတော့ fasttext နဲ့ သက်ဆိုင်ပြီး၊ .json ဖိုင်ကတော့ tf-idf မော်ဒယ်ရဲ့ feature information ကိုသိမ်းဆည်းပေးထားတာ ဖြစ်ပါတယ်။  

```
(base) rnd@gpu:~/demo/ai4my/corpus$ ls *.{json,npy} -lh
-rw-rw-r-- 1 rnd rnd 763M Jul 13 00:52 segmentation-data-updated2_fasttext.model.wv.vectors_ngrams.npy
-rw-rw-r-- 1 rnd rnd 5.0M Jul 13 00:51 segmentation-data-updated2_tfidf_features.json
```

## 81. [test_embedding.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/test_embedding.py)  

အထက်က ပရိုဂရမ် နံပါတ် 80 ကိုသုံးပြီး ဆောက်ထားခဲ့တဲ့ tf-idf, word2vec နဲ့ fasttext မော်ဒယ်တွေကိုသုံးပြီး similar word တွေကို ဆွဲထုတ်ကြည့်ကြရအောင်။  

command line ကနေ ကိုယ်ရှာချင်တဲ့ မြန်မာစာလုံးကို parse လုပ်ပြီး သက်ဆိုင်ရာ tf-idf, wrod2vec, fasttext တန်ဖိုးတွေကို ကြည့်ဖို့အတွက် အောက်ပါ shell script ကို ရေးခဲ့တယ်။  

```bash
#!/bin/bash

echo "##Testing 1";
echo "Result for tfidf:";
python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json

echo "Result for word2vec:";
python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_word2vec.model

echo "Result for fasttext:";
python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_fasttext.model

echo "##Testing 2"
echo "Result for tfidf:";
python test_embedding.py -i "ရန်ကုန်"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json
echo "Result for word2vec:";
python test_embedding.py -i "ရန်ကုန်"  -m ./corpus/segmentation-data-updated2_word2vec.model
echo "Result for fasttext:";
python test_embedding.py -i "ရန်ကုန်"  -m ./corpus/segmentation-data-updated2_fasttext.model

echo "##Testing 3";
echo "Result for tfidf:";
python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json
echo "Result for word2vec:";
python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_word2vec.model
echo "Result for fasttext:";
python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_fasttext.model

echo "##Testing 4";
echo "Result for tfidf:";
python test_embedding.py -i "ကို"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json
echo "Result for word2vec:";
python test_embedding.py -i "ကို"  -m ./corpus/segmentation-data-updated2_word2vec.model
echo "Result for fasttext:";
python test_embedding.py -i "ကို"  -m ./corpus/segmentation-data-updated2_fasttext.model

echo "##Testing 5";
echo "Result for tfidf:";
python test_embedding.py -i "ပြော"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json
echo "Result for word2vec:";
python test_embedding.py -i "ပြော"  -m ./corpus/segmentation-data-updated2_word2vec.model
echo "Result for fasttext:";
python test_embedding.py -i "ပြော"  -m ./corpus/segmentation-data-updated2_fasttext.model
(ai4my) rnd@gpu:~/demo/ai4my$
```

run ကြည့်ရင် အောက်ပါအတိုင်း ...  

```
(ai4my) rnd@gpu:~/demo/ai4my$ ./run_test.sh
##Testing 1
Result for tfidf:
[0.         0.         0.         ... 0.41451251 0.         0.        ]
Result for word2vec:
[ 0.14051841 -0.68668884  0.5115563  -3.0499332   5.7556815   0.8454542
 -0.62324345  0.12552062 -2.5734239  -0.76783305 -2.173285    1.3419219
 -2.2723837  -0.77935576  0.10348039 -0.19630149 -0.60146797 -0.22666754
  0.09633887 -0.2954048   0.0366744   0.62919784 -0.15426072  2.6627114
  0.79220194 -0.52254665 -0.74671394  0.06791671  1.1348633   3.1314154
 -1.0291815  -0.7988967   2.2117496   1.1573496  -0.36746907 -0.82535917
  0.16629383  0.2895536  -0.68847436  1.8033355   2.4647312  -0.889936
  0.9412505  -0.4174117   1.3694437   0.29462582 -1.896008    2.7443807
  0.59922063 -1.0600252   2.0065672   2.527175   -1.5921103   1.0148772
  3.1927683  -0.94838655 -0.60671645  1.2138846   0.86101097 -0.49720362
  1.4193966   1.8640296   2.3634326   0.5610619  -1.1966776  -0.27746892
 -0.9176449  -0.8144077   0.58145666  2.4334896   1.8968152   1.4962431
  0.50146633  1.4751241   4.116864    1.3352146   1.1782668  -3.0635712
 -0.33884022 -0.8616385  -1.9249173   2.688064    1.196899   -3.0315707
  1.2786375  -1.1624686  -1.4380375   3.120259   -2.0206847   0.5624521
  0.29767874  0.0896015   0.16789739 -0.55603665  1.3717598   1.9484823
 -0.35269892 -2.5118613   2.5260692  -1.8374244 ]
Result for fasttext:
[ 6.4878267e-01 -2.2126536e+00  3.5132480e-01 -1.9267787e+00
  1.3093240e+00  8.2213067e-02 -3.3618832e+00 -1.8596691e+00
  2.5085211e+00  1.6204206e+00 -2.2018734e-01  1.8130890e+00
 -9.7072142e-01 -4.7185069e-01 -7.7207899e-01 -3.9259508e+00
  3.2554364e+00 -9.2827684e-01  1.6309135e+00  9.4588619e-01
  5.5521264e+00  3.1193027e-01 -1.4385113e-01  1.0924323e+00
  7.7641851e-01 -1.0916375e+00 -1.8533227e-01 -1.8374684e+00
 -3.4286072e+00 -1.8732318e+00 -1.2631197e+00 -1.3165445e+00
  2.8898897e+00  3.2409310e-01 -1.1185416e+00 -2.3375571e+00
 -1.0281185e+00  8.8011628e-01 -2.5302870e+00  2.1656573e+00
  1.5026281e+00  5.8797646e-01 -5.8619261e-01  7.0694208e-01
  1.9595686e+00 -1.5482435e+00 -1.1912521e+00  6.7752784e-01
  9.3396658e-01 -2.8947026e-01 -1.3444813e-01  1.7677765e+00
  2.0283196e+00 -5.3005405e-03  3.2050428e-01  1.0289551e+00
  2.9077005e-01  1.2997566e+00  1.3598216e+00  1.4854397e+00
 -1.1261486e+00  1.6196610e+00  1.8652878e+00 -6.0013080e-01
 -4.3698782e-01 -8.6271900e-01  7.0951372e-01 -2.1031220e+00
 -1.3900040e+00 -8.3275932e-01 -4.3193415e-02 -2.9695997e-01
  7.9311484e-01 -5.4200944e-02  1.6178486e+00  1.0724357e+00
  2.7259400e+00  1.6974579e+00  2.3183799e+00 -2.3489056e+00
 -3.5775792e-02  1.4519529e+00 -2.0625870e+00  1.1440476e+00
  9.3639505e-01 -3.2858031e+00 -1.6901885e+00  2.2528982e-01
  1.3262314e+00  1.1254174e+00 -8.1627232e-01  2.2790864e+00
  1.6439852e+00 -1.8453045e-01  1.0372702e+00  1.5200241e+00
  1.7925552e+00 -4.9159089e-01  8.3837211e-01  1.0181752e+00]
##Testing 2
Result for tfidf:
[0.         0.         0.04719886 ... 0.         0.         0.        ]
Result for word2vec:
[ 1.2270965e-01 -4.4734806e-01  1.3054602e+00 -9.8946428e-01
 -5.7505184e-01 -3.7023365e-01 -5.5133802e-01 -7.2360116e-01
 -6.7729712e-02  2.1428950e+00 -6.2880248e-01 -5.2580804e-02
  1.7056438e+00 -1.8507591e+00  2.5781792e-01  3.6815444e-01
 -4.4058105e-01  1.4582782e+00 -2.1958508e+00 -6.6873997e-01
 -8.5130024e-01 -5.7022477e-04  1.1989934e+00 -5.9115160e-01
 -1.3952394e+00 -1.1350691e+00 -9.4991797e-01 -5.7709861e-01
 -8.2162684e-01  1.1989971e+00 -2.2318950e+00  1.9599870e+00
 -1.3187227e-01  7.9408121e-01 -2.4910252e+00 -6.2546104e-01
  9.7835816e-02 -8.4523940e-01 -3.2417295e+00 -2.8182435e-01
 -2.0712113e-02 -1.1770766e+00  1.2072645e+00  9.5745623e-01
  5.3826070e-01  2.1184756e-01  7.5747085e-01  9.6323001e-01
 -3.5952663e-01 -8.5082579e-01 -3.8863990e-02 -5.4823327e-01
 -8.6159572e-02  2.7309844e-01  1.3976886e+00  3.9402670e-01
  3.3213109e-02  1.8270534e+00 -6.9701992e-02  1.5283072e+00
 -2.2302857e-01  3.5051128e-01 -9.0043056e-01  9.2274457e-02
 -2.1546297e+00  6.3314676e-01  6.2537682e-01  1.5430897e+00
 -4.5778593e-01  3.1117392e+00  1.5718734e+00  2.4501428e-01
 -4.4538903e-01  1.9765707e+00  2.5041788e+00  9.0311724e-01
  1.8411336e+00 -1.8967642e+00 -1.0270299e+00 -4.8204470e-01
  3.0148568e+00  1.3572037e+00 -1.4558589e+00  2.5059795e-02
  1.2647073e+00 -3.0855205e+00  1.5200443e+00 -3.2841574e-02
  7.7630776e-01  6.8860334e-01  3.8432975e+00 -1.2118469e+00
 -3.1935351e+00  1.1565547e+00  1.8162262e-01 -2.9027835e-01
  1.6397494e+00  5.2901953e-02 -2.1265829e+00 -3.3723432e-01]
Result for fasttext:
[-0.6361631   0.62779856  1.3213146   0.9079998   2.3932645   1.3627672
 -1.8484497  -1.3626038   0.11744618  2.942417   -0.6264652   1.0650853
 -0.98996186  0.54999447  1.3791728  -0.83108485  0.8637263   0.10267539
  1.2134392   1.7886801   0.8637289   0.6288908   1.8183595  -1.117163
 -0.69149363 -0.5036909  -0.08005434  0.4842983   0.346397   -0.16952164
 -1.4862751  -0.6207821  -0.6737978   0.7475163  -2.4579499  -2.248669
 -1.5824851   0.14525604  0.05684421  0.11168259  1.789096   -0.7581389
 -0.47209436 -1.594165    1.4723188  -0.18920977  0.46342534  0.9080119
 -0.645447    0.11764483 -0.74307626  0.18171385  1.9033517   0.08937106
 -1.7511262   0.43485495  0.99314314  0.46964297 -1.4794544   1.8889741
  0.9616479   1.718148    2.2450998  -0.5867397   0.84659845 -0.86456954
  0.54616296 -1.5595441  -0.93912077 -0.49514198  2.9942365  -0.00455472
  0.87639815 -0.39843082  1.3285798   1.8241441   2.7094789  -0.8381784
  1.9179137  -1.5173602   1.6716202  -1.7165194  -1.550415   -0.9543342
  3.5618758   0.15005668  1.6383522  -0.38377097  0.62665135  0.869812
 -0.55141723  2.1693108   1.430942    0.1470999   1.4739555   1.8327043
  2.4896657  -1.8906456  -0.67493254  1.2716726 ]
##Testing 3
Result for tfidf:
[0. 0. 0. ... 0. 0. 0.]
Result for word2vec:
[ 0.69895744  1.7035804   0.26416656 -1.9733937   2.0747793  -1.728741
 -0.08189844  0.3345483  -0.56823856  0.3971722  -0.56936044  0.36417115
  0.40414402 -1.0295753   0.09591323  1.2250938   0.03655427  1.4405861
  0.66317004  0.43025726 -0.02040155  0.8754927   1.9771714  -1.3997589
  0.9612858  -1.7389172  -3.1401813   0.8935191   0.42119387 -0.69758207
 -1.5504438   0.04810734 -1.4186044  -3.2529957  -0.16704623  1.0886049
 -2.174095    1.1274984   0.09097596  0.3555762  -1.0875266   0.67455053
  0.66063976 -0.218132    0.2606721   1.7466654  -0.20466359  0.3246377
 -1.3238297  -0.59340346  0.33047897 -0.28495374 -1.0321076   1.8621501
  1.9038272   0.02092399 -0.3452814  -0.7387104   0.7708498   0.29719603
 -0.44430235 -0.7239091  -0.56967086 -0.7242254  -2.2229667  -0.14797176
  1.7222528  -0.11899084 -0.47613937  0.8170952  -0.84545153  1.2019769
  0.25642157 -0.15528235 -0.16700314 -2.0369241   1.9957031  -0.757653
  0.17743541 -1.0478177  -0.7055978  -1.1440797  -1.0011085  -0.5742367
  1.610336   -1.3943346   0.21532725 -1.0385683   0.9299243  -2.2836359
  0.2207929  -2.6860151  -1.1570061  -0.53735685  1.2063202  -0.17196049
  2.0707643  -0.1877383   1.2330178  -0.02342723]
Result for fasttext:
[-0.6489557  -0.25290647 -0.08434823 -0.15006442  2.2063725   0.66332406
 -2.2300813  -0.2880821  -1.0230708   2.5726047  -2.4057844   1.0362469
 -1.7515664   0.5038087   1.1834717  -1.0888407  -0.13244109  1.0700059
  1.0473096   1.3342286   0.7708888  -1.3571353   0.49130228 -1.9576011
 -0.73438686 -2.0383554  -1.8787242   1.9164919  -1.8629423  -0.73095495
 -0.6540214  -1.1681898   0.5266402  -0.9848126  -0.7402335  -1.5753915
 -1.8739663   0.9532183  -1.7579603   1.7742863   0.4400874   1.2926852
  0.9675013   0.0159838   1.9316694   0.30409205 -0.7306754  -0.38338572
  2.6900725  -0.5991156   1.1034269   0.4805179   0.7279444  -0.8924669
 -0.34542552 -1.7345234  -0.11183441  1.392388   -0.7358206   0.6613287
 -1.294083    0.3867318   1.8981076  -0.08296779  0.8336608   0.11973418
  1.2389419  -0.47387367 -0.8047763  -1.5671037   1.7233411   2.4629478
  0.2084879  -1.2225091   0.5887275  -1.4766147   1.072224    0.39647585
  3.0369787  -1.2017491   2.065978   -0.89253694 -1.3678023  -0.07931086
  3.3431835  -2.3524678   0.7661552   1.1111164   0.92970115 -0.49112326
  1.1098192   1.9711285   1.1325277  -2.2397923   0.55876315  1.308969
  1.1113003  -1.7563425   0.57209253  0.04291309]
##Testing 4
Result for tfidf:
[0.         0.         0.06894288 ... 0.         0.         0.        ]
Result for word2vec:
[-0.93825954 -0.00961295  0.53314495 -0.6591227   0.43519998 -0.47384772
  1.1025747   0.68551797 -0.2889349   1.2697752  -1.7964897   1.0096194
 -1.8584777   1.1752249  -2.4700086  -0.57174534  0.31336358  1.1568208
  1.9147282   1.9305745  -0.6611268  -0.24247588  2.4354885  -0.05779067
  0.9767606  -0.10083608  2.0393476   0.00897138 -0.64189285  1.8822868
  1.4829233   0.9572122   1.7481154  -0.92224777 -0.95673716 -2.182542
 -2.0136135   0.5040549   3.068723   -0.4868198  -0.6401897   0.79060155
  2.5881817  -0.6938135  -0.4654665  -0.49740532 -1.5735247  -0.72548413
 -1.7619287   0.56981134 -0.9627237   0.5081709  -0.3077781  -0.22965513
  0.47880504 -0.22228912 -1.1768544  -1.2952234  -0.7311484   0.25664043
 -0.4090658  -2.5487175   0.16843325  0.38859722 -0.36795062 -1.0629914
 -1.6308092  -0.6238539  -0.10960454  0.47946724  1.2697546   0.32540458
  0.12201419 -2.7243366   1.2345186  -0.4954973  -0.71923983 -0.9764071
  2.3039606  -1.0696303  -1.5274887  -0.566662    0.46678418 -1.0408866
 -0.49566492  0.32987022  0.10917977 -1.475449   -0.18422763  0.24197859
 -0.7043917  -1.1791917   2.0177584  -0.57909507  0.6122327  -0.31805527
  0.49696854  0.24800262 -0.7432837  -1.420609  ]
Result for fasttext:
[ 2.7371788  -0.7761516   0.43105212 -4.719612    3.895206   -1.6086811
 -1.3693687  -1.2664331  -1.7358569   3.0254529  -6.3919244   3.111768
 -3.8499382  -1.8155634  -0.50089335 -2.27489     0.80681556  0.6150584
  0.19695923  1.8129684   1.2521867   0.72757465  2.9945853   0.9755165
 -0.06805675 -4.4627733   0.8415971   0.51373535 -3.2762356  -1.0155107
 -0.65600055 -1.7388322  -2.608796   -2.3710313  -1.3554868   1.4550648
  1.9394338   0.05512938  1.8628252   0.14325391  1.0320551  -1.3995707
 -4.2130527   0.03983252  2.0111005   0.67041385 -0.5102685  -0.98581594
  0.8245984   0.5648612  -0.48498568  0.8579308   0.2636111  -0.13872351
 -1.4525892  -0.6131347   0.799131    1.9769952   1.3249596   0.72032946
 -3.7985148   0.6801938   2.217403    1.4105198   0.4548169  -1.0783273
  0.941724    0.3622     -0.88892275 -4.5744925   2.8654838   2.1814687
  1.4388918   1.8457215  -0.38617808 -3.9152749  -1.7515956   1.4299259
  3.4198575  -2.6485057   1.3213524   4.342451    2.3715854  -0.16779746
  2.8487194  -0.9219263   1.3901459  -1.1826473  -0.55259466  2.402348
  2.2155154   3.1694105   2.2908     -1.8347274  -4.6078253  -1.1465931
 -0.2074201   1.2289896   4.104323   -0.22790702]
##Testing 5
Result for tfidf:
[0.         0.         0.02895184 ... 0.         0.         0.        ]
Result for word2vec:
[ 1.6194572  -0.03492118  3.3439617  -0.20580487  1.4787526   1.6370938
  0.33778408 -1.9926445  -1.2435061  -1.3616204  -1.9210085   1.3226957
  0.8271677   1.3583868  -0.38910404  0.32567593  0.55514455  3.6517181
 -0.61669534  0.46639177 -2.7662597   1.3838487   1.0296245  -1.5944326
  1.6575867   0.72526723 -1.8140944  -0.28833047 -2.0930364   0.36338833
 -2.7823248   1.1556163   2.605529    0.86584896 -3.3329065  -0.58157593
 -1.8147562  -0.7480684   0.96098864 -0.0052429  -0.5687052   0.9814332
  1.5453783   1.1093374   3.2404287   1.1250422  -1.8857259  -1.6521062
  1.6133857   3.334385   -0.1945936   0.3904088  -2.3536077   1.0564667
  0.02598833 -2.4438417  -1.2946568  -0.36335495 -0.39820755 -0.87656146
  3.0555623  -0.18602413 -1.004952    0.27900535 -1.1044401   1.031716
  0.00906927 -0.15624318 -0.93282795  1.2871661  -2.301975   -1.9578388
  1.1402628   0.60911363  0.99618125  0.9636864  -1.5455405  -0.33273232
  0.9649582   0.5223821  -2.4302378  -0.9470154  -2.6636178   0.10083264
 -1.8360826  -0.05272459  1.2484702   1.0907835  -2.590439   -3.0026903
 -1.0336273   2.0983727  -1.6753342   0.6041936  -1.2642086   0.18861918
 -2.403913   -1.1022836  -0.503316    4.5843    ]
Result for fasttext:
[ 6.5786165e-01  1.5526073e+00 -1.1905812e+00 -1.6403775e+00
 -6.1880589e-02 -1.0354117e+00 -1.9926165e+00  2.1048214e+00
  2.6047053e+00  3.0945640e+00 -3.4027216e+00 -3.2380608e-01
 -3.7407091e+00 -2.4914484e+00  5.8789295e-01 -2.5035377e+00
  1.7687613e-01 -8.1358200e-01  2.1860625e-01 -1.2122063e-01
  1.4743336e+00 -1.8990232e+00  2.4459748e+00 -3.4047639e+00
  9.1642934e-01 -2.9752341e-01 -2.2008052e+00  5.2997074e+00
 -6.6252095e-01 -2.6092834e+00 -1.8174934e+00  2.0490589e+00
 -6.7212486e-01 -2.2427433e+00 -4.4480276e-01 -2.2435248e+00
 -1.9961236e+00  1.1293635e+00  8.3127058e-01 -2.4154239e+00
 -2.6391059e-01 -3.4367881e+00  1.1983750e+00  8.2866096e-01
  2.8669493e+00  5.0199616e-01 -1.2459706e+00 -1.0535737e+00
  3.2480910e+00  3.2374945e+00  3.3033943e-01  4.0790701e-01
  1.5413636e+00  9.5885158e-01  1.6756953e+00  3.8584123e+00
 -3.9909971e-01  1.0745918e+00 -7.9104805e-01  2.5062253e+00
  6.8137914e-01  3.6574450e+00  1.0949779e+00  2.6086278e+00
 -7.7932972e-01 -9.0031952e-02 -3.2800062e+00  1.6859978e+00
 -1.7034217e+00 -2.0363882e+00  1.0862254e+00  1.3389182e+00
 -7.1506023e-02 -5.0557494e-01  3.3975129e+00  3.9278790e-02
  6.4525056e+00  9.1399229e-01  1.0089362e+00 -1.3336537e+00
  1.3535805e+00  2.0644169e-01 -2.3464112e+00  1.0617567e+00
  3.9366917e-03 -2.0838249e+00 -3.3957849e+00  4.3812332e+00
  1.1261879e+00  1.6104217e+00 -2.1970444e+00  1.8461636e+00
 -9.3395233e-01  2.2673984e-01 -2.0429640e+00 -1.0231953e+00
 -5.1478130e-01  4.1655305e-01 -1.1071616e+00  3.7170107e+00]
(ai4my) rnd@gpu:~/demo/ai4my$
```

similar word တွေကို ဆွဲထုတ်တာကို စမ်းကြည့်ဖို့အတွက် run_test_sim.sh လို့ နာမည်ပေးထားတဲ့ shell script ကို အောက်ပါအတိုင်း ရေးခဲ့ ...  

```bash
#!/bin/bash

echo "##Testing 1";
echo "Result for tfidf:";
python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_tfidf.npz -j ./corpus/segmentation-data-updated2_tfidf_features.json -s -n 10

echo "Result for word2vec:";
python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_word2vec.model -s -n 10

echo "Result for fasttext:";
python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 10

echo "##Testing 2"
echo "Result for tfidf:";
python test_embedding.py -i "ရန်ကုန်"  -m ./corpus/segmentation-data-updated2_tfidf.npz -j ./corpus/segmentation-data-updated2_tfidf_features.json -s -n 10
echo "Result for word2vec:";
python test_embedding.py -i "ရန်ကုန်"  -m ./corpus/segmentation-data-updated2_word2vec.model  -s -n 10
echo "Result for fasttext:";
python test_embedding.py -i "ရန်ကုန်"  -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 10

echo "##Testing 3";
echo "Result for tfidf:";
python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_tfidf.npz -j ./corpus/segmentation-data-updated2_tfidf_features.json -s -n 10
echo "Result for word2vec:";
python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_word2vec.model  -s -n 10
echo "Result for fasttext:";
python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 10

echo "##Testing 4";
echo "Result for tfidf:";
python test_embedding.py -i "ကို"  -m ./corpus/segmentation-data-updated2_tfidf.npz -s -j ./corpus/segmentation-data-updated2_tfidf_features.json -n 10
echo "Result for word2vec:";
python test_embedding.py -i "ကို"  -m ./corpus/segmentation-data-updated2_word2vec.model -s -n 10
echo "Result for fasttext:";
python test_embedding.py -i "ကို"  -m ./corpus/segmentation-data-updated2_fasttext.model -s -n 10

echo "##Testing 5";
echo "Result for tfidf:";
python test_embedding.py -i "ပြော"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json  -s -n 10
echo "Result for word2vec:";
python test_embedding.py -i "ပြော"  -m ./corpus/segmentation-data-updated2_word2vec.model  -s -n 10
echo "Result for fasttext:";
python test_embedding.py -i "ပြော"  -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 10
```

run လုပ်ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
(ai4my) rnd@gpu:~/demo/ai4my$ ./run_test_sim.sh
##Testing 1
Result for tfidf:
Top 10 similar words to "မြန်မာ" are: [('မြန်မာ', 1.0000000000000013), ('ပြည်', 0.273471589607703), ('နိုင်ငံ', 0.27005681708361867), ('တွေ', 0.11708429926640464), ('ကွ', 0.10677336013589758), ('ပါ', 0.10574834803263558), ('ဟေ့', 0.10505454552388548), ('အသင်း', 0.10478332258036356), ('ထိုင်း', 0.1042064933659561), ('လူမျိုး', 0.10034017556447775)]
Result for word2vec:
Top 10 similar words to "မြန်မာ" are: [('ဂျပန်', 0.6804201006889343), ('ကပိလဝတ်', 0.6760845184326172), ('ထိုင်း', 0.6742671728134155), ('တရုတ်', 0.6723996996879578), ('ဗမာ', 0.6601355671882629), ('ရုရှား', 0.6231737732887268), ('အိန္ဒိယ', 0.6192973852157593), ('စင်ကာပူ', 0.6131458282470703), ('အိမ်နီးချင်း', 0.6096110343933105), ('ဗီယက်နမ်', 0.5903227925300598)]
Result for fasttext:
Top 10 similar words to "မြန်မာ" are: [('၁မြန်မာ', 0.9791991710662842), ('/မြန်မာ', 0.9791245460510254), ('မြန်မာမ', 0.9785462021827698), ('မြန်မာ.', 0.97700434923172), ('မြန်မာ၊', 0.9763777256011963), ('ချီမြန်မာ', 0.9577509164810181), ('ပန်မြန်မာ', 0.955920934677124), ('ဆိုမြန်မာ', 0.938961923122406), ('....မြန်မာ', 0.9376091957092285), ('မြန်မာစာ', 0.9261715412139893)]
##Testing 2
Result for tfidf:
Top 10 similar words to "ရန်ကုန်" are: [('ရန်ကုန်', 1.0), ('မြို့', 0.1523952699860383), ('မြို့နယ်၊', 0.1237027032745848), ('မတ်', 0.11380429482328343), ('တက္ကသိုလ်', 0.10628590200560405), ('မြို့တော်', 0.08969922993133339), ('လမ်း၊', 0.0870804456227539), ('ဒေသ', 0.07810196111871584), ('ကျောက်တံတား', 0.07736974960827972), ('မန္တလေး', 0.07302696082234376)]
Result for word2vec:
Top 10 similar words to "ရန်ကုန်" are: [('မန္တလေး', 0.8848780989646912), ('ပဲခူး', 0.8507481813430786), ('မကွေး', 0.839241087436676), ('မော်လမြိုင်', 0.8092986345291138), ('လားရှိုး', 0.7910878658294678), ('ပုသိမ်', 0.7684634327888489), ('ဘားအံ', 0.7606132626533508), ('မုံရွာ', 0.7584335803985596), ('မြစ်ကြီးနား', 0.7455849647521973), ('ပြင်ဦးလွင်', 0.7449188232421875)]
Result for fasttext:
Top 10 similar words to "ရန်ကုန်" are: [('(ရန်ကုန်', 0.9789490103721619), ('ရန်ကုန်\u200b', 0.9732760190963745), ('ရန်ကုန်၊', 0.9615545272827148), ('ရန်ကုန်သစ်', 0.9603621363639832), ('ရန်ကုန်သူ', 0.9397627115249634), ('ရန်ကုန်သား', 0.920741856098175), ('ရန်ကုန်သူကြီး', 0.9043094515800476), ('နိဗ္ဗာန်ကုန်', 0.9024113416671753), ('ဆန်ကုန်', 0.8951334953308105), ('ကုန်ကုန်', 0.881989061832428)]
##Testing 3
Result for tfidf:
Top 10 similar words to "ကျောင်းသား" are: [('ကျောင်းသား', 1.000000000000001), ('ကျောင်းသူ', 0.2716536698781178), ('သမဂ္ဂ', 0.08297832320870044), ('ငညှောင့်', 0.08245099511953359), ('တက္ကသိုလ်', 0.0771137405996299), ('ဂီတစာဆို', 0.07279020382802218), ('ဆေးကျောင်းသား', 0.06600522742497493), ('တွေ', 0.0652168748380101), ('သစ်ဆုံ', 0.06240310265969447), ('အဆိုကျော်', 0.06091473920127301)]
Result for word2vec:
Top 10 similar words to "ကျောင်းသား" are: [('ကျောင်းသူ', 0.7797659635543823), ('လူငယ်', 0.7149488925933838), ('သင်တန်းသား', 0.6295153498649597), ('မူလတန်း', 0.6149675846099854), ('ဆရာ၊', 0.6093628406524658), ('ကျောင်းအုပ်ကြီး၊', 0.5891454219818115), ('ကလေးငယ်', 0.5886870622634888), ('ကျောင်းဆရာ', 0.5840626955032349), ('သူနာပြု', 0.5738692283630371), ('ဆရာကြီး', 0.5653407573699951)]
Result for fasttext:
Top 10 similar words to "ကျောင်းသား" are: [('ကျွဲကျောင်းသား', 0.9848452210426331), ('ကျောင်းသား၊', 0.9800302386283875), ('နွားကျောင်းသား', 0.9744942784309387), ('ကျောင်းသူ', 0.9632477760314941), ('ကျောင်းသားကြီး', 0.9572359919548035), ('ကျောင်သား', 0.9550759792327881), ('ဘုန်းကြီးကျောင်းသား', 0.9491896033287048), ('ကျောင်းသားလေး', 0.9451152682304382), ('မိကျောင်းသမား', 0.9421031475067139), ('ကျောင်းဆရာ', 0.936782717704773)]
##Testing 4
Result for tfidf:
Top 10 similar words to "ကို" are: [('ကို', 1.0000000000000138), ('က', 0.33999240503684897), ('သည်', 0.2992399082964584), ('ပါ', 0.2922393698998403), ('ပြီး', 0.28554895401597474), ('တယ်', 0.2831978516305748), ('တဲ့', 0.2731189280981615), ('နေ', 0.27078379931580127), ('ရ', 0.26972899499548336), ('တွေ', 0.2665982699692581)]
Result for word2vec:
Top 10 similar words to "ကို" are: [('အား', 0.5367994904518127), ('အပေါ်', 0.47894394397735596), ('ပတ်သက်', 0.4326164722442627), ('ဖျက်ဆီး', 0.41861504316329956), ('မဲဆွယ်', 0.4175712764263153), ('ဖြုတ်', 0.40778300166130066), ('ဖျက်', 0.4066329002380371), ('ဖော်', 0.400238960981369), ('အတွက်', 0.3915502727031708), ('ဖယ်ရှား', 0.39133211970329285)]
Result for fasttext:
Top 10 similar words to "ကို" are: [('\ufeffကို', 0.8085247874259949), ('\u200bကို', 0.8061599135398865), ('ယာမကို', 0.7904666066169739), ('သကို', 0.7818582057952881), ('ကို့ကို', 0.754964292049408), ('ညီကို', 0.7171929478645325), ('တီကို', 0.7170444130897522), ('ကိုတင်ကို', 0.7116729021072388), ('ခေမီကို', 0.7102035284042358), ('ဂျက်ကို', 0.6989907026290894)]
##Testing 5
Result for tfidf:
Top 10 similar words to "ပြော" are: [('ပြော', 1.0000000000000029), ('က', 0.22515994414157484), ('တာ', 0.2223203826862618), ('မ', 0.21481735936973112), ('လို့', 0.2029837264744172), ('စကား', 0.20049350418865794), ('ပြ', 0.17811611175581188), ('ကို', 0.17805364905605758), ('ပါ', 0.17755000959037165), ('တယ်', 0.17522935191807393)]
Result for word2vec:
Top 10 similar words to "ပြော" are: [('ရှင်း', 0.7355074882507324), ('မေး', 0.6970934271812439), ('ယုံ', 0.6724133491516113), ('ငြင်း', 0.6718965768814087), ('ကြွား', 0.5936403870582581), ('တွေး', 0.5816888213157654), ('ဖြေ', 0.580407440662384), ('လျှောက်ပြော', 0.5596990585327148), ('မှား', 0.5576841235160828), ('စိတ်ဆိုး', 0.5537082552909851)]
Result for fasttext:
Top 10 similar words to "ပြော" are: [('\u200cပြော', 0.9523098468780518), ('\ufeffပြော', 0.9508911371231079), ('\ufeff\ufeffပြော', 0.9496182203292847), ('\u200bပြော', 0.9485007524490356), ('ဝပြော', 0.9479262828826904), ('ဒဲ့ပြော', 0.9470230340957642), ('ပြောဟော', 0.9353154301643372), ('ထူပြော', 0.9330112934112549), ('ပြော၊', 0.9272229075431824), ('ပြော)', 0.9271009564399719)]
(ai4my) rnd@gpu:~/demo/ai4my$
```

အထက်ပါ ရလဒ်တွေကို ကြည့်ရင် စိတ်ဝင်စားဖို့ ကောင်းတယ် မဟုတ်လား ...  
ဒီတစ်ခါတော့ ရှာဖွေကြည့်ချင်တဲ့ စာလုံးတွေကို ဖိုင်အနေနဲ့ ပြင်ထားပြီး သုံးတဲ့ ပုံစံကို စမ်းပြပါမယ်။ နောက်ပိုင်း run ချင်တဲ့အခါမှာ အလွယ်တကူ run လို့ ရဖို့အတွက် ပြင်ဆင်ခဲ့တာပါ။ shell script ထဲကနေ ခေါ် run မယ်။  

run_test_sim_file.sh ဆိုတဲ့ နာမည်ပေးခဲ့တယ်။  

```bash
#!/bin/bash

# -f for input filename
echo "tfidf:";
python ./test_embedding.py -m ./corpus/segmentation-data-updated2_tfidf.npz -j ./corpus/segmentation-data-updated2_tfidf_features.json  -s -n 5 -f ./my_text.txt

echo "word2vec:";
python ./test_embedding.py -m ./corpus/segmentation-data-updated2_word2vec.model  -s -n 5 -f ./my_text.txt

echo "fasttext";
python ./test_embedding.py -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 5 -f ./my_text.txt
```

running output က အောက်ပါအတိုင်းပါ။  

```
(ai4my) rnd@gpu:~/demo/ai4my$ ./run_test_sim_file.sh
tfidf:
Top 5 similar words to "သုတေသန" are: [('သုတေသန', 0.9999999999999998), ('ရှေးဟောင်း', 0.13356810694361262), ('ဆယ်လူလာ', 0.11534717147940245), ('တီထွင်ဆန်းသစ်', 0.10113346161499598), ('ဦးစီးဌာန', 0.09652904434517666)]
Top 5 similar words to "ဂျပန်" are: [('ဂျပန်', 1.0000000000000013), ('၁၃၇၁.၉', 0.09659662900943045), ('နေမျိုးနွယ်', 0.08684242913313667), ('ယန်း', 0.08571298198764987), ('တိုကျို', 0.07721793269146873)]
Top 5 similar words to "ပေါင်မုန့်" are: [('ပေါင်မုန့်', 0.9999999999999998), ('အုန်းနို့ဆမ်း', 0.5012479433931549), ('ချိုဆိမ့်လေး', 0.2909015087266119), ('confectionery', 0.2538503050173973), ('ငှက်ပျောသီး၊', 0.2115428776766402)]
Top 5 similar words to "ရခိုင်မုန့်တီ" are: [('ရခိုင်မုန့်တီ', 1.0), ('ကပျာကသီ', 0.39525850202519897), ('အသုပ်', 0.2599878295779212), ('မုန့်ဟင်းခါး', 0.12405845391010076), ('၃၀၀', 0.10692748456847033)]
"ဘိန်းမုန့်" not found in TF-IDF vocabulary.
Top 5 similar words to "ဘိန်းမုန့်" are: []
"ငြိမ်းချမ်းရေး" not found in TF-IDF vocabulary.
Top 5 similar words to "ငြိမ်းချမ်းရေး" are: []
word2vec:
Top 5 similar words to "သုတေသန" are: [('ရူပဗေဒ', 0.7693567872047424), ('ဘူမိဗေဒ', 0.7691071033477783), ('ပညာရပ်', 0.76316899061203), ('ဗေဒ', 0.7556723952293396), ('မှုခင်း', 0.7532738447189331)]
Top 5 similar words to "ဂျပန်" are: [('အိန္ဒိယ', 0.8293510675430298), ('တရုတ်', 0.7748363614082336), ('ရုရှား', 0.7620962858200073), ('တောင်ကိုရီးယား', 0.7605290412902832), ('စင်ကာပူ', 0.7484836578369141)]
Top 5 similar words to "ပေါင်မုန့်" are: [('ဟင်းသီးဟင်းရွက်', 0.8090328574180603), ('ထောပတ်', 0.7979607582092285), ('လက်ပြတ်', 0.7949730157852173), ('ပေါင်မုန့်', 0.7943387031555176), ('ခရမ်းချဉ်သီး', 0.7898463010787964)]
"ရခိုင်မုန့်တီ" not found in model vocabulary.
Top 5 similar words to "ရခိုင်မုန့်တီ" are: []
"ဘိန်းမုန့်" not found in model vocabulary.
Top 5 similar words to "ဘိန်းမုန့်" are: []
"ငြိမ်းချမ်းရေး" not found in model vocabulary.
Top 5 similar words to "ငြိမ်းချမ်းရေး" are: []
fasttext
Top 5 similar words to "သုတေသန" are: [('သုတေသန=', 0.9908668398857117), ('သုတေသီ', 0.9241949915885925), ('ရှေးဟောင်းသုတေသန', 0.8289024829864502), ('နည်းပညာရှင်', 0.81951904296875), ('ရေးဆရာ', 0.8066650629043579)]
Top 5 similar words to "ဂျပန်" are: [('ဂျပန်မ', 0.9119203090667725), ('ဂျာမန်', 0.9108649492263794), ('အင်္ဂလန်', 0.8909609317779541), ('ဂျပိန်', 0.8831645846366882), ('အီသီယိုပီးယား', 0.8786143064498901)]
Top 5 similar words to "ပေါင်မုန့်" are: [('ပေါင်မုန့်', 0.954434335231781), ('ပေါင်ဒါမှုန့်', 0.9338068962097168), ('ပေါင်မုန့်မီးကင်', 0.9288087487220764), ('ပေါင်ဒါနံ့', 0.9285176396369934), ('ပေါင်', 0.9229799509048462)]
Top 5 similar words to "ရခိုင်မုန့်တီ" are: [('ရခိုင်မ', 0.9652368426322937), ('ရခိုင်ချီ', 0.9612852931022644), ('ရခိုင်', 0.9575817584991455), ('ရခိုင်\u200c', 0.9538776278495789), ('ရခိုင့်', 0.9530232548713684)]
Top 5 similar words to "ဘိန်းမုန့်" are: [('ဘိန်းမည်း', 0.9285106658935547), ('ပလိန်းကိတ်', 0.9197248816490173), ('စိန့်ပီတာစဘတ်', 0.9160558581352234), ('ငှက်ပိန်း', 0.9116246700286865), ('ဘိန်းပင်', 0.9104881882667542)]
Top 5 similar words to "ငြိမ်းချမ်းရေး" are: [('ငြိမ်းငြိမ်းချမ်းချမ်း', 0.9733818173408508), ('ငြိမ်းချမ်း\u200c', 0.9731578230857849), ('ငြိမ်းချမ်း', 0.9719025492668152), ('ခင်ငြိမ်းချမ်း', 0.9678707718849182), ('ငြိမ်းချမ်းအောင်', 0.9597541689872742)]
(ai4my) rnd@gpu:~/demo/ai4my$
```

တစ်ခုရှိတာက embedding မော်ဒယ်တွေကို ဆောက်ထားတဲ့ corpus က စာကြောင်းရေ နှစ်သိန်းကျော်ပဲ ရှိပါတယ်။ တခြား ဘာသာစကားတွေ ဖြစ်တဲ့ အင်္ဂလိပ်စာတို့ ဂျပန်စာတို့နဲ့ ယှဉ်လိုက်ရင် ဗမာစာအတွက် က အများကြီး အလုပ်လုပ်ကြရပါလိမ့်ဦးမယ်။ တကယ်လို့သာ စာကြောင်းရေ အရေအတွက် နှစ်သန်းလောက်နဲ့သာ word embedding မော်ဒယ်တွေကို ဆောက်နိုင်ခဲ့ရင် လက်ရှိတဲ့ အများကြီး စိတ်ဝင်စားစရာကောင်းတဲ့ ရလဒ်တွေကို မြင့်တွေ့ကြရပါလိမ့်မယ်။ အဓိပ္ပါယ် ဆင်တူတဲ့ ဗမာစာလုံးတွေကိုလည်း လက်ရှိထက် အများကြီး မှန်မှန်ကန်ကန် ဆွဲထုတ်ပေးနိုင်ပါလိမ့်မယ်။  

## 82. [convert_to_conllu.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/convert_to_conllu.py)    

CONLLU format က NLP သမားတွေအနေနဲ့ အားလုံး သိပြီးသားဖြစ်ပြီး၊ တော်တော်များများသော modeling လုပ်ပေးနိုင်တဲ့ machine learning tool တွေ၊ framework တွေက အဲဒီ format ကို input file အနေနဲ့ လက်ခံကြတာများပါတယ်။ ဒီ python script က ငါတို့ရဲ့ မြန်မာစာ POS tag dataset ဖြစ်တဲ့ myPOS tagged data format (ပုံမှန်အတိုင်း ဘယ်ကနေ ညာဘက် ရေးသွားပြီး slash ခြားထားပြီး POS tag တွဲထားတဲ့ ပုံစံ) ကနေ CONLLU format (ကော်လံအလိုက် ရေးထားပြီးတော့ mophological information, dependency information တွေပါ ပါတဲ့ 10 column format) ကို ပြောင်းဖို့ ရေးခဲ့တယ်။  

test run အတွက် myPOS corpus ထဲကနေ စာကြောင်း ၅ကြောင်းကို အောက်ပါအတိုင်း ဆွဲထုတ်ထားပါတယ်။ pipe တွေလည်း ဖြုတ်ထားပါတယ်။  

```
၁၉၆၂/num ခုနှစ်/n ခန့်မှန်း/v သန်းခေါင်စာရင်း/n အရ/ppm လူဦးရေ/n ၁၁၅၉၃၁/num ယောက်/part ရှိ/v သည်/ppm ။/punc
လူ/n တိုင်း/part တွင်/ppm သင့်မြတ်/v လျော်ကန်/v စွာ/part ကန့်သတ်/v ထား/part သည့်/part အလုပ်/n လုပ်/v ချိန်/n အပြင်/conj ၊/punc လစာ/n နှင့်တကွ/conj အခါ/n ကာလ/n အားလျော်စွာ/ppm သတ်မှတ်/v ထား/part သည့်/part အလုပ်/n အားလပ်ရက်/n များ/part ပါဝင်/v သည့်/part အနားယူခွင့်/n နှင့်/conj အားလပ်ခွင့်/n ခံစားပိုင်ခွင့်/n ရှိ/v သည်/ppm ။/punc
ဤ/adj နည်း/n ကို/ppm စစ်ယူ/v သော/part နည်း/n ဟု/part ခေါ်/v သည်/ppm ။/punc
စာပြန်ပွဲ/n ဆို/v တာ/part က/ppm အာဂုံဆောင်/v အလွတ်ကျက်/v ထား/part တဲ့/part ပိဋကတ်သုံးပုံ/n စာပေ/n တွေ/part ကို/ppm စာစစ်/v သံဃာတော်ကြီး/n တွေ/part ရဲ့/ppm ရှေ့/n မှာ/ppm အလွတ်/adv ပြန်/v ပြီး/part ရွတ်ပြ/v ရ/part တာ/part ပေါ့/part ။/punc
ဒီ/pron မှာ/ppm ကျွန်တော့်/pron သက်သေခံကတ်/n ပါ/part ။/punc
```

running လုပ်တဲ့ ပုံစံက အောက်ပါအတိုင်းပါ။  

```bash
python convert_to_conllu.py --input .\corpus\mypos_5lines.txt --output mypos_5lines.conllu
```

output file မှာက လိုချင်တဲ့ CONLLU format အဖြစ် ပြောင်းပေးသွားတာကို မြင်ကြရပါလိမ့်မယ်။  

```
1	၁၉၆၂	_	num	_	_	_	_	_	_
2	ခုနှစ်	_	n	_	_	_	_	_	_
3	ခန့်မှန်း	_	v	_	_	_	_	_	_
4	သန်းခေါင်စာရင်း	_	n	_	_	_	_	_	_
5	အရ	_	ppm	_	_	_	_	_	_
6	လူဦးရေ	_	n	_	_	_	_	_	_
7	၁၁၅၉၃၁	_	num	_	_	_	_	_	_
8	ယောက်	_	part	_	_	_	_	_	_
9	ရှိ	_	v	_	_	_	_	_	_
10	သည်	_	ppm	_	_	_	_	_	_
11	။	_	punc	_	_	_	_	_	_

1	လူ	_	n	_	_	_	_	_	_
2	တိုင်း	_	part	_	_	_	_	_	_
3	တွင်	_	ppm	_	_	_	_	_	_
4	သင့်မြတ်	_	v	_	_	_	_	_	_
5	လျော်ကန်	_	v	_	_	_	_	_	_
6	စွာ	_	part	_	_	_	_	_	_
7	ကန့်သတ်	_	v	_	_	_	_	_	_
8	ထား	_	part	_	_	_	_	_	_
9	သည့်	_	part	_	_	_	_	_	_
10	အလုပ်	_	n	_	_	_	_	_	_
11	လုပ်	_	v	_	_	_	_	_	_
12	ချိန်	_	n	_	_	_	_	_	_
13	အပြင်	_	conj	_	_	_	_	_	_
14	၊	_	punc	_	_	_	_	_	_
15	လစာ	_	n	_	_	_	_	_	_
16	နှင့်တကွ	_	conj	_	_	_	_	_	_
17	အခါ	_	n	_	_	_	_	_	_
18	ကာလ	_	n	_	_	_	_	_	_
19	အားလျော်စွာ	_	ppm	_	_	_	_	_	_
20	သတ်မှတ်	_	v	_	_	_	_	_	_
21	ထား	_	part	_	_	_	_	_	_
22	သည့်	_	part	_	_	_	_	_	_
23	အလုပ်	_	n	_	_	_	_	_	_
24	အားလပ်ရက်	_	n	_	_	_	_	_	_
25	များ	_	part	_	_	_	_	_	_
26	ပါဝင်	_	v	_	_	_	_	_	_
27	သည့်	_	part	_	_	_	_	_	_
28	အနားယူခွင့်	_	n	_	_	_	_	_	_
29	နှင့်	_	conj	_	_	_	_	_	_
30	အားလပ်ခွင့်	_	n	_	_	_	_	_	_
31	ခံစားပိုင်ခွင့်	_	n	_	_	_	_	_	_
32	ရှိ	_	v	_	_	_	_	_	_
33	သည်	_	ppm	_	_	_	_	_	_
34	။	_	punc	_	_	_	_	_	_

1	ဤ	_	adj	_	_	_	_	_	_
2	နည်း	_	n	_	_	_	_	_	_
3	ကို	_	ppm	_	_	_	_	_	_
4	စစ်ယူ	_	v	_	_	_	_	_	_
5	သော	_	part	_	_	_	_	_	_
6	နည်း	_	n	_	_	_	_	_	_
7	ဟု	_	part	_	_	_	_	_	_
8	ခေါ်	_	v	_	_	_	_	_	_
9	သည်	_	ppm	_	_	_	_	_	_
10	။	_	punc	_	_	_	_	_	_

1	စာပြန်ပွဲ	_	n	_	_	_	_	_	_
2	ဆို	_	v	_	_	_	_	_	_
3	တာ	_	part	_	_	_	_	_	_
4	က	_	ppm	_	_	_	_	_	_
5	အာဂုံဆောင်	_	v	_	_	_	_	_	_
6	အလွတ်ကျက်	_	v	_	_	_	_	_	_
7	ထား	_	part	_	_	_	_	_	_
8	တဲ့	_	part	_	_	_	_	_	_
9	ပိဋကတ်သုံးပုံ	_	n	_	_	_	_	_	_
10	စာပေ	_	n	_	_	_	_	_	_
11	တွေ	_	part	_	_	_	_	_	_
12	ကို	_	ppm	_	_	_	_	_	_
13	စာစစ်	_	v	_	_	_	_	_	_
14	သံဃာတော်ကြီး	_	n	_	_	_	_	_	_
15	တွေ	_	part	_	_	_	_	_	_
16	ရဲ့	_	ppm	_	_	_	_	_	_
17	ရှေ့	_	n	_	_	_	_	_	_
18	မှာ	_	ppm	_	_	_	_	_	_
19	အလွတ်	_	adv	_	_	_	_	_	_
20	ပြန်	_	v	_	_	_	_	_	_
21	ပြီး	_	part	_	_	_	_	_	_
22	ရွတ်ပြ	_	v	_	_	_	_	_	_
23	ရ	_	part	_	_	_	_	_	_
24	တာ	_	part	_	_	_	_	_	_
25	ပေါ့	_	part	_	_	_	_	_	_
26	။	_	punc	_	_	_	_	_	_

1	ဒီ	_	pron	_	_	_	_	_	_
2	မှာ	_	ppm	_	_	_	_	_	_
3	ကျွန်တော့်	_	pron	_	_	_	_	_	_
4	သက်သေခံကတ်	_	n	_	_	_	_	_	_
5	ပါ	_	part	_	_	_	_	_	_
6	။	_	punc	_	_	_	_	_	_

```

## 83. [convert_to_spacyNER_json.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/convert_to_spacyNER_json.py)

ပထမဆုံး အနေနဲ့ myPOS Corpus format ကနေ Spacy NER format ကို ပြောင်းပြမယ်။  

```
python convert_to_spacyNER_json.py --input .\corpus\mypos_5lines.txt --output mypos_5lines.json
```

json format အဖြစ် ပြောင်းပေးသွားတာကို တွေ့ရပါလိမ့်မယ်။  
```
[["၁၉၆၂ ခုနှစ် ခန့်မှန်း သန်းခေါင်စာရင်း အရ လူဦးရေ ၁၁၅၉၃၁ ယောက် ရှိ သည် ။", {"entities": [[0, 4, "num"], [5, 11, "n"], [12, 21, "v"], [22, 37, "n"], [38, 40, "ppm"], [41, 47, "n"], [48, 54, "num"], [55, 60, "part"], [61, 64, "v"], [65, 68, "ppm"], [69, 70, "punc"]]}], ["လူ တိုင်း တွင် သင့်မြတ် လျော်ကန် စွာ ကန့်သတ် ထား သည့် အလုပ် လုပ် ချိန် အပြင် ၊ လစာ နှင့်တကွ အခါ ကာလ အားလျော်စွာ သတ်မှတ် ထား သည့် အလုပ် အားလပ်ရက် များ ပါဝင် သည့် အနားယူခွင့် နှင့် အားလပ်ခွင့် ခံစားပိုင်ခွင့် ရှိ သည် ။", {"entities": [[0, 2, "n"], [3, 9, "part"], [10, 14, "ppm"], [15, 23, "v"], [24, 32, "v"], [33, 36, "part"], [37, 44, "v"], [45, 48, "part"], [49, 53, "part"], [54, 59, "n"], [60, 64, "v"], [65, 70, "n"], [71, 76, "conj"], [77, 78, "punc"], [79, 82, "n"], [83, 91, "conj"], [92, 95, "n"], [96, 99, "n"], [100, 111, "ppm"], [112, 119, "v"], [120, 123, "part"], [124, 128, "part"], [129, 134, "n"], [135, 144, "n"], [145, 149, "part"], [150, 155, "v"], [156, 160, "part"], [161, 172, "n"], [173, 178, "conj"], [179, 190, "n"], [191, 206, "n"], [207, 210, "v"], [211, 214, "ppm"], [215, 216, "punc"]]}], ["ဤ နည်း ကို စစ်ယူ သော နည်း ဟု ခေါ် သည် ။", {"entities": [[0, 1, "adj"], [2, 6, "n"], [7, 10, "ppm"], [11, 16, "v"], [17, 20, "part"], [21, 25, "n"], [26, 28, "part"], [29, 33, "v"], [34, 37, "ppm"], [38, 39, "punc"]]}], ["စာပြန်ပွဲ ဆို တာ က အာဂုံဆောင် အလွတ်ကျက် ထား တဲ့ ပိဋကတ်သုံးပုံ စာပေ တွေ ကို စာစစ် သံဃာတော်ကြီး တွေ ရဲ့ ရှေ့ မှာ အလွတ် ပြန် ပြီး ရွတ်ပြ ရ တာ ပေါ့ ။", {"entities": [[0, 9, "n"], [10, 13, "v"], [14, 16, "part"], [17, 18, "ppm"], [19, 29, "v"], [30, 39, "v"], [40, 43, "part"], [44, 47, "part"], [48, 61, "n"], [62, 66, "n"], [67, 70, "part"], [71, 74, "ppm"], [75, 80, "v"], [81, 93, "n"], [94, 97, "part"], [98, 101, "ppm"], [102, 106, "n"], [107, 110, "ppm"], [111, 116, "adv"], [117, 121, "v"], [122, 126, "part"], [127, 133, "v"], [134, 135, "part"], [136, 138, "part"], [139, 143, "part"], [144, 145, "punc"]]}], ["ဒီ မှာ ကျွန်တော့် သက်သေခံကတ် ပါ ။", {"entities": [[0, 2, "pron"], [3, 6, "ppm"], [7, 17, "pron"], [18, 28, "n"], [29, 31, "part"], [32, 33, "punc"]]}]]
```

--unicode_repr ဆိုတဲ့ option ကို တွဲလိုက်ရင်တော့ အောက်ပါအတိုင်း output ကို ရလိမ့်မယ်။  

```
[["4161_4169_4166_4162 4097_4143_4116_4158_4101_4154 4097_4116_4154_4151_4121_4158_4116_4154_4152 4126_4116_4154_4152_4097_4145_4139_4100_4154_4101_4140_4123_4100_4154_4152 4129_4123 4124_4144_4134_4152_4123_4145 4161_4161_4165_4169_4163_4161 4122_4145_4140_4096_4154 4123_4158_4141 4126_4106_4154 4171", {"entities": [[0, 4, "num"], [5, 11, "n"], [12, 21, "v"], [22, 37, "n"], [38, 40, "ppm"], [41, 47, "n"], [48, 54, "num"], [55, 60, "part"], [61, 64, "v"], [65, 68, "ppm"], [69, 70, "punc"]]}], ["4124_4144 4112_4141_4143_4100_4154_4152 4112_4157_4100_4154 4126_4100_4154_4151_4121_4156_4112_4154 4124_4155_4145_4140_4154_4096_4116_4154 4101_4157_4140 4096_4116_4154_4151_4126_4112_4154 4113_4140_4152 4126_4106_4154_4151 4129_4124_4143_4117_4154 4124_4143_4117_4154 4097_4155_4141_4116_4154 4129_4117_4156_4100_4154 4170 4124_4101_4140 4116_4158_4100_4154_4151_4112_4096_4157 4129_4097_4139 4096_4140_4124 4129_4140_4152_4124_4155_4145_4140_4154_4101_4157_4140 4126_4112_4154_4121_4158_4112_4154 4113_4140_4152 4126_4106_4154_4151 4129_4124_4143_4117_4154 4129_4140_4152_4124_4117_4154_4123_4096_4154 4121_4155_4140_4152 4117_4139_4125_4100_4154 4126_4106_4154_4151 4129_4116_4140_4152_4122_4144_4097_4157_4100_4154_4151 4116_4158_4100_4154_4151 4129_4140_4152_4124_4117_4154_4097_4157_4100_4154_4151 4097_4150_4101_4140_4152_4117_4141_4143_4100_4154_4097_4157_4100_4154_4151 4123_4158_4141 4126_4106_4154 4171", {"entities": [[0, 2, "n"], [3, 9, "part"], [10, 14, "ppm"], [15, 23, "v"], [24, 32, "v"], [33, 36, "part"], [37, 44, "v"], [45, 48, "part"], [49, 53, "part"], [54, 59, "n"], [60, 64, "v"], [65, 70, "n"], [71, 76, "conj"], [77, 78, "punc"], [79, 82, "n"], [83, 91, "conj"], [92, 95, "n"], [96, 99, "n"], [100, 111, "ppm"], [112, 119, "v"], [120, 123, "part"], [124, 128, "part"], [129, 134, "n"], [135, 144, "n"], [145, 149, "part"], [150, 155, "v"], [156, 160, "part"], [161, 172, "n"], [173, 178, "conj"], [179, 190, "n"], [191, 206, "n"], [207, 210, "v"], [211, 214, "ppm"], [215, 216, "punc"]]}], ["4132 4116_4106_4154_4152 4096_4141_4143 4101_4101_4154_4122_4144 4126_4145_4140 4116_4106_4154_4152 4127_4143 4097_4145_4139_4154 4126_4106_4154 4171", {"entities": [[0, 1, "adj"], [2, 6, "n"], [7, 10, "ppm"], [11, 16, "v"], [17, 20, "part"], [21, 25, "n"], [26, 28, "part"], [29, 33, "v"], [34, 37, "ppm"], [38, 39, "punc"]]}], ["4101_4140_4117_4156_4116_4154_4117_4157_4146 4102_4141_4143 4112_4140 4096 4129_4140_4098_4143_4150_4102_4145_4140_4100_4154 4129_4124_4157_4112_4154_4096_4155_4096_4154 4113_4140_4152 4112_4146_4151 4117_4141_4107_4096_4112_4154_4126_4143_4150_4152_4117_4143_4150 4101_4140_4117_4145 4112_4157_4145 4096_4141_4143 4101_4140_4101_4101_4154 4126_4150_4099_4140_4112_4145_4140_4154_4096_4156_4142_4152 4112_4157_4145 4123_4146_4151 4123_4158_4145_4151 4121_4158_4140 4129_4124_4157_4112_4154 4117_4156_4116_4154 4117_4156_4142_4152 4123_4157_4112_4154_4117_4156 4123 4112_4140 4117_4145_4139_4151 4171", {"entities": [[0, 9, "n"], [10, 13, "v"], [14, 16, "part"], [17, 18, "ppm"], [19, 29, "v"], [30, 39, "v"], [40, 43, "part"], [44, 47, "part"], [48, 61, "n"], [62, 66, "n"], [67, 70, "part"], [71, 74, "ppm"], [75, 80, "v"], [81, 93, "n"], [94, 97, "part"], [98, 101, "ppm"], [102, 106, "n"], [107, 110, "ppm"], [111, 116, "adv"], [117, 121, "v"], [122, 126, "part"], [127, 133, "v"], [134, 135, "part"], [136, 138, "part"], [139, 143, "part"], [144, 145, "punc"]]}], ["4114_4142 4121_4158_4140 4096_4155_4157_4116_4154_4112_4145_4140_4154_4151 4126_4096_4154_4126_4145_4097_4150_4096_4112_4154 4117_4139 4171", {"entities": [[0, 2, "pron"], [3, 6, "ppm"], [7, 17, "pron"], [18, 28, "n"], [29, 31, "part"], [32, 33, "punc"]]}]]
```
## 84. [split_parallel_data.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/split_parallel_data.py)  

ဒီ အလုပ်က NLP preprocessing အလုပ်အနေနဲ့ အကြိမ်ကြိမ်အခါခါလုပ်ရတဲ့ အလုပ်ပါ။ အသုံးဝင်ပါလိမ့်မယ်။ -h သို့မဟုတ် --help ဆိုတဲ့ option နဲ့ running လုပ်ရတဲ့ ပုံစံကို ခေါ်ကြည့်ပါ။   

```
python split_parallel_data.py --help
usage: split_parallel_data.py [-h] -d DELIMITER -s SOURCE_FILENAME -t TARGET_FILENAME input_filename

positional arguments:
  input_filename        Input filename

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter to use when splitting data
  -s SOURCE_FILENAME, --source_filename SOURCE_FILENAME
                        Source output filename
  -t TARGET_FILENAME, --target_filename TARGET_FILENAME
                        Target output filename
```

ဥပမာ အနေနဲ့ စကောကရင်၊ ဗမာစာ parallel data ဖိုင်ထဲကနေ စာကြောင်း ငါးကြောင်းကို ဆွဲထုတ်ပြီး run ပြမယ်။ source ဖိုင်၊ target ဖိုင် အဖြစ် မခွဲခင် parallel ဒေတာက အောက်ပါအတိုင်းပါ။ စကောကရင် စာနဲ့ ဗမာစာ စာကြောင်း ကို TAB ကီးနဲ့ ခြားပေးထားပါတယ်။  

```
တုၤလါလၢာ်လံ, ကဘၣ် ကွၢ်သူကွၢ်စွဲတိၢ်န့ၣ်လီၤ.	လကုန် ရက် ရောက် ပြီ  ငွေ ချွေတာ ရ မယ် 
အသီမ့ၢ်ပှဲၤန့ၣ် မၢလဲကဒီးန့ၣ်ဒံးဧါ.	ရက် စေ့ ရင် ထပ် ပြီး ဆက် ငှား လို့ ရ ပါ သလား 
မ့ၢ်လဲၤဆူပျီဖၠါ န့ၣ်ဘၣ်ဒိးမနုၤသိလ့ၣ်လဲၣ်.	လဟာပြင်ဈေး ကို သွား ရင် ဘယ် ကား စီး ရ မလဲ 
တုၤဆူအဖီခိၣ်တကထၢအခါ.	အပေါ် ထပ် ရောက် သော် 
ကပှ့ၤ မနုၤတၢ်သ့ၣ်နီၣ်တၢ်ပိးတၢ်လီ ဖဲဝ့ၢ်ပကၣ်လဲၣ်.	ပုဂံ မြို့ က အမှတ်တရ ပစ္စည်း ဘာ ဝယ် ရ မလဲ 
```

```bash
python split_parallel_data.py .\small_sgmy_parallel_corpus.txt -d '\t' -s source.sg -t target.my
```

သို့မဟုတ်   

```bash
python split_parallel_data.py .\small_sgmy_parallel_corpus.txt -d "\t" -s source.sg -t target.my
```

source.sg ဖိုင်ကို အောက်ပါအတိုင်း ရလိမ့်မယ်။  

```
တုၤလါလၢာ်လံ, ကဘၣ် ကွၢ်သူကွၢ်စွဲတိၢ်န့ၣ်လီၤ.
အသီမ့ၢ်ပှဲၤန့ၣ် မၢလဲကဒီးန့ၣ်ဒံးဧါ.
မ့ၢ်လဲၤဆူပျီဖၠါ န့ၣ်ဘၣ်ဒိးမနုၤသိလ့ၣ်လဲၣ်.
တုၤဆူအဖီခိၣ်တကထၢအခါ.
ကပှ့ၤ မနုၤတၢ်သ့ၣ်နီၣ်တၢ်ပိးတၢ်လီ ဖဲဝ့ၢ်ပကၣ်လဲၣ်.
```

target.my ဖိုင်က အောက်ပါအတိုင်းပါ။  

```
လကုန် ရက် ရောက် ပြီ  ငွေ ချွေတာ ရ မယ်
ရက် စေ့ ရင် ထပ် ပြီး ဆက် ငှား လို့ ရ ပါ သလား
လဟာပြင်ဈေး ကို သွား ရင် ဘယ် ကား စီး ရ မလဲ
အပေါ် ထပ် ရောက် သော်
ပုဂံ မြို့ က အမှတ်တရ ပစ္စည်း ဘာ ဝယ် ရ မလဲ
```

## 86. [extract_emoji.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/extract_emoji.py)  

ဖိုင်ထဲမှာ ပါနေတဲ့ emoji စာလုံးတွေကို ဆွဲထုတ်ပြီးတော့ list လုပ်ပြလိမ့်မယ်။ ထပ်ခါထပ်ခါ ပါနေတဲ့ emoji တွေကိလည်း တစ်ခါပဲ ပြပေးမှာမို့ unique list ပါ။  
test input ဖိုင်က အောက်ပါအတိုင်းပါ။  

```
RIP the future of 🧑‍⚕️&🚝
ငွေသား ဒေါ်လှ တစ်သိန်းလောက် ထုတ်ပြလ်ုက် ကွီးတင် ။ 😉
ဟိ.. တိုတိုထိုးလိုက်ဦးမယ်😅
Hi! 😅
```

ဥပမာ အနေနဲ့ run ကြည့်ထားတဲ့ output က အေက်ပါအတိုင်းပါ။  

```
(base) C:\Users\801680\.spyder-py3>python extract_emoji.py ./emoji.txt
Emoji Character: 🧑
Unicode Value: 129489
Emoji Name: :person:
Emoji Definition: :person:

Emoji Character: ⚕
Unicode Value: 9877
Emoji Name: :medical_symbol:
Emoji Definition: :medical_symbol:

Emoji Character: 🚝
Unicode Value: 128669
Emoji Name: :monorail:
Emoji Definition: :monorail:

Emoji Character: 😉
Unicode Value: 128521
Emoji Name: :winking_face:
Emoji Definition: :winking_face:

Emoji Character: 😅
Unicode Value: 128517
Emoji Name: :grinning_face_with_sweat:
Emoji Definition: :grinning_face_with_sweat:
```

## 87. [compare_characters.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/compare_characters.py)   

Running example ...  

```
(base) ye@lst-gpu-3090:~/exp/bg-br/data/splitting/segmentation/space_cleaned$ python ./compare_characters
.py ./train.bg ./train.br
Total Bengali characters: 3758690
Total Braille characters: 9614764
Braille has 155.80% more characters than Bengali.
(base) ye@lst-gpu-3090:~/exp/bg-br/data/splitting/segmentation/space_cleaned$ python ./compare_characters.py ./valid.bg ./valid.br
Total Bengali characters: 449140
Total Braille characters: 1143854
Braille has 154.68% more characters than Bengali.
(base) ye@lst-gpu-3090:~/exp/bg-br/data/splitting/segmentation/space_cleaned$ python ./compare_characters.py ./test.bg ./test.br
Total Bengali characters: 445636
Total Braille characters: 1137612
Braille has 155.28% more characters than Bengali.
```

88. [word_length_analysis.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/word_length_analysis.py)

Running example of usage of the program is as follows:  

```
(base) ye@lst-gpu-3090:~/exp/bg-br/data$ python word_length_analysis.py ./final4nmt/vocab/all.bg
Minimum word length: 8
Maximum word length: 537

Sentences with Minimum Word Length:
Line 2032: খ ে ল ো য় া ড় ?

Sentences with Maximum Word Length:
Line 8619: ন ি উ স া উ থ ও য় ে ল স ে র স া ঁ ত া র ু গ ণ প ্ র ত ি ন ি ধ ি ত ্ ব ক র ছ ে র ে প ট ন ে র ম া ই ক ে ল অ ্ য া ন ্ ড া র স ন , জ র ্ জ স হ ল ে র ট ি ম অ ্ য া ন ্ ট া ল ফ ি , প ি ক হ া র ্ স ্ ট ে র ম া ই ক ে ল অ প ্ র ি ন ্ স , স ্ ক া র ব র ো র ব ্ ল ে ক ক ো ক ্ র ে ন , অ ্ য া ন া ব ে র ট ে ই ল র ক ো র ি , গ ি ল ি স ্ ট ন হ া ই ট স ে র ম ্ য া ড ি স ন ই ল ি য় ট , স ্ ক ি ন া র স হ ে ড ে র জ ্ য া ক ু ই ল ি ন ফ ্ র ে ন ি , ব ্ ল ্ য া ক ্ স ল ্ য া ন ্ ড ে র অ ্ য া ম া ন ্ ড া ফ া উ ল া র , ক া র ্ ল ট ন ে র ম ি শ ে ল ক ি ল ড া ফ , প ে ন র ি থ ে র ক া র া ল ি ও , ন র ্ থ ব ্ র ি জ ে র ম ্ য া থ ি উ ল ি ভ া ই , ক ্ য া স ে ল হ ি ল ে র অ ্ য া ন ্ ড ্ র ি উ প ্ য া স ্ ট া র ফ ি ল ্ ড , ন ি উ ট া উ ন ে র ক ্ য া ট র ি ন া প ো র ্ ট া র , ই য় া স ে র অ ্ য া র ন র া ই ন ্ ড , প ি ম ্ ব ল ে র স া র া হ র ো জ , র ি ভ ে স ব ি র শ ন র ু স ো , ব ্ য া ট ি উ ব ে র ট ে ই গ া ন ভ ্ য া ন র ু জ ম ্ য া ল ে ন , গ ্ র ে স প য় ে ন ্ ট ে র র ি গ ্ য া ন উ ই ক ে ন ্ স এ ব ং শ ে ল ট ে ন হ ্ য া ম ে র অ ্ য া ন া ব ে ল উ ই ল ি য় া ম স এ র ন া ম ঘ ো ষ ণ া ক র া হ য় ে ছ ে ।
(base) ye@lst-gpu-3090:~/exp/bg-br/data$
(base) ye@lst-gpu-3090:~/exp/bg-br/data$ python word_length_analysis.py ./final4nmt/vocab/all.br
Minimum word length: 14
Maximum word length: 1316

Sentences with Minimum Word Length:
Line 2030: ⠩ ⠊ ⠟ ⠜ ⠛ ⠞ ⠄ ⡳ ⠭ ⠴ ⠴ ⠒ ⠋ ⠄

Sentences with Maximum Word Length:
Line 14517: ⠃ ⠚ ⠚ ⠋ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠙ ⠄ ⠑ ⠗ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠈ ⠏ ⠗ ⠞ ⠊ ⠽ ⠕ ⠛ ⠊ ⠞ ⠜ ⠗ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠚ ⠈ ⠝ ⠽ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠝ ⠔ ⠉ ⠑ ⠗ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠙ ⠑ ⠩ ⠛ ⠥ ⠇ ⠊ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠝ ⠊ ⠈ ⠗ ⠃ ⠜ ⠉ ⠊ ⠞ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠓ ⠢ ⠑ ⠡ ⠑ ⠄ ⡳ ⠭ ⠴ ⠴ ⠒ ⠁ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠁ ⠈ ⠽ ⠜ ⠈ ⠝ ⠫ ⠕ ⠗ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠁ ⠈ ⠽ ⠜ ⠈ ⠬ ⠛ ⠕ ⠇ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠁ ⠈ ⠽ ⠜ ⠈ ⠝ ⠾ ⠊ ⠛ ⠥ ⠢ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠕ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠃ ⠜ ⠈ ⠗ ⠃ ⠥ ⠫ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠎ ⠪ ⠙ ⠊ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠜ ⠗ ⠃ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠃ ⠜ ⠈ ⠗ ⠃ ⠜ ⠫ ⠕ ⠚ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠃ ⠈ ⠞ ⠄ ⡳ ⠭ ⠆ ⠴ ⠴ ⠉ ⠄ ⠎ ⠕ ⠢ ⠜ ⠝ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠈ ⠃ ⠗ ⠥ ⠝ ⠑ ⠊ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠙ ⠜ ⠗ ⠥ ⠈ ⠎ ⠄ ⡳ ⠭ ⠆ ⠴ ⠴ ⠉ ⠄ ⠎ ⠜ ⠇ ⠜ ⠍ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠈ ⠅ ⠽ ⠜ ⠃ ⠕ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠘ ⠜ ⠈ ⠗ ⠙ ⠑ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠅ ⠕ ⠍ ⠕ ⠗ ⠑ ⠎ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠅ ⠕ ⠗ ⠊ ⠢ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠈ ⠏ ⠗ ⠚ ⠜ ⠞ ⠈ ⠝ ⠈ ⠞ ⠗ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠛ ⠜ ⠈ ⠍ ⠃ ⠊ ⠢ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠚ ⠜ ⠏ ⠜ ⠝ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠈ ⠛ ⠗ ⠔ ⠎ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠈ ⠛ ⠗ ⠑ ⠝ ⠜ ⠫ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠛ ⠥ ⠢ ⠜ ⠞ ⠑ ⠍ ⠜ ⠇ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠊ ⠅ ⠥ ⠢ ⠜ ⠾ ⠕ ⠗ ⠊ ⠢ ⠜ ⠇ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠛ ⠊ ⠝ ⠊ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠊ ⠚ ⠗ ⠜ ⠢ ⠑ ⠇ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠅ ⠊ ⠗ ⠊ ⠃ ⠜ ⠞ ⠊ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠛ ⠼ ⠈ ⠏ ⠗ ⠚ ⠜ ⠞ ⠈ ⠝ ⠈ ⠞ ⠗ ⠔ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠇ ⠜ ⠕ ⠎ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠇ ⠊ ⠉ ⠑ ⠈ ⠄ ⡳ ⠭ ⠆ ⠴ ⠴ ⠉ ⠄ ⠝ ⠈ ⠎ ⠾ ⠑ ⠊ ⠝ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠜ ⠇ ⠈ ⠙ ⠃ ⠔ ⠏ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠜ ⠈ ⠇ ⠾ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠎ ⠜ ⠝ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠜ ⠗ ⠊ ⠝ ⠕ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠜ ⠈ ⠗ ⠩ ⠜ ⠇ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠜ ⠊ ⠈ ⠇ ⠽ ⠜ ⠈ ⠝ ⠫ ⠎ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠗ ⠊ ⠩ ⠜ ⠎ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠑ ⠈ ⠅ ⠎ ⠊ ⠅ ⠕ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠜ ⠊ ⠈ ⠅ ⠗ ⠕ ⠝ ⠑ ⠩ ⠊ ⠢ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠈ ⠇ ⠄ ⡳ ⠭ ⠆ ⠴ ⠴ ⠉ ⠄ ⠙ ⠕ ⠘ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠍ ⠕ ⠝ ⠜ ⠅ ⠕ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠝ ⠗ ⠁ ⠕ ⠢ ⠑ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠕ ⠍ ⠜ ⠝ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠏ ⠜ ⠝ ⠜ ⠍ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠏ ⠈ ⠗ ⠞ ⠥ ⠛ ⠜ ⠇ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠎ ⠑ ⠈ ⠝ ⠾ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠇ ⠥ ⠎ ⠊ ⠢ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠎ ⠜ ⠍ ⠕ ⠢ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠎ ⠇ ⠕ ⠍ ⠝ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠜ ⠊ ⠈ ⠇ ⠽ ⠜ ⠈ ⠝ ⠫ ⠎ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠎ ⠥ ⠊ ⠚ ⠜ ⠗ ⠈ ⠇ ⠽ ⠜ ⠈ ⠝ ⠫ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠞ ⠜ ⠚ ⠊ ⠅ ⠊ ⠈ ⠎ ⠞ ⠜ ⠝ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠾ ⠕ ⠈ ⠬ ⠛ ⠜ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠾ ⠥ ⠘ ⠜ ⠇ ⠥ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠉ ⠄ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠊ ⠥ ⠑ ⠎ ⠁ ⠑ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠕ ⠄ ⡳ ⠭ ⠴ ⠴ ⠆ ⠴ ⠄ ⠘ ⠊ ⠢ ⠑ ⠞ ⠝ ⠜ ⠍ ⠄ ⡳ ⠭ ⠴ ⠔ ⠖ ⠲ ⠄
(base) ye@lst-gpu-3090:~/exp/bg-br/data$
```

## 89. [comma2tab_label2digit.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/comma2tab_label2digit.py)  

ကော်မာခြားထားတဲ့ ဖိုင်ပုံစံကနေ TAB ကီးနဲ့ခြားထားတဲ့ ပုံစံအဖြစ်ပြောင်းလဲဖို့နဲ့ စာသားနဲ့ ရိုက်ထားတဲ့ လေဘယ်နှစ်မျိုးကို digit label (i.e. 0, 1) အဖြစ် ပြောင်းဖို့အတွက် ရေးခဲ့တယ်။ အသုံးပြုပုံ ဥပမာက အောက်ပါအတိုင်းပါ။  

ဥပမာအဖြစ် run ပြဖို့အတွက် သုံးမယ့် CSV ဖိုင်က အောက်ပါအတိုင်းပါ။  

```
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ head sentiment_my_dataset.csv
text,sentiment
အရမ်း လှ နေ ပါလား,positive
ရုပ်ဆိုး ကြီး,negative
အပေါက် ဆိုး တယ်,negative
စောက် သုံး မကျ,negative
မင်္ဂလာ ပါ,positive
စား လို့ ကောင်း တယ်,positive
အိပ် လို့ ကောင်း တယ်,positive
လိမ္မာ တယ်,positive
မ လိမ္မာ ဘူး,negative
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$
```

Run ပြီးသွားတဲ့အခါမှာ ပြောင်းသွားတဲ့ TSV file format က အောက်ပါအတိုင်းပါ။  

```
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ python ./comma2tab_label2digit.py ./sentiment_my_dataset.csv sentiment_my_dataset.tsv
Processed data saved to sentiment_my_dataset.tsv
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ head sentiment_my_dataset.tsv
text    sentiment
အရမ်း လှ နေ ပါလား       0
ရုပ်ဆိုး ကြီး   1
အပေါက် ဆိုး တယ် 1
စောက် သုံး မကျ  1
မင်္ဂလာ ပါ      0
စား လို့ ကောင်း တယ်     0
အိပ် လို့ ကောင်း တယ်    0
လိမ္မာ တယ်      0
မ လိမ္မာ ဘူး    1
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$
```

## 90. [conv_delimiter_label2digit.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/conv_delimiter_label2digit.py)  

အထက်က ပရိုဂရမ် ၈၉ တုန်းကလို CSV ကနေ TSV ကိုပဲ ပြောင်းတာ မဟုတ်ပဲ လက်ရှိဖိုင်ရဲ့ delimiter နဲ့ ကိုယ်ပြောင်းချင်တဲ့ delimiter တွေကို -f or --from, -t or --to ဆိုတဲ့ option နှစ်ခုသုံးပြီး သတ်မှတ်ပေးလို့ ရအောင် ရေးခဲ့တယ်။ text label တွေကိုလည်း ပေးလိုက်တဲ့ input corpus ဖိုင်မှာ ဘယ်နှစ်မျိုး ရှိတာလဲ ဆိုတာကို python code က ရေတွက်ပြီး digit label တွေကို သတ်မှတ်ပေးလိမ့်မယ်။ အဲဒါကြောင့် ဒီပရိုဂရမ်ကတော့ ပိုအသုံးရတာ အဆင်ပြေလိမ့်မယ်။  

```
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ python ./conv_delimiter_label2digit.py --help
usage: conv_delimiter_label2digit.py [-h] [-f FROM_DELIMITER] [-t TO_DELIMITER]
                                     input_filename output_filename

Convert file formats and text labels to digits.

positional arguments:
  input_filename        Path to the input file.
  output_filename       Path to the output file.

optional arguments:
  -h, --help            show this help message and exit
  -f FROM_DELIMITER, --from-delimiter FROM_DELIMITER
                        Original delimiter (default is ',').
  -t TO_DELIMITER, --to-delimiter TO_DELIMITER
                        New delimiter (default is tab).
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$
```

CSV ကနေ TSV ကို ပြောင်းပေးတာက default delimiter တွေအဖြစ် သတ်မှတ်ထားတာမို့လို့ --from, --to တွေကို assign မလုပ်ပေးရင်လည်း အိုကေတယ်။ ဥပမာ အောက်ပါလိုမျိုး command ပေးပြီး run လို့ ရပါတယ်။  

```
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ python ./conv_delimiter_label2digit.py ./sentiment_my_dataset.csv output.tsv
Processed data saved to output.tsv

Label to Digit Mapping:
'negative': 0
'positive': 1
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ head output.tsv
text    sentiment
အရမ်း လှ နေ ပါလား       1
ရုပ်ဆိုး ကြီး   0
အပေါက် ဆိုး တယ် 0
စောက် သုံး မကျ  0
မင်္ဂလာ ပါ      1
စား လို့ ကောင်း တယ်     1
အိပ် လို့ ကောင်း တယ်    1
လိမ္မာ တယ်      1
မ လိမ္မာ ဘူး    0
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$
```

CSV ဖိုင်ကနေ pipe character နဲ့ ခြားထားတဲ့ file format အဖြစ် ပြောင်းချင်ရင်တော့ အောက်ပါအတိုင်း ...  
တစ်ခုရှိတာက 0, 1 ... ဆိုပြီး digit label တွေအဖြစ် ပြောင်းတဲ့ အခါမှာတော့ auto assign လုပ်သွားမှာ ဖြစ်တယ်။  

```
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ python ./conv_delimiter_label2digit.py -t "|" ./sentiment_my_dataset.csv output.psv
Processed data saved to output.psv

Label to Digit Mapping:
'negative': 0
'positive': 1
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$ head output.psv
text|sentiment
အရမ်း လှ နေ ပါလား|1
ရုပ်ဆိုး ကြီး|0
အပေါက် ဆိုး တယ်|0
စောက် သုံး မကျ|0
မင်္ဂလာ ပါ|1
စား လို့ ကောင်း တယ်|1
အိပ် လို့ ကောင်း တယ်|1
လိမ္မာ တယ်|1
မ လိမ္မာ ဘူး|0
(demo) ye@lst-gpu-3090:~/exp/demo/relativity_meaning/data/tmp$
```

## 91. [padsint_detection.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/padsint_detection.py)

Input ဖိုင်ထဲက စာကြောင်းတွေထဲကနေ ပါဌ်ဆင့် တွေကိုပဲ ဆွဲထုတ်ဖို့ ရေးခဲ့တ့ ပရိုဂရမ်ပါ။ word level unit အနေနဲ့ ဆွဲထုတ်တာ မဟုတ်ပါဘူး။ character+padsint_symbol+character ဆိုတဲ့ pattern ကိုပဲ ဆွဲထုတ်ကြည့်ထားတာပါ။ ဥပမာ ပေးလိုက်တဲ့ input corpus ထဲမှာ ဆင့်ထားတဲ့ pattern ဘယ်နှစ်မျိုး ပါသလဲ ဆိုတာကို သိချင်တဲ့အခါမှာ အသုံးဝင်ပါလိမ့်မယ်။ သိတဲ့အတိုင်းပဲ လက်တွေ့ စာကြောင်းတွေထဲမှာက လူတွေက မှားရိုက်ထားတာတွေကော၊ textbook ထဲမှာ သတ်မှတ်ထားတဲ့အတိုင်း မဟုတ်တဲ့ ဆင့်ပုံဆင့်နည်းတွေကိုလည်း လုပ်ကြတာမို့လို့ raw data ကနေ ဆွဲထုတ်ကြည့်ဖို့ ပါ။  

Example running ကတော့ အောက်ပါအတိုင်းပါ။  

```
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$ cat input.txt
ကျွန်တော်က တက္ကသိုလ် ကျောင်းသားပါ။
သစ္စာရှိမှ သစ္စာပန်း ပွင့်လိမ့်မယ်
ဒုက္ခသစ္စာ
```

output filename ကို option နဲ့ မပေးပဲ run ရင် output ကို scree မှာပဲ print လုပ်ပေးပါလိမ့်မယ်။  

```
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$ python ./padsint_detection.py ./input.txt
က္က
စ္စ, စ္စ
က္ခ, စ္စ
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$
```

## 93. [pos_pattern_checker.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/pos_pattern_checker.py)

လေ့လာစေချင်တာက ဒီ code ကို ရေးတဲ့အခါမှာ DSL parser library တစ်ခုကို ယူသုံးပြထားတယ်။ အသုံးဝင်ပါလိမ့်မယ်။   

```
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$ python ./pos_pattern_checker.py --help
usage: pos_pattern_checker.py [-h] -p PATTERN [-o OUTPUT_FILENAME] filename

Parse Burmese POS-tagged sentences against a pattern.

positional arguments:
  filename              Input filename with POS-tagged Burmese sentences.

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        Pattern DSL string.
  -o OUTPUT_FILENAME, --output_filename OUTPUT_FILENAME
                        Output filename to save the results. Defaults to printing on screen.
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$
```

မြန်မာစာရဲ့ POS pattern အမျိုးမျိုးကို ဆွဲထုတ်ကြည့်ခဲ့တယ်။   
ဒီနေရာမှာ demo run ပြဖို့အတွက် head command နဲ့ ၁၀ကြောင်းစီကိုပဲ ဆွဲထုတ်ကြည့်ခဲ့တယ်။ Python ရဲ့ print နဲ့ ရိုက်ထုတ်ထားတဲ့ output ကို head commnad ကို ပေးရင် စာကြောင်းအရေအတွက် များတဲ့အခါမှာ Broken pipe error ပေးတာကြောင့်မို့လို့ အဲဒီ error ကို မပေါ်အောင် "2> /dev/null" လုပ်ထားတာပါ။  

ဆွဲထုတ်ကြည့်လို့ ထွက်လာတဲ့ ရလဒ်တွေက အောက်ပါအတိုင်း ...   

```
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$ python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: pron n END" 2> /dev/null | head
အဲ့ဒီ/pron အခန်း/n
ခင်ဗျား/pron သူဌေး/n
ခင်ဗျား/pron အသက်/n
ငါ့/pron စကား/n
ဒီ/pron နန်းတော်/n
ကျွန်တော်/pron အိမ်နီးနားချင်း/n
အဲဒီ/pron လူ/n
ကျွန်တော့်/pron အရွယ်အစား/n
ခင်ဗျား/pron အပေါ်/n
ကျွန်တော်/pron ရှေ့လျှောက်/n
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$
```

```
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$ python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: pron v END" 2> /dev/null | head
ကျွန်တော်/pron စဉ်းစား/v
မင်း/pron စား/v
သူ/pron ခေါင်းဆောင်/v
ဘာ/pron ဖြစ်/v
ဘာ/pron ဖြစ်/v
ဘာ/pron ဝယ်/v
ဘာ/pron ကျွေး/v
မင်း/pron အကြံပြု/v
ဘာ/pron လုပ်/v
ကျွန်တော်/pron ဆိုလို/v
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$
```

```
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$ python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: n adj v n END" 2> /dev/null | head
ဒေသ/n အသီးသီး/adj ရှိ/v ဥရောပ/n
မြို့/n ဟောင်း/adj ရှိ/v ပုဂံ/n
နယ်မြေ/n သစ်/adj ရှိ/v မကောင်းဆိုးဝါး/n
ဆရာမ/n ကြီး/adj ဖြစ်/v သူ/n
ဆရာ/n ဘာ/adj အရေးကြီး/v ကိစ္စ/n
ကုန်ပစ္စည်း/n ထက်/adj ယှဉ်ပြိုင်/v အား/n
အာဏာ/n ကြီးမား/adj ထင်ပေါ်/v အရာရာ/n
အခန်း/n လွတ်/adj ရှိ/v လား/n
ကီလို/n အခမဲ့/adj သယ်/v ခွင့်/n
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$
```

```
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$ python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: adv v END" 2> /dev/null | head
ဆက်လက်/adv လုပ်ကိုင်/v
ဘယ်လို/adv ရှိ/v
ဘယ်လောက်/adv ရှိ/v
အမြန်/adv ထွက်/v
အမြဲ/adv သတိရ/v
ဆင်ဆင်/adv တူ/v
နည်းနည်း/adv လျော့/v
တော်တော်/adv ကြာ/v
အလွန်/adv ပြင်းထန်/v
လတ်တလော/adv ရှာဖွေ/v
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$
```

```
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$ python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: n v n END" 2> /dev/null | head
သမ္မတ/n ဖြစ်/v သူ/n
အပြင်/n ရှိ/v ရုပ်ဝတ္ထု/n
ကုန်/n ထုတ်လုပ်/v သူ/n
နှစ်/n ပြည့်/v မွေးနေ့/n
ဂျိုဝါ/n ခေါ်/v ကောက်/n
အရောင်း/n ဖြစ်/v ပမာဏ/n
စစ်တပ်/n ပိုင်/v လေယာဉ်/n
နတ်/n ကိုးကွယ်/v သူ/n
မေမြို့/n ရှိ/v လူဦးရေ/n
နိုင်ငံ/n ရှိ/v ပြည်ထောင်စုသား/n
(base) ye@lst-gpu-3090:~/exp/4teaching/dsl_parser$
```

94. [sort_ngram.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/sort_ngram.py)

NLP task တွေအတွက်က ngram ဖိုင်တွေကိုသုံးပြီး အလုပ်အမျိုးမျိုး လုပ်လို့ ရတာမို့လို့ အရေးကြီးပါတယ်။ အဲဒီ ngram ဖိုင်တွေကို တခါတလေမှာ လူအနေနဲ့ ဖွင့်ပြီး ဘယ်လိုတွေ ဖြစ်နေသလဲ ဆိုတာကို လေ့လာဖို့ လိုအပ်ပါတယ်။ ngram value နဲ့ ဒါမှမဟုတ်လည်း text နဲ့ sorting လုပ်ပြီး ကြည့်တာမျိုး လုပ်ကြရပါတယ်။ ဒီ ပရိုဂရမ် ၉၄ က အဲဒီအတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။  

--help ခေါ်ကြည့်ရင် အောက်ပါအတိုင်း help screen ပြပေးပါလိမ့်မယ်။ ဘယ်လို သုံးရမလဲ ဆိုတာကို လေ့လာပါ။  

```
(base) ye@lst-gpu-3090:~/exp/sylbreak4all/lang_detection/lib$ python sort_ngram.py --help
usage: sort_ngram.py [-h] [-o OUTPUT] [--sort_by {text,value}] [--order {asc,desc}] filename

Sort the ngram profile file.

positional arguments:
  filename              Input filename

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename
  --sort_by {text,value}
                        Choose the sorting column: text or value
  --order {asc,desc}    Sorting order: asc or desc
```

မြန်မာစာ ngram ဖိုင် တစ်ဖိုင်ကို ဥပမာအနေနဲ့ သုံးပြီး python ပရိုဂရမ်ကို sorting အမျိုးမျိုး စီပြီး ထိပ်ဆုံး စာကြောင်း အကြောင်း ၃၀ ကို လေ့လာကြည့်ပါမယ်။  
ပထမဆုံး စာသားကိုပဲ (i.e. alphabetical) က ကနေ အ အစီအစဉ်နဲ့ စီကြည့်ပါမယ်။ သင်္ကေတတွေက စာလုံးတွေရဲ့ ရှေ့မှာ လာပါလိမ့်မယ်။   

```
(base) ye@lst-gpu-3090:~/exp/sylbreak4all/lang_detection/lib$ python ./sort_ngram.py --sort_by text --order asc ./syl_profile/beik.profile | head -n 30
( ရီး ) 1.4765224883877354e-05
( ၆ ) 1.4765224883877354e-05
) နာ ရီ 1.4765224883877354e-05
) ။ နင် 1.4765224883877354e-05
က က စား 4.400329396086221e-05
က ကမ္ဘာ မှာ 1.4765224883877354e-05
က ကား ဘ 1.4765224883877354e-05
က ကား ရပ် 2.938425942236978e-05
က ကား ရေ 1.4765224883877354e-05
က ကိန်း တစ် 1.4765224883877354e-05
က ကို စာ 1.4765224883877354e-05
က ကို မ 1.4765224883877354e-05
က ကိုင် ထား 1.4765224883877354e-05
က ကိုယ် ကို 2.938425942236978e-05
က ကော ။ 4.400329396086221e-05
က ကောင် တွေ 1.4765224883877354e-05
က ကောင်း ကောင်း 1.4765224883877354e-05
က ကံ ကောင်း 1.4765224883877354e-05
က ကျ တော် 2.938425942236978e-05
က ကျက် အား 1.4765224883877354e-05
က ကျေ နပ် 1.4765224883877354e-05
က ကျောင်း ဆ 1.4765224883877354e-05
က ကျောင်း မှာ 1.4765224883877354e-05
က ကျောင်း အုပ် 1.4765224883877354e-05
က ကျွန် တော့ 1.4765224883877354e-05
က ကျွန် တော် 5.862232849935464e-05
က ကျွန် တော့် 7.324136303784707e-05
က ကျွန် မ 4.400329396086221e-05
က ကြ ရ 1.4765224883877354e-05
က ကြမ်း ပြင် 1.4765224883877354e-05
```

ဒီတစ်ခါတော့ စာသားနဲ့ စီတာကိုပဲ descending order နဲ့ run ကြည့်ကြရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/sylbreak4all/lang_detection/lib$ python ./sort_ngram.py --sort_by text --order desc ./syl_profile/beik.profile | head -n 30
၎င်း က နား 1.4765224883877354e-05
၍ အ ထဲ 1.4765224883877354e-05
၍ သ တင်း 1.4765224883877354e-05
၍ လက် ဖက် 1.4765224883877354e-05
၍ ထိုင် ပါ 1.4765224883877354e-05
၍ ထိုင် ချ 1.4765224883877354e-05
၍ ကျွန် တော့် 1.4765224883877354e-05
။ ၆ နာ 2.938425942236978e-05
။ ၅ မိ 1.4765224883877354e-05
။ ၂ ချက် 2.938425942236978e-05
။ ၁ ၉ 1.4765224883877354e-05
။ ၁ ၀ 1.4765224883877354e-05
။ ၁ နာ 1.4765224883877354e-05
။ ဧည့် ခန်း 4.400329396086221e-05
။ ဦး စိုး 1.4765224883877354e-05
။ ဦး ကျော် 1.4765224883877354e-05
။ ဥ ဥ 1.4765224883877354e-05
။ ဥ ပ 4.400329396086221e-05
။ အံ ဆွဲ 1.4765224883877354e-05
။ အဲ့ အ 0.00039486012288468054
။ အဲ့ မှာ 1.4765224883877354e-05
။ အဲ့ မျိုး 1.4765224883877354e-05
။ အဲ့ မိန်း 1.4765224883877354e-05
။ အဲ့ မ 1.4765224883877354e-05
။ အဲ့ ဘာ 1.4765224883877354e-05
။ အဲ့ ဒါ 4.400329396086221e-05
။ အဲ့ ဒယ် 0.00020481267388427894
။ အဲ့ ဇာ 0.00013171750119181678
။ အဲ့ စာ 2.938425942236978e-05
။ အဲ လေ 1.4765224883877354e-05
```

ဒီတခါတော့ n-gram value ကို ascending order (ငယ်စဉ်ကြီးလိုက်) စီကြည့်ကြရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/sylbreak4all/lang_detection/lib$ python ./sort_ngram.py --sort_by value --or
der asc ./syl_profile/bamar.profile | head -n 30
သာ မောင်း ပြိုင် 1.4197879296225912e-07
မောင်း ပြိုင် သာ 1.4197879296225912e-07
ပြိုင် သာ ပြိုင် 1.4197879296225912e-07
သာ ပြိုင် ကို 1.4197879296225912e-07
ယ့် ကိုယ် ပိုင် 1.4197879296225912e-07
ဖြစ် ရင် ထွက် 1.4197879296225912e-07
ရင် ထွက် ပြေး 1.4197879296225912e-07
ထွက် ပြေး အေး 1.4197879296225912e-07
ပြေး အေး အေး 1.4197879296225912e-07
ပြန် မောင်း လု 1.4197879296225912e-07
မောင်း လု သာ 1.4197879296225912e-07
သာ မောင်း သမ္မ 1.4197879296225912e-07
မောင်း သမ္မ တ 1.4197879296225912e-07
ထင် ကျော် အင်း 1.4197879296225912e-07
ကျော် အင်း လေး 1.4197879296225912e-07
လေး သူ ဆို 1.4197879296225912e-07
သူ ဆို လည်း 1.4197879296225912e-07
ကစ် က ဖြူ 1.4197879296225912e-07
ဖွေး လေး ဆို 1.4197879296225912e-07
တော့ ရှမ်း မ 1.4197879296225912e-07
တွေ တော့ ထိုင် 1.4197879296225912e-07
တော့ ထိုင် ငို 1.4197879296225912e-07
အင်း လေး နဲ့ 1.4197879296225912e-07
သက် လုံး တ 1.4197879296225912e-07
ကယ် လာ နေ 1.4197879296225912e-07
မ ကစ် ဇင် 1.4197879296225912e-07
ကစ် ဇင် ဇင် 1.4197879296225912e-07
ဇင် ဇင် တို့ 1.4197879296225912e-07
ဇင် တို့ မွန် 1.4197879296225912e-07
တို့ မွန် ပြည် 1.4197879296225912e-07

```

n-gram value နဲ့ပဲ ကြီးစဉ်ငယ်လိုက် စီကြည့်မယ် ဆိုရင်တော့ အောက်ပါအတိုင်းပါ။  

```
(base) ye@lst-gpu-3090:~/exp/sylbreak4all/lang_detection/lib$ python ./sort_ngram.py --sort_by value --order desc ./syl_profile/bamar.profile | head -n 30
က ကျွန် တော် 0.0016813958043658524
အား ပေး နေ 0.0009744538738636732
မင်္ဂ လာ ပါ 0.0008286796082182645
ကျွန် တော် တို့ 0.0005963123361721117
ဖြစ် ပါ တယ် 0.0005665108469562712
ပါ တယ် အ 0.0005592010477146499
နေ ပါ တယ် 0.0005473929104781848
အ စိုး ရ 0.0005317893005585702
၀ ၀ ၀ 0.0005107033412077396
သာ ဓု သာ 0.0004986140578465967
ဓု သာ ဓု 0.0004984734847842579
မြန် မာ နိုင် 0.0004325447185473277
က ကျွန် တော့် 0.00041483251269263
ရ ပါ တယ် 0.00039979119502237085
ဥ ပ ဒေ 0.00039712030683793233
မာ နိုင် ငံ 0.00038236013529235094
မ ဟုတ် ဘူး 0.0003802515393572679
၂ ၀ ၁ 0.00037617492054944066
မြဲ အား ပေး 0.0003609930298168426
အ မြဲ အား 0.00035944672613111506
ခဲ့ ပါ တယ် 0.00035747870325837086
ပေး နေ ပါ 0.000350871769328444
အ ရမ်း ချစ် 0.00034482712764787255
ပ ရိ သတ် 0.0003434213970244838
က ကျွန် မ 0.00034004764352835095
ချစ် စ ရာ 0.00033892305902964
ပေး နေ တယ် 0.00033498701328415163
ကို နေ တိုး 0.0003264120564814805
ဒါ ပေ မဲ့ 0.0003259903372944639
နိုင် ပါ စေ 0.0003231788760476865
```

## 95. [analyze_NER_corpus.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/analyze_NER_corpus.py)  

NER corpus မှာ တပ်ထားတဲ့ tag အရေအတွက်ရဲ့ frequency/distribution တွေကို စစ်ဆေးဖို့အတွက် ရေးခဲ့တဲ့ ပရိုဂရမ်ပါ။ Corpus တစ်ခု ဆောက်တဲ့နေရာမှာ tag တစ်ခုတည်းက များနေတာမျိုး ဖြစ်နေရင် မော်ဒယ်မှာ bias ဖြစ်တာမို့လို့ ...  

--help နဲ့ ဘယ်လို run ရသလဲ ဆိုတာကို ခေါ်ကြည့်ရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/myNER/data$ python ./analyze_NER_corpus.py --help
usage: analyze_NER_corpus.py [-h] [-f {abstract,detailed}] filename

Analyze NER tagged data.

positional arguments:
  filename              Path to the input file.

optional arguments:
  -h, --help            show this help message and exit
  -f {abstract,detailed}, --format {abstract,detailed}
                        Output format. "abstract" to consider all B, I, E, S tags as one
                        tag; "detailed" for detailed tags.
```

ဒီ ပရိုဂရမ်မှာက format နှစ်မျိုးနဲ့ print လုပ်ပေးဖို့ ရေးထားပါတယ်။  
Running example with --format abstract:  

```
(base) ye@lst-gpu-3090:~/exp/myNER/data$ python ./analyze_NER_corpus.py ./10k_NER_draft_version1_KaungLwinThant.txt --format abstract
Analysis of './10k_NER_draft_version1_KaungLwinThant.txt'
----------------------------------------
1. Number of sentences without named entities: 7490
2. Frequency of each tag:
   DATE: 1647
   EVENT: 186
   LOC: 3190
   NUM: 1093
   O: 137129
   ORG: 990
   PER: 1179
   PRODUCT: 49
   TIME: 404
3. Distribution of each tag:
   DATE: 1.13%
   EVENT: 0.13%
   LOC: 2.19%
   NUM: 0.75%
   O: 94.01%
   ORG: 0.68%
   PER: 0.81%
   PRODUCT: 0.03%
   TIME: 0.28%

(base) ye@lst-gpu-3090:~/exp/myNER/data$
```

Running example with --format option:  

```
(base) ye@lst-gpu-3090:~/exp/myNER/data$ python ./analyze_NER_corpus.py ./10k_NER_draft_version1_KaungLwinThant.txt --format detailed
Analysis of './10k_NER_draft_version1_KaungLwinThant.txt'
----------------------------------------
1. Number of sentences without named entities: 7490
2. Frequency of each tag:
   B-DATE: 540
   B-EVENT: 61
   B-LOC: 1066
   B-NUM: 179
   B-ORG: 307
   B-PER: 235
   B-PRODUCT: 15
   B-TIME: 133
   E-DATE: 540
   E-EVENT: 61
   E-LOC: 1066
   E-NUM: 179
   E-ORG: 307
   E-PER: 235
   E-PRODUCT: 15
   E-TIME: 133
   I-DATE: 444
   I-EVENT: 52
   I-LOC: 166
   I-NUM: 32
   I-ORG: 226
   I-PER: 11
   I-PRODUCT: 2
   I-TIME: 82
   O: 137129
   S-DATE: 123
   S-EVENT: 12
   S-LOC: 892
   S-NUM: 703
   S-ORG: 150
   S-PER: 698
   S-PRODUCT: 17
   S-TIME: 56
3. Distribution of each tag:
   B-DATE: 0.37%
   B-EVENT: 0.04%
   B-LOC: 0.73%
   B-NUM: 0.12%
   B-ORG: 0.21%
   B-PER: 0.16%
   B-PRODUCT: 0.01%
   B-TIME: 0.09%
   E-DATE: 0.37%
   E-EVENT: 0.04%
   E-LOC: 0.73%
   E-NUM: 0.12%
   E-ORG: 0.21%
   E-PER: 0.16%
   E-PRODUCT: 0.01%
   E-TIME: 0.09%
   I-DATE: 0.30%
   I-EVENT: 0.04%
   I-LOC: 0.11%
   I-NUM: 0.02%
   I-ORG: 0.15%
   I-PER: 0.01%
   I-PRODUCT: 0.00%
   I-TIME: 0.06%
   O: 94.01%
   S-DATE: 0.08%
   S-EVENT: 0.01%
   S-LOC: 0.61%
   S-NUM: 0.48%
   S-ORG: 0.10%
   S-PER: 0.48%
   S-PRODUCT: 0.01%
   S-TIME: 0.04%

(base) ye@lst-gpu-3090:~/exp/myNER/data$
```

အထက်မှာ မြင်ရတဲ့အတိုင်းပါပဲ လက်ရှိ develop လုပ်နေတဲ့ NER corpus မှာ O tag တွေက တအားများနေတာကို တွေ့ရပါလိမ့်မယ်။  
O tag တွေကလည်း မပါလို့ မဖြစ်ပါဘူး။ သို့သော် လက်ရှိလိုမျိုး တအားများနေရင်လည်း အဆင်မပြေပါဘူး။  

## 96. [compare_sentence_tag_distributions.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/compare_sentence_tag_distributions.py)

Hatespeech တွေကို GPT-2 LLM မော်ဒယ်ဆောက်ပြီး generate လုပ်တဲ့ experiment ကို လုပ်ကြည့်ခဲ့တယ်။ Testing ၅ခါ လုပ်ခဲ့ပြီး အဲဒီ ထွက်လာတဲ့ output တွေမှာ ဘယ်လို hatespeech စာကြောင်းတွေက များနေသလဲ ဆိုတာကို သိချင်လို့ manually sentence level အနေနဲ့ tagging ပြန်လုပ်ပြီး အဲဒီ testing ၅ခုရဲ့ output တွေအကြား hatespeech distribution ကို graph အနေနဲ့ ထုတ်ပြီး နှိုင်းယှဉ်ကြည့်နိုင်ဖို့အတွက် ဒီ python code ကို ရေးခဲ့တယ်။  

GPT-2 model ကနေ ထုတ်ပေးထားတဲ့ စာကြောင်းတွေကို sentence level tagging လုပ်ထားတဲ့ format က အောက်ပါအတိုင်းပါ။  

```
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/sentence$ ls
Test-1  Test-2  Test-3  Test-4  Test-5
```

```
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/sentence$ head -n 3 Test-1
မနက် ၅ နာရီ ခု ထိ မ လာ ဘူး ၅ မိနစ် ၅ နာရီ ထိ ပျက် သွား အောင် ပေး တာ လား လီး ပဲ ဟေ့ မအေလိုး တွေပျက် သွား ပြီ ပြန် ဖျက် သလို ပဲောင် မ ပြည့် တော့ ဘူး မအေလိုး တွေ မီး နာရီ ပြန် ပျက် တယ် ဆို တော့ မ သိဝက် လည်း ပျက် ပြီ လီး ပဲ ဟေ့     ab
မအေလိုး တွေ မီတာခ ကျတော့ ပြည်သူ တွေ အကုန်လုံး ခု မီး လာ မယ့် အချိန် မှန် အိပ် ပေး ပြီ နော် မီး ပျက် နေ တာေ ရေ     ab
မအေလိုး တွေ တစ် နေကုန် ပျက် ၉ နာရီ လာ ပြီး ၉ နာရီ တော့ မှာ လာ ဖြတ် နေ တာ ပဲ     ab
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/sentence$ tail -n 3 Test-5
ဘုန်းကြီး က တော့ မင်း တို့ က ဘယ်လို အဟုတ် မှာ လဲ ကျေနပ် မ ဆိုင် တာ နဲ့ တစ် ယောက် မှာ လေးစား ပါ တယ်        no
လူ က ရော နင် တို့ တစ် ယောက် က အစား ဖူး တုန်း က ကိုယ့် အများကြီး လို့ ရ တယ် ရှင်း ပေါ် က နေ မြန်မာ လူမျိုး တွေ က သူ တို့ နိုင်ငံ လေး တွေ က လုပ် ခဲ့ ရ လေ နေ လို့ အမေ မ ဟုတ် ဘူး တဲ့ သူ တွေ သူ တို့ အတွက် တောင် မ စား လို့ လား နော်   no
အခု မှ သန့် တာ ပဲ မြန်မာ ပြည် မှာ ပဲ လေ မအလ ကြီး ရာ ချင် စရာ    ab
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/sentence$
```

--help ခေါ်ကြည့်ရင် ...  

```
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script$ python ./compare_sentence_tag_distributions.py --help
usage: compare_sentence_tag_distributions.py [-h] -p PATH -g GRAPH_FILENAME

Compare Hate Speech Tag Distributions Among Files.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the folder containing the files.
  -g GRAPH_FILENAME, --graph_filename GRAPH_FILENAME
                        Output graph filename.
```

Run တဲ့ ပုံစံက အောက်ပါအတိုင်း  

```
python ./compare_sentence_tag_distributions.py -p ./sentence/ -g ./sentence_compare.png
```

Testing ၅ခု အတွက် ဆွဲပေးခဲ့တဲ့ graph က အောက်ပါအတိုင်းပါ။  

<p align="center" width="100%">
    <img width="75%" src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/sentence_compare.png">
</p>

## 97. [compare_word_tag_distributions.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/compare_word_tag_distributions.py)

အထက်က ပရိုဂရမ် နံပါတ် 96 ကို modify လုပ်ထားတဲ့ python code ပါ။ အလုပ်လုပ်တဲ့ ပုံစံကလည်း အတူတူပါပဲ။ ဒီတစ်ခါတော့ ဖတ်ယူရတဲ့ ဖိုင်က word level or phrase level အနေနဲ့ tag လုပ်ထားတဲ့ input text ဖိုင်ပါ။  ဖိုင် format ကအောက်ပါအတိုင်းပါ။  

```
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/word_phrase$ head -n 3 Test-2
မနက် ၅ နာရီ ခု ထိ မ လာ ဘူး ၅ မိနစ် ၅ နာရီ ထိ ပျက် သွား အောင် ပေး တာ လား လီး/ab ပဲ ဟေ့ မအေလိုး/ab တွေ
မီး ပျက် သွား ပြီ ပြန် ဖျက် သလို ပဲ
မီး လာ ရ မှာ မီး ပေး ပြီး ၅ မိနစ် တောင် မ ပြည့် တော့ ဘူး မအေလိုး/ab တွေ မီး နာရီ ပြန် ပျက် တယ် ဆို တော့ မ သိ ရင် လည်း နာရီဝက် လည်း ပျက် ပြီ လီး/ab ပဲ ဟေ့
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/word_phrase$ tail -n 3 Test-5
ဘုန်းကြီး က တော့ မင်း တို့ က ဘယ်လို အဟုတ် မှာ လဲ ကျေနပ် မ ဆိုင် တာ နဲ့ တစ် ယောက် မှာ လေးစား ပါ တယ်
လူ က ရော နင် တို့ တစ် ယောက် က အစား ဖူး တုန်း က ကိုယ့် အများကြီး လို့ ရ တယ် ရှင်း ပေါ် က နေ မြန်မာ လူမျိုး တွေ က သူ တို့ နိုင်ငံ လေး တွေ က လုပ် ခဲ့ ရ လေ နေ လို့ အမေ မ ဟုတ် ဘူး တဲ့ သူ တွေ သူ တို့ အတွက် တောင် မ စား လို့ လား နော်
အခု မှ သန့် တာ ပဲ မြန်မာ ပြည် မှာ ပဲ လေ မအလ/ab ကြီး ရာ ချင် စရာ
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/word_phrase$ head -n 3 Test-1
မနက် ၅ နာရီ ခု ထိ မ လာ ဘူး ၅ မိနစ် ၅ နာရီ ထိ ပျက် သွား အောင် ပေး တာ လား လီး/ab ပဲ ဟေ့ မအေလိုး/ab တွေပျက် သွား ပြီ ပြန် ဖျက် သလို ပဲောင် မ ပြည့် တော့ ဘူး မအေလိုး/ab တွေ မီး နာရီ ပြန် ပျက် တယ် ဆို တော့ မ သိဝက် လည်း ပျက် ပြီ လီး/ab ပဲ ဟေ့
မအေလိုး/ab တွေ မီတာခ ကျတော့ ပြည်သူ တွေ အကုန်လုံး ခု မီး လာ မယ့် အချိန် မှန် အိပ် ပေး ပြီ နော် မီး ပျက် နေ တာေ ရေ
မအေလိုး/ab တွေ တစ် နေကုန် ပျက် ၉ နာရီ လာ ပြီး ၉ နာရီ တော့ မှာ လာ ဖြတ် နေ တာ ပဲ
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/word_phrase$
```

help screen ခေါ်ကြည့်ချင်ရင် --help ကို သုံးပါ။  

```
(base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script$ python ./compare_word_tag_distributions.py --help
usage: compare_word_tag_distributions.py [-h] -p PATH -g GRAPH_FILENAME

Compare Hate Speech Tag Distributions Among Files.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the folder containing the files.
  -g GRAPH_FILENAME, --graph_filename GRAPH_FILENAME
                        Output graph filename.
```

Running example is as follows:  

```
 python ./compare_word_tag_distributions.py -p ./word_phrase/ -g word_compare.png
```

output graph က အောက်ပါ အတိုင်းပါ။  

<p align="center" width="100%">
    <img width="75%" src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/word_compare.png">
</p>

## 98. [print_codepoint.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/print_codepoint.py)

မိတ်ဆွေ တစ်ယောက်က request လုပ်တာနဲ့ Perl programming language နဲ့ ရေးထားတဲ့ print_codepoint.pl ဖိုင်ကို Python အတွက် ရေးခဲ့တာပါ။   

```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ python ./print_codepoint.py --help
usage: print_codepoint.py [-h] [--output_type {ordinal,unicode,both}] [--output OUTPUT]
                          [--no_print_original]
                          filename

Process a text file with various options.

positional arguments:
  filename              The filename to process

optional arguments:
  -h, --help            show this help message and exit
  --output_type {ordinal,unicode,both}
                        Choose to print ordinal value, Unicode code point, or both
                        (default: both)
  --output OUTPUT       Output file name (optional)
  --no_print_original   Do not print the original sentences (default: False)
```

Example input file:  

```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ cat khmer.txt
ខ្ញុំស្រឡាញ់កម្ពុជា។
អាហាររបស់ខ្មែរឆ្ងាញ់ណាស់។
យើងត្រូវរួមគ្នាថែរក្សាបរិស្ថាន។
បណ្ឌិតសភាចារ្យជាអ្នកបង្រៀនដ៏ល្អ។
កុំភ្លេចយកឆ័ត្រទៅរៀននៅសាលា។
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$
```

Example running with several commandline arguments are as follows. The first one is running with default printing setting.   

```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ python ./print_codepoint.py khmer.txt
ខ្ញុំស្រឡាញ់កម្ពុជា។
ខ (6017, U1781) ្ (6098, U17d2) ញ (6025, U1789) ុ (6075, U17bb) ំ (6086, U17c6) ស (6047, U179f) ្ (6098, U17d2) រ (6042, U179a) ឡ (6049, U17a1) ា (6070, U17b6) ញ (6025, U1789) ់ (6091, U17cb) ក (6016, U1780) ម (6040, U1798) ្ (6098, U17d2) ព (6038, U1796) ុ (6075, U17bb) ជ (6023, U1787) ា (6070, U17b6) ។ (6100, U17d4) , no. of char = 20
អាហាររបស់ខ្មែរឆ្ងាញ់ណាស់។
អ (6050, U17a2) ា (6070, U17b6) ហ (6048, U17a0) ា (6070, U17b6) រ (6042, U179a) រ (6042, U179a) ប (6036, U1794) ស (6047, U179f) ់ (6091, U17cb) ខ (6017, U1781) ្ (6098, U17d2) ម (6040, U1798) ែ (6082, U17c2) រ (6042, U179a) ឆ (6022, U1786) ្ (6098, U17d2) ង (6020, U1784) ា (6070, U17b6) ញ (6025, U1789) ់ (6091, U17cb) ណ (6030, U178e) ា (6070, U17b6) ស (6047, U179f) ់ (6091, U17cb) ។ (6100, U17d4) , no. of char = 25
យើងត្រូវរួមគ្នាថែរក្សាបរិស្ថាន។
យ (6041, U1799) ើ (6078, U17be) ង (6020, U1784) ត (6031, U178f) ្ (6098, U17d2) រ (6042, U179a) ូ (6076, U17bc) វ (6044, U179c) រ (6042, U179a) ួ (6077, U17bd) ម (6040, U1798) គ (6018, U1782) ្ (6098, U17d2) ន (6035, U1793) ា (6070, U17b6) ថ (6032, U1790) ែ (6082, U17c2) រ (6042, U179a) ក (6016, U1780) ្ (6098, U17d2) ស (6047, U179f) ា (6070, U17b6) ប (6036, U1794) រ (6042, U179a) ិ (6071, U17b7) ស (6047, U179f) ្ (6098, U17d2) ថ (6032, U1790) ា (6070, U17b6) ន (6035, U1793) ។ (6100, U17d4) , no. of char = 31
បណ្ឌិតសភាចារ្យជាអ្នកបង្រៀនដ៏ល្អ។
ប (6036, U1794) ណ (6030, U178e) ្ (6098, U17d2) ឌ (6028, U178c) ិ (6071, U17b7) ត (6031, U178f) ស (6047, U179f) ភ (6039, U1797) ា (6070, U17b6) ច (6021, U1785) ា (6070, U17b6) រ (6042, U179a) ្ (6098, U17d2) យ (6041, U1799) ជ (6023, U1787) ា (6070, U17b6) អ (6050, U17a2) ្ (6098, U17d2) ន (6035, U1793) ក (6016, U1780) ប (6036, U1794) ង (6020, U1784) ្ (6098, U17d2) រ (6042, U179a) ៀ (6080, U17c0) ន (6035, U1793) ដ (6026, U178a) ៏ (6095, U17cf) ល (6043, U179b) ្ (6098, U17d2) អ (6050, U17a2) ។ (6100, U17d4) , no. of char = 32
កុំភ្លេចយកឆ័ត្រទៅរៀននៅសាលា។
ក (6016, U1780) ុ (6075, U17bb) ំ (6086, U17c6) ភ (6039, U1797) ្ (6098, U17d2) ល (6043, U179b) េ (6081, U17c1) ច (6021, U1785) យ (6041, U1799) ក (6016, U1780) ឆ (6022, U1786) ័ (6096, U17d0) ត (6031, U178f) ្ (6098, U17d2) រ (6042, U179a) ទ (6033, U1791) ៅ (6085, U17c5) រ (6042, U179a) ៀ (6080, U17c0) ន (6035, U1793) ន (6035, U1793) ៅ (6085, U17c5) ស (6047, U179f) ា (6070, U17b6) ល (6043, U179b) ា (6070, U17b6) ។ (6100, U17d4) , no. of char = 27
```

Print out only Unicode numbers:  
```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ python ./print_codepoint.py khmer.txt --output_type unicode
ខ្ញុំស្រឡាញ់កម្ពុជា។
ខ (U1781) ្ (U17d2) ញ (U1789) ុ (U17bb) ំ (U17c6) ស (U179f) ្ (U17d2) រ (U179a) ឡ (U17a1) ា (U17b6) ញ (U1789) ់ (U17cb) ក (U1780) ម (U1798) ្ (U17d2) ព (U1796) ុ (U17bb) ជ (U1787) ា (U17b6) ។ (U17d4) , no. of char = 20
អាហាររបស់ខ្មែរឆ្ងាញ់ណាស់។
អ (U17a2) ា (U17b6) ហ (U17a0) ា (U17b6) រ (U179a) រ (U179a) ប (U1794) ស (U179f) ់ (U17cb) ខ (U1781) ្ (U17d2) ម (U1798) ែ (U17c2) រ (U179a) ឆ (U1786) ្ (U17d2) ង (U1784) ា (U17b6) ញ (U1789) ់ (U17cb) ណ (U178e) ា (U17b6) ស (U179f) ់ (U17cb) ។ (U17d4) , no. of char = 25
យើងត្រូវរួមគ្នាថែរក្សាបរិស្ថាន។
យ (U1799) ើ (U17be) ង (U1784) ត (U178f) ្ (U17d2) រ (U179a) ូ (U17bc) វ (U179c) រ (U179a) ួ (U17bd) ម (U1798) គ (U1782) ្ (U17d2) ន (U1793) ា (U17b6) ថ (U1790) ែ (U17c2) រ (U179a) ក (U1780) ្ (U17d2) ស (U179f) ា (U17b6) ប (U1794) រ (U179a) ិ (U17b7) ស (U179f) ្ (U17d2) ថ (U1790) ា (U17b6) ន (U1793) ។ (U17d4) , no. of char = 31
បណ្ឌិតសភាចារ្យជាអ្នកបង្រៀនដ៏ល្អ។
ប (U1794) ណ (U178e) ្ (U17d2) ឌ (U178c) ិ (U17b7) ត (U178f) ស (U179f) ភ (U1797) ា (U17b6) ច (U1785) ា (U17b6) រ (U179a) ្ (U17d2) យ (U1799) ជ (U1787) ា (U17b6) អ (U17a2) ្ (U17d2) ន (U1793) ក (U1780) ប (U1794) ង (U1784) ្ (U17d2) រ (U179a) ៀ (U17c0) ន (U1793) ដ (U178a) ៏ (U17cf) ល (U179b) ្ (U17d2) អ (U17a2) ។ (U17d4) , no. of char = 32
កុំភ្លេចយកឆ័ត្រទៅរៀននៅសាលា។
ក (U1780) ុ (U17bb) ំ (U17c6) ភ (U1797) ្ (U17d2) ល (U179b) េ (U17c1) ច (U1785) យ (U1799) ក (U1780) ឆ (U1786) ័ (U17d0) ត (U178f) ្ (U17d2) រ (U179a) ទ (U1791) ៅ (U17c5) រ (U179a) ៀ (U17c0) ន (U1793) ន (U1793) ៅ (U17c5) ស (U179f) ា (U17b6) ល (U179b) ា (U17b6) ។ (U17d4) , no. of char = 27
```

Print out only ordinal numbers:  

```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ python ./print_codepoint.py khmer.txt --output_type ordinal
ខ្ញុំស្រឡាញ់កម្ពុជា។
ខ (6017) ្ (6098) ញ (6025) ុ (6075) ំ (6086) ស (6047) ្ (6098) រ (6042) ឡ (6049) ា (6070) ញ (6025) ់ (6091) ក (6016) ម (6040) ្ (6098) ព (6038) ុ (6075) ជ (6023) ា (6070) ។ (6100) , no. of char = 20
អាហាររបស់ខ្មែរឆ្ងាញ់ណាស់។
អ (6050) ា (6070) ហ (6048) ា (6070) រ (6042) រ (6042) ប (6036) ស (6047) ់ (6091) ខ (6017) ្ (6098) ម (6040) ែ (6082) រ (6042) ឆ (6022) ្ (6098) ង (6020) ា (6070) ញ (6025) ់ (6091) ណ (6030) ា (6070) ស (6047) ់ (6091) ។ (6100) , no. of char = 25
យើងត្រូវរួមគ្នាថែរក្សាបរិស្ថាន។
យ (6041) ើ (6078) ង (6020) ត (6031) ្ (6098) រ (6042) ូ (6076) វ (6044) រ (6042) ួ (6077) ម (6040) គ (6018) ្ (6098) ន (6035) ា (6070) ថ (6032) ែ (6082) រ (6042) ក (6016) ្ (6098) ស (6047) ា (6070) ប (6036) រ (6042) ិ (6071) ស (6047) ្ (6098) ថ (6032) ា (6070) ន (6035) ។ (6100) , no. of char = 31
បណ្ឌិតសភាចារ្យជាអ្នកបង្រៀនដ៏ល្អ។
ប (6036) ណ (6030) ្ (6098) ឌ (6028) ិ (6071) ត (6031) ស (6047) ភ (6039) ា (6070) ច (6021) ា (6070) រ (6042) ្ (6098) យ (6041) ជ (6023) ា (6070) អ (6050) ្ (6098) ន (6035) ក (6016) ប (6036) ង (6020) ្ (6098) រ (6042) ៀ (6080) ន (6035) ដ (6026) ៏ (6095) ល (6043) ្ (6098) អ (6050) ។ (6100) , no. of char = 32
កុំភ្លេចយកឆ័ត្រទៅរៀននៅសាលា។
ក (6016) ុ (6075) ំ (6086) ភ (6039) ្ (6098) ល (6043) េ (6081) ច (6021) យ (6041) ក (6016) ឆ (6022) ័ (6096) ត (6031) ្ (6098) រ (6042) ទ (6033) ៅ (6085) រ (6042) ៀ (6080) ន (6035) ន (6035) ៅ (6085) ស (6047) ា (6070) ល (6043) ា (6070) ។ (6100) , no. of char = 27
```

Print out both ordinal and Unicode numbers:  

```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ python ./print_codepoint.py khmer.txt --output_type unicode --no_print_original
ខ (U1781) ្ (U17d2) ញ (U1789) ុ (U17bb) ំ (U17c6) ស (U179f) ្ (U17d2) រ (U179a) ឡ (U17a1) ា (U17b6) ញ (U1789) ់ (U17cb) ក (U1780) ម (U1798) ្ (U17d2) ព (U1796) ុ (U17bb) ជ (U1787) ា (U17b6) ។ (U17d4) , no. of char = 20
អ (U17a2) ា (U17b6) ហ (U17a0) ា (U17b6) រ (U179a) រ (U179a) ប (U1794) ស (U179f) ់ (U17cb) ខ (U1781) ្ (U17d2) ម (U1798) ែ (U17c2) រ (U179a) ឆ (U1786) ្ (U17d2) ង (U1784) ា (U17b6) ញ (U1789) ់ (U17cb) ណ (U178e) ា (U17b6) ស (U179f) ់ (U17cb) ។ (U17d4) , no. of char = 25
យ (U1799) ើ (U17be) ង (U1784) ត (U178f) ្ (U17d2) រ (U179a) ូ (U17bc) វ (U179c) រ (U179a) ួ (U17bd) ម (U1798) គ (U1782) ្ (U17d2) ន (U1793) ា (U17b6) ថ (U1790) ែ (U17c2) រ (U179a) ក (U1780) ្ (U17d2) ស (U179f) ា (U17b6) ប (U1794) រ (U179a) ិ (U17b7) ស (U179f) ្ (U17d2) ថ (U1790) ា (U17b6) ន (U1793) ។ (U17d4) , no. of char = 31
ប (U1794) ណ (U178e) ្ (U17d2) ឌ (U178c) ិ (U17b7) ត (U178f) ស (U179f) ភ (U1797) ា (U17b6) ច (U1785) ា (U17b6) រ (U179a) ្ (U17d2) យ (U1799) ជ (U1787) ា (U17b6) អ (U17a2) ្ (U17d2) ន (U1793) ក (U1780) ប (U1794) ង (U1784) ្ (U17d2) រ (U179a) ៀ (U17c0) ន (U1793) ដ (U178a) ៏ (U17cf) ល (U179b) ្ (U17d2) អ (U17a2) ។ (U17d4) , no. of char = 32
ក (U1780) ុ (U17bb) ំ (U17c6) ភ (U1797) ្ (U17d2) ល (U179b) េ (U17c1) ច (U1785) យ (U1799) ក (U1780) ឆ (U1786) ័ (U17d0) ត (U178f) ្ (U17d2) រ (U179a) ទ (U1791) ៅ (U17c5) រ (U179a) ៀ (U17c0) ន (U1793) ន (U1793) ៅ (U17c5) ស (U179f) ា (U17b6) ល (U179b) ា (U17b6) ។ (U17d4) , no. of char = 27

```

If you need as output file:  

```
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$ python ./print_codepoint.py khmer.txt --output_type unicode --no_print_original --output code.txt
(base) ye@lst-gpu-3090:~/exp/demo/print_unicode$
```

## 99. [syl_ngram_mi.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/syl_ngram_mi.py)

မြန်မာစာအတွက်က syllable unit တွေက အရေးကြီးတယ်။ Syllable cooccurrence တွေကို ngram အလိုက် ဆွဲထုတ်ဖို့အတွက် ရေးထားတဲ့ python code ပါ။ Information theory ကို အခြေခံတဲ့ mutual information တွက်တဲ့နည်းကို apply လုပ်ထားတယ်။  

### Mutual Information Calculation:

The Mutual Information (MI) of a bigram (or n-gram) measures the amount of information that the presence of one word contributes about the presence of the other. In simpler terms, it tells us how much knowing one word helps in predicting the other.

For a bigram (word1, word2), the Mutual Information is calculated as follows:

1. **Probability of word1 (P(w1))**: The frequency of word1 divided by the total number of words.
2. **Probability of word2 (P(w2))**: The frequency of word2 divided by the total number of words.
3. **Joint Probability of word1 and word2 (P(w1, w2))**: The frequency of the bigram (word1, word2) divided by the total number of bigrams.
4. **MI Score**: The MI score is calculated using the formula:
   
   \[ MI(word1, word2) = \log\frac{P(w1, w2)}{P(w1) \times P(w2)} \]

   Here, log is the natural logarithm. This formula measures how much more often the words co-occur than if they were independent.

--help ခေါ်ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရလိမ့်မယ်။  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ python ./syl_ngram_mi.py --help
usage: syl_ngram_mi.py [-h] [-f FILE] [-n {2,3,4,5,6,7}] [-o OUTPUT] [-c COUNT]

N-Gram Collocation Extraction with Mutual Information (Supports 2 to 7-grams)

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the syllable-segmented corpus file
  -n {2,3,4,5,6,7}, --ngram {2,3,4,5,6,7}
                        Size of the n-gram (2 to 7)
  -o OUTPUT, --output OUTPUT
                        Optional output file to write the collocations
  -c COUNT, --count COUNT
                        Minimum count of co-occurrences to be considered for MI
                        calculation
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$
```

Test run လုပ်ဖို့အတွက် shell script ကို အောက်ပါအတိုင်း ရေးခဲ့တယ်။  

```bash
#!/bin/bash

time python ./syl_ngram_mi.py --file ./segmentation-data-updated2.cleaned.syl \
--ngram 2 --count 3 --output 2gram_c3_mi.txt

time python ./syl_ngram_mi.py --file ./segmentation-data-updated2.cleaned.syl \
--ngram 3 --count 3 --output 3gram_c3_mi.txt

time python ./syl_ngram_mi.py --file ./segmentation-data-updated2.cleaned.syl \
--ngram 4 --count 3 --output 4gram_c3_mi.txt

time python ./syl_ngram_mi.py --file ./segmentation-data-updated2.cleaned.syl \
--ngram 5 --count 3 --output 5gram_c3_mi.txt
```

Test run as follows:  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ ./run.sh

real    0m6.163s
user    0m6.283s
sys     0m1.547s

real    0m8.001s
user    0m8.154s
sys     0m1.700s

real    0m7.942s
user    0m8.203s
sys     0m2.188s

real    0m7.891s
user    0m7.820s
sys     0m1.796s
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$
```

2-gram output ဖိုင်ကို လေ့လာကြည့်ရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ head 2gram_c3_mi.txt
ဟန္တ ဒုန္ဒု: 14.676212467075088
ဒန္နိ မိတ္တံ: 14.676212467075088
ရမ်းစ် ဒေးလ်: 14.388530394623306
ပစ္စုပ္ပန္နာ အဇ္စျတ္တံ: 14.165386843309097
ာ ါ: 14.165386843309097
တင်္ခ ဏုပ္ပတ္တိ: 13.828914606687883
ဝေက္ခိ တဗ္ဗံ: 13.828914606687883
ကုရ် အာန်: 13.605771055373674
ဝေါ့ထ် ဝေါ့ထ်: 13.577600178406977
ပုဏ္ဍ ရိက်: 13.541232534236103
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ tail 2gram_c3_mi.txt
အ ချင်: -5.469481635862199
အ တွေ: -5.490230424997056
အ တော့: -5.8408427049724585
အ တယ်: -5.896372282545035
အ ဒီ: -5.9906562283077385
အ ဘူး: -6.170574156759379
အ လည်း: -6.272625387051672
အ သည်: -6.305896698282836
အ တစ်: -6.410758586441049
အ တဲ့: -6.575146473363342(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$
```

3gram output ဖိုင်ကို လေ့လာကြည့်ရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ head 3gram_c3_mi.txt
ဋိစ္စ သ မုပ္ပါဒ်: 14.16538670235403
သဒ္ဓေါ ပါ ပဂ္ဂ: 14.16538670235403
တော်လ် စ တွိုင်း: 13.983065145560078
ဏှံ ပစ္စ ဝေက္ခိ: 13.828914465732819
အက်ဒ် ဝုဒ် ဝက်ဒ်: 13.577600037451912
ဝတ္တေ ယျ လဗ္ဘေ: 13.184557449342305
ဝဇ္ဇေ န သောတ္ထိ: 13.172134929343748
ဘွေ လပ် ယိန်း: 13.135767285172873
ဒမ္ပိ သံ ဃေ: 12.815459985405015
ဝဏ္ဏိ နော ဣဒ္ဓိ: 12.634991997260384
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ tail 3gram_c3_mi.txt
အ တောက် အ: -8.34688337353481
အ ယုတ် အ: -8.34688337353481
အ ချ အ: -8.34688337353481
အ ကြေး အ: -8.34688337353481
အ ချီး အ: -8.34688337353481
အ ကွယ် အ: -8.34688337353481
အ မြိုက် အ: -8.34688337353481
အ ဖျား အ: -8.34688337353481
အ မြား အ: -8.34688337353481
အ ကျူး အ: -8.34688337353481
```

4gram output ဖိုင်ကို လေ့လာကြည့်ရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ head 4gram_c3_mi.txt
အဇ္စျတ္တံ ဝါ ဗ ဟိဒ္ဓါ: 14.165386561398947
သမ္မပ္ပ ညာ ယ ဒဋ္ဌဗ္ဗံ: 14.165386561398947
ဏှံ ပစ္စ ဝေက္ခိ တဗ္ဗံ: 13.828914324777735
ဒမ္မ သာ ရ ထိံ: 13.376929201034676
နိစ္စာ ဝါ အ နိစ္စာ: 12.98161646439053
ချတ် မာ စ တာစ်: 12.912623592903579
သစ္စ ဝဇ္ဇေ န သောတ္ထိ: 12.804410008263346
သမ္ဗော ဓာ ယ နိဗ္ဗာ: 12.730302036109624
ကမ္မံ ဉာ ဏ ပုဗ္ဗင်္ဂ: 12.624941520451799
ကမ္မံ ဉာ ဏာ ပုဗ္ဗင်္ဂ: 12.624941520451799
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ tail 4gram_c3_mi.txt
အ သင်း ဘုတ် အ: -8.346883514489894
အ ချို့ မှာ အ: -8.346883514489894
အ စား ဆုံး အ: -8.346883514489894
အ လံ တွင် အ: -8.346883514489894
အ လံ ရှိ အ: -8.346883514489894
အ ဘိ ဓာန် အ: -8.346883514489894
အ စ တွင် အ: -8.346883514489894
အ မြု တေ အ: -8.346883514489894
အ သံ ရဲ့ အ: -8.346883514489894
အ လံ ၏ အ: -8.346883514489894
```

5gram output ဖိုင်ကို လေ့လာကြည့်ရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ head 5gram_c3_mi.txt
မိတ္တံ အ ဝ မင်္ဂ လဉ္စ: 14.676212044209832
ပစ္စုပ္ပန္နာ အဇ္စျတ္တံ ဝါ ဗ ဟိဒ္ဓါ: 14.165386420443841
ဣန္ဒ နာ မာ မ ဟဗ္ဗ: 13.605770632508419
သစ္စန္တိ မေ ဘိက္ခ ဝေ ပုဗ္ဗေ: 13.066774131775732
တဗ္ဗန္တိ မေ ဘိက္ခ ဝေ ပုဗ္ဗေ: 13.066774131775732
မီးစ် ရို ဒ ရီ ဂွက်ဇ်: 13.027553418622452
သန္နိ ပ တိ တာ ဟောန္တိ: 13.002235610638161
ဿု ပိ နံ အ ကန္တံ: 12.941610988821726
ပုဗ္ဗေ အ န နု ဿု: 12.718467437507517
ဇု တိ မန္တော ဝဏ္ဏ ဝန္တော: 12.614789008032675
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ tail 5gram_c3_mi.txt
အ ရန် သ င့် အ: -8.346883655445
အ မြင့် မား ဆုံး အ: -8.346883655445
အ မေ ရိ က အ: -8.346883655445
အ ချိတ် အ ဆက် အ: -8.346883655445
အ လံ တော် ရှိ အ: -8.346883655445
အ ရောင် ဖြစ် သော အ: -8.346883655445
အ နား များ တွင် အ: -8.346883655445
အ လုပ် အ ကျွေး အ: -8.346883655445
အ ဘယ် ရွာ နေ အ: -8.346883655445
အ ရောင် ပုံ သဏ္ဌာန် အ: -8.346883655445
```

Python code ထဲမှာက 7-gram အထိ support လုပ်ထားတယ်။ အောက်ပါ အတိုင်း coding လုပ်ထားတယ်။  

```python
    for ngram in ngram_fd:
        if 2 <= len(ngram) <= 7 and ngram_fd[ngram] >= min_count:
            score = mutual_information_score(word_fd, ngram_fd, total_ngrams, ngram)
            collocations[ngram] = score
```

syllable ngram pair တွေကို ဆွဲထုတ်ပြီး output ထွက်လာတဲ့ဖိုင်တွေရဲ့ size ကို နှိုင်းယှဉ်ကြည့်ရင် အောက်ပါအတိုင်း ရတယ်။  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ wc *gram_c3*txt
  163829   491490  6918570 2gram_c3_mi.txt
  415352  1661412 20957724 3gram_c3_mi.txt
  381016  1905085 22405431 4gram_c3_mi.txt
  244918  1469514 16578552 5gram_c3_mi.txt
 1205115  5527501 66860277 total
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$
```

တကယ်လို့ count တန်ဖိုးကို မကန့်သတ်ဘူး ဆိုရင် count=1 ကနေ စယူမှာမို့ ထွက်လာတဲ့ ဖိုင်တွေရဲ့ size က ပိုကြီးလိမ့်မယ်။ ကိုယ်က ဘာလုပ်ချင်တာလဲဆိုတဲ့ NLP task အပေါ်ကို မူတည်ပြီးတော့ ngram value နဲ့ count ကို ကစားပါ။  

```
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$ wc *gram_mi.txt
   364950   1094853  15695346 2gram_mi.txt
  1977491   7909968 102251276 3gram_mi.txt
  3860349  19301750 233980848 4gram_mi.txt
  5059678  30358074 353671348 5gram_mi.txt
 11262468  58664645 705598818 total
(base) ye@lst-gpu-3090:~/exp/demo/mutual_info$
```

## 100. [txt_dl.py](https://github.com/ye-kyaw-thu/tools/blob/master/python/txt_dl.py)

text web mining လုပ်ဖို့အတွက် ရေးခဲ့တဲ့ python code ပါ။ မြန်မာစာ စာကြောင်းတွေထဲကနေ ကိုယ်ဆွဲထုတ်ယူချင်တဲ့ keyword စာလုံးကို သတ်မှတ်ပြီး ဆွဲထုတ်လို့ ရဖို့ ရည်ရွယ်တယ်။ တခုရှိတာက website အပေါ်ကို မူတည်ပြီး extract လုပ်ဖို့ အခက်အခဲရှိတာတွေလည်း ရှိပါတယ်။ နောက် သတိထားရမှာက အဲဒီလို mining လုပ်ပြီး ယူထားတဲ့ စာကြောင်းတွေကို သုံးတဲ့အခါမှာ copyright ကိစ္စတို့ commercial အတွက် ခွင့်ပြု/မပြုတဲ့ ကိစ္စတို့ကိုတော့ ကိုယ်တိုင် တာဝန်ယူရပါလိမ့်မယ်။   

ထုံးစံအတိုင်း command line argument တွေကို လေ့လာဖို့အတွက်က --help ခေါ်ကြည့်ပါ။  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ python ./txt_dl.py --help
usage: txt_dl.py [-h] (--url URL | --url_file URL_FILE) --keyword KEYWORD
                 [--num_sentences NUM_SENTENCES] [--output_filename OUTPUT_FILENAME]

Download sentences from webpages containing a specific keyword.

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL of the webpage to scrape
  --url_file URL_FILE   File containing URLs to scrape, one per line
  --keyword KEYWORD     Keyword to search in sentences
  --num_sentences NUM_SENTENCES
                        Number of sentences to return
  --output_filename OUTPUT_FILENAME
                        File to save the downloaded sentences (optional, prints to
                        stdout if not specified)
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$
```

ဥပမာ အနေနဲ့ "တိုက်ပွဲ" ဆိုတဲ့ keyword နဲ့ BBC Burmese website ကနေ ဆွဲထုတ်ကြည့်ရင် အောက်ပါလိုမျိုး ရတယ်။  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ python ./txt_dl.py --url "https://bbc.com/burmese" --keyword "တိုက်ပွဲ" --num_sentences 5
လွန်ခဲ့သော တစ်နာရီ က၁၀၂၇ စစ်ဆင်ရေး ရက်စွဲမှတ်တမ်းရှမ်းမြောက်က ၁၀၂၇ စစ်ဆင်ရေးနဲ့ပတ်သက်ပြီး အဓိကကျတဲ့နေ့ရက်တွေအကြောင်း ရုပ်မြင်အထူးပြုလုပ်ချက်နဲ့စုစည်းတင်ဆက်မှု ၁၃ နိုဝင်ဘာ ၂၀၂၃ရခိုင်တိုက်ပွဲ အေအေ ဘာပြောလဲရသေ့တောင်မြို့ထဲကနေရာအချို့နဲ့ မင်းပြားမြို့နယ်ထဲ တိုက်ပွဲတွေဖြစ်နေပြီး ရသေ့တောင်က တပ်စခန်းအချို့ကိုသိမ်းပိုက်ရရှိထားတယ်လို့ ‌ရက္ခိုင့်တပ်တော်(အေအေ)ပြောခွင့်ရ ခိုင်သုခက ဘီဘီစီကို အတည်ပြုပါတယ်
၁၃ နိုဝင်ဘာ ၂၀၂၃နိုဝင်ဘာ ၁၃ ရက် ထိပ်တန်းသတင်းများ - တိုက်ပွဲဆက်ပြင်းထန်နေတဲ့ လွိုင်ကော်မှာ အရပ်သားတွေပိတ်မိနေဆဲ ပြီးခဲ့တဲ့ရက်ပိုင်းက ရန်ကုန်အပါအဝင်မြို့ကြီးအချို့မှာ စက်သုံးဆီပြတ်လပ်တာကြုံတွေ့ခဲ့ရပြီးနောက်မှာပဲ  စက်သုံးဆီသင်္ဘောတွေဆိုက်ကပ်လာပြီဖြစ်တယ်လို့ စစ်ကောင်စီဘက်က ပြောလာပါတယ်

၁၂ နိုဝင်ဘာ ၂၀၂၃“တပ်ကိုတပ်နဲ့တူအောင်တည်ဆောက်ပြီး စစ်ကိုစစ်နဲ့တူအောင်တိုက်ခိုက်မယ်” - မန္တလေး PDF ကွပ်ကဲရေးမှူးမန္တလေး PDF ဟာ ၁၀၂၇ စစ်ဆင်ရေးရဲ့ ရှမ်းပြည်နယ်မြောက်ပိုင်းက ထိုးစစ်တိုက်ပွဲတွေဆီ စစ်ကူသွားဖို့ စစ်ကောင်စီတပ်ဖြတ်သန်းရတဲ့ မိုးကုတ်
 ဂါဇာက နောက်ဆုံးအခြေအနေ ... စတဲ့ နိုဝင်ဘာလ ၁၂ ရက်ညပိုင်းနိုင်ငံတကာသတင်းများ ၁၂ နိုဝင်ဘာ ၂၀၂၃နိုဝင်ဘာ ၁၂ ရက်ထိပ်တန်းသတင်းများ - ကွမ်းလုံမြို့ကို MNDAA သိမ်းပိုက်ဗမာပြည်ကွန်မြူနစ်ပါတီနဲ့ တိုက်ခဲ့တဲ့ နာမည်ကျော် ‘‘ကွမ်းလုံ ရက် ၄၀ တိုက်ပွဲ’’ပြီးကတည်းက နှစ်ပေါင်း ငါးဆယ်ကျော်ထိန်းချုပ်နိုင်ခဲ့တဲ့အရေးပါတဲ့ကွမ်းလုံကြိုးတံတားကို မြန်မာစစ်တပ်က လက်လွှတ်လိုက်ရတာပဲဖြစ်ပါတယ်
 ၁၁ နိုဝင်ဘာ ၂၀၂၃အထူးစာမျက်နှာ၉၉ တပ်မမှူး သေဆုံးမှု ဘာတွေထူးခြားလဲ၈ နိုဝင်ဘာ ၂၀၂၃လောက်ကိုင် - တိုက်ပွဲတွေဝန်းရံနေတဲ့မြို့ ၈ နိုဝင်ဘာ ၂၀၂၃၁၀ ရက်အတွင်း စစ်ကောင်စီ လက်လွှတ်လိုက်ရတဲ့နယ်မြေတိုးလာတဲ့ မြောက်ပိုင်းအခြေအနေ၆ နိုဝင်ဘာ ၂၀၂၃အီလွန်မတ်စ်ခ်ကို  အေအိုင်အကြောင်း ယူကေဝန်ကြီးချုပ် မေးမြန်းခန်း၄ နိုဝင်ဘာ ၂၀၂၃ဟက်ဇ်ဘိုလာတပ် ဘယ်လောက် အင်အားကြီးလဲ
```

စကရင်မှာ ရိုက်ပြတာမျိုးကို မလိုချင်ပဲ output ဖိုင်တစ်ဖိုင် အနေနဲ့ သိမ်းဆည်းချင်ရင် --output_file ဆိုတဲ့ argument ကို သုံးပါ။  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ python ./txt_dl.py --url "https://bbc.com/burmese" --keyword "တိုက်ပွဲ" --num_sentences 5 --output_file result.txt
```

output ဖိုင်ထဲမှာ သိမ်းပေးထားတာကို confirm လုပ်ကြည့်ရင် အောက်ပါအတိုင်း မြင်ရပါလိမ့်မယ်။  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ cat result.txt
လွန်ခဲ့သော တစ်နာရီ က၁၀၂၇ စစ်ဆင်ရေး ရက်စွဲမှတ်တမ်းရှမ်းမြောက်က ၁၀၂၇ စစ်ဆင်ရေးနဲ့ပတ်သက်ပြီး အဓိကကျတဲ့နေ့ရက်တွေအကြောင်း ရုပ်မြင်အထူးပြုလုပ်ချက်နဲ့စုစည်းတင်ဆက်မှု ၁၃ နိုဝင်ဘာ ၂၀၂၃ရခိုင်တိုက်ပွဲ အေအေ ဘာပြောလဲရသေ့တောင်မြို့ထဲကနေရာအချို့နဲ့ မင်းပြားမြို့နယ်ထဲ တိုက်ပွဲတွေဖြစ်နေပြီး ရသေ့တောင်က တပ်စခန်းအချို့ကိုသိမ်းပိုက်ရရှိထားတယ်လို့ ‌ရက္ခိုင့်တပ်တော်(အေအေ)ပြောခွင့်ရ ခိုင်သုခက ဘီဘီစီကို အတည်ပြုပါတယ်
၁၃ နိုဝင်ဘာ ၂၀၂၃နိုဝင်ဘာ ၁၃ ရက် ထိပ်တန်းသတင်းများ - တိုက်ပွဲဆက်ပြင်းထန်နေတဲ့ လွိုင်ကော်မှာ အရပ်သားတွေပိတ်မိနေဆဲ ပြီးခဲ့တဲ့ရက်ပိုင်းက ရန်ကုန်အပါအဝင်မြို့ကြီးအချို့မှာ စက်သုံးဆီပြတ်လပ်တာကြုံတွေ့ခဲ့ရပြီးနောက်မှာပဲ  စက်သုံးဆီသင်္ဘောတွေဆိုက်ကပ်လာပြီဖြစ်တယ်လို့ စစ်ကောင်စီဘက်က ပြောလာပါတယ်

၁၂ နိုဝင်ဘာ ၂၀၂၃“တပ်ကိုတပ်နဲ့တူအောင်တည်ဆောက်ပြီး စစ်ကိုစစ်နဲ့တူအောင်တိုက်ခိုက်မယ်” - မန္တလေး PDF ကွပ်ကဲရေးမှူးမန္တလေး PDF ဟာ ၁၀၂၇ စစ်ဆင်ရေးရဲ့ ရှမ်းပြည်နယ်မြောက်ပိုင်းက ထိုးစစ်တိုက်ပွဲတွေဆီ စစ်ကူသွားဖို့ စစ်ကောင်စီတပ်ဖြတ်သန်းရတဲ့ မိုးကုတ်
 ဂါဇာက နောက်ဆုံးအခြေအနေ ... စတဲ့ နိုဝင်ဘာလ ၁၂ ရက်ညပိုင်းနိုင်ငံတကာသတင်းများ ၁၂ နိုဝင်ဘာ ၂၀၂၃နိုဝင်ဘာ ၁၂ ရက်ထိပ်တန်းသတင်းများ - ကွမ်းလုံမြို့ကို MNDAA သိမ်းပိုက်ဗမာပြည်ကွန်မြူနစ်ပါတီနဲ့ တိုက်ခဲ့တဲ့ နာမည်ကျော် ‘‘ကွမ်းလုံ ရက် ၄၀ တိုက်ပွဲ’’ပြီးကတည်းက နှစ်ပေါင်း ငါးဆယ်ကျော်ထိန်းချုပ်နိုင်ခဲ့တဲ့အရေးပါတဲ့ကွမ်းလုံကြိုးတံတားကို မြန်မာစစ်တပ်က လက်လွှတ်လိုက်ရတာပဲဖြစ်ပါတယ်
 ၁၁ နိုဝင်ဘာ ၂၀၂၃အထူးစာမျက်နှာ၉၉ တပ်မမှူး သေဆုံးမှု ဘာတွေထူးခြားလဲ၈ နိုဝင်ဘာ ၂၀၂၃လောက်ကိုင် - တိုက်ပွဲတွေဝန်းရံနေတဲ့မြို့ ၈ နိုဝင်ဘာ ၂၀၂၃၁၀ ရက်အတွင်း စစ်ကောင်စီ လက်လွှတ်လိုက်ရတဲ့နယ်မြေတိုးလာတဲ့ မြောက်ပိုင်းအခြေအနေ၆ နိုဝင်ဘာ ၂၀၂၃အီလွန်မတ်စ်ခ်ကို  အေအိုင်အကြောင်း ယူကေဝန်ကြီးချုပ် မေးမြန်းခန်း၄ နိုဝင်ဘာ ၂၀၂၃ဟက်ဇ်ဘိုလာတပ် ဘယ်လောက် အင်အားကြီးလဲ
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$
```

တကယ်လို့ ကိုယ်က url ကို တစ်ခုထက်မကဆီက မြန်မာစာ စာကြောင်းတွေကို extract လုပ်ချင်တယ် ဆိုရင်တော့၊ ဖိုင်တစ်ဖိုင်မှာ url တွေကို စာကြောင်းတစ်ကြောင်းမှာ url address တစ်ခုစီ တန်းစီရိုက်ထည့်ထားပြီး အဲဒီဖိုင်ကို အသုံးပြုပြီးလည်း mining လုပ်လို့ ရအောင် coding လုပ်ပေးထားပါတယ်။  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ cat url_file.txt
https://my.wikipedia.org/wiki/%E1%80%A1%E1%80%91%E1%80%B0%E1%80%B8:%E1%80%85%E1%80%AC%E1%80%99%E1%80%BB%E1%80%80%E1%80%BA%E1%80%94%E1%80%BE%E1%80%AC%E1%80%A1%E1%80%AC%E1%80%B8%E1%80%9C%E1%80%AF%E1%80%B6%E1%80%B8/%E1%80%90
https://bbc.com/burmese
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$
```

url file ကို သုံးပြီး mining လုပ်တဲ့ Example running က အောက်ပါအတိုင်းပါ။  
```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ python ./txt_dl.py --url_file ./url_file.txt --key "တက် --num_sentences 10 --output_file result2.txt
```

output file ကို စစ်ကြည့်ရအောင် ...  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ cat ./result2.txt
 ကျိုက်ထိုမြို့နယ်
တကဲအုချိ ယူးကို
တက္ကစီ
တက္ကဆက်ပြည်နယ်
တက္ကဆပ် ကန်းထရီးဂီတ
တက္ကဆပ်ပြည်နယ်
တက္ကဆပ်သမ္မတနိုင်ငံ
တက္ကနက်တီယမ်
တက္ကပဏ္ဍိတဇာတ်
တက္ကလဇာတ်
တက္ကသိုလ်
တက္ကသိုလ် ကျောင်းသားများ သမဂ္ဂ
တက္ကသိုလ် ခင်မောင်ဇော်
တက္ကသိုလ် နေဝင်း
တက္ကသိုလ် ပညာပဒေသာစာစောင်
တက္ကသိုလ် မြတ်စိုး
တက္ကသိုလ် လှကြွယ်
တက္ကသိုလ်ကြယ်ပွင့်
တက္ကသိုလ်စိန်တင်
တက္ကသိုလ်စိုး
တက္ကသိုလ်ဆုမြိုင်
တက္ကသိုလ်တင်ခ
တက္ကသိုလ်တင်မြင့်
တက္ကသိုလ်ထင်ကြီး
တက္ကသိုလ်ထွန်းနောင်
တက္ကသိုလ်နန္ဒမိတ်
တက္ကသိုလ်နန္ဒမိတ် စာ‌ရေးဆရာ
တက္ကသိုလ်နေဝင်း
တက္ကသိုလ်နှင်းဝေ
တက္ကသိုလ်ပြည်
တက္ကသိုလ်ဘုန်းနိုင်
တက္ကသိုလ်မင်းမော်
တက္ကသိုလ်မောင်မောင်ကြီး
တက္ကသိုလ်များ ဘောလုံးအသင်း
တက္ကသိုလ်များ​ သမိုင်း​ သု​တေသန ဌာန
တက္ကသိုလ်မြစိမ်း
တက္ကသိုလ်လှ(မောင်မောင်လှ)
တက္ကသိုလ်ဝင်တန်းစာမေးပွဲ
တက္ကသိုလ်ဝင်း
တက္ကသိုလ်ဝင်းမွန်
တက္ကသီလာ
တက်ကဆပ်ပြည်နယ်
တက်ကပ်မှာ ပညာ
 ဆုတ်ကပ်မှာ ဥစ္စာ
တက်ကော့ရွာ
တက်ကော့ရွာ
 ရမ်းဗြဲငယ်ချောင်းဖျား
တက်ကျမ်း
တက်ကျသံ
တက်ကျသံဘာသာစကား
တက်ကြွထက်သန်သူများ
တက်ခက်ရွာ
 ဟုမ္မလင်းမြို့နယ်
တက်ခလေး (မြောက်)ရွာ
 ပဲခူးမြို့နယ်
တက်ခိုမြို့
 အအိုမိုရိ
တက်ခေါင်းရွာ
 ဒီပဲယင်းမြို့နယ်
တက်ခ်တိုင်ဘာဟီ
တက်ဂျမဟာ သင်းချိုင်းဂူ
တက်စည်ရွာ
 နွားထိုးကြီးမြို့နယ်
တက်စမေးနီးယား
တက်စမေးနီးယား တောရိုင်းမြေ ကမ္ဘာ့အမွေအနှစ်ဒေသ
တက်စမေးနီးယားကျွန်း
တက်စမေးနီးယားပြည်နယ်
တက်စိန်
တက်စီဒါမီအတတ်
တက်စ်ဆေးလီး နာဂျဲ
တက်စ်မန်ပင်လယ်
တက်ဆက်ပြည်နယ်
တက်ဆိပ်ရွာ
 တက်ဆိပ်
တက်ဆိပ်ရွာ
 ဘိုးတီလွတ်
တက်ဆိပ်ရွာ
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$
```

တစ်ခုသတိထားရမှာက --url နဲ့ --url_file option နှစ်ခုစလုံးကိုတော့ ရောပြီး သုံးလို့ မရပါဘူး။ အောက်ပါလိုမျိုး error message ပေးပါလိမ့်မယ်။  

```
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$ python ./txt_dl.py -"--url "https://bbc.com/burmese" --key"တက်" --url_file ur_file.txt --num_sentences 5--output_file result2.txt
usage: txt_dl.py [-h] (--url URL | --url_file URL_FILE) --keyword KEYWORD
                 [--num_sentences NUM_SENTENCES] [--output_filename OUTPUT_FILENAME]
txt_dl.py: error: argument --url_file: not allowed with argument --url
(base) ye@lst-gpu-3090:~/exp/demo/data_mining$
```

## Next Program  

```

```

```

```

```

```

```

```

```

```
