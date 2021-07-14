import sys
import argparse
from nltk.corpus import wordnet

# Measuring Wu-and-Palmer Similarity for English
# Date: 14 July 2021 
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand

# Reference:
# Zhibiao Wu, Martha Palmer,  “Verbs  semantics  and  lexical selection,”  InProceedings  of  the  32nd  annual  meeting  on Association  for  Computational  Linguistics,  pp.  133-138. Association for Computational Linguistics, 1994, June

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textLines=args.inputFile.readlines()

count=0
for line in textLines:
   count +=1
   word1, word2 = line.split( )
   word1syn = wordnet.synsets(word1)[0]
   word2syn = wordnet.synsets(word2)[0]
   wup_value=word1syn.wup_similarity(word2syn)
   print(word1+', '+word2+': ', str(wup_value))

