# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:24:46 2023
@author: Ye Kyaw Thu, LST, NECTEC, Thailand

Calculation of Word Error Rate (WER),
Match Error Rate (MER),
Word Information Lost (WIL).

How to run:
python jiwer_wer_mer_wil.py -s "ye kyaw thu" "thu ye kyaw"
python jiwer_wer_mer_wil.py -f ref.txt hyp.txt
"""

import sys
import argparse
import jiwer

def calculate_scores(ref, hyp):
    measures = jiwer.compute_measures(ref, hyp)
    WER = measures['wer']
    MER = measures['mer']
    WIL = measures['wil']

    print(f"WER: {WER}")
    print(f"MER: {MER}")
    print(f"WIL: {WIL}")

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--strings', nargs=2, help='reference and hypothesis strings')
    group.add_argument('-f', '--files', nargs=2, help='reference and hypothesis files')

    args = parser.parse_args()

    if args.strings:
        ref, hyp = args.strings
    else:
        with open(args.files[0], 'r', encoding='utf-8') as f:
            ref = f.read()
        with open(args.files[1], 'r', encoding='utf-8') as f:
            hyp = f.read()

    calculate_scores(ref, hyp)

if __name__ == '__main__':
    main()
