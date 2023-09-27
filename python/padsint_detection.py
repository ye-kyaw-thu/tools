# Written by Ye, LU Lab., Myanmar
# Last updated: 27 Sept 2023
# For detecting Padsints
# How to run:
# e.g. python padsint_detection.py ./input.txt

import argparse

def detect_subscripts(input_file):
    lines_with_subscripts = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            subscripts_in_line = []
            subscript_indices = [i for i, char in enumerate(line) if char == '္']
            for index in subscript_indices:
                # For each subscript marker, get the previous character (if exists)
                # and concatenate with the subscript marker and the next character
                if index > 0 and index < len(line) - 1:
                    stacked_syllable = f"{line[index-1]}္{line[index+1]}"
                    subscripts_in_line.append(stacked_syllable)
            if subscripts_in_line:
                lines_with_subscripts.append(', '.join(subscripts_in_line))
    return lines_with_subscripts

def main():
    parser = argparse.ArgumentParser(description='Detect Burmese subscript combinations or Padsint in a file.')
    parser.add_argument('input_file', help='Input file containing Burmese text')
    parser.add_argument('-o', '--output_filename', help='Output file to save results. If not provided, results are printed to the console.', default=None)

    args = parser.parse_args()

    results = detect_subscripts(args.input_file)

    if args.output_filename:
        with open(args.output_filename, 'w', encoding='utf-8') as f:
            for line in results:
                f.write(line + '\n')
    else:
        for line in results:
            print(line)

if __name__ == '__main__':
    main()
