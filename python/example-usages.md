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

[audio_exploration library](https://github.com/phrasenmaeher/audio_exploration) ကို သုံးဖို့ ပြင်ခဲ့တဲ့ python script ပါ။ script ထဲမှာ assign လုပ်ထားတဲ့ path ကနေ full path အားလုံးကို ဆွဲထုတ်ပြီး၊ folder path ကို Python dictionary key အဖြစ်ထားပြီး အဲဒီအောက်က filename တွေကို value list အဖြစ်ထားပေးတဲ့ dictionary creation ပရိုဂရမ်ပါ။  

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
<img src="https://github.com/ye-kyaw-thu/tools/blob/master/python/pic/audio-exploration-combined.png" alt="drawing" width="1200"/>  
</p>  
<div align="center">
  Fig. Exploring audio datasets with Streamlit and audio_exploration github code  
</div>   

