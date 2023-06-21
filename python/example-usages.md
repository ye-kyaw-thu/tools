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


