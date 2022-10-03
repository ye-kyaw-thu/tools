from icu import Transliterator
import sys
import re

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Converting Zawgyi to Unicode Encoding and syllable unit breaking
# Last updated: 3 Oct 2022
# How to run:
# If you don't have icu library, do installation: "pip install PyICU"
# $ python ./zawgyi2unicode-syl.py ./eg-corpus-zawgyi.txt
#
# References
# https://github.com/google/myanmar-tools/blob/master/clients/python/README.rst

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

with open(sys.argv[1]) as f:
    corpus = []
    for line in f:
        corpus.append(line.rstrip())
#print(corpus)

for zawgyi_line in corpus:
   converter = Transliterator.createInstance('Zawgyi-my')
   # Zawgyi ကနေ Unicode ကို ပြောင်း
   uni_line = converter.transliterate(zawgyi_line)
   # Unicode encoding အဖြစ် ပြောင်းထားတဲ့ စာကြောင်းကို syllable ဖြတ်
   uni_line_syl = sylbreak_my(uni_line)
   # list ကို space ခြားထားတဲ့ string အဖြစ် ရိုက်ခိုင်းချင်လို့ * ထည့်ထားတာ
   print(*uni_line_syl) 


