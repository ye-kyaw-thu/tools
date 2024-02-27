"""

for extracting .parquet files.
Written by Ye Kyaw Thu.
Last updated: 27 Feb 2024
Usage:
python parquet_extractor.py --parquet_file ./train-00000-of-00001-d3450385c0ae3f98.parquet

"""

import argparse
import os
import pandas as pd

def extract_parquet(parquet_filename):

    df = pd.read_parquet(parquet_filename)

    # Extract original filename without extension
    original_filename = os.path.splitext(os.path.basename(parquet_filename))[0]

    # Define output filename
    output_filename = f"{original_filename}.csv"

    # Write dataFrame to CSV format
    df.to_csv(output_filename, index=False)

    print(f"Parquet file '{parquet_filename}' extracted to '{output_filename}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from a Parquet file to CSV.")
    parser.add_argument("-p", "--parquet_filename", type=str, required=True, help="Input Parquet filename")
    args = parser.parse_args()

    extract_parquet(args.parquet_filename)
