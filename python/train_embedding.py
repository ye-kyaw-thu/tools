"""

For training tfidf, cbow, skipgram, doc2vec, fasttext embeddings
Written by Ye Kyaw Thu, LST Lab., Myanmar
Last updated: 16 April 2024
Usage: python ./train_embedding.py --help

"""

import argparse
import os
import logging
from gensim.models import Word2Vec, FastText, Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from gensim.models.callbacks import CallbackAny2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import numpy as np

class EpochLogger(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 0
        self.loss_to_be_subed = 0

    def on_epoch_begin(self, model):
        logging.info("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()
        loss_now = loss - self.loss_to_be_subed
        self.loss_to_be_subed = loss
        logging.info("Epoch #{} end, loss: {}".format(self.epoch, loss_now))
        self.epoch += 1

def train_word_embedding(input_file, output_file, method, min_count=10, window=5, vector_size=100, epochs=5, workers=4, stopwords_file=None, verbose=False):
    # Set up logging
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt='%H:%M:%S', level=logging.INFO if verbose else logging.WARNING)

    # Load the word-segmented text file
    sentences = [line.strip().split() for line in open(input_file, 'r', encoding='utf-8')]

    # Load stopwords file if provided
    stopwords = None
    if stopwords_file:
        with open(stopwords_file, 'r', encoding='utf-8') as f:
            stopwords = [line.strip() for line in f]

    # Remove stopwords
    if method in ['cbow', 'skipgram', 'doc2vec', 'fasttext'] and stopwords:
        sentences = remove_stopwords(sentences, stopwords)

    # Check if the output file already exists
    if os.path.exists(output_file):
        overwrite = input(f"The file '{output_file}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Exiting without overwriting the existing file.")
            return

    callbacks = [EpochLogger()]

    if method in ['cbow', 'skipgram', 'doc2vec', 'fasttext']:
        # Train Word2Vec, Doc2Vec, or FastText model
        logging.info(f"Training {method.capitalize()} model...")
        model = train_word_embedding_method(sentences, method, min_count, window, vector_size, epochs, workers, callbacks)
        # Save the trained model
        save_word_embedding_model(model, output_file)
    elif method == 'tfidf':
        # Train TF-IDF model
        logging.info("Training TF-IDF model...")
        joined_sentences = [' '.join(sentence) for sentence in sentences]
        vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(), stop_words=stopwords, use_idf=True, norm='l2', min_df=min_count)
        tfidf_embeddings = vectorizer.fit_transform(joined_sentences)
        # Save TF-IDF model in JSON format
        save_tfidf_model_json(vectorizer.vocabulary_, output_file + '.json')

        # Save TF-IDF model in binary format
        save_tfidf_model_binary(tfidf_embeddings, output_file + '.bin')

        print(f"TF-IDF model saved to {output_file}.json and {output_file}.bin")
        return
    else:
        print("Invalid method selected. Please choose 'cbow', 'skipgram', 'doc2vec', 'fasttext', or 'tfidf'.")
        return

def train_word_embedding_method(sentences, method, min_count, window, vector_size, epochs, workers, callbacks):
    if method == 'cbow':
        return Word2Vec(sentences, sg=0, min_count=min_count, window=window, vector_size=vector_size, epochs=epochs, workers=workers, callbacks=callbacks)
    elif method == 'skipgram':
        return Word2Vec(sentences, sg=1, min_count=min_count, window=window, vector_size=vector_size, epochs=epochs, workers=workers, callbacks=callbacks)
    elif method == 'doc2vec':
        return Doc2Vec([TaggedDocument(doc, [i]) for i, doc in enumerate(sentences)], vector_size=vector_size, window=window, epochs=epochs, workers=workers, callbacks=callbacks)
    elif method == 'fasttext':
        return FastText(sentences, sg=1, min_count=min_count, window=window, vector_size=vector_size, epochs=epochs, workers=workers, callbacks=callbacks)

def save_word_embedding_model(model, output_file):
    # Save the trained model in binary format
    model.wv.save_word2vec_format(output_file + '.bin', binary=True)
    # Save the trained model in plain text format
    model.wv.save_word2vec_format(output_file + '.vec', binary=False)

def save_tfidf_model_json(vocabulary, output_file):
    # Save TF-IDF model vocabulary in JSON format
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False)

def save_tfidf_model_binary(tfidf_embeddings, output_file):
    # Save TF-IDF model in binary format
    np.save(output_file, tfidf_embeddings.toarray())

def remove_stopwords(sentences, stopwords):
    return [[word for word in sentence if word not in stopwords] for sentence in sentences]

def main():
    parser = argparse.ArgumentParser(description="Train Word Embeddings")
    parser.add_argument("input_file", help="Input file containing word-segmented text")
    parser.add_argument("--output", help="Output filename for the trained word embedding model", required=True)
    parser.add_argument("--method", choices=["tfidf", "cbow", "skipgram", "doc2vec", "fasttext"], default="cbow", help="Embedding method (default: cbow)")
    parser.add_argument("--min_count", type=int, default=10, help="Ignore all words with total frequency lower than this")
    parser.add_argument("--window", type=int, default=5, help="Maximum distance between the current and predicted word within a sentence")
    parser.add_argument("--vector_size", type=int, default=100, help="Dimensionality of the word vectors")
    parser.add_argument("--epochs", type=int, default=5, help="Number of iterations (epochs) over the corpus")
    parser.add_argument("--workers", type=int, default=4, help="Use these many worker threads to train the model (default: 4). Relevant for Word2Vec and FastText.")
    parser.add_argument("--stopwords_file", help="Filename containing stopwords (one word per line) in UTF-8 format")
    parser.add_argument("--verbose", action="store_true", help="Show training information")
    args = parser.parse_args()

    # Train word embedding model
    train_word_embedding(args.input_file, args.output, args.method, args.min_count, args.window, args.vector_size, args.epochs, args.workers, args.stopwords_file, args.verbose)

if __name__ == "__main__":
    main()
