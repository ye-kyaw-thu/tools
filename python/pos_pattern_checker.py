## Written by Ye Kyaw Thu, LU Lab., Myanmar
## for analysis on POS pattern combinations of Burmese
## Last updated: 27 Sept 2023
## How to run:
## python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: pron v END" 2> /dev/null | head
## python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: pron v END" 2> /dev/null | head
## python ./pos_pattern_checker.py ./pos_data/mypos-ver.3.0.nopipe.txt --pattern "pattern basic: pron n END" 2> /dev/null | head

import argparse
from textx import metamodel_from_file

# Define the DSL Grammar with myPOS tagset
grammar = """
Model: patterns*=Pattern;
Pattern: 'pattern' name=ID ':' elements*=ELEMENT 'END';
ELEMENT: 'abb' | 'adj' | 'adv' | 'conj' | 'fw' | 'int' | 'n' | 'num' | 'part' | 'ppm' | 'pron' | 'punc' | 'sb' | 'tn' | 'v';
"""

# Save the grammar to a temporary file
with open("temp.tx", "w", encoding="utf-8") as f:
    f.write(grammar)

# Load the grammar
mm = metamodel_from_file('temp.tx')

def matched_subsentence(sentence, pattern):
    words = sentence.split()
    pos_tags = [word.split('/')[1] for word in words]
    pattern_elements = [elem for elem in pattern.elements]

    # Find and return matched sub-pattern in sentences
    for i in range(len(pos_tags) - len(pattern_elements) + 1):
        if pos_tags[i:i+len(pattern_elements)] == pattern_elements:
            return ' '.join(words[i:i+len(pattern_elements)])
    return None

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Parse Burmese POS-tagged sentences against a pattern.")
    parser.add_argument("filename", type=str, help="Input filename with POS-tagged Burmese sentences.")
    parser.add_argument("-p", "--pattern", type=str, required=True, help="Pattern DSL string.")
    parser.add_argument("-o", "--output_filename", type=str, help="Output filename to save the results. Defaults to printing on screen.")
    args = parser.parse_args()

    # Parse the DSL pattern
    dsl_model = mm.model_from_str(args.pattern)

    # Read the input file
    with open(args.filename, "r", encoding="utf-8") as f:
        sentences = f.readlines()

    results = []
    # Check sentences against defined patterns
    for pattern in dsl_model.patterns:
        for sentence in sentences:
            match = matched_subsentence(sentence.strip(), pattern)
            if match:
                results.append(match)

    # Print results or save to a file
    if args.output_filename:
        with open(args.output_filename, "w", encoding="utf-8") as f:
            for result in results:
                f.write(result + "\n")
    else:
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
