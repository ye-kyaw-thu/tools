"""
For word shuffling line by line.
Ye@Lab
Last Updated: 12 Sept 2024

How to run:
python ./word_shuffle.py --input ./proverb_sample.syl.chk --output ./proverb_sample.syl.shuf1.txt

"""

import argparse
import random
import sys

def shuffle_words_line_by_line(input_file, output_file):
    # Open input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Shuffle words for each line
    shuffled_lines = []
    for line in lines:
        words = line.strip().split()  # Split by whitespace
        random.shuffle(words)
        shuffled_lines.append(' '.join(words))
    # Handle output: write to file or print to stdout
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(shuffled_lines) + '\n')
    else:
        sys.stdout.write('\n'.join(shuffled_lines) + '\n')

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Shuffle words in each line of a file.")
    parser.add_argument('--input', required=True, help="Input file containing text")
    parser.add_argument('--output', help="Output file to save shuffled lines. Default is stdout.")

    args = parser.parse_args()

    # Shuffle words line by line
    shuffle_words_line_by_line(args.input, args.output)

if __name__ == "__main__":
    main()
