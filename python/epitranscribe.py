#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original code from: https://github.com/dmort27/epitran
# Ref: https://stackoverflow.com/questions/21689365/python-3-typeerror-must-be-str-not-bytes-with-sys-stdout-write/21689447
# http://ipa-reader.xyz/

import sys
import unicodedata
import epitran
import argparse


def main(code):
    epi = epitran.Epitran(code)
    for line in sys.stdin:  # pointless
        #line = line.decode('utf-8') # commented out by Ye
        line = unicodedata.normalize('NFD', line.lower())
        line = epi.transliterate(line)
        #line = line.encode('utf-8') # comented out by Ye
        sys.stdout.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Coverts text from STDIN (in the language specified),' +
        'into Unicode IPA and emits it to STDOUT.')
    parser.add_argument('code', help='ISO 639-3 code for conversion language')
    args = parser.parse_args()
    main(args.code)
