## for searching/retrieving similar words
## last updated: 13 July 2023
## @author: Ye Kyaw Thu
## 
## How to use
## *** Getting embedding value/vector:  
## python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_tfidf.npz  -j ./corpus/segmentation-data-updated2_tfidf_features.json
##
## python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_word2vec.model
##
## python test_embedding.py -i "ကျောင်းသား"  -m ./corpus/segmentation-data-updated2_fasttext.model
##
## *** Retrieving top 10 similar words
## python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_tfidf.npz -j ./corpus/segmentation-data-updated2_tfidf_features.json -s -n 10
##
## python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_word2vec.model -s -n 10
##
## python test_embedding.py -i "မြန်မာ"  -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 10
##
## *** Retrieving top 5 similar words with input file
## python ./test_embedding.py -m ./corpus/segmentation-data-updated2_tfidf.npz -j ./corpus/segmentation-data-updated2_tfidf_features.json  -s -n 5 -f ./my_text.txt
##
## python ./test_embedding.py -m ./corpus/segmentation-data-updated2_word2vec.model  -s -n 5 -f ./my_text.txt
##
##python ./test_embedding.py -m ./corpus/segmentation-data-updated2_fasttext.model  -s -n 5 -f ./my_text.txt

import gensim
import argparse
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import load_npz
import json

def load_model(filename, feature_names_file='./corpus/segmentation-data-updated2_tfidf_features.json'):
    if filename.endswith("_fasttext.model"):
        model = gensim.models.FastText.load(filename)
    elif filename.endswith("_glove.model"):
        model = gensim.models.KeyedVectors.load_word2vec_format(filename, binary=False)
    elif filename.endswith("_word2vec.model"):
        model = gensim.models.Word2Vec.load(filename)
    elif filename.endswith("_tfidf.npz"):
        if feature_names_file is None:
            raise ValueError("Feature names file must be provided for TF-IDF model.")
        with open(feature_names_file, 'r') as f:
            feature_names = json.load(f)
        my_stop_words = ['၊', '။', '၏', '၍', '၌']  # Added Burmese stop words
        vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(), stop_words=my_stop_words, vocabulary=feature_names)  # Updated Vectorizer
        tfidf_embeddings = load_npz(filename)  # load the npz file
        model = (tfidf_embeddings, vectorizer)
    else:
        raise ValueError("Unsupported model type.")
    return model

def process_input_string(input_string, model):
    if isinstance(model, gensim.models.KeyedVectors) or isinstance(model, gensim.models.Word2Vec) or isinstance(model, gensim.models.FastText):
        try:
            vector = model.wv[input_string]
        except KeyError:
            print(f'"{input_string}" not found in model vocabulary.')
            vector = None
    elif isinstance(model, tuple):
        tfidf_embeddings, vectorizer = model
        feature_names = vectorizer.get_feature_names_out()
        try:
            word_index = np.where(feature_names == input_string)[0][0]
            vector = tfidf_embeddings[:, word_index].toarray().flatten()
        except (ValueError, IndexError):
            print(f'"{input_string}" not found in TF-IDF vocabulary.')
            vector = None
    else:
        raise ValueError("Unsupported model type.")
    return vector

def find_similar_words(input_string, model, number_of_words):
    similar_words = []
    if isinstance(model, gensim.models.KeyedVectors) or isinstance(model, gensim.models.Word2Vec) or isinstance(model, gensim.models.FastText):
        try:
            similar_words = model.wv.most_similar(input_string, topn=number_of_words)
        except KeyError:
            print(f'"{input_string}" not found in model vocabulary.')
    elif isinstance(model, tuple):
        tfidf_embeddings, vectorizer = model
        feature_names = vectorizer.get_feature_names_out()
        try:
            word_index = np.where(feature_names == input_string)[0][0]
            input_vector = tfidf_embeddings[:, word_index]
            similarity_scores = cosine_similarity(tfidf_embeddings.T, input_vector.T).flatten()
            top_similar_indices = np.argsort(similarity_scores)[::-1][:number_of_words]
            similar_words = [(feature_names[i], similarity_scores[i]) for i in top_similar_indices]
        except (ValueError, IndexError):
            print(f'"{input_string}" not found in TF-IDF vocabulary.')
    else:
        raise ValueError("Unsupported model type.")
    return similar_words

def process_input_file(filename, model, number_of_words, similarity):
    try:
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                if similarity:
                    similar_words = find_similar_words(line, model, number_of_words)
                    print(f'Top {number_of_words} similar words to "{line}" are: {similar_words}')
                else:
                    vector = process_input_string(line, model)
                    if vector is not None:
                        print(vector)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    parser = argparse.ArgumentParser(description="Test embedding models")
    parser.add_argument("-i", "--input", help="Input word")
    parser.add_argument("-m", "--model", required=True, help="Path to the model file")
    parser.add_argument("-s", "--similarity_words", action="store_true", help="Find similarity words")
    parser.add_argument("-n", "--number_of_words", type=int, default=5, help="Number of similarity words to retrieve")
    parser.add_argument("-f", "--filename", help="File containing words")
    parser.add_argument("-j", "--json_filename", help="Json file containing tf-idf features")

    args = parser.parse_args()

    model = load_model(args.model, args.json_filename)

    if args.filename:
        process_input_file(args.filename, model, args.number_of_words, args.similarity_words)
    elif args.input:
        if args.similarity_words:
            similar_words = find_similar_words(args.input, model, args.number_of_words)
            print(f'Top {args.number_of_words} similar words to "{args.input}" are: {similar_words}')
        else:
            vector = process_input_string(args.input, model)
            if vector is not None:
                print(vector)

if __name__ == "__main__":
    main()
