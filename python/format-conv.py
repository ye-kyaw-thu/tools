"""
Format conversion of spelling corpus.
Written by Ye Kyaw Thu, Visiting Professor, NECTEC, Thailand.
Last updated: 11 Mar 2024

Usage:
time python ./format-conv.py --input ./pp_spelldata_v2_shuf.txt \
--wrong w.txt --tagged t.txt --correct c.txt --error err.txt
"""

import argparse

def process_line(line):
    left, right = line.strip().split(" ||| ")

    # Process left side
    # Add space before "<" and after ">"
    left = left.replace("<", " <").replace(">", "> ")
    right = right.replace("<", " <").replace(">", "> ")

    # Split the string into individual items
    left_segments = left.split()

    # Process and print the first sentence
    wrong_sentence = ' '.join(segment.split('|')[0] + '>' if '|' in segment else segment for segment in left_segments)

    # Process and print the second sentence
    tagged_sentence = ' '.join('$' + segment.split('|')[1].rstrip('>') if '|' in segment else '$keep' for segment in left_segments)

    # Process right side
    right_processed = ""
    right_segments = right.split()

    # Process and print the first sentence
    correct_sentence = ' '.join(segment.split('|')[0] + '>' if '|' in segment else segment for segment in right_segments)

    return wrong_sentence, tagged_sentence, correct_sentence

def convert_format(input_file, wrong_file, tagged_file, correct_file, error_file):
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(wrong_file, 'w', encoding='utf-8') as fwrong, \
         open(tagged_file, 'w', encoding='utf-8') as ftagged, \
         open(correct_file, 'w', encoding='utf-8') as fcorrect, \
         open(error_file, 'w', encoding='utf-8') as ferr:

        for line in fin:
            try:
                wrong_sentence, tagged_sentence, correct_sentence = process_line(line)
                fwrong.write(wrong_sentence + "\n")
                ftagged.write(tagged_sentence + "\n")
                fcorrect.write(correct_sentence + "\n")
            except Exception as e:
                ferr.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text file format as per specified rules")
    parser.add_argument("-i", "--input", help="Input file name", required=True)
    parser.add_argument("-w", "--wrong", help="Wrong output file name", required=True)
    parser.add_argument("-t", "--tagged", help="Tagged output file name", required=True)
    parser.add_argument("-c", "--correct", help="Correct output file name", required=True)
    parser.add_argument("-e", "--error", help="Error file name", required=True)
    args = parser.parse_args()

    convert_format(args.input, args.wrong, args.tagged, args.correct, args.error)
