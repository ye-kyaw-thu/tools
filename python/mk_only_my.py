"""

a Python script that can process a text file to remove all characters and symbols except for Burmese/Myanmar words and characters
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 19 Jan 2024

Usage:
python ./mk_only_my.py --input MyanmarTotal.my --output MyanmarTotal.my.clean
cat MyanmarTotal.my | python ./mk_only_my.py
python ./mk_only_my.py --input MyanmarTotal.my


"""

import sys
import argparse
import re

def clean_text(text):
    # Regular expression to match Burmese characters and whitespace
    # Burmese Unicode range: U+1000–U+109F
    pattern = r'[\u1000-\u109F\s]+'
    return re.findall(pattern, text)

def main():
    parser = argparse.ArgumentParser(description='Clean text file by keeping only Burmese characters.')
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

    cleaned_lines = []
    for line in text.splitlines():
        cleaned_line = ' '.join(clean_text(line))
        cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()  # Replace multiple spaces with a single space and strip leading spaces
        cleaned_lines.append(cleaned_line)

    cleaned_text = '\n'.join(cleaned_lines)  # Join the cleaned lines with newline character

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
    else:
        print(cleaned_text)

if __name__ == "__main__":
    main()
