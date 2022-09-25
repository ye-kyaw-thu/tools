from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import sys
import pandas as pd
import re

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Calculating syllable idf
# Last updated: 25 Sept 2022
# How to run:
# $ python ./syl2idf.py ./eg-corpus.txt

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
syllable_idf = pd.DataFrame({'feature_name':vectorizer.get_feature_names_out(), 'idf_weights':tfidf_transformer.idf_})

print(syllable_idf)

