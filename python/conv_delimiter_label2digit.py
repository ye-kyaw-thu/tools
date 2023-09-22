import csv
import sys
import argparse

def label_to_digit(data, header):
    # Create a mapping based on unique labels in the sentiment column
    unique_labels = sorted(set(row[1] for row in data))
    label_mapping = {label: idx for idx, label in enumerate(unique_labels)}

    digitized_data = []
    for row in data:
        text, sentiment = row
        sentiment_num = label_mapping[sentiment]
        digitized_data.append([text, sentiment_num])

    return [header] + digitized_data

def main():
    parser = argparse.ArgumentParser(description="Convert file formats and text labels to digits.")
    parser.add_argument("input_filename", help="Path to the input file.")
    parser.add_argument("output_filename", help="Path to the output file.")
    parser.add_argument("-f", "--from-delimiter", default=",", help="Original delimiter (default is ',').")
    parser.add_argument("-t", "--to-delimiter", default="\t", help="New delimiter (default is tab).")

    args = parser.parse_args()

    with open(args.input_filename, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=args.from_delimiter)
        data = list(reader)

    digitized_data = label_to_digit(data[1:], data[0])

    with open(args.output_filename, 'w', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=args.to_delimiter)
        writer.writerows(digitized_data)

    print(f"Processed data saved to {args.output_filename}")

if __name__ == "__main__":
    main()
