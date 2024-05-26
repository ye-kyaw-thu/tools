"""
For checking tag distributions.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 26 May 2024.
Usage: (py3.8) ye@lst-gpu-server-197:~/ye/exp/entc$ python ./check_tag_distribution.py --train ./data/train.txt --valid ./data/valid.txt --test ./data/test.txt
"""

import argparse
from collections import Counter
import pandas as pd

def count_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tags = [line.split('\t')[0] for line in file if line.strip()]
    return Counter(tags)

def print_distribution(counter, name):
    total = sum(counter.values())
    print(f"\n{name} Tag Distribution:")
    print(f"{'Tag':<15}{'Count':<10}{'Percentage':<10}")
    for tag, count in counter.items():
        percentage = (count / total) * 100
        print(f"{tag:<15}{count:<10}{percentage:.2f}%")
    print(f"{'Total':<15}{total:<10}{'100.00%'}")

def main(train_file, valid_file, test_file):
    train_counter = count_tags(train_file)
    valid_counter = count_tags(valid_file)
    test_counter = count_tags(test_file)

    print_distribution(train_counter, "Training")
    print_distribution(valid_counter, "Validation")
    print_distribution(test_counter, "Test")

    all_tags = set(train_counter.keys()).union(set(valid_counter.keys()), set(test_counter.keys()))
    all_data = []

    for tag in all_tags:
        train_count = train_counter.get(tag, 0)
        valid_count = valid_counter.get(tag, 0)
        test_count = test_counter.get(tag, 0)
        all_data.append({'Tag': tag, 'Train': train_count, 'Valid': valid_count, 'Test': test_count})

    all_data_df = pd.DataFrame(all_data)

    print("\nCombined Tag Distribution:")
    print(all_data_df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check tag distribution in training, validation, and test datasets.")
    parser.add_argument('--train', type=str, required=True, help='Path to the training data file.')
    parser.add_argument('--valid', type=str, required=True, help='Path to the validation data file.')
    parser.add_argument('--test', type=str, required=True, help='Path to the test data file.')

    args = parser.parse_args()

    main(args.train, args.valid, args.test)
