"""
for converting one word, one line format into two words, one line format.
written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 26 April 2024

Usage:
python ./convert_to_two_words_dict.py --input ./g2p.f2  --output ./g2p.f2.two_words

python ./convert_to_two_words_dict.py --input ./g2p.f2  --delimiter "|" | tail

python ./convert_to_two_words_dict.py --input ./g2p.f2  --delimiter "|||" | head
"""

import argparse
import sys

def convert_to_two_words(input_file, output_file, delimiter):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    two_words_lines = []
    for i in range(0, len(lines), 2):
        first_word = lines[i].strip()
        if i+1 < len(lines):
            second_word = lines[i+1].strip()
            two_words_lines.append(delimiter.join([first_word, second_word]))

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in two_words_lines:
                f.write(line + '\n')
    else:
        for line in two_words_lines:
            try:
                print(line)
            except BrokenPipeError:
                # Exit gracefully on Broken Pipe Error
                sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert dictionary file into two words one line format.")
    parser.add_argument("--input", required=True, help="Input file name")
    parser.add_argument("--output", help="Output file name")
    parser.add_argument("--delimiter", default=" ", help="Delimiter between two words, default is space")
    args = parser.parse_args()

    convert_to_two_words(args.input, args.output, args.delimiter)
