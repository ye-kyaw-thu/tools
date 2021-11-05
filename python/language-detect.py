"""
languge detection with googletrans
written by Ye Kyaw Thu, LST, NECTEC, Thailand
Date: 5 Nov 2021
"""

import numpy as np
from googletrans import Translator


# googletrans library ကို သုံးပြီး input string ရဲ့ ဖြစ်နိုင်တဲ့ ဘာသာစကားကို detect လုပ်တဲ့ function
# return value က string ဒါမဟုတ် nan
def detect_lang(x):
    translate = Translator()
    try:
        return translate.detect(x).lang
    except:
        return np.nan
         
# testing with Myanmar or Burmese sentence         
print('input: နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။')
language=detect_lang('နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။')   
print('language: ', language)

# testing with Japanese sentence
print('\ninput: 元気です。毎日働いています。') 
language=detect_lang('元気です。毎日働いています。')   
print('language: ', language)

# testing with English sentence containing Romanized Myanmar name
print('\ninput: My name is Ye Kyaw Thu.')   
language=detect_lang('My name is Ye Kyaw Thu.')   
print('language: ', language)

# testing with Thai sentence
print('\ninput: กระดาษสีถ่ายเอกสาร 1 A4 80 แกรม ฟ้า 500 แผ่น')
language=detect_lang('กระดาษสีถ่ายเอกสาร 1 A4 80 แกรม ฟ้า 500 แผ่น')
print('language: ', language)

# testing with Myanmar+Japanese sentence
print('\ninput: နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။ 元気です。毎日働いています。')   
language=detect_lang('နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။ 元気です。毎日働いています。')   
print('language: ', language)

# testing with Japanese+Myanmar sentence
print('\ninput: 元気です。毎日働いています。နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။')
language=detect_lang(' 元気です。毎日働いています。နေကောင်းတယ်။ နေ့တိုင်း အလုပ်လုပ်တယ်။')   
print('language: ', language)

# testing with Kachin sentence
print('\ninput: N dai tsi n tsin hpe tsi gawk kaw sa shaw la u.')   
language=detect_lang('N dai tsi n tsin hpe tsi gawk kaw sa shaw la u.')   
print('language: ', language)

# testing with Rawang sentence
print('\ninput: NÀ HPÀRVT LĒGA TÌQCVNG SĒ GØ̀ MĒRØ DAQ Ó .')   
language=detect_lang('NÀ HPÀRVT LĒGA TÌQCVNG SĒ GØ̀ MĒRØ DAQ Ó .')   
print('language: ', language)

# testing with Rawang sentence
print('\ninput: အဲဝယ်ဟှား ခံဗျား ဟှို အဲဇာ ပေး ဟှို့ မှုဝ ။')   
language=detect_lang('အဲဝယ်ဟှား ခံဗျား ဟှို အဲဇာ ပေး ဟှို့ မှုဝ ။')   
print('language: ', language)
