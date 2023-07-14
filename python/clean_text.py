# -*- coding: utf-8 -*-
"""
for cleaning extra spaces and ZWSP
Last updated: Jul 14, 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar

How to run:
python clean_text.py train.mya train.my
python clean_text.py train.sgk train.sg
"""

import argparse
import re

def clean_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        # Remove extra spaces
        cleaned_line = re.sub(' +', ' ', line)

        # Remove extra heading and trailing spaces per line
        cleaned_line = cleaned_line.strip()

        # Remove ZWSP
        cleaned_line = cleaned_line.replace('\u200B', '')

        cleaned_lines.append(cleaned_line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(cleaned_lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean file content.')
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')

    args = parser.parse_args()

    clean_file(args.input_file, args.output_file)
