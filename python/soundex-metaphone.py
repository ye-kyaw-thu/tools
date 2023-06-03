# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:47:13 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
How to run:
python soundex-metaphone.py -f en-word.txt -c "soundex"
python soundex-metaphone.py -f en-word.txt -c "metaphone"

Ref: https://en.wikipedia.org/wiki/Soundex
Ref: https://en.wikipedia.org/wiki/Metaphone
"""

import sys
import argparse
from metaphone import doublemetaphone

def soundex(word):
    codes = ("bfpv", "cgjkqsxz", "dt", "l", "mn", "r")
    soundDict = dict((ch, str(ix+1)) for ix, code in enumerate(codes) for ch in code)
    cmap2 = lambda kar: soundDict.get(kar, '9')
    sdx =  ''.join(cmap2(kar) for kar in word.lower())
    sdx2 = word[0].upper() + ''.join(k for k, g in list(zip(sdx[1:], sdx[:-1])) if k != g if int(k) != 9)
    sdx3 = sdx2[0:4].ljust(4, '0')
    return sdx3

def get_metaphone(word):
    return doublemetaphone(word)

def process_word(word, code):
    if code == "soundex":
        return soundex(word)
    elif code == "metaphone":
        return get_metaphone(word)

def process_file(file_name, code):
    results = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            word = line.strip()
            result = process_word(word, code)
            results.append(result)
    return results

parser = argparse.ArgumentParser(description="Generate phonetic code")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-w", "--word", help="Word to be encoded")
group.add_argument("-f", "--file", help="File containing words to be encoded")
parser.add_argument("-c", "--code", choices=["soundex", "metaphone"], required=True, help="Type of encoding")
args = parser.parse_args()

if args.word:
    result = process_word(args.word, args.code)
    print(result)
elif args.file:
    results = process_file(args.file, args.code)
    for result in results:
        print(result)
