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

#def load_model(model_path):
#    with open(model_path, 'rb') as f:
#        model = dill.load(f)
#    return model

def load_model(model_path):
    with open(model_path, 'rb') as f:
        try:
            model = dill.load(f)
        except ModuleNotFoundError:
            f.seek(0)
            model = f.read()
    return model

def predict_next_word(model, sentence):
    tokens = sentence.lower().split()
    context = tuple(tokens[-(model.order-1):])

    predictions = []
    for word in model.vocab:
        prediction = model.logscore(word, context)
        predictions.append((word, prediction))

    predictions = sorted(predictions, key=lambda x: x[1], reverse=True)

    return [word for word, _ in predictions[:5]]

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
