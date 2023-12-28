"""

For simulation of possible word segmentation.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 28 Dec 2023

How to use:
python ./ngram_segmentation.py --input ./corpus.txt --ngram 3
python ./ngram_segmentation.py --input ./corpus.txt --ngram 3 --output out
python ./ngram_segmentation.py --input ./corpus.txt --ngram 3 --output out --max 20

"""

import argparse
import itertools
import random

def segment_line(line, max_segment_length, max_sentences=None):
    """Segment the line into segments, each containing up to max_segment_length words."""
    words = line.split()
    n = len(words)

    def segment_helper(start, end):
        """Helper function to create segments."""
        if start == n:
            yield []
        elif start <= n:
            for mid in range(start + 1, min(start + max_segment_length, n) + 1):
                for segment in segment_helper(mid, end):
                    yield ["".join(words[start:mid])] + segment

    all_segments = [" ".join(result) for result in segment_helper(0, n)]
    if max_sentences and len(all_segments) > max_sentences:
        return random.sample(all_segments, max_sentences)
    return all_segments

def main():
    parser = argparse.ArgumentParser(description='N-gram Segmentation Script')
    parser.add_argument('--input', type=str, required=True, help='Input file path')
    parser.add_argument('--ngram', type=int, required=True, help='N-gram size')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('-m', '--max', type=int, help='Maximum number of sentences to generate per input line')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    segmented_lines = []
    for line in lines:
        line = line.strip()
        if line:
            segmented_lines.extend(segment_line(line, args.ngram, args.max))

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            for line in segmented_lines:
                file.write(line + '\n')
    else:
        for line in segmented_lines:
            print(line)

if __name__ == '__main__':
    main()
