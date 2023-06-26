# -*- coding: utf-8 -*-
"""
Last updated on Mon Jun 26 17:24:36 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.
Next word prediction with language model.

How to run:
python ..\nltk-predict.py -m .\mypos.lm.txt

Reference:
https://medium.com/swlh/language-modelling-with-nltk-20eac7e70853#6463
"""

import argparse
import dill
import os
import codecs
import nltk

def load_model(model_path):
    _, ext = os.path.splitext(model_path)

    if ext == '.txt':
        model = {}
        with codecs.open(model_path, 'r', encoding='utf-8') as f:
            for line in f:
                ngram_str, count = line.rsplit(' ', 1)
                ngram = eval(ngram_str)  # convert string tuple to actual tuple
                model[ngram] = int(count)

        # determine the order of the model from the first key
        model['order'] = len(list(model.keys())[0])
    else:
        # assume it's a binary file
        with open(model_path, 'rb') as f:
            try:
                model = dill.load(f)
            except (_pickle.UnpicklingError, ModuleNotFoundError):
                f.seek(0)
                model = f.read()

    return model

def predict_next_word(model, sentence):
    tokens = sentence.lower().split()

    # Check if the model is an nltk.lm object
    if isinstance(model, nltk.lm.api.LanguageModel):
        context = tuple(tokens[-(model.order-1):])

        predictions = []
        for word in model.vocab:
            prediction = model.logscore(word, context)
            predictions.append((word, prediction))

        predictions = sorted(predictions, key=lambda x: x[1], reverse=True)

        return [word for word, _ in predictions[:5]]

    # Check if the model is a dictionary (from a text file)
    elif isinstance(model, dict):
        context = tuple(tokens[-(model['order']-1):])

        predictions = []
        for word in model:
            if word[:-1] == context:
                predictions.append((word[-1], model[word]))

        predictions = sorted(predictions, key=lambda x: x[1], reverse=True)

        return [word for word, _ in predictions[:5]]

    else:
        print("Unsupported model type.")
        return None



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict the next word using a language model.')
    parser.add_argument('-m', '--model', help='Path to the language model file.', required=True)
    args = parser.parse_args()

    model = load_model(args.model)

    print("Language model loaded successfully.")

    while True:
        user_input = input("Enter a sentence or phrase (or press 'q' to quit): ")

        if user_input == 'q':
            break

        predictions = predict_next_word(model, user_input)

        print(f"Next possible words: {predictions}")
