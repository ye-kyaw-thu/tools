# -*- coding: utf-8 -*-
"""
Last Updated on Mon Jun 26 16:09:47 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.

Example building of language model with NLTK library.

How to run:
python ..\nltk-lm.py -c mypos.txt -s stopwords.txt -n 3 -o mypos.3gram.txt -sm 1

Reference:
https://medium.com/swlh/language-modelling-with-nltk-20eac7e70853#6463

"""

import argparse
from nltk.util import ngrams
from nltk import FreqDist
from nltk.lm import Laplace, MLE
from nltk.lm.preprocessing import padded_everygram_pipeline
import dill

def load_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='utf-8') as f:
        return set(word.strip() for word in f)

def remove_stopwords(ngram_list, stop_words):
    return [ngram for ngram in ngram_list if any(word not in stop_words for word in ngram)]

def build_model(corpus_path, stopwords_path, n, model_path, binary, smoothing_value):
    stop_words = load_stopwords(stopwords_path)
    ngram_list = []
    tokenized_text = []

    # Read the corpus
    with open(corpus_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

    for sentence in lines:
        sentence = sentence.lower()
        sequence = [word for word in sentence.split() if word != '.']
        ngram_list.extend(list(ngrams(sequence, n)))
        tokenized_text.append(sequence)

    ngram_list = remove_stopwords(ngram_list, stop_words)
    freq_dist = FreqDist(ngram_list)

    print(f"Most common {n}-grams: ", freq_dist.most_common(5))

    # Train the model
    if smoothing_value == 1:
        model = Laplace(n)
    else:
        model = MLE(n)

    # Prepare the data for the model
    train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
    model.fit(train_data, padded_sents)

    # Save the model
    if binary:
        with open(model_path, 'wb') as f:
            dill.dump(model, f)
    else:
        with open(model_path, 'w', encoding='utf-8') as f:
            for ngram, freq in freq_dist.items():
                f.write(f"{ngram} {freq}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a language model.')
    parser.add_argument('-c', '--corpus', help='Path to the corpus file.', required=True)
    parser.add_argument('-s', '--stopwords', help='Path to the stopwords file.', required=True)
    parser.add_argument('-n', '--ngram', help='Ngram value.', type=int, default=2)
    parser.add_argument('-o', '--output', help='Path to the output model file.', required=True)
    parser.add_argument('-b', '--binary', help='Whether to save the model in binary format.', action='store_true')
    parser.add_argument('-sm', '--smoothing', help='Smoothing value.', type=int, default=0)
    args = parser.parse_args()

    build_model(args.corpus, args.stopwords, args.ngram, args.output, args.binary, args.smoothing)
