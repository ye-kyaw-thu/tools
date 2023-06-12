# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:39:57 2023
@author: Ye Kyaw Thu
Prepared for checking mes journal paper.
"""

import argparse
from spellchecker import SpellChecker
import re

def check_spelling_in_file(filename, filetype, output_filename=None, dictionary_filename=None, language='en', suggest='most'):
    # load spell checker
    spell = SpellChecker(language=language)
    # if a custom dictionary is specified, load it
    if dictionary_filename is not None:
        spell.word_frequency.load_text_file(dictionary_filename)

    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        if filetype == "tex":
            # Ignore LaTeX commands
            data = re.sub(r'\\[a-z]+', '', data)
        words = re.findall(r'\b\w+\b', data)

    # find those words that may be misspelled
    misspelled = spell.unknown(words)

    output = []
    for word in misspelled:
        output.append(f"Misspelled word: {word}")
        if suggest == 'most':
            output.append(f"Suggested correction: {spell.correction(word)}")
        else:
            candidates = spell.candidates(word)
            # if no candidates were found, use an empty list
            if candidates is None:
                candidates = []
            output.append(f"Other suggestions: {list(candidates)}")

    if output_filename is None:
        print("\n".join(output))
    else:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(output))

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Check the spelling in a file.")
    parser.add_argument("filename", help="The filename of the file to check.")
    parser.add_argument("--type", choices=["tex", "txt"], default="txt", help="The type of the file to check. Options are 'tex' and 'txt'. Default is 'txt'.")
    parser.add_argument("--output", default=None, help="The filename to output the results to. If not specified, prints to the console.")
    parser.add_argument("--dictionary", default=None, help="The filename of the custom dictionary to use. If not specified, uses the default dictionary.")
    parser.add_argument("--language", default='en', help="The language of the dictionary to use. Default is 'en' for English. Other options are 'es' for Spanish, 'ru' for Russian, 'ar' for Arabic, etc.")
    parser.add_argument("--suggest", '-s', default='most', choices=['most', 'likely'], help="Choose 'most' to get the most likely correction, or 'likely' to get a list of likely corrections. Default is 'most'.")

    args = parser.parse_args()

    # usage
    check_spelling_in_file(args.filename, args.type, args.output, args.dictionary, args.language, args.suggest)

if __name__ == "__main__":
    main()
