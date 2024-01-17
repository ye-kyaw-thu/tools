"""

For prefix, suffix extraction.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 17 Jan 2024

How to run:
python ./prefix_suffix_extract.py --help


"""

import argparse

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def extract_prefixes_suffixes(dictionary, corpus, freq, delimiter, verbose):
    prefixes, suffixes = {}, {}

    for line in corpus:
        words = line.split()
        for word in words:
            for dict_word in dictionary:
                # Check for prefixes
                if word.startswith(dict_word):
                    suffix = word[len(dict_word):]
                    if suffix:
                        if verbose:
                            combination = f'{dict_word}+{suffix}'
                        else:
                            combination = dict_word
                        if combination not in prefixes:
                            prefixes[combination] = 0
                        prefixes[combination] += 1

                # Check for suffixes
                if word.endswith(dict_word):
                    prefix = word[:-len(dict_word)]
                    if prefix:
                        if verbose:
                            combination = f'{prefix}+{dict_word}'
                        else:
                            combination = dict_word
                        if combination not in suffixes:
                            suffixes[combination] = 0
                        suffixes[combination] += 1

    filtered_prefixes = {k: v for k, v in prefixes.items() if v >= freq}
    filtered_suffixes = {k: v for k, v in suffixes.items() if v >= freq}

    return filtered_prefixes, filtered_suffixes

def save_to_file(data, filename, delimiter):
    with open(filename, 'w', encoding='utf-8') as file:
        for item, freq in sorted(data.items()):
            file.write(f'{item}{delimiter}{freq}\n')

def main():
    parser = argparse.ArgumentParser(description='Extract prefixes and suffixes from a corpus based on a dictionary.')
    parser.add_argument('--dict', required=True, help='Path to the dictionary file.')
    parser.add_argument('--corpus', required=True, help='Path to the corpus file.')
    parser.add_argument('--prefix', required=True, help='Path to save the prefixes.')
    parser.add_argument('--suffix', required=True, help='Path to save the suffixes.')
    parser.add_argument('--freq', type=int, default=2, help='Minimum frequency for extraction (default: 2)')
    parser.add_argument('--delimiter', default='|||', help='Delimiter for output (default: "|||")')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode.')

    args = parser.parse_args()

    dictionary = read_file(args.dict)
    corpus = read_file(args.corpus)

    prefixes, suffixes = extract_prefixes_suffixes(dictionary, corpus, args.freq, args.delimiter, args.verbose)

    save_to_file(prefixes, args.prefix, args.delimiter)
    save_to_file(suffixes, args.suffix, args.delimiter)

if __name__ == "__main__":
    main()
