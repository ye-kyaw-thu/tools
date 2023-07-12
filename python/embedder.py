## for building tf-idf, word2vec and fasttext embedding models
## Note, input corpus should be word or syllable segmented
## last updated: 13 July 2023
## @author: Ye Kyaw Thu
## 
## How to use:
## Training with default parameters ...  
## time python ./embedder.py ./corpus/segmentation-data-updated2 -e tfidf
## time python ./embedder.py ./corpus/segmentation-data-updated2 -e word2vec
## time python ./embedder.py ./corpus/segmentation-data-updated2 -e fasttext

import os
import sys
import argparse
import gensim
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec, KeyedVectors
from gensim.models.fasttext import FastText
import pandas as pd
from scipy.sparse import save_npz

def read_corpus(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        document = file.readlines()
    return document

def preprocess(document):
    tokens = [line.split() for line in document]
    return tokens

def create_tfidf_embeddings(preprocessed_doc):
    my_stop_words = ['၊', '။', '၏', '၍', '၌']
    joined_sentences = [' '.join(sentence) for sentence in preprocessed_doc]
    vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(), stop_words=my_stop_words, use_idf=True, norm='l2')
    tfidf_embeddings = vectorizer.fit_transform(joined_sentences)
    return tfidf_embeddings, vectorizer

def create_word2vec_embeddings(preprocessed_doc, vector_size, window, min_count, workers):
    model = Word2Vec(preprocessed_doc, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    return model

def create_fasttext_embeddings(preprocessed_doc, vector_size, window, min_count, workers):
    model = FastText(preprocessed_doc, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    return model

def main():
    parser = argparse.ArgumentParser(description="Generate text embeddings")
    parser.add_argument("filename", help="Path to input text file. The output files will be saved under the same folder with the input corpus, and they will be named based on the input file's name and the embedding technique used.")
    parser.add_argument("-e", "--embedding", choices=["tfidf", "word2vec", "fasttext"], required=True, help="Embedding technique to use")
    parser.add_argument("-v", "--vector_size", type=int, default=100, help="Dimensionality of the word vectors (default: 100). Relevant for Word2Vec and FastText.")
    parser.add_argument("-w", "--window", type=int, default=5, help="Maximum distance between the current and predicted word within a sentence (default: 5). Relevant for Word2Vec and FastText.")
    parser.add_argument("-m", "--min_count", type=int, default=2, help="Ignores all words with total frequency lower than this (default: 2). Relevant for Word2Vec and FastText.")
    parser.add_argument("-j", "--workers", type=int, default=4, help="Use these many worker threads to train the model (default: 4). Relevant for Word2Vec and FastText.")
    args = parser.parse_args()

    document = read_corpus(args.filename)
    preprocessed_doc = preprocess(document)

    if args.embedding == "tfidf":
        tfidf_embeddings, vectorizer = create_tfidf_embeddings(preprocessed_doc)
        output_filename = os.path.splitext(args.filename)[0] + "_tfidf.npz"

        # Save TF-IDF embeddings
        save_npz(output_filename, tfidf_embeddings)
        print(f"TF-IDF embeddings have been saved to {output_filename}")

        # Save TF-IDF features into JSON file
        features_filename = os.path.splitext(args.filename)[0] + "_tfidf_features.json"
        features_list = vectorizer.get_feature_names_out().tolist()
        with open(features_filename, 'w', encoding='utf-8') as f:
            json.dump(features_list, f)
        print(f"TF-IDF features have been saved to {features_filename}")

    elif args.embedding == "word2vec":
        model = create_word2vec_embeddings(preprocessed_doc, args.vector_size, args.window, args.min_count, args.workers)
        output_filename = os.path.splitext(args.filename)[0] + "_word2vec.model"
        model.save(output_filename)
        print(f"Word2Vec model has been saved to {output_filename}")

    elif args.embedding == "fasttext":
        model = create_fasttext_embeddings(preprocessed_doc, args.vector_size, args.window, args.min_count, args.workers)
        output_filename = os.path.splitext(args.filename)[0] + "_fasttext.model"
        model.save(output_filename)
        print(f"FastText model has been saved to {output_filename}")

if __name__ == "__main__":
    main()
