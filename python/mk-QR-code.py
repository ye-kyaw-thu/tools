import sys
import argparse
import qrcode

# word tokenizing for English with NLTK library
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Reference: Python 3 Text Processing with NLTK 3 Cookbook

# How to run:
# python ./en-word-tokenizer.py ./en.sentence.txt
# cat en.sentence.txt | python ./en-word-tokenizer.py
# python ./en-word-tokenizer.py < ./en.sentence.txt

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textLines=args.inputFile.readlines()

count=0
for line in textLines:
   count +=1
   qrImage = qrcode.make(line)
   qrImage.save ("qrcode-"+str(count)+".jpg")
   




