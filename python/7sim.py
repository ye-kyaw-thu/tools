# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:56:34 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand

How to Run:
python 7sim.py -m all ref.txt hyp.txt
python 7sim.py -m cosine "သမီးတော်" "သမားတော်"
python 7sim.py -m lcs_ratio "သမီးတော်" "သမားတော်"
"""

import argparse
import textdistance
import os

# Create an argument parser
parser = argparse.ArgumentParser(description='String similarity measurements')
parser.add_argument('text1', type=str, help='First text string or file')
parser.add_argument('text2', type=str, help='Second text string or file')
parser.add_argument('-m', '--measurement', type=str, help='String similarity measurement to use: levenshtein, jaro_winkler, cosine, dices_coefficient, jaccard, lcs_ratio, sorensen_dice_coefficient')

args = parser.parse_args()

# Function to read file content or return string as is
def read_file_or_string(path):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    return path

# Get the two texts
text1 = read_file_or_string(args.text1)
text2 = read_file_or_string(args.text2)

# Function for longest common subsequence ratio
def lcs_ratio(s1, s2):
    lcs = textdistance.lcsseq(s1, s2)
    return len(lcs) / ((len(s1) + len(s2)) / 2)

# Define our measurements
measurements = {
    'levenshtein': textdistance.levenshtein,
    'jaro_winkler': textdistance.jaro_winkler,
    'cosine': textdistance.cosine,
    'dices_coefficient': textdistance.sorensen,
    'jaccard': textdistance.jaccard,
    'lcs_ratio': lcs_ratio,  # Replace 'longest_common_subsequence' with 'lcs_ratio'
    'sorensen_dice_coefficient': textdistance.sorensen_dice,
}

# Function to print measurement result
def print_measurement(name, func):
    print(f'{name}: {func(text1, text2)}')

# Get the measurement to use
measurement = args.measurement.lower()

# Perform the measurement
if measurement == 'all':
    for name, func in measurements.items():
        print_measurement(name, func)
else:
    if measurement in measurements:
        print_measurement(measurement, measurements[measurement])
    else:
        print(f'Invalid measurement: {measurement}. Valid options are: {list(measurements.keys())} or "all".')
