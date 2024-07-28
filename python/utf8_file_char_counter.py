'''
To verify the character count (not byte count) accurately.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
How to run:
python ./utf8_file_char_counter.py --filename ./myWord_myPOS_myPara_myNovel1v1_wordseg.shuf.cleaned
'''

import argparse

def count_characters(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        corpus = f.read()
    return len(corpus)

def main():
    parser = argparse.ArgumentParser(description='Character Count Tool')
    parser.add_argument('--filename', type=str, required=True, help='Path to the text file')
    args = parser.parse_args()

    character_count = count_characters(args.filename)
    print(f'Character count for {args.filename}: {character_count}')

if __name__ == '__main__':
    main()
