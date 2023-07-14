# -*- coding: utf-8 -*-
"""
For splitting into source and target files
Last updated: Jul 14, 2023
@author: Ye Kyaw Thu

How to run:
python split_parallel_data.py --help
python split_parallel_data.py .\corpus\sgaw_kayin\sayar_3.12.22\sayar_3.12.22\prallel_sgk-mya_68571 -d '\t' -s all.sg -t all.my
python split_parallel_data.py .\corpus\sgaw_kayin\sayar_3.12.22\sayar_3.12.22\prallel_sgk-mya_68571 -d "\t" -s all.sg -t all.my
"""

import argparse
import ast

def split_parallel_data(input_filename, delimiter, source_filename, target_filename):
    # Convert the string delimiter to its actual value
    delimiter = ast.literal_eval(f'"{delimiter}"')

    with open(input_filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    source = []
    target = []
    for line in lines:
        if delimiter in line:
            source_item, target_item = line.strip().split(delimiter, 1)
            source.append(source_item)
            target.append(target_item)

    # Write to source file
    with open(source_filename, 'w', encoding="utf-8") as f:
        f.write("\n".join(source))

    # Write to target file
    with open(target_filename, 'w', encoding="utf-8") as f:
        f.write("\n".join(target))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', help='Input filename')
    parser.add_argument('-d', '--delimiter', help='Delimiter to use when splitting data', required=True)
    parser.add_argument('-s', '--source_filename', help='Source output filename', required=True)
    parser.add_argument('-t', '--target_filename', help='Target output filename', required=True)

    args = parser.parse_args()

    # Check if the delimiter is surrounded by single or double quotes and remove them
    if args.delimiter[0] == args.delimiter[-1] and args.delimiter.startswith(("'", '"')):
        delimiter = args.delimiter[1:-1]
    else:
        delimiter = args.delimiter

    # Proceed to splitting the data
    split_parallel_data(args.input_filename, delimiter, args.source_filename, args.target_filename)

if __name__ == "__main__":
    main()
