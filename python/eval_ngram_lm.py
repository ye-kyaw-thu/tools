"""

Evaluation on ngram LM with test file.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 11 Feb 2024

Usage:
time python ./eval_ngram_lm.py --language_model ./model/5gram.arpa \
--vocab_file ./corpus/vocab.txt --test_data ./corpus/test1.txt --perplexity

time python ./eval_ngram_lm.py --language_model ./model/5gram.arpa \
--vocab_file ./corpus/vocab.txt --test_data ./corpus/test1.txt --perplexity

Reference:
https://tiefenauer.github.io/blog/wiki-n-gram-lm/#training-the-lm
https://thegradient.pub/author/chip/

"""

import argparse
import kenlm

def load_vocab(vocab_file):
    vocab = set()
    with open(vocab_file, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            vocab.add(word)

    # Check if <s> and </s> are not present in the vocabulary, then add them
    if '<s>' not in vocab:
        vocab.add('<s>')
    if '</s>' not in vocab:
        vocab.add('</s>')

    return vocab

def evaluate_language_model(lm_path, vocab_path, test_data_path, calculate_perplexity):
    model = kenlm.LanguageModel(lm_path)
    vocab = load_vocab(vocab_path)

    num_sentences = 0
    num_words = 0
    total_logprob = 0
    total_oov = 0

    with open(test_data_path, 'r', encoding='utf-8') as f:
        for line in f:
            sentence = line.strip()

            # Prepend <s> and append </s> to the sentence
            sentence = '<s> ' + sentence + ' </s>'

            num_sentences += 1

            # Get OOV words in the sentence
            oov_words = [word for word in sentence.split() if word not in vocab]
            oov_count = len(oov_words)
            total_oov += oov_count

            num_words += len(sentence.split())

            logprob = model.score(sentence)
            total_logprob += logprob

            print(f'Sentence: {sentence}')
            print(f'Log Probability Score: {logprob}')
            print(f'OOV Words: {", ".join(oov_words)}')
            print(f'Number of OOV words: {oov_count}')

            # Generate suggestions for the next word
            if not calculate_perplexity:
                words = sentence.split()
                prefix = ' '.join(words[:-1])
                suggestions = [(model.score(prefix + ' ' + next_word), next_word) for next_word in vocab]
                suggestions.sort(reverse=True)

                print("Next word suggestions:")
                for score, word in suggestions[:5]:
                    print(f'\t{word}\tScore: {score}')

                print()

    if calculate_perplexity:
        print(f"\n{num_sentences} sentences, {num_words} words")
        print(f"logprob= {total_logprob}")

    print(f"Total number of OOV words: {total_oov}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a language model.")
    parser.add_argument("-l", "--language_model", required=True, help="Path to the KenLM language model file")
    parser.add_argument("-v", "--vocab_file", required=True, help="Path to the vocabulary file")
    parser.add_argument("-t", "--test_data", required=True, help="Path to the test data file")
    parser.add_argument("-p", "--perplexity", action="store_true", help="Calculate perplexity")
    args = parser.parse_args()

    evaluate_language_model(args.language_model, args.vocab_file, args.test_data, args.perplexity)
