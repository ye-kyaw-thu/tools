"""

A format converter for use with FastText, supporting reverse format conversion as well.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 22 Jan 2024

Usage:
    python ./fasttext_format_converter.py --help
    python ./fasttext_format_converter.py --input ./all_languages.txt --output ./all_languages.fasttext
    python ./fasttext_format_converter.py --input ./all_languages.fasttext --output output.txt --reverse

"""

import argparse
import sys

def convert_to_fasttext_format(line, reverse=False):
    if reverse:
        if line.startswith('__label__'):
            parts = line[len('__label__'):].split("\t")
            if len(parts) != 2:
                return None
            return f"{parts[1].strip()}\t{parts[0].strip()}"
        else:
            return None  # Return None if line does not start with '__label__'
    else:
        parts = line.split("\t")
        if len(parts) != 2:
            return None
        return f"__label__{parts[1].strip()}\t{parts[0].strip()}"

def process_file(input_stream, output_stream, reverse=False):
    for line in input_stream:
        converted_line = convert_to_fasttext_format(line.strip(), reverse)
        if converted_line:
            output_stream.write(converted_line + '\n')

def main():
    parser = argparse.ArgumentParser(description="Converts text data for FastText format.")
    parser.add_argument('--input', type=str, help='Input file path. If not provided, reads from stdin.')
    parser.add_argument('--output', type=str, help='Output file path. If not provided, writes to stdout.')
    parser.add_argument('--reverse', action='store_true', help='Reverse conversion (from FastText format to original).')

    args = parser.parse_args()

    input_stream = open(args.input, 'r', encoding='utf-8') if args.input else sys.stdin
    output_stream = open(args.output, 'w', encoding='utf-8') if args.output else sys.stdout

    try:
        process_file(input_stream, output_stream, args.reverse)
    finally:
        if args.input:
            input_stream.close()
        if args.output:
            output_stream.close()

if __name__ == "__main__":
    main()
