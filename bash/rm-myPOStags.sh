#!/bin/bash

# removing myPOS tags
# myPOS link: https://github.com/ye-kyaw-thu/myPOS
#head -n 3 mypos.test
#ဆယ် /tn ရာခိုင်နှုန်း /n ဈေး /n လျှော့ /v ပေး /part ရင် /conj ဝယ် /v မယ် /ppm ။ /punc
#ယခု /n လ /n ၏ /ppm အထိမ်းအမှတ် /n ပန်း /n မှာ /ppm မြတ်လေးပန်း /n Pomeacoccinea /fw ဖြစ် /v သည် /ppm ။ /punc
#ကရင် /n ဗမာ /n အဓိကရုဏ်း /n သည် /ppm သူ့ /pron အား /ppm များ /adj စွာ /part ဒေါမနဿ /n ဖြစ် /v စေ /part ပါ /part သည် /ppm ။ /punc
### After running ./rm-myPOStags.sh
#head -n 3 mypos.test.rmtag 
#ဆယ် ရာခိုင်နှုန်း ဈေး လျှော့ ပေး ရင် ဝယ် မယ် ။
#ယခု လ ၏ အထိမ်းအမှတ် ပန်း မှာ မြတ်လေးပန်း Pomeacoccinea ဖြစ် သည် ။
#ကရင် ဗမာ အဓိကရုဏ်း သည် သူ့ အား များ စွာ ဒေါမနဿ ဖြစ် စေ ပါ သည် ။

# Written by Ye, LST Lab., NECTEC, Thailand
# How to run: ./rm-myPOStags.sh

 cat ./mypos.test | sed "s/\/n \|\/part \|\/ppm \|\/v \|\/punc \| \/punc\|\/conj \|\/adj \|\/num \|\/adv \|\/pron \|\/tn \|\/fw \|\/abb \|\/sb \|\/int //g;" > mypos.test.rmtag

