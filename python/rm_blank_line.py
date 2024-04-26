"""
For removing blank lines.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 26 April 2024.

Usage:
python ./rm_blank_line.py --input ./myPoetry.txt.clean --output ./myPoetry.txt.clean.rm_blank_lines
"""

import sys
import argparse

def remove_blank_lines(input_file, output_file=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Input file not found.")
        return

    non_blank_lines = [line.rstrip('\n') for line in lines if line.strip()]

    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in non_blank_lines:
                    f.write(line + '\n')
        except FileNotFoundError:
            print("Output file directory not found.")
    else:
        for line in non_blank_lines:
            try:
                print(line)
            except BrokenPipeError:
                # Exit gracefully on Broken Pipe Error
                sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove blank lines from a file")
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    if not output_file:
        output_file = None  # Ensure output_file is None if not provided

    remove_blank_lines(input_file, output_file)
