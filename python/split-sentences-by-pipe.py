"""
Split sentences by pipe delimiter.
Written by Ye Kyaw Thu, CADT, Cambodia.
Last upated: 10 Mar 2024
Usage:
python ./split-sentences-by-pipe.py --input ./Harry_Potter_all_char_separated.txt \
--output harry-potter.txt

"""

import argparse

def clean_sentences(input_file, output_file=None):
    with open(input_file, "r", encoding="utf-8") as file:
        data = file.read().split('|')

    cleaned_sentences = [sentence.strip() for sentence in data if sentence.strip()]

    if output_file:
        with open(output_file, "w", encoding="utf-8") as out_file:
            out_file.write('\n'.join(cleaned_sentences))
    else:
        print('\n'.join(cleaned_sentences))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean sentences from a text file.")
    parser.add_argument("-i", "--input", required=True, help="Input filename")
    parser.add_argument("-o", "--output", help="Output filename")
    args = parser.parse_args()

    clean_sentences(args.input, args.output)
