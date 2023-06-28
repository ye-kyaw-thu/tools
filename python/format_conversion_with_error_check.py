
"""
Last updated on Wed Jun 28 18:05:25 2023
@author: Ye Kyaw Thu, Visiting Professor, NECTEC, Thailand

How to run:

Error checking for test-NER corpus (crf or top-down format):
\crf>python ..\..\..\..\format_conversion_with_error_check.py test.ner tmp.out -f left-to-right -l labels.txt -e tmp-error.out -d " "
Found 28 lines with format errors. Details are written to 'tmp-error.out' if provided.
    
Error checking for test-NER corpus (left-to-right format):
\ltor>python ..\..\..\..\format_conversion_with_error_check.py test.ner tmp.out -f top-down -l labels.txt -e tmp-error.out -d "/"
Found 73 lines with format errors. Details are written to 'tmp-error.out' if provided.

Testing with a small corpus (without error):
python ..\..\..\..\format_conversion_with_error_check.py tmp.out tmp.out.crf -f top-down -l labels.txt -d "/" -e tmp-error.out
python ..\..\..\..\format_conversion_with_error_check.py tmp.out.crf tmp.out.ltr -f left-to-right -l labels.txt -d " " -e tmp-error.out
"""


import argparse
import pandas as pd

def load_labels(label_filename):
    with open(label_filename, 'r', encoding='utf-8') as f:
        labels = set(f.read().split())
    return labels

def check_format_error(lines, format_type, error_filename, labels, delimiter):
    error_lines = []
    sentence_num = 1  
    for idx, line in enumerate(lines):
        tokens = line.strip().split()
        #print(tokens)
        if format_type == 'top-down':
            if line.strip():  
                if len(tokens) != 2 or any(not t for t in tokens) or tokens[1] not in labels:
                    error_lines.append((sentence_num, idx + 1, line))
            else:  # if the line is empty
                sentence_num += 1
        elif format_type == 'left-to-right':
            if line.strip():  
                for token_no, token in enumerate(tokens, 1):
                    parts = token.split(delimiter)
                    if len(parts) != 2 or parts[0] == '' or parts[1] not in labels:
                        error_lines.append((sentence_num, token_no, token+"\n"))
            sentence_num += 1  # increment sentence_num for each new line

    if error_filename and error_lines:
        with open(error_filename, "w", encoding='utf-8') as f:
            for sent_no, token_no, token in error_lines:
                f.write(f"Sentence {sent_no}, Token {token_no}: {token}")
    elif not error_filename and error_lines:
        for sent_no, token_no, token in error_lines:
            print(f"Sentence {sent_no}, Token {token_no}: {token}")

    return error_lines


def convert_crf_to_ltr(df):
    ltr_data = []
    current_sentence = []
    #print(df)
    for row in df.itertuples():
        #print(row)
        if pd.isna(row.labels):
            ltr_data.append(current_sentence)
            #print("append: ", current_sentence)
            #print(length(ltr_data))
            current_sentence = []
        else:
            current_sentence.append(f"{row.words}/{row.labels}")
    #print(ltr_data)
    return [" ".join(sentence) for sentence in ltr_data]

def convert_ltr_to_crf(lines):
    crf_data = []
    for line in lines:
        for token in line.split():
            parts = token.split("/")
            if len(parts) != 2:
                print(f"Error: token '{token}' in line '{line}' does not have exactly one '/'")
                continue
            word, label = parts
            crf_data.append((word, label))
        crf_data.append(("", ""))
    return pd.DataFrame(crf_data, columns=["words", "labels"])

def main(input_file, output_file, format_type, error_filename, label_filename, delimiter):
    with open(input_file, "r", encoding='utf-8') as f:
        lines = f.readlines()

    labels = load_labels(label_filename)

    input_format_type = 'top-down' if format_type == 'left-to-right' else 'left-to-right'
    error_lines = check_format_error(lines, input_format_type, error_filename, labels, delimiter)

    if error_lines:
        print(f"Found {len(error_lines)} lines with format errors. Details are written to '{error_filename}' if provided.")
        return

    if format_type == 'top-down':
        #print("td")
        df = convert_ltr_to_crf(lines)
        df.to_csv(output_file, sep=" ", index=False, header=False)
    elif format_type == 'left-to-right':
        #print("ltr")
        df = pd.read_csv(input_file, sep=delimiter, names=["words", "labels"], skip_blank_lines=False)
        #print(df)
        ltr_data = convert_crf_to_ltr(df)
        #print(ltr_data)
        with open(output_file, "w", encoding='utf-8') as f:
            for line in ltr_data:
                f.write(line + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert between CRF and left-to-right formats.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    parser.add_argument('-d', '--delimiter', type=str, required=True, help='Delimiter between word and tag')
    parser.add_argument('-f', '--format', type=str, required=True, 
                        choices=['top-down', 'left-to-right'], help='Format of the output file')
    parser.add_argument('-e', '--error_filename', type=str, required=False,
                        help='Filename to write error details to')
    parser.add_argument('-l', '--label_filename', type=str, required=True,
                        help='Filename for valid labels')
    args = parser.parse_args()
    main(args.input_file, args.output_file, args.format, args.error_filename, args.label_filename, args.delimiter)
