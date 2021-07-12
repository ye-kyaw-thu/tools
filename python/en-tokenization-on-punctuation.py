import sys
import argparse

# တကယ်က word_tokenize() function က TreebankWordTokenizer class ကိုပဲ
# ခေါ်သုံးထားတဲ့ wrapper function ပါ။
#from nltk.tokenize import word_tokenize 

# ဒီတစ်ခါတော့ TreebankWordTokenizer class ကိုပဲ တန်းခေါ်ပြီး သုံးပါမယ်။
# tokenized output က word_tokenize() ကို ခေါ်သုံးတာနဲ့ အတူတူပဲ ဖြစ်ပါလိမ့်မယ်။
from nltk.tokenize import TreebankWordTokenizer

# အောက်ပါ WordPunctTokenizer ကတော့ punctuation သင်္ကေတတွေ အားလုံးကို token တစ်ခုစီအနေနဲ့ ဖြတ်ပေးမှာ ဖြစ်ပါတယ်။
from nltk.tokenize import WordPunctTokenizer

# word tokenizing for English with NLTK library
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 12 July 2021
# Reference: Python 3 Text Processing with NLTK 3 Cookbook
# NLTK စာအုပ်ထဲမှာက PunktWordTokenizer အကြောင်းကိုပါ ဆွေးနွေးထားပေမဲ့ နောက်ပိုင်း NLTK version တွေမှာ အဲဒီကောင်က မပါတော့ပါဘူး...
# Reference: https://stackoverflow.com/questions/44238864/importerror-cannot-import-name-punktwordtokenizer/53923708

# How to run:
# $ echo "Don't do it! I can't stand it!" | python ./en-tokenization-on-punctuation.py

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textLines=args.inputFile.readlines()

tb_tokenizer = TreebankWordTokenizer()
wp_tokenizer = WordPunctTokenizer()

count=0
for line in textLines:
   count +=1
   print("Treebank: ", tb_tokenizer.tokenize(line))
   print("WordPunct", wp_tokenizer.tokenize(line))   

