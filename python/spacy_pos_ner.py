# -*- coding: utf-8 -*-
"""
Last Updated: Fri Jun 23 22:01:27 2023
@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

POS/NER tagger for English with Spacy Library.

Library Installation:
    pip install spacy
    python -m spacy download en_core_web_sm
    
How to run:
    python spacy_pos_ner.py -i input.txt -o output.txt -t pos -f left-to-right
    python spacy_pos_ner.py -i input.txt -o output.txt -t ner -f column

If you want tags only:
    python spacy_pos_ner.py -i input.txt -o output.txt -t pos -f left-to-right -to
    python spacy_pos_ner.py -i input.txt -o output.txt -t ner -f column -to

If you want tagged output to console, don't add -o or -output option. 
"""

import spacy
import argparse

def tag_text(input_file, output_file, tag_type, format_type, tags_only):
    nlp = spacy.load("en_core_web_sm")
    with open(input_file, 'r') as f:
        text = f.read()

    doc = nlp(text)
    entities = [(i, i.label_, i.start_char, i.end_char) for i in doc.ents]
    results = []

    if tag_type == 'pos':
        if format_type == 'column':
            for sent in doc.sents:
                for token in sent:
                    if not token.is_space:
                        results.append(f'{token.pos_}\n' if tags_only else f'{token.text}/{token.pos_}\n')
                results.append('\n')
        else:
            for sent in doc.sents:
                results.append(' '.join([f'{token.pos_}' if tags_only else f'{token.text}/{token.pos_}' for token in sent if not token.is_space]))
                results.append('\n')
    elif tag_type == 'ner':
        if format_type == 'column':
            for sent in doc.sents:
                for token in sent:
                    if not token.is_space:
                        entity = [i for i in entities if i[2] <= token.idx < i[3]]
                        if entity:
                            results.append(f'{entity[0][1]}\n' if tags_only else f'{token.text}/{entity[0][1]}\n')
                        else:
                            results.append('O\n' if tags_only else f'{token.text}/O\n')
                results.append('\n')
        else:
            for sent in doc.sents:
                tagged_tokens = []
                for token in sent:
                    if not token.is_space:
                        entity = [i for i in entities if i[2] <= token.idx < i[3]]
                        if entity:
                            tagged_tokens.append(f'{entity[0][1]}' if tags_only else f'{token.text}/{entity[0][1]}')
                        else:
                            tagged_tokens.append('O' if tags_only else f'{token.text}/O')
                results.append(' '.join(tagged_tokens))
                results.append('\n')

    if output_file:
        with open(output_file, 'w') as f:
            f.writelines(results)
    else:
        print(''.join(results))

def main():
    parser = argparse.ArgumentParser(description='POS or NER tagging for English text.')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=False)
    parser.add_argument('-t', '--tag', help='Tag type (pos or ner)', required=True)
    parser.add_argument('-f', '--format', help='Output format (column or left-to-right)', required=False, default='column')
    parser.add_argument('-to', '--tags-only', help='Output only tags without words', required=False, action='store_true')
    args = parser.parse_args()

    tag_text(args.input, args.output, args.tag, args.format, args.tags_only)

if __name__ == '__main__':
    main()
