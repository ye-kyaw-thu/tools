"""
For spacing or character segmentation for punctuation characters including two Myanmar symbols "၊" and "။".
Spacing for emoji also doing with --emoji command line option.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 26 April 2024.
Usage:
python ./punc_emoji_spacing.py --input ./tst.txt
python ./punc_emoji_spacing.py --input ./tst.txt --emoji
"""

import re
import argparse
import sys
import string

def add_spacing_to_text(input_file, output_file=None, emoji=False):
    emoji_ranges = [
        (0x1F300, 0x1F5FF),
        (0x1F600, 0x1F64F),
        (0x1F680, 0x1F6FF),
        (0x1F700, 0x1F77F),
        (0x1F780, 0x1F7FF),
        (0x1F800, 0x1F8FF),
        (0x1F900, 0x1F9FF),
        (0x1FA00, 0x1FA6F),
        (0x1FA70, 0x1FAFF),
        (0x2600, 0x26FF),
        (0x2700, 0x27BF),
        (0xFE00, 0xFE0F),
        (0x1F1E6, 0x1F1FF)
    ]

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        # Strip leading and trailing spaces
        line = line.strip()

        # Add spacing for all symbols including Myanmar symbols "၊", "။", and "▁" if not standalone or together with other characters
        line = re.sub(r'(?:(?<=\S)|(?=\S))([၊။▁]|[{}])'.format(re.escape(string.punctuation)), r' \1 ', line)

        if emoji:
            # Add spacing for emoji characters if not standalone or together with other characters
            for emoji_range in emoji_ranges:
                start, end = emoji_range
                line = re.sub(r'(?:(?<=\S)|(?=\S))([' + ''.join([chr(c) for c in range(start, end + 1)]) + '])', r' \1 ', line)

        # Remove multiple consecutive spaces
        line = re.sub(r'\s+', ' ', line)
        line = line.strip()

        output_lines.append(line.rstrip('\n'))

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in output_lines:
                f.write(line + '\n')  # Write each line with a newline character
    else:
        for line in output_lines:
            try:
                print(line)
            except BrokenPipeError:
                # Exit gracefully on Broken Pipe Error
                sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add spacing to punctuation symbols, Myanmar symbols, and optionally emoji in a text file")
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--emoji", help="Add spacing for emoji characters", action="store_true")
    args = parser.parse_args()

    add_spacing_to_text(args.input, args.output, args.emoji)
