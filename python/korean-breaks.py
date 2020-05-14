import sys
from hangul_utils import *

# for word segmentation and pos tagging of Korean text
# Note: You need to install "hangul-utils" in advanced
# Ref link: https://github.com/kaniblu/hangul-utils
# written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
#
# How to run: python ./korean-breaks.py <input-filename> <word|morph|pos>
# eg 1: python ./korean-breaks.py ./tst.ko -pos
# eg 2: python ./korean-breaks.py ./tst.ko -morph
# e.g 3: python ./korean-breaks.py ./tst.ko -word

if len(sys.argv) < 3:
   print ("You must set two arguments!")
   print ("How to run:")
   print ("python ./korean-breaks.py <raw-korean-text-filename> <-word|-morph|-pos>")
   sys.exit()
else:
   f1 = sys.argv[1]
   arg = sys.argv[2]
   fp1=open(f1,"r")

   for line1 in fp1:
      if arg.lower() == '-word':
         # Word tokenization (mainly using space):
         print (" ".join(list(word_tokenize(line1.strip()))))
      elif arg.lower() == '-morph':
         # Morpheme tokenization
         print (" ".join(list(morph_tokenize(line1.strip()))))
      elif arg.lower() == '-pos':
         # Morpheme tokenization with POS
         print (list(morph_tokenize(line1.strip(), pos=True)))
        
   fp1.close()
