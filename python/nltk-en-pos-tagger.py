import sys
import argparse
import nltk
from nltk.tokenize import word_tokenize

# POS tagging for English with NLTK library
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Reference: Python 3 Text Processing with NLTK 3 Cookbook
# Reference: https://stackoverflow.com/questions/42865623/how-to-output-nltk-pos-tag-in-the-string-instead-of-a-list
# Reference for quotes: https://quotabulary.com/quotes-by-famous-scientists

# How to run:
# $ echo "Who am I?" | python ./nltk-en-pos-tagger.py
# $ python ./nltk-en-pos-tagger.py < ./Quotes-By-Famous-Scientists.txt
# $ cat ./Quotes-By-Famous-Scientists.txt | python ./nltk-en-pos-tagger.py

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textLines=args.inputFile.readlines()

count=0
for line in textLines:
   count +=1
   tokenizedText=word_tokenize(line)
   posText=nltk.pos_tag(tokenizedText)
   print(' '.join([word + '/' + pos for word, pos in posText]))
   
