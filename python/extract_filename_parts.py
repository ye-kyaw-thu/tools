# -*- coding: utf-8 -*-
"""
Last updated on Fri Jun 30 09:24:58 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

"""

#How to run:
#python extract_filename_parts.py -d _ -c 2 -t count -f 'F:\NECTEC\Project\MyanmarSpeech\MyanmarSpeech'
#python extract_filename_parts.py -d _ -c 2 -t count -f 'F:\NECTEC\Project\MyanmarSpeech\MyanmarSpeech' -v True


import os
import argparse

def extract_filename_parts(folder, delimiter, column, verbose):
    parts = set()  # Use a set to automatically remove duplicates
    for filename in os.listdir(folder):
        if filename.endswith(".wav"):
            filename_without_extension = os.path.splitext(filename)[0]
            split_name = filename_without_extension.split(delimiter)
            if verbose:  # Only print processing info if verbose is True
                print(f"Processing file: {repr(filename)}, split parts: {split_name}, delimiter: {repr(delimiter)}")
            if len(split_name) >= column:
                parts.add(split_name[column])  # Add to the set
    return parts

def main():
    parser = argparse.ArgumentParser(description='Process some wave filenames.')
    parser.add_argument('-d', '--delimiter', type=str, required=True,
                        help='The delimiter to use when splitting the filenames.')
    parser.add_argument('-c', '--column', type=int, required=True,
                        help='The column (1-indexed) to extract from the split filenames.')
    parser.add_argument('-t', '--task', type=str, choices=['count', 'print'], required=True,
                        help='The task to perform: "count" for total number of unique columns, "print" for all unique columns.')
    parser.add_argument('-f', '--folder', type=str, required=True,
                        help='The folder where the wave files are located.')
    parser.add_argument('-v', '--verbose', type=bool, default=False,
                        help='Print processing information for each file. (default: False)')

    args = parser.parse_args()

    # Extract the required parts of the filenames
    parts = extract_filename_parts(args.folder, args.delimiter, args.column - 1, args.verbose)  # Convert to 0-indexed here

    # Depending on the task, print the count of unique parts or all unique parts
    if args.task == 'count':
        print(len(parts))  # The length of the set is the count of unique items
    elif args.task == 'print':
        print(', '.join(parts))

if __name__ == "__main__":
    main()
