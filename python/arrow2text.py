"""
for converting arrow files to a plain text file or CSV file.
Written by Ye Kyaw Thu, LU Lab., Myanmar
How to use: python arrow2text.py <folder_path>
Last updated: 24 Nov 2024
"""

import os
import sys
from datasets import Dataset

def decide_output_format(column_names):
    """
    Decide whether to output as plain text or CSV based on the column structure.
    
    Args:
    - column_names (list): List of column names in the dataset.

    Returns:
    - str: "text" for plain text or "csv" for CSV format.
    """
    if len(column_names) == 1:
        return "text"
    return "csv"

def convert_arrow_file(arrow_file, output_folder):
    """
    Convert a single Arrow file to a plain text or CSV file.
    
    Args:
    - arrow_file (str): Path to the input Arrow file.
    - output_folder (str): Folder to save the output file.
    """
    # Load the dataset
    print(f"Converting: {arrow_file}")
    dataset = Dataset.from_file(arrow_file)

    # Decide output format
    output_format = decide_output_format(dataset.column_names)
    output_file = os.path.join(
        output_folder, os.path.basename(arrow_file).replace(".arrow", f".{output_format}")
    )

    # Write to the file
    with open(output_file, 'w', encoding='utf-8') as f:
        for row in dataset:
            if output_format == "csv":
                f.write(",".join([str(value) for value in row.values()]) + "\n")
            else:  # Plain text
                f.write(" ".join([str(value) for value in row.values()]) + "\n")
    
    print(f"Saved: {output_file} in {output_format} format.")

def convert_all_arrow_files(input_folder):
    """
    Convert all Arrow files in a folder to text or CSV format.
    
    Args:
    - input_folder (str): Path to the folder containing Arrow files.
    """
    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' does not exist.")
        sys.exit(1)

    output_folder = os.path.join(input_folder, "converted")
    os.makedirs(output_folder, exist_ok=True)

    arrow_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".arrow")]

    if not arrow_files:
        print(f"No Arrow files found in the folder '{input_folder}'.")
        return

    print(f"Found {len(arrow_files)} Arrow file(s) to convert.")
    for arrow_file in arrow_files:
        convert_arrow_file(arrow_file, output_folder)

    print(f"Conversion complete. All files saved in '{output_folder}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_arrow.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    convert_all_arrow_files(folder_path)
