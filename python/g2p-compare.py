"""

for comparing the g2p model output and manually updated file.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 9 Mar 2024

Usage:
time python ./g2p-compare.py --original_file ./trans.my.syl.g2p.line.original \
--checked_file ./trans.my.normalized.syl.g2p.line.checked \
--extracted_file ./extract-line.txt

time python ./g2p-compare.py --original_file ./trans.my.syl.g2p.line.original \
--checked_file ./trans.my.normalized.syl.g2p.line.checked --word \
--extracted_file ./extract-word.txt

"""

import argparse

def load_file(filename):
    """Load the contents of a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def extract_differences(original_lines, checked_lines):
    """Extract the differences between two sets of lines."""
    differences = []
    for i, (orig_line, checked_line) in enumerate(zip(original_lines, checked_lines)):
        if orig_line != checked_line:
            differences.append((i+1, orig_line.strip(), checked_line.strip()))
    return differences

def format_differences(differences, word_level=False):
    """Format the differences for output."""
    formatted_diffs = []
    for line_num, orig_line, checked_line in differences:
        if word_level:
            orig_words = orig_line.split()
            checked_words = checked_line.split()
            for j, (orig_word, checked_word) in enumerate(zip(orig_words, checked_words)):
                if orig_word != checked_word:
                    formatted_diffs.append(f"{line_num}, {j+1}:\t{orig_word}\t{checked_word}\n")
        else:
            formatted_diffs.append(f"{line_num}, Original:\t{orig_line}\n"
                                   f"{line_num}, Checked:\t{checked_line}\n")
    return formatted_diffs

def save_to_file(data, filename):
    """Save the data to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(data)

def main():
    parser = argparse.ArgumentParser(description="Compare two G2P files and extract differences.")
    parser.add_argument('-o', '--original_file', help='Path to the original G2P file', required=True)
    parser.add_argument('-c', '--checked_file', help='Path to the manually checked G2P file', required=True)
    parser.add_argument('-e', '--extracted_file', help='Path to save the extracted differences')
    parser.add_argument('-w', '--word', action='store_true', help='Print differences at the word level')
    args = parser.parse_args()

    original_lines = load_file(args.original_file)
    checked_lines = load_file(args.checked_file)

    differences = extract_differences(original_lines, checked_lines)

    if args.extracted_file:
        formatted_diffs = format_differences(differences, args.word)
        save_to_file(formatted_diffs, args.extracted_file)
    else:
        for diff in format_differences(differences, args.word):
            print(diff)

if __name__ == "__main__":
    main()
