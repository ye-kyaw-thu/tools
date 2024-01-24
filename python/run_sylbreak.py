"""

Run syllable breaking for both source and target file extensions.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 25 Jan 2024

Usage:
    python ./run_sylbreak.py --source_extension my --target_extension rk

"""

import subprocess
import glob
import argparse

def run_command(file_path, output_path):
    command = f"python ./sylbreak.py --input {file_path} --separator ' ' --output {output_path}"
    subprocess.run(command, shell=True)

def process_files(extension):
    for file_path in glob.glob(f'*.{extension}'):
        output_path = f"{file_path}.syl"
        run_command(file_path, output_path)
        print(f"Processed {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Process files with specified extensions.')
    parser.add_argument('--source_extension', type=str, help='Source file extension')
    parser.add_argument('--target_extension', type=str, help='Target file extension')

    args = parser.parse_args()

    process_files(args.source_extension)
    process_files(args.target_extension)

if __name__ == "__main__":
    main()
