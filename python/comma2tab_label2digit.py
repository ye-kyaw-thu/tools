import csv
import sys

# Written by Ye Kyaw Thu, LU Lab., Myanmar
# How to run
# python comma2tab_label2digit.py ./sentiment_my_dataset.csv ./sentiment_my_dataset.tsv

if len(sys.argv) != 3:
    print("Usage: python script_name.py input_filename output_filename")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter='\t')

    header = next(reader)  # skip the header
    writer.writerow(header)

    for row in reader:
        text, sentiment = row
        sentiment_num = 0 if sentiment == "positive" else 1
        writer.writerow([text, sentiment_num])

print(f"Processed data saved to {output_filename}")
