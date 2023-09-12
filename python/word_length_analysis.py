import sys

def analyze_word_lengths(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("No lines found in the input file.")
                return

            min_length = float('inf')
            max_length = 0
            min_length_sentences = []
            max_length_sentences = []

            for line_num, line in enumerate(lines, 1):
                words = line.split()  # Split line into words by spaces
                if words:
                    # Calculate word lengths
                    word_lengths = [len(word) for word in words]
                    line_length = sum(word_lengths)

                    # Update min_length and min_length_sentences
                    if line_length < min_length:
                        min_length = line_length
                        min_length_sentences = [(line_num, line)]
                    elif line_length == min_length:
                        min_length_sentences.append((line_num, line))

                    # Update max_length and max_length_sentences
                    if line_length > max_length:
                        max_length = line_length
                        max_length_sentences = [(line_num, line)]
                    elif line_length == max_length:
                        max_length_sentences.append((line_num, line))

            return min_length, max_length, min_length_sentences, max_length_sentences

    except FileNotFoundError:
        print(f"Couldn't open input file {file_path}!")

def main():
    if len(sys.argv) != 2:
        print("Usage: python word_length_analysis.py <input-file>")
        sys.exit(1)

    input_file = sys.argv[1]

    result = analyze_word_lengths(input_file)

    if result:
        min_length, max_length, min_length_sentences, max_length_sentences = result
        print(f"Minimum word length: {min_length}")
        print(f"Maximum word length: {max_length}")

        print("\nSentences with Minimum Word Length:")
        for line_num, sentence in min_length_sentences:
            print(f"Line {line_num}: {sentence.strip()}")

        print("\nSentences with Maximum Word Length:")
        for line_num, sentence in max_length_sentences:
            print(f"Line {line_num}: {sentence.strip()}")

if __name__ == "__main__":
    main()
