## Written by Ye Kyaw Thu, LU Lab., Myanmar
## For conversion between 23 and 9 NER tagsets
## The mapping table was prepared by my master student Kaung Lwin Thant
## Last updated: 7 Dec 2023

## How to run:
## python ./NER_23to9_conv.py --input train_23tag.txt --output train_9tag.txt

import argparse

# Define the mapping from 23 NER tags to 9 NER tags
ner_tag_mapping = {
    'S-PER': 'S-PER',
    'B-PER': 'B-PER',
    'I-PER': 'I-PER',
    'E-PER': 'E-PER',
    'S-GPE': 'S-LOC',
    'B-GPE': 'B-LOC',
    'I-GPE': 'I-LOC',
    'E-GPE': 'E-LOC',
    'S-LOC': 'S-LOC',
    'B-LOC': 'B-LOC',
    'I-LOC': 'I-LOC',
    'E-LOC': 'E-LOC',
    'S-ORG': 'S-ORG',
    'B-ORG': 'B-ORG',
    'I-ORG': 'I-ORG',
    'E-ORG': 'E-ORG',
    'S-NOP': 'S-ORG',
    'B-NOP': 'B-ORG',
    'I-NOP': 'I-ORG',
    'E-NOP': 'E-ORG',
    'S-REL': 'O',
    'B-REL': 'O',
    'I-REL': 'O',
    'E-REL': 'O',
    'S-DATE': 'S-DATE',
    'B-DATE': 'B-DATE',
    'I-DATE': 'I-DATE',
    'E-DATE': 'E-DATE',
    'S-TIME': 'S-TIME',
    'B-TIME': 'B-TIME',
    'I-TIME': 'I-TIME',
    'E-TIME': 'E-TIME',
    'S-FOOD': 'O',
    'B-FOOD': 'O',
    'I-FOOD': 'O',
    'E-FOOD': 'O',
    'S-PROD': 'S-PRODUCT',
    'B-PROD': 'B-PRODUCT',
    'I-PROD': 'I-PRODUCT',
    'E-PROD': 'E-PRODUCT',
    'S-LAW': 'O',
    'B-LAW': 'O',
    'I-LAW': 'O',
    'E-LAW': 'O',
    'S-ENT': 'O',
    'B-ENT': 'O',
    'I-ENT': 'O',
    'E-ENT': 'O',
    'S-BOOK': 'O',
    'B-BOOK': 'O',
    'I-BOOK': 'O',
    'E-BOOK': 'O',
    'S-SPORT': 'O',
    'B-SPORT': 'O',
    'I-SPORT': 'O',
    'E-SPORT': 'O',
    'S-JOB': 'O',
    'B-JOB': 'O',
    'I-JOB': 'O',
    'E-JOB': 'O',
    'S-MONEY': 'S-NUM',
    'B-MONEY': 'S-NUM',
    'I-MONEY': 'O',
    'E-MONEY': 'O',
    'S-ORDINAL': 'O',
    'B-ORDINAL': 'O',
    'I-ORDINAL': 'O',
    'E-ORDINAL': 'O',
    'S-PERCENT': 'S-NUM',
    'B-PERCENT': 'S-NUM',
    'I-PERCENT': 'O',
    'E-PERCENT': 'O',
    'S-NUM': 'S-NUM',
    'B-NUM': 'S-NUM',
    'I-NUM': 'O',
    'E-NUM': 'O',
    'S-DISEASE': 'O',
    'B-DISEASE': 'O',
    'I-DISEASE': 'O',
    'E-DISEASE': 'O',
    'S-DRUG': 'O',
    'B-DRUG': 'O',
    'I-DRUG': 'O',
    'E-DRUG': 'O',
    'S-EVENT': 'S-EVENT',
    'B-EVENT': 'B-EVENT',
    'I-EVENT': 'I-EVENT',
    'E-EVENT': 'E-EVENT',
    'S-LANG': 'O',
    'B-LANG': 'O',
    'I-LANG': 'O',
    'E-LANG': 'O'
}

def convert_ner_tags(input_file, output_file=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = infile.read().splitlines()
        
        converted_data = []

        for line in data:
            tokens = line.split()
            converted_tokens = []

            for token in tokens:
                parts = token.split('/')
                if len(parts) == 2:
                    ner_tag = parts[1]
                    if ner_tag in ner_tag_mapping:
                        converted_tag = ner_tag_mapping[ner_tag]
                        converted_token = f'{parts[0]}/{converted_tag}'
                        converted_tokens.append(converted_token)
                    else:
                        converted_tokens.append(token)
                else:
                    converted_tokens.append(token)

            converted_line = ' '.join(converted_tokens)
            converted_data.append(converted_line)

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write('\n'.join(converted_data))
        else:
            for line in converted_data:
                print(line)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert NER tags from 23 NER tagset to 9 NER tagset.")
    parser.add_argument("-i", "--input", required=True, help="Input file containing NER tagged data")
    parser.add_argument("-o", "--output", help="Output file for converted data (default is to print to console)")
    args = parser.parse_args()

    convert_ner_tags(args.input, args.output)
