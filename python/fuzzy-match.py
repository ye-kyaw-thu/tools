import sys
from fuzzywuzzy import process

# Fuzzy matching test for myG2P phonemes
# fuzzywuzzy link: https://github.com/seatgeek/fuzzywuzzy
# myG2P link: https://github.com/ye-kyaw-thu/myG2P 
#
# Written by Ye Kyaw Thu
# How to run: python ./fuzzy-match.py <dictionary_filename> <search_word>
# eg 1: python ./fuzzy-match.py ./f4 "ra- khain"

def fuzzy_match(searchWord, dictFilename, limit=5):
   with open(dictFilename) as dictFile:
      dictWords = [line.rstrip('\n') for line in dictFile]

   suggestedWord = process.extract(searchWord, dictWords, limit=limit)
   return suggestedWord

dictFilename =  sys.argv[1]
searchWord = sys.argv[2]

print(fuzzy_match(searchWord, dictFilename))

