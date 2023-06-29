# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 20:40:49 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

How to run:
python cut_columns.py -i myg2p.txt -o dict.txt -c 2
python cut_columns.py -i myg2p.txt -o dict.txt -c 3,5
python cut_columns.py -i myg2p.txt -o dict.txt -c 2,4-5
"""

#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd
import argparse

def parse_column_range(columns_str):
    column_ranges = (x.split('-') for x in columns_str.split(','))
    columns = [i for r in column_ranges for i in range(int(r[0]), int(r[-1]) + 1)]
    return [i - 1 for i in columns]  # convert to zero-based

def cut_columns(input_file, output_file, columns_str):
    columns = parse_column_range(columns_str)
    
    # Load the file:
    data = pd.read_csv(input_file, header=None, sep="\t")
    
    # Extract the desired columns:
    extracted_columns = data[columns]
    
    # Write to the output file:
    #extracted_columns.to_csv(output_file, header=False, index=False, sep="\t", line_terminator='\n')
    extracted_columns.to_csv(output_file, header=False, index=False, sep="\t", lineterminator='\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cut specific columns from a tab-separated file')
    parser.add_argument('-i', '--input', type=str, required=True, help='input file')
    parser.add_argument('-o', '--output', type=str, required=True, help='output file')
    parser.add_argument('-c', '--columns', type=str, required=True, help='one-based index of the columns to cut, e.g. "1,3" or "1-3" or "1,3-5"')
    args = parser.parse_args()

    cut_columns(args.input, args.output, args.columns)
