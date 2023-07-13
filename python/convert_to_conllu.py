# -*- coding: utf-8 -*-
"""
conversion from left-to-right format to conllu format

Last updated: 13 Jul, 2023
@author: Ye Kyaw Thu, LU Lab, Myanmar


How to run:
python convert_to_conllu.py --input .\corpus\mypos_5lines.txt --output mypos_5lines.conllu
"""

import argparse
from typing import List, Tuple


def parse_sentence(sentence: str) -> List[Tuple[str, str]]:
    """Parse sentence into list of tuples (word, POS)"""
    tokens = sentence.strip().split()
    parsed_tokens = []
    for token in tokens:
        try:
            word, pos = token.rsplit("/", 1)
            parsed_tokens.append((word, pos))
        except ValueError:
            print(f"Could not parse token: {token}")
    return parsed_tokens


def convert_to_conllu(input_file: str, output_file: str):
    with open(input_file, "r", encoding='utf-8') as f_in, open(output_file, "w", encoding='utf-8') as f_out:
        for idx, line in enumerate(f_in, start=1):
            parsed = parse_sentence(line)
            for idy, (word, pos) in enumerate(parsed, start=1):
                # CoNLL-U format: ID, FORM, LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS, MISC
                f_out.write(f"{idy}\t{word}\t_\t{pos}\t_\t_\t_\t_\t_\t_\n")
            f_out.write("\n")  # empty line between sentences


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert POS tagged corpus to CoNLL-U format.")
    parser.add_argument("--input", "-i", type=str, required=True, help="Input file path")
    parser.add_argument("--output", "-o", type=str, required=True, help="Output file path")
    args = parser.parse_args()

    convert_to_conllu(args.input, args.output)
