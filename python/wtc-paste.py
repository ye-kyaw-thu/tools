"""
This Python code interleaves the contents of three files.
Written by Ye Kyaw Thu, Visiting Professor, NECTEC, Thailand.
Last updated: 11 Mar 2024

Usage:
python wtc-paste.py --wrong ./w.txt --tagged ./t.txt --correct \
./c.txt > wrong-tagged-correct.txt
"""

import argparse

def combine_files(wrong_file, tagged_file, correct_file):
    with open(wrong_file, 'r', encoding='utf-8') as w, \
         open(tagged_file, 'r', encoding='utf-8') as t, \
         open(correct_file, 'r', encoding='utf-8') as c:

        w_lines = w.readlines()
        t_lines = t.readlines()
        c_lines = c.readlines()

        for w_line, t_line, c_line in zip(w_lines, t_lines, c_lines):
            print(w_line.strip())
            print(t_line.strip())
            print(c_line.strip())
            print()

def main():
    parser = argparse.ArgumentParser(description='Combine lines from three files.')
    parser.add_argument('--wrong', '-w', type=str, required=True, help='Path to the file containing wrong lines')
    parser.add_argument('--tagged', '-t', type=str, required=True, help='Path to the file containing tagged lines')
    parser.add_argument('--correct', '-c', type=str, required=True, help='Path to the file containing correct lines')

    args = parser.parse_args()

    combine_files(args.wrong, args.tagged, args.correct)

if __name__ == "__main__":
    main()
