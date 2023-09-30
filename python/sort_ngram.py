## Written by Ye, LU Lab., Myanmar
## Last updated: 30 Sept 2023
## for sorting ngram files

import argparse

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []
    for line in lines:
        parts = line.strip().split()
        ngram = ' '.join(parts[:-1])
        value = parts[-1]
        data.append([ngram, value])
    return data

def sort_data(data, key_index, reverse_order):
    # Additional diagnostic information
    for index, item in enumerate(data):
        try:
            _ = float(item[key_index]) if key_index == 1 else item[key_index]
        except ValueError as e:
            raise ValueError(f"Error processing item at line {index+1}: {item}. Error: {str(e)}")

    return sorted(data, key=lambda x: float(x[key_index]) if key_index == 1 else x[key_index], reverse=reverse_order)

def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(' '.join(line) + '\n')

def main():
    parser = argparse.ArgumentParser(description="Sort the ngram profile file.")
    parser.add_argument("filename", type=str, help="Input filename")
    parser.add_argument("-o", "--output", type=str, help="Output filename", default="")
    parser.add_argument("--sort_by", choices=["text", "value"], default="text", help="Choose the sorting column: text or value")
    parser.add_argument("--order", choices=["asc", "desc"], default="asc", help="Sorting order: asc or desc")

    args = parser.parse_args()

    data = load_data(args.filename)

    if args.sort_by == "text":
        key_index = 0
    else:
        key_index = 1  # we have only two columns

    reverse_order = args.order == "desc"
    sorted_data = sort_data(data, key_index, reverse_order)

    if args.output:
        write_to_file(sorted_data, args.output)
    else:
        for line in sorted_data:
            print(' '.join(line))

if __name__ == "__main__":
    main()
