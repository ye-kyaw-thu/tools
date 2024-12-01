"""
to find files with one extension (-e1 or --extension1) that do not have a corresponding file with another extension (-e2 or --extension2)

Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 1 Dec 2024
How to run: python3 find_unmatched_files.py -e1 epub -e2 pdf /path/to/directory
"""

import os
import argparse

def find_unmatched_files(extension1, extension2, directory):
    ext1_files = set()
    ext2_files = set()
    
    # Traverse the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(f".{extension1}"):
                ext1_files.add(os.path.join(root, file).rsplit(f".{extension1}", 1)[0])
            elif file.endswith(f".{extension2}"):
                ext2_files.add(os.path.join(root, file).rsplit(f".{extension2}", 1)[0])
    
    unmatched = ext1_files - ext2_files
    return unmatched

def main():
    parser = argparse.ArgumentParser(description="Find files with one extension that don't have a corresponding file with another extension.")
    parser.add_argument("-e1", "--extension1", required=True, help="First file extension to compare (e.g., epub)")
    parser.add_argument("-e2", "--extension2", required=True, help="Second file extension to compare (e.g., pdf)")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to search (default: current directory)")
    args = parser.parse_args()
    
    unmatched_files = find_unmatched_files(args.extension1, args.extension2, args.directory)
    for file in unmatched_files:
        print(f"{file}.{args.extension1}")

if __name__ == "__main__":
    main()
