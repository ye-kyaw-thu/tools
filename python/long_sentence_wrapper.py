"""

To wrap long sentences.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 29 Dec 2023

"""

import argparse
import sys

def wrap_sentence(text, num_words):
    words = text.split()
    wrapped_sentences = []
    current_sentence = []

    for word in words:
        current_sentence.append(word)
        if len(current_sentence) >= num_words:
            wrapped_sentences.append(' '.join(current_sentence))
            current_sentence = []

    if current_sentence:
        wrapped_sentences.append(' '.join(current_sentence))

    return wrapped_sentences

def process_file(input_path, output_path, num_words):
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    wrapped_lines = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if line:
            wrapped_sentences = wrap_sentence(line, num_words)
            wrapped_lines.extend(wrapped_sentences)

    wrapped_text = '\n'.join(wrapped_lines)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(wrapped_text)
    else:
        print(wrapped_text)

def main():
    parser = argparse.ArgumentParser(description='Wrap sentences in a text file.')
    parser.add_argument('-n', '--no_of_words', type=int, help='Number of words per sentence', required=True)
    parser.add_argument('-i', '--input', type=str, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')

    args = parser.parse_args()

    if not args.input:
        print("No input file provided. Exiting.")
        sys.exit(1)

    process_file(args.input, args.output, args.no_of_words)

if __name__ == "__main__":
    main()
