"""
for dataset creation for various corss-validation.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 18 Mar 2024

Usage:
time python cv-split.py -i ./100.km -o ./holdout --method holdout --test_size 0.2
time python cv-split.py -i ./100.km -o ./5-fold --method kfold -k 5
time python cv-split.py -i ./100.km -o ./leave-one-out --method leaveoneout
time python cv-split.py -i ./100.km -o ./leave-p3-out --method leavepout -p 3
time python cv-split.py -i ./100.km -o ./s-5k-fold --method stratifiedkfold -k 5
time python cv-split.py -i ./100.km -o ./r3-5k-fold --method repeatedkfold \
-k 5 --n_repeats 3

"""

import argparse
import os
from sklearn.model_selection import KFold, LeaveOneOut, LeavePOut, StratifiedKFold, RepeatedKFold, train_test_split

def read_text_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def write_text_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(data)

def ensure_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def holdout_split(input_file, output_folder, test_size):
    ensure_output_folder(output_folder)
    data = read_text_file(input_file)
    train_data, test_data = train_test_split(data, test_size=test_size)
    write_text_file(train_data, os.path.join(output_folder, 'train.txt'))
    write_text_file(test_data, os.path.join(output_folder, 'test.txt'))

def kfold_split(input_file, output_folder, k_value):
    ensure_output_folder(output_folder)
    data = read_text_file(input_file)
    kf = KFold(n_splits=k_value)
    for i, (train_index, test_index) in enumerate(kf.split(data)):
        train_data = [data[j] for j in train_index]
        test_data = [data[j] for j in test_index]
        # Adjust index to start from 1 instead of 0
        write_text_file(train_data, os.path.join(output_folder, f'train_fold_{i+1}.txt'))
        write_text_file(test_data, os.path.join(output_folder, f'test_fold_{i+1}.txt'))

def leave_one_out_split(input_file, output_folder):
    ensure_output_folder(output_folder)
    data = read_text_file(input_file)
    loo = LeaveOneOut()
    for i, (train_index, test_index) in enumerate(loo.split(data)):
        train_data = [data[j] for j in train_index]
        test_data = [data[j] for j in test_index]
        write_text_file(train_data, os.path.join(output_folder, f'train_{i+1}.txt'))
        write_text_file(test_data, os.path.join(output_folder, f'test_{i+1}.txt'))

def leave_p_out_split(input_file, output_folder, p_value):
    ensure_output_folder(output_folder)
    data = read_text_file(input_file)
    lpo = LeavePOut(p=p_value)
    for i, (train_index, test_index) in enumerate(lpo.split(data)):
        train_data = [data[j] for j in train_index]
        test_data = [data[j] for j in test_index]
        write_text_file(train_data, os.path.join(output_folder, f'train_{i+1}.txt'))
        write_text_file(test_data, os.path.join(output_folder, f'test_{i+1}.txt'))

def stratified_kfold_split(input_file, output_folder, k_value):
    ensure_output_folder(output_folder)
    data = read_text_file(input_file)
    skf = StratifiedKFold(n_splits=k_value)
    for i, (train_index, test_index) in enumerate(skf.split(data, [0]*len(data))):
        train_data = [data[j] for j in train_index]
        test_data = [data[j] for j in test_index]
        write_text_file(train_data, os.path.join(output_folder, f'train_fold_{i+1}.txt'))
        write_text_file(test_data, os.path.join(output_folder, f'test_fold_{i+1}.txt'))

def repeated_kfold_split(input_file, output_folder, k_value, n_repeats):
    ensure_output_folder(output_folder)
    data = read_text_file(input_file)
    rkf = RepeatedKFold(n_splits=k_value, n_repeats=n_repeats)
    for i, (train_index, test_index) in enumerate(rkf.split(data)):
        train_data = [data[j] for j in train_index]
        test_data = [data[j] for j in test_index]
        write_text_file(train_data, os.path.join(output_folder, f'train_fold_{i+1}.txt'))
        write_text_file(test_data, os.path.join(output_folder, f'test_fold_{i+1}.txt'))

# Add other split methods as necessary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split input file based on specified cross-validation method")
    parser.add_argument("-i", "--input_file", type=str, help="Input file path")
    parser.add_argument("-o", "--output_folder", type=str, help="Output folder path")
    parser.add_argument("--method", type=str, choices=["holdout", "kfold", "leaveoneout", "leavepout", "stratifiedkfold", "repeatedkfold"], help="Cross-validation method")
    parser.add_argument("-k", "--k_value", type=int, help="Value of k for k-fold cross-validation")
    parser.add_argument("-p", "--p_value", type=int, help="Value of p for leave-p-out cross-validation")
    parser.add_argument("--test_size", type=float, help="Fraction of the dataset to include in the test split for holdout method")
    parser.add_argument("--n_repeats", type=int, help="Number of times cross-validator needs to be repeated")

    args = parser.parse_args()

    if args.method == "holdout":
        holdout_split(args.input_file, args.output_folder, args.test_size)
    elif args.method == "kfold":
        kfold_split(args.input_file, args.output_folder, args.k_value)
    elif args.method == "leaveoneout":
        leave_one_out_split(args.input_file, args.output_folder)
    elif args.method == "leavepout":
        leave_p_out_split(args.input_file, args.output_folder, args.p_value)
    elif args.method == "stratifiedkfold":
        stratified_kfold_split(args.input_file, args.output_folder, args.k_value)
    elif args.method == "repeatedkfold":
        repeated_kfold_split(args.input_file, args.output_folder, args.k_value, args.n_repeats)
