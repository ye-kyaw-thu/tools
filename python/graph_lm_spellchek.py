# -*- coding: utf-8 -*-
"""
@author: Ye Kyaw Thu, LU Lab., Myanmar
Testing graph+LM based spelling checking
Last updated: 9 July 2023
How to run:
python ./graph_spellcheck2.py -d ./corpus/dict.txt -e ./spell_err.txt -o checked.txt -m 6 -c ./corpus/mypos.txt -n 3

"""

import networkx as nx
import argparse
import os
import marisa_trie
import itertools
from collections import defaultdict
import pickle
import nltk

def generate_edit_graph(words, max_edit_distance):
    G = nx.Graph()
    G.add_nodes_from(words)
    
    for word1, word2 in itertools.combinations(words, 2):
        if is_within_edit_distance(word1, word2, max_edit_distance):
            G.add_edge(word1, word2)
            
    return G

def is_within_edit_distance(word1, word2, max_edit_distance):
    if abs(len(word1) - len(word2)) > max_edit_distance:
        return False
    else:
        return sum(a != b for a, b in zip(word1, word2)) <= max_edit_distance

def correct_spelling(graph, misspelled_word, language_model, preceding_word):
    try:
        lengths = nx.shortest_path_length(graph, misspelled_word)
        correct_word_candidates = [word for word in lengths if word != misspelled_word]
        if not correct_word_candidates: 
            return None

        # Choose the word that most commonly follows the preceding word according to the language model
        return max(correct_word_candidates, key=lambda x: language_model[(preceding_word, x)])

    except nx.NetworkXError:
        return None

def generate_language_model(corpus_file, n):
    language_model = defaultdict(int)
    with open(corpus_file, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for gram in nltk.ngrams(words, n):
                language_model[gram] += 1
    return language_model

def main():
    parser = argparse.ArgumentParser(description='Spelling correction based on Graph Theory, Network Flow, and N-gram Language Models.')
    parser.add_argument('-d', '--dictionary', help='Dictionary file name', required=True)
    parser.add_argument('-e', '--errors', help='Error words file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    parser.add_argument('-t', '--trie', help='Marisa Trie file name', default='marisa_trie.dat')
    parser.add_argument('-m', '--max_distance', help='Max edit distance', type=int, default=1)
    parser.add_argument('-c', '--corpus', help='Monolingual corpus file name', required=True)
    parser.add_argument('-l', '--lm', help='Language model file name', default='language_model.pickle')
    parser.add_argument('-n', '--ngram', help='N-gram size', type=int, default=2)

    args = parser.parse_args()

    if os.path.exists(args.trie):
        trie = marisa_trie.Trie().load(args.trie)
    else:
        with open(args.dictionary, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f]
            trie = marisa_trie.Trie(words)
            trie.save(args.trie)

    if os.path.exists(args.lm):
        with open(args.lm, 'rb') as f:
            language_model = pickle.load(f)
    else:
        language_model = generate_language_model(args.corpus, args.ngram)
        with open(args.lm, 'wb') as f:
            pickle.dump(language_model, f)

    with open(args.errors, 'r', encoding='utf-8') as f, open(args.output, 'w', encoding='utf-8') as out:
        for line in f:
            words = line.strip().split()
            for i, misspelled_word in enumerate(words):
                preceding_word = words[i-1] if i > 0 else None
                nearby_words = trie.keys(misspelled_word)
                G = generate_edit_graph(nearby_words + [misspelled_word], args.max_distance)
                correct_word = correct_spelling(G, misspelled_word, language_model, preceding_word)
                if correct_word:
                    out.write(f'The correction for "{misspelled_word}" is "{correct_word}"\n')
                else:
                    out.write(f'No correction found for "{misspelled_word}"\n')

if __name__ == "__main__":
    main()
