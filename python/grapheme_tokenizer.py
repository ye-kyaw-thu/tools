"""

ICU based Grapheme Segmenter
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 12 Jan 2024

Reference:
https://pypi.org/project/PyICU/
https://github.com/unicode-org/icu4x
https://www.reddit.com/r/rust/comments/xrh7h6/comment/iqikdsl/?context=1

"""

import sys
import argparse
import icu

def segment_graphemes(text, locale):
    # Create a BreakIterator for grapheme segmentation using the specified locale
    boundary = icu.BreakIterator.createCharacterInstance(icu.Locale(locale))
    boundary.setText(text)

    # Segment the text into graphemes
    start = boundary.first()
    graphemes = []
    for end in boundary:
        graphemes.append(text[start:end])
        start = end

    return graphemes

def print_supported_locales():
    print("Supported locale codes:")
    for locale_id in icu.Locale.getAvailableLocales():
        print(locale_id)

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Grapheme segmentation script supporting multiple languages.")
    parser.add_argument("-i", "--input", help="Input file name (optional, default: stdin)")
    parser.add_argument("-l", "--locale", default="en_US", help="Locale code for text segmentation (default: en_US)")
    parser.add_argument("-o", "--output", help="Output file name (optional, default: stdout)")
    parser.add_argument("--list-locales", action="store_true", help="List all supported locale codes")
    args = parser.parse_args()

    # List all supported locales if requested
    if args.list_locales:
        print_supported_locales()
        sys.exit()

    # Read input from file or stdin
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            input_text = file.read()
    else:
        input_text = sys.stdin.read()

    # Perform grapheme segmentation
    segmented_lines = [segment_graphemes(line, args.locale) for line in input_text.splitlines()]

    # Convert segmented lines to space-separated strings
    output_lines = [' '.join(graphemes) for graphemes in segmented_lines]

    # Output to file or stdout
    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write('\n'.join(output_lines))
    else:
        print('\n'.join(output_lines))

if __name__ == "__main__":
    main()
