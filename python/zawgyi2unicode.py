from icu import Transliterator
import sys

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Converting Zawgyi to Unicode Encoding
# Last updated: 1 Oct 2022
# How to run:
# If you don't have icu library, do installation: "pip install PyICU"
# $ python ./zawgyi2unicode.py ./eg-corpus-zawgyi.txt
#
# References
# https://github.com/google/myanmar-tools/blob/master/clients/python/README.rst

with open(sys.argv[1]) as f:
    corpus = []
    for line in f:
        corpus.append(line.rstrip())
#print(corpus)

for zawgyi_line in corpus:
   converter = Transliterator.createInstance('Zawgyi-my')
   uni_line = converter.transliterate(zawgyi_line)
   print(uni_line)



