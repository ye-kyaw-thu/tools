# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:17:27 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

How to run:
python sort_openslr_transcript.py -i .\sorting\line_index_female.tsv -o line_index_female_sort.txt -d "\t" -s asc

"""

import argparse
import csv
import operator

def main():
    # define and parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    parser.add_argument('-d', '--delimiter', help='Delimiter used in the file', default='\t')
    parser.add_argument('-s', '--sort', help='Sorting order: asc or desc', default='asc')
    args = parser.parse_args()

    # If the delimiter is passed as the string '\t' or '\\t', 
    # replace it with an actual tab character
    if args.delimiter == '\\t' or args.delimiter == '\t':
        args.delimiter = '\t'
            
    # Ensure delimiter is a single character
    assert len(args.delimiter) == 1, 'Delimiter must be a single character.'

    # load the data
    data = []
    with open(args.input, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=args.delimiter)
        for row in reader:
            data.append(row)

    # sort the data
    if args.sort == 'desc':
        data.sort(key=operator.itemgetter(0), reverse=True)
    else:
        data.sort(key=operator.itemgetter(0))

    # write the sorted data to the output file
    with open(args.output, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=args.delimiter)
        writer.writerows(data)

if __name__ == '__main__':
    main()
