# -*- coding: utf-8 -*-
"""
Last updated: on Tue Jun 27 15:24:00 2023
@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

Changing data format from left-to-right to top-down and vice versa.

How to run:
Changing from left-to-right to column or CRF format:
python format_conversion.py .\small-ner.txt .\top-down.txt -f top-down

Changing from CRF to left-to-right format
python format_conversion.py .\top-down.txt .\left-to-right.txt -f left-to-right
"""

import argparse
import pandas as pd


def convert_crf_to_ltr(df):
    """ Convert CRF format DataFrame to left-to-right format. """
    ltr_data = []
    current_sentence = []
    for row in df.itertuples():
        if pd.isna(row.labels):
            ltr_data.append(current_sentence)
            current_sentence = []
        else:
            current_sentence.append(f"{row.words}/{row.labels}")
    return [" ".join(sentence) for sentence in ltr_data]


def convert_ltr_to_crf(lines):
    """ Convert left-to-right format to CRF format. """
    crf_data = []
    for line in lines:
        for token in line.split():
            word, label = token.split("/")
            crf_data.append((word, label))
        crf_data.append(("", ""))
    return pd.DataFrame(crf_data, columns=["words", "labels"])


def main(input_file, output_file, format_type):
    if format_type == 'top-down':
        # Read data
        with open(input_file, "r", encoding='utf-8') as f:
            lines = f.readlines()
        # Convert
        df = convert_ltr_to_crf(lines)
        # Write to file
        df.to_csv(output_file, sep="\t", index=False, header=False)
    elif format_type == 'left-to-right':
        # Load data
        df = pd.read_csv(input_file, sep="\t", names=["words", "labels"])
        # Convert
        ltr_data = convert_crf_to_ltr(df)
        # Write to file
        with open(output_file, "w", encoding='utf-8') as f:
            for line in ltr_data:
                f.write(line + "\n")
    else:
        print("Unknown format. Please specify either 'top-down' or 'left-to-right'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert between CRF and left-to-right formats.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    parser.add_argument('-f', '--format', type=str, required=True, 
                        choices=['top-down', 'left-to-right'], help='Format of the output file')
    args = parser.parse_args()
    main(args.input_file, args.output_file, args.format)
