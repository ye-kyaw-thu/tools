from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import sys
import re

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Calculating syllable frequency
# Last updated: 25 Sept 2022
# How to run: python ./syl2freq.py ./eg-corpus.txt
#
#
# sklearn library က ကိုယ့်စက်ထဲမှာ မရှိသေးရင် အောက်ပါ command နဲ့ install လုပ်ပါ
# pip install sklearn
# Referene: https://investigate.ai/text-analysis/how-to-make-scikit-learn-natural-language-processing-work-with-japanese-chinese/
# https://stackoverflow.com/questions/28328372/why-isnt-the-token-pattern-parameter-in-tfidfvectorizer-working-with-scikit-lea
# https://www.davidsbatista.net/blog/2018/02/28/TfidfVectorizer/


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

#print("input corpus:\n", corpus, "\n")

# Dummy stop word example, you have to replace it
my_stop_words = ['၊', '။', '၏', '၍', '၌'] 

vectorizer = CountVectorizer(tokenizer=sylbreak_my, stop_words=my_stop_words)
matrix = vectorizer.fit_transform(corpus)

syllable_df = pd.DataFrame(matrix.toarray(),
                        columns=vectorizer.get_feature_names_out())
print(syllable_df)

