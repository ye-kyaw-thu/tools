## Written by Ye Kyaw Thu, Visiting Professor, NECTEC, Thailand
## Demo code for text generation with Markov Chain
## Last updated: 16 Nov 2023

import collections, random, sys, textwrap, argparse, json, os

def build_possibles(input_stream, n):
    possibles = collections.defaultdict(list)
    buffer = [''] * (n - 1)

    for line in input_stream:
        for word in line.split():
            possibles[tuple(buffer)].append(word)
            buffer.pop(0)
            buffer.append(word)

    buffer.append('')
    while len(buffer) > 1:
        possibles[tuple(buffer[:-1])].append(buffer[-1])
        buffer.pop(0)

    return possibles

def save_model(possibles, filename):
    # Convert tuple keys to strings
    possibles_serializable = {str(key): value for key, value in possibles.items()}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(possibles_serializable, file)

def load_model(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        possibles_serializable = json.load(file)
    # Convert string keys back to tuples
    return {eval(key): value for key, value in possibles_serializable.items()}

def generate_text(possibles, length, n, prefix=None):
    if prefix:
        words = prefix.split()
        # Create a tuple for the prefix. If it's shorter than expected, fill with empty strings
        if len(words) < n - 1:
            prefix_tuple = tuple([''] * (n - 1 - len(words)) + words)
        else:
            prefix_tuple = tuple(words[:n-1])

        if prefix_tuple in possibles:
            output = list(prefix_tuple)
        else:
            print("Warning: Prefix not found in model. Using a random prefix.")
            # Choose a random start if the prefix is not found
            output = list(random.choice([k for k in possibles if len(k) == n - 1]))
    else:
        # If no prefix is provided, start with a random prefix
        output = list(random.choice([k for k in possibles if len(k) == n - 1]))

    for _ in range(length - len(output)):
        next_word = random.choice(possibles[tuple(output[-(n - 1):])])
        output.append(next_word)

    return ' '.join(output)


def main():
    parser = argparse.ArgumentParser(description="Generate text using a Markov chain model.")
    parser.add_argument('--input', type=str, help="Input file name for training")
    parser.add_argument('--output', type=str, help="Output file name for generated text")
    parser.add_argument('--ngram', type=int, default=2, help="Size of the n-gram. For generation, this must match the n-gram size used during training.")
    parser.add_argument('--length', type=int, default=100, help="Length of the generated text")
    parser.add_argument('--prefix', type=str, help="Custom prefix for text generation")
    parser.add_argument('--mode', choices=['training', 'generation'], required=True, help="Mode: training or generation")
    parser.add_argument('--model_filename', type=str, help="Model file name")

    args = parser.parse_args()

    if args.mode == 'training':
        if not args.input:
            raise ValueError("Input file is required for training mode.")
        input_stream = open(args.input, 'r', encoding='utf-8') if args.input != sys.stdin else sys.stdin
        possibles = build_possibles(input_stream, args.ngram)
        model_filename = args.model_filename if args.model_filename else f"{args.ngram}gram_model.json"
        save_model(possibles, model_filename)
        if input_stream != sys.stdin:
            input_stream.close()

    elif args.mode == 'generation':
        if not args.model_filename:
            raise ValueError("Model file name is required for generation mode.")
        if not os.path.exists(args.model_filename):
            raise ValueError("Model file does not exist.")
        # Extract n-gram size from the model filename
        trained_ngram_size = int(args.model_filename.split('gram')[0][-1])
        if args.ngram != trained_ngram_size:
            raise ValueError(f"Generation n-gram size must match training n-gram size ({trained_ngram_size}).")
        possibles = load_model(args.model_filename)
        text = generate_text(possibles, args.length, args.ngram, args.prefix)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(textwrap.fill(text))
        else:
            print(textwrap.fill(text))

if __name__ == "__main__":
    main()
