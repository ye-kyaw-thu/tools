"""
a Python script that removes the two Burmese symbols "၊" and "။"
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 19 Jan 2024

Usage:

python ./rm_my_two_symbols.py --help

python ./rm_my_two_symbols.py --input ./MyanmarTotal.my.clean \
--output ./MyanmarTotal.my.clean.nosymbol

cat ./MyanmarTotal.my.clean | python ./rm_my_two_symbols.py \
--output ./MyanmarTotal.my.clean.nosymbol


"""

import sys
import argparse
import re

def remove_burmese_symbols(text):
    # Remove specific Burmese symbols "၊" and "။"
    text = text.replace("၊", "").replace("။", "")
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    parser = argparse.ArgumentParser(description='Remove specific Burmese symbols from text.')
    parser.add_argument('--input', type=str, help='Input file name.')
    parser.add_argument('--output', type=str, help='Output file name.')

    args = parser.parse_args()

    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{args.input}' was not found.")
            sys.exit(1)
    else:
        text = sys.stdin.read()

    # Process each line and maintain the same number of lines
    cleaned_lines = []
    for line in text.splitlines():
        cleaned_line = remove_burmese_symbols(line)
        cleaned_lines.append(cleaned_line)

    cleaned_text = '\n'.join(cleaned_lines)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
    else:
        print(cleaned_text)

if __name__ == "__main__":
    main()
