# -*- coding: utf-8 -*-
"""
Last updated on Fri Jun 30 02:15:17 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.
How to run:  
For character unit ...  
python bidirectional_maximum_matching.py -i input-my.txt -o seg.out -d .\corpus\dict.txt -l 20

For syllable unit ...  
python bidirectional_maximum_matching.py -i input-my.txt -o seg.out -d .\corpus\dict.txt -l 20 -u syllable

Running with Bi-directional Maximum Matching Approach:

python bidirectional_maximum_matching.py -i input-my.txt -o seg.out -d .\corpus\dict.txt -l 20 -b
python bidirectional_maximum_matching.py -i input-my.txt -o seg.out -d .\corpus\dict.txt -l 20 -u syllable -b
"""

import argparse
from collections import defaultdict
import bisect
import re

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False

def add(root, word: list):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node.children.sort(key=lambda x: x.char)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix: list):
    node = root
    if not root.children:
        return False
    for char in prefix:
        char_not_found = True
        i = bisect.bisect_left([child.char for child in node.children], char)
        if i != len(node.children) and node.children[i].char == char:
            char_not_found = False 
            node = node.children[i]
        if char_not_found:
            return False
    return True

def max_match(sentence, node, longest):
    if not sentence:
        return []
    for i in range(min(len(sentence), longest), 0, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if find_prefix(node, first_word):
            return ["".join(first_word)] + max_match(remainder, node, longest)
    return [sentence[0]] + max_match(sentence[1:], node, longest)

def max_match_reverse(sentence, node, longest):
    if not sentence:
        return []
    for i in range(min(len(sentence), longest), 0, -1):
        first_word = sentence[-i:]
        remainder = sentence[:-i]
        if find_prefix(node, first_word):
            return max_match_reverse(remainder, node, longest) + ["".join(first_word)]
    return max_match_reverse(sentence[:-1], node, longest) + [sentence[-1]]

def syllable_breaking(text):
    myConsonant = r"က-အ"
    ssSymbol = r'္'
    aThat = r'်'
    BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"]))")
    text = BreakPattern.sub('|' + r"\1", text)
    syllables = text.split('|')
    syllables = [s.strip() for s in syllables]  # Remove leading and trailing spaces
    return syllables

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Word segmentation for Burmese language')
    parser.add_argument('-i', '--input', type=str, default='input.txt', help='input file')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='output file')
    parser.add_argument('-d', '--dictionary', type=str, default='dictionary.txt', help='dictionary file')
    parser.add_argument('-l', '--longest', type=int, default=2, help='longest word')
    parser.add_argument('-u', '--unit', type=str, default='character', help='unit for segmentation')
    parser.add_argument('-b', '--bidirectional', default=False, action=argparse.BooleanOptionalAction, help='bidirectional segmentation')
    args = parser.parse_args()

    root = TrieNode('*')
    with open(args.dictionary, 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.strip()
            if args.unit == 'syllable':
                word = syllable_breaking(word)
            add(root, word)
   
    with open(args.input, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    output_data = []
    for line in input_data:
        if args.unit == 'syllable':
            line = syllable_breaking(line)
        if args.bidirectional:
            forward = max_match(line, root, args.longest)
            reverse = max_match_reverse(line, root, args.longest)
            output_data.append(forward if len(forward) < len(reverse) else reverse)
        else:
            output_data.append(max_match(line, root, args.longest))

    output_data = '\n'.join([' '.join(line) for line in output_data])

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(output_data)
