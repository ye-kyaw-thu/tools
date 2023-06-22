# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 08:57:10 2023
@author: Ye Kyaw Thu, LST, NECTEC, Thailand

Rule-based password generator (just my attempts for Burmese)

How to run:
python ./rule_based_password_gen.py -s syllable.txt -n number.txt -e extra.txt -r sen
python ./rule_based_password_gen.py -r se
python ./rule_based_password_gen.py -r nsnseses
"""

import argparse
import random

def read_file(filename):
    """Read a file and return a list of its lines.
    
    Args:
    filename: The name of the file to read.

    Returns:
    A list of lines from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]
    except IOError:
        print(f"Could not read file {filename}.")
        return []

def generate_password(syllables, numbers, extras, rule):
    """Generate a password using a rule-based approach.

    Args:
    syllables: The list of possible syllables.
    numbers: The list of possible numbers.
    extras: The list of possible special characters.
    rule: The rule to use for generating the password.

    Returns:
    The generated password as a string.
    """
    rule_dict = {
        's': syllables,
        'n': numbers,
        'e': extras,
    }

    password = []
    for char in rule:
        if char in rule_dict and rule_dict[char]:
            password.append(random.choice(rule_dict[char]))
        else:
            print(f"Invalid character '{char}' in rule or empty file for '{char}'.")
            return ""

    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='Generate a rule-based password.')
    parser.add_argument('-s', '--syllable', default='syllable.txt', 
                        help='The file name for the syllable list (default: syllable.txt).')
    parser.add_argument('-n', '--number', default='number.txt', 
                        help='The file name for the number list (default: number.txt).')
    parser.add_argument('-e', '--extra', default='extra.txt', 
                        help='The file name for the special characters list (default: extra.txt).')
    parser.add_argument('-r', '--rule', required=True, 
                        help='The rule for generating the password, for example "s+e+n+n".')
    args = parser.parse_args()

    syllables = read_file(args.syllable)
    numbers = read_file(args.number)
    extras = read_file(args.extra)

    # Generate and print the password
    password = generate_password(syllables, numbers, extras, args.rule)
    if password:
        print(password)

if __name__ == "__main__":
    main()
