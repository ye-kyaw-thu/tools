# -*- coding: utf-8 -*-
"""
conversion from left-to-right format to Spacy NER Json format

Last updated: 13 Jul, 2023
@author: Ye Kyaw Thu, LU Lab, Myanmar


How to run:
python convert_to_spacyNER_json.py --input .\corpus\mypos_5lines.txt --output mypos_5lines.json
"""

import argparse
import json

def parse_sentence(sentence: str):
    """Parse sentence into list of tuples (word, POS)"""
    tokens = sentence.strip().split()
    parsed_tokens = []
    for token in tokens:
        try:
            word, pos = token.rsplit("/", 1)
            parsed_tokens.append((word, pos))
        except ValueError:
            print(f"Could not parse token: {token}")
    return parsed_tokens

def convert_to_spacy_ner_format(input_file: str, output_file: str, unicode_repr: bool):
    TRAIN_DATA = []
    with open(input_file, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            parsed = parse_sentence(line)
            words, tags = zip(*parsed)

            # Create character-based offset tags
            entities = []
            offset = 0
            for word, tag in parsed:
                entities.append((offset, offset + len(word), tag))
                offset += len(word) + 1  # Plus one for space
            
            # If unicode_repr is True, use Unicode numbers representation of words
            sentence = ' '.join(words)
            if unicode_repr:
                sentence = " ".join(["_".join([str(ord(ch)) for ch in word]) for word in words])
                
            TRAIN_DATA.append((sentence, {'entities': entities}))

    # Save to JSON file
    with open(output_file, 'w', encoding='utf-8') as f_out:
        json.dump(TRAIN_DATA, f_out, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert POS tagged corpus to SpaCy NER format.")
    parser.add_argument("--input", "-i", type=str, required=True, help="Input file path")
    parser.add_argument("--output", "-o", type=str, required=True, help="Output file path")
    parser.add_argument("--unicode_repr", "-u", action="store_true", help="Use Unicode representation of words")
    args = parser.parse_args()

    convert_to_spacy_ner_format(args.input, args.output, args.unicode_repr)
