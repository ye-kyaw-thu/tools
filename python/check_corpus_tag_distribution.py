"""
For checking tag distributions.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 26 May 2024.
Usage: (py3.8) ye@lst-gpu-server-197:~/ye/exp/entc$ python ./check_corpus_tag_distribution.py --corpus ./data/my_news.shuf.txt
"""

import argparse
from collections import Counter

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

def main(corpus_file):
    corpus_counter = count_tags(corpus_file)
    print_distribution(corpus_counter, "Corpus")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find tag distribution in a corpus.")
    parser.add_argument('--corpus', type=str, required=True, help='Path to the corpus data file.')

    args = parser.parse_args()

    main(args.corpus)
