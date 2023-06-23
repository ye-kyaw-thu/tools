# -*- coding: utf-8 -*-
"""
Last Updated: Fri Jun 23 23:05:46 2023
@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

POS/NER tagger for Japanese with Spacy Library.

If you don't have:
    pip install spacy
    python -m spacy download ja_core_news_sm
    
How to run:

python spacy_pos_dep_jp.py -i jp-sentence.txt -t pos -f column    
python spacy_pos_dep_jp.py -i jp-sentence.txt -t dep -f column

python spacy_pos_dep_jp.py -i jp-sentence.txt -t pos -f left-to-right
python spacy_pos_dep_jp.py -i jp-sentence.txt -t dep -f left-to-right    

python spacy_pos_dep_jp.py -i jp-sentence.txt -t pos -f left-to-right -to
python spacy_pos_dep_jp.py -i jp-sentence.txt -t dep -f left-to-right -to    

Moreover, -o or --output option is for saving as a file.

"""

import spacy
import argparse

def tag_text(input_file, output_file, tag_type, format_type, tags_only):
    
    nlp = spacy.load("ja_core_news_sm")

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    doc = nlp(text)
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
    elif tag_type == 'dep':
        if format_type == 'column':
            for sent in doc.sents:
                for token in sent:
                    if not token.is_space:
                        results.append(f'{token.dep_}\n' if tags_only else f'{token.text}/{token.dep_}\n')
                results.append('\n')
        else:
            for sent in doc.sents:
                results.append(' '.join([f'{token.dep_}' if tags_only else f'{token.text}/{token.dep_}' for token in sent if not token.is_space]))
                results.append('\n')

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(results)
    else:
        print(''.join(results))

def main():
    parser = argparse.ArgumentParser(description='POS tagging for Japanese text.')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=False)
    parser.add_argument('-t', '--tag', help='Tag type (pos, dep)', required=True)
    parser.add_argument('-f', '--format', help='Output format (column or left-to-right)', required=False, default='column')
    parser.add_argument('-to', '--tags-only', help='Output only tags without words', required=False, action='store_true')
    args = parser.parse_args()

    tag_text(args.input, args.output, args.tag, args.format, args.tags_only)

if __name__ == '__main__':
    main()
