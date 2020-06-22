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
