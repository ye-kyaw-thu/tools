from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import sys
import pandas as pd
import re
import numpy as np
from numpy import array
import itertools
from numpy import argmax

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# example code for syllable to one-hot encoding (for using as an embedding tool)
# Last updated: 28 Sept 2022
# How to run:
# $ python ./syl2onehot-sklearn.py ./eg-corpus.txt

# References
# https://github.com/gearmonkey/tfidf-python/blob/master/tfidf.py
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
# https://stackoverflow.com/questions/69218610/onehotencoder-expected-2d-array-got-1d-array-instead
# https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
# https://github.com/yashu-seth/dummyPy

# syllable breaking လုပ်ပေးမယ့် function ပါ
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

# argument 1 အဖြစ် ပေးလိုက်တဲ့ ဖိုင်ကို ဖွင့်ပြီး စာကြောင်း တစ်ကြောင်းချင်းစီကို
# corpus ဆိုတဲ့ list ထဲမှာ သိမ်း
with open(sys.argv[1]) as f:
    corpus = []
    for line in f:
        corpus.append(line.rstrip())
#print(corpus)
#print(type(corpus))

# ဒီ function က corpus list ထဲမှာ ရှိတဲ့ list တစ်ခုချင်းစီကို looping ပတ်ပြီးတော့
# sylbreak_my function ကို ပို့ပေးပြီးတော့ syllable unit ဖြတ်ခိုင်းတဲ့ function ပါ
def list_sylbreak(pass_corpus):
   corpus_syl = []
   for line in pass_corpus:
      corpus_syl.append(sylbreak_my(line))
   return corpus_syl

corpus_syl = list_sylbreak(corpus)

#Extract values from syllable breaked corpus list
#Flatten the list by using itertools
#(FYI: faster than "list comprehension" and "iterate over the list of lists")
syllables = list(itertools.chain(*corpus_syl))

#Label encoding or encoding for all syllables
label_encoder = LabelEncoder()
syllables = array(syllables)
integer_encoded = label_encoder.fit_transform(syllables)

#One-Hot Encoding
onehot_encoder = OneHotEncoder(sparse='False')
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded).toarray()

for input_sentence in corpus_syl:
   # input စာကြောင်းကိုပါ တွဲပြီး ရိုက်ထုတ်ပြမှ လူအတွက်က ကြည့်ရအဆင်ပြေလို့
   #print("input sentence: ", input_sentence)

   nparray_string = np.empty(onehot_encoded[0, :].shape, dtype=int)
   #print("nparray_string info: ", nparray_string.shape)
   for w in input_sentence:
      # looping numpy array
      for x in onehot_encoded:
         inverted = label_encoder.inverse_transform([argmax(x)])
         if (inverted == w ):
            nparray_string = np.vstack((nparray_string, x))
            break
   print(nparray_string[1:])

