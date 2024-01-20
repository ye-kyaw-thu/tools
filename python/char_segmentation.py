"""
For character segmentation.
Written by Ye Kyaw Thu.
Last updated: 20 Jan 2024

Usage:
python ./char_segmentation.py --input ./MyanmarTotal.my.clean.nosymbol --output ./char_seg/MyanmarTotal.my.clean.nosymbol.char

"""

import sys
import argparse
import re  # Importing the regular expressions module

def segment_characters(text):
    segmented = ' '.join(text)
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    cleaned = re.sub(r'\s+', ' ', segmented).strip()
    return cleaned

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Character segmentation of text.')
    parser.add_argument('-i', '--input', type=str, default=None, help='Input file path. If not specified, will read from stdin.')
    parser.add_argument('-o', '--output', type=str, default=None, help='Output file path. If not specified, will write to stdout.')

    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    segmented_lines = [segment_characters(line) for line in lines]

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write('\n'.join(segmented_lines))
    else:
        sys.stdout.write('\n'.join(segmented_lines))
