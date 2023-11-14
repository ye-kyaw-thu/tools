## Written by Ye Kyaw Thu, LU Lab., Myanmar
## Last updated: 14 Nov 2023
## for extracting syllable pairs based on the mutual information

import argparse
import nltk
from nltk import ngrams
from nltk.probability import FreqDist
from collections import defaultdict
import math

def mutual_information_score(word_fd, ngram_fd, total_ngrams, ngram):
    """Compute Mutual Information score for a given n-gram."""
    p_w1 = word_fd[ngram[0]] / total_ngrams
    p_w2 = word_fd[ngram[-1]] / total_ngrams
    p_w1_w2 = ngram_fd[ngram] / total_ngrams
    return math.log(p_w1_w2 / (p_w1 * p_w2))

def extract_collocations(corpus_file, ngram_size=2, min_count=1):
    """Extract collocations using Mutual Information from a given corpus file."""
    with open(corpus_file, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = text.split()
    word_fd = FreqDist(tokens)
    ngram_fd = FreqDist(ngrams(tokens, ngram_size))
    total_ngrams = sum(ngram_fd.values())

    collocations = defaultdict(float)
    for ngram in ngram_fd:
        if 2 <= len(ngram) <= 7 and ngram_fd[ngram] >= min_count:
            score = mutual_information_score(word_fd, ngram_fd, total_ngrams, ngram)
            collocations[ngram] = score

    return sorted(collocations.items(), key=lambda item: item[1], reverse=True)

def output_collocations(collocations, output_file=None):
    """Output collocations to stdout or a file."""
    lines = [f"{' '.join(ngram)}: {score}" for ngram, score in collocations]
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(lines))
    else:
        for line in lines:
            print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='N-Gram Collocation Extraction with Mutual Information (Supports 2 to 7-grams)')
    parser.add_argument('-f', '--file', type=str, default='burmese_corpus.txt', help='Path to the syllable-segmented corpus file')
    parser.add_argument('-n', '--ngram', type=int, default=2, choices=range(2, 8), help='Size of the n-gram (2 to 7)')
    parser.add_argument('-o', '--output', type=str, help='Optional output file to write the collocations')
    parser.add_argument('-c', '--count', type=int, default=1, help='Minimum count of co-occurrences to be considered for MI calculation')
    args = parser.parse_args()

    collocations = extract_collocations(args.file, args.ngram, args.count)
    output_collocations(collocations, args.output)
