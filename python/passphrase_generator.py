# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 07:40:50 2023
@author: Ye Kyaw Thu, LST, NECTEC, Thailand

Testing passphrase generator

How to run:
python passphrase_generator.py word-my.txt
python passphrase_generator.py word-my.txt -s
python passphrase_generator.py word-my.txt -s -n 3

"""

import argparse
import random

def generate_passphrase(words, num_words, include_spaces):
    """Generate a passphrase using a given list of words.
    
    Args:
    words: The list of possible words for the passphrase.
    num_words: The number of words to include in the passphrase.
    include_spaces: Boolean indicating whether to include spaces between words.

    Returns:
    The generated passphrase as a string.
    """
    if num_words > len(words):
        print("The number of words in passphrase is more than the available words. Please decrease the num_words.")
        return ""
    chosen_words = random.sample(words, num_words)
    separator = ' ' if include_spaces else ''
    return separator.join(chosen_words)

def main():
    parser = argparse.ArgumentParser(description='Generate a passphrase from a list of words.')
    parser.add_argument('wordlist', help='The file name of the word list.')
    parser.add_argument('-n', '--num_words', type=int, default=3, 
                        help='The number of words in the passphrase (default: 3).')
    parser.add_argument('-s', '--space', action='store_true',
                        help='Include spaces between words.')
    args = parser.parse_args()
    
    # Read the word list file
    try:
        with open(args.wordlist, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f]
    except IOError:
        print(f"Could not read word list file {args.wordlist}.")
        return
    
    # Generate and print the passphrase
    passphrase = generate_passphrase(words, args.num_words, args.space)
    if passphrase:
        print(passphrase)

if __name__ == "__main__":
    main()
