import sys
import argparse
from nltk.tokenize import sent_tokenize

# sentence tokenizing for English
# Written by Ye Kyaw Thu
# Reference: Python 3 Text Processing with NLTK 3 Cookbook

# How to run:
# python ./en-sentence-tokenizer.py ./en.text.txt
# echo "Hello! This is Ye. I hope you remember me. We met at InterSpeech 2019. I attended your paper presentation. We also discussed about zeroshot ASR. Please keep in touch!" | python ./en-sentence-tokenizer.py

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textData=args.inputFile.read()

print(sent_tokenize(textData))

