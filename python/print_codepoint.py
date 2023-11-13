# for printing code points (decimal, unicode) of each Myanmar character and counting total no. of characters
# written by Ye Kyaw Thu, Visiting Professor,
# Language Semantic Technology Research Team (LST), NECTEC, Thailand
# Last updated: 13 Nov 2023
# how to run:
# python ./print_codepoint.py --help
# python ./print_codepoint.py khmer.txt
# python ./print_codepoint.py khmer.txt --output_type unicode
# python ./print_codepoint.py khmer.txt --output_type ordinal
# python ./print_codepoint.py khmer.txt --output_type unicode --no_print_original
# python ./print_codepoint.py khmer.txt --output_type unicode --no_print_original --output code.txt


import sys
import argparse

def process_line(line, output_type, output_file):
    line = line.rstrip('\n')
    string_length = len(line)
    output = ''

    for char in line:
        char_no = ord(char)
        if output_type == 'both':
            output += f"{char} ({char_no}, U{char_no:02x}) "
        elif output_type == 'ordinal':
            output += f"{char} ({char_no}) "
        elif output_type == 'unicode':
            output += f"{char} (U{char_no:02x}) "

    output += f", no. of char = {string_length}\n"
    if output_file:
        output_file.write(output)
    else:
        print(output, end='')

def main():
    parser = argparse.ArgumentParser(description="Process a text file with various options.")
    parser.add_argument("filename", help="The filename to process")
    parser.add_argument("--output_type", choices=['ordinal', 'unicode', 'both'], default='both',
                        help="Choose to print ordinal value, Unicode code point, or both (default: both)")
    parser.add_argument("--output", help="Output file name (optional)")
    parser.add_argument("--no_print_original", action="store_true",
                        help="Do not print the original sentences (default: False)")

    args = parser.parse_args()

    output_file = None
    if args.output:
        output_file = open(args.output, 'w', encoding='utf-8')

    try:
        with open(args.filename, 'r', encoding='utf-8') as file:
            for line in file:
                if not args.no_print_original:
                    print(line, end='')
                process_line(line, args.output_type, output_file)

    except FileNotFoundError:
        print(f"File not found: {args.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
