"""

For removing ZWNJ, ZWSP, HSP
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last Updated: 25 Jan 2024

Usage:
     python rm_zwnj_zwsp_hsp.py --help
     python ./rm_zwnj_zwsp_hsp.py --input ./train.my.syl --verbose | head
     python ./rm_zwnj_zwsp_hsp.py --input ./train.my.syl --output ./train.my.syl.rm

"""

import sys
import argparse
import errno
import re

def remove_special_chars(text, verbose=False):
    # Unicode representations
    zwnj = '\u200C'  # Zero Width Non-Joiner
    zwsp = '\u200B'  # Zero Width Space
    hsp = '\u00AD'   # Half Space (Soft Hyphen)

    # Counters for verbose mode
    count_zwnj = text.count(zwnj)
    count_zwsp = text.count(zwsp)
    count_hsp = text.count(hsp)

    # Removing the characters
    cleaned_text = text.replace(zwnj, '').replace(zwsp, '').replace(hsp, '')

    # Normalize spaces: Remove leading/trailing spaces in each line and replace multiple spaces with a single space
    cleaned_text = '\n'.join([re.sub(r'[ \t]+', ' ', line).strip() for line in cleaned_text.splitlines()])

    
    if verbose:
        print(f"Removed {count_zwnj} ZWNJ, {count_zwsp} ZWSP, {count_hsp} HSP characters")

    return cleaned_text

def main():
    parser = argparse.ArgumentParser(description='Remove ZWNJ, ZWSP, HSP characters from text')
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--verbose', action='store_true', help='Print counts of removed characters')
    args = parser.parse_args()

    # Read from input file or stdin
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = sys.stdin.read()

    # Process the text
    cleaned_text = remove_special_chars(text, verbose=args.verbose)

    # Write to output file or stdout
    try:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)
        else:
            sys.stdout.write(cleaned_text)
    except BrokenPipeError:
        # Handle broken pipe error caused by piping output to commands like 'head'
        sys.stdout.close()
        sys.stderr.close()

if __name__ == "__main__":
    main()
