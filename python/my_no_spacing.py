"""

Add spacing to all Myanmar numbers.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 26 April 2024.
Usage:
python ./my_no_spacing.py --input ./eg_input.txt
python ./my_no_spacing.py --input ./eg_input.txt --output ./eg_input.space

"""

import re
import argparse
import sys

def add_spacing_to_myanmar_numbers(input_file, output_file=None):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        # Use regular expression to find Myanmar numbers without spacing
        matches = re.findall(r'[၀၁၂၃၄၅၆၇၈၉]+', line)
        for match in matches:
            # Add spacing between Myanmar numbers without spacing
            line = line.replace(match, ' '.join(match))
        output_lines.append(line.rstrip('\n'))  # Strip newline character

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(output_lines)
    else:
        for line in output_lines:
            try:
                print(line)
            except BrokenPipeError:
                # Exit gracefully on Broken Pipe Error
                sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add spacing to Myanmar numbers in a text file")
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    add_spacing_to_myanmar_numbers(args.input, args.output)
