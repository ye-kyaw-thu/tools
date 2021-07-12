import sys
import argparse
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# filter English stopwords
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Reference: Python 3 Text Processing with NLTK 3 Cookbook

# How to run:
# $ python ./filter-en-stopwords.py ./en.sentence.txt

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textLines=args.inputFile.readlines()

english_stops = set(stopwords.words('english'))

count=0
for line in textLines:
   count +=1
   words=word_tokenize(line)
   print([word for word in words if word not in english_stops])
   

