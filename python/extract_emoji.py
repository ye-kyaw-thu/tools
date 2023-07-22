# -*- coding: utf-8 -*-
"""
List emoji characters
Created on Sun Jul 23 00:42:47 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar

How to run:
python extract_emoji.py ./emoji.txt
"""

import emoji
import re
import sys

def extract_emojis_from_line(line):
    # Create a pattern for matching emoji characters
    emoji_pattern = re.compile(pattern="[" "\U0001F600-\U0001F64F"  # emoticons
                                        "\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        "\U0001F680-\U0001F6FF"  # transport & map symbols
                                        "\U0001F700-\U0001F77F"  # alchemical symbols
                                        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                                        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                                        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                                        "\U0001FA00-\U0001FA6F"  # Chess Symbols
                                        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                                        "\U00002702-\U000027B0"  # Dingbats
                                        "\U00002600-\U000027BF"  # Misc symbols
                                        "]+", flags=re.UNICODE)
    
    # Return a list of all matched emojis
    return emoji_pattern.findall(line)

def main(filename):
    # Open the input file in utf-8 encoding and read line by line
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            emojis_in_line = extract_emojis_from_line(line)
            for e in emojis_in_line:
                print(f"Emoji Character: {e}")
                print(f"Unicode Value: {ord(e)}")
                print(f"Emoji Name: {emoji.demojize(e)}")
                # We don't have definitions, so just display name as a placeholder
                print(f"Emoji Definition: {emoji.demojize(e)}\n")

if __name__ == '__main__':
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python <script_name.py> <input_filename>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    main(input_filename)
