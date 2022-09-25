from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import pandas as pd
import re

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Calculating syllable tf
# Last updated: 25 Sept 2022
# How to run:
# $ python ./syl2tf.py ./eg-corpus.txt
#
# References
# https://github.com/gearmonkey/tfidf-python/blob/master/tfidf.py
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#:~:text=The%20formula%20that%20is%20used,document%20frequency%20of%20t%3B%20the

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

# Add a custom list of stopwords for punctuation
my_stop_words = ['၊', '။', '၏', '၍', '၌']

tf_vectorizer = TfidfVectorizer(tokenizer=sylbreak_my, stop_words=my_stop_words, use_idf=False, norm='l1')
#tf_vectorizer = TfidfVectorizer(stop_words=my_stop_words, tokenizer=sylbreak, use_idf=False, norm='l2') # l2 normalizer is the default normalizer
matrix = tf_vectorizer.fit_transform(corpus)
df = pd.DataFrame(matrix.toarray(), columns=tf_vectorizer.get_feature_names_out())
print(df)

