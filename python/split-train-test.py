"""
 splitting parallel data into training data and test data
 written by Ye Kyaw Thu, LST, NECTEC, Thailand
 last updated date: 13 Feb 2022
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split

# ခွဲပြီးထွက်လာတဲ့ training, test ဖိုင်တွေကို train-test_data ဆိုတဲ့ folder အောက်မှာ သိမ်းချင်လို့ ဒေတာ path ကို define လုပ်တာ  
data_dir = './train-test_data'
# train-test_data ဆိုတဲ့ folder က လက်ရှိ path မှာ မရှိသေးရင် directory အသစ်တစ်ခု ဆောက်ပေးပါလိမ့်မယ်။  
if not os.path.isdir(data_dir):
   os.makedirs(data_dir)

# parallel corpus ဖိုင်နာမည်ပါ။  
# input parallel corpus ဖိုင်က language တစ်ခုချင်းစီရဲ့ စာကြောင်းတွေကို TAB ခြားပြီး သိမ်းထားပေးရပါမယ်။  
# ဥပမာ မြန်မာ-အင်္ဂလိပ်-ဂျပန် သုံးဘာသာအတွက် parallel corpus ဆိုရင် အောက်ပါလိုမျိုး
# နေကောင်းလား<TAB>How are you?<TAB>元気ですか？
# Note: <TAB> ဆိုတာက မြင်သာအောင် ရိုက်ပြထားတာ၊ တကယ်တမ်းက TAB key ကိုနှိပ်ပြီး ခြားထားရမှာ။ TAB မဟုတ်ရင်လည်း ကော်မာ "," နဲ့လည်း ခြားလို့ ရပါတယ်။  
data_path = './data.tsv'

# panda library ရဲ့ read_csv ကို သုံးပြီး ./data.tsv ဖိုင်ကို ဖတ်ယူပြီး dataframe ဆိုတဲ့ variable ထဲကို သိမ်းခိုင်းတာ။  
# field တစ်ခုနဲ့ တစ်ခုစီကို ခြားထားတာက TAB မို့လို့ '\t' လို့ ရေးထားတာ။  
dataframe = pd.read_csv(data_path, sep='\t')

# train_test_split ဆိုတဲ့ function ကို သုံးပြီး ရလာတဲ့ training data က train ဆိုတဲ့ variable ထဲမှာ သိမ်းမယ်။
# test data က test ဆိုတဲ့ variable မှာ သိမ်းမယ်။ 
# test_size=0.2 ဆိုတာက 20% ကို test set အဖြစ် ထားမယ်လို့ သတ်မှတ်တာ။ train_size တည်ပြီး ပြောရင်လည်း ရတယ်။  
# random_state=42 ဆိုတာက random generator ရဲ့ seed ကို 42 ဆိုပြီး သတ်မှတ်ထားတာပါ။ ကြိုက်တဲ့ ဂဏန်းပေးလို့ ရပါတယ်။ 
# အဲဒီလို seed ကို သတ်မှတ်ထားတော့ နောက်ပိုင်း shuffle ထပ်လုပ်ပြီး တူတဲ့ ဒေတာကို ပြန်လုပ်ယူလို့တာပေါ့။ မဟုတ်ရင် shuffle တစ်ခါလုပ်ရင် တစ်ခါ ပြောင်းနေမှာလေ။ 
# shuffle=True ဆိုတာက train, test အနေနဲ့ မခွဲခင်မှာ အရင်ဆုံး shuffle လုပ်ပေးပါ ကျပန်းမွှေပေးပါလို့ ခိုင်းထားတာပါ။ မလိုအပ်ရင် False လုပ်ပါ။  
train, test = train_test_split(dataframe, test_size=0.2, random_state=42, shuffle=True)

# train.tsv ဖိုင်နဲ့ test.tsv ဖိုင်တွေကို သိမ်းဖို့ path တွေကို သတ်မှတ်တာပါ။
# string နှစ်ခုကို ဆက်တာမို့လို့ + ကို သုံးထားပါတယ်။
# data_dir က အထက်မှာ './train-test_data' ဆိုပြီး သတ်မှတ်ထားတာမို့ train_path = './train-test_data/train.tsv' ဖြစ်ပြီးတော့၊ 
# test_path ကတော့ './train-test_data/test.tsv' ဆိုတဲ့ string တွေ ဖြစ်သွားမှာပါ။  
train_path = data_dir + '/train.tsv'
test_path = data_dir + '/test.tsv'

# ဖိုင်တွေကို save လုပ်တဲ့ အပိုင်းပါ။  
# index=False ဆိုတာက ရေးပေးမဲ့ ဖိုင်အသစ်တွေ (i.e. output files) မှာ index ကော်လံ တစ်ခုအပို ပါလာမှာကို မလိုချင်လို့ပါ။  
train.to_csv(train_path, sep='\t', index=False)
test.to_csv(test_path, sep='\t', index=False)


