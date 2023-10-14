## Written by Ye, LU Lab., Myanmar
## for checking NER tagged data
## Last updated: 28 Sept 2023

import sys
import argparse

def analyze_corpus(filename, format_option):
    # Initialize counters and dictionaries
    sentences_without_entities = 0
    tag_frequency = {}
    total_tags = 0

    # Open and read the corpus file line by line
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            tags = [token.split('/')[-1] for token in line.split()]

            if format_option == "abstract":
                # Converting the B, I, E and S tags to the general category
                #tags = ['O' if tag == 'O' else tag.split('-')[1] for tag in tags]
                tags = ['O' if tag == 'O' else (tag.split('-')[1] if '-' in tag else 'UNKNOWN') for tag in tags]


            unique_tags = set(tags)

            # Check if only the O tag is present in the sentence
            if unique_tags == {'O'}:
                sentences_without_entities += 1

            # Count the frequency of each tag
            for tag in tags:
                tag_frequency[tag] = tag_frequency.get(tag, 0) + 1
                total_tags += 1

    # Generate the report
    report = f"Analysis of '{filename}'\n"
    report += "-" * 40 + "\n"
    report += f"1. Number of sentences without named entities: {sentences_without_entities}\n"
    report += "2. Frequency of each tag:\n"
    for tag, count in sorted(tag_frequency.items()):
        report += f"   {tag}: {count}\n"
    report += "3. Distribution of each tag:\n"
    for tag, count in sorted(tag_frequency.items()):
        percentage = (count / total_tags) * 100
        report += f"   {tag}: {percentage:.2f}%\n"

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze NER tagged data.')
    parser.add_argument('filename', type=str, help='Path to the input file.')
    parser.add_argument('-f', '--format', type=str, choices=['abstract', 'detailed'], default='detailed', help='Output format. "abstract" to consider all B, I, E, S tags as one tag; "detailed" for detailed tags.')

    args = parser.parse_args()

    result = analyze_corpus(args.filename, args.format)
    print(result)
