"""

ICU based Collation.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 12 Jan 2024

Reference:
https://www.evertype.com/standards/wynnyogh/thorn.html
https://gist.github.com/dpk/8325992

How to use:
python ./icu_collation.py --help
python ./icu_collation.py --show_locales
python ./icu_collation.py --input ./my_names.txt
python ./icu_collation.py --input ./thai_names.txt --locale th_TH


"""

import icu
import argparse
import sys

def list_supported_locales():
    """List all supported locales."""
    for locale in icu.Locale.getAvailableLocales():
        print(locale)  # Directly print the locale string

def sort_lines(input_lines, locale):
    """Sort a list of strings based on the specified locale."""
    collator = icu.Collator.createInstance(icu.Locale(locale))
    return sorted(input_lines, key=collator.getSortKey)

def main():
    parser = argparse.ArgumentParser(description='Sort lines of text using ICU Collation')
    parser.add_argument('--input', help='Input file path')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('-l', '--locale', default='my_MM', help='Locale for collation (default: my_MM)')
    parser.add_argument('--show_locales', action='store_true', help='Show all supported locales')

    args = parser.parse_args()

    if args.show_locales:
        list_supported_locales()
        return

    # Read input
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            input_lines = file.readlines()
    else:
        input_lines = [line for line in sys.stdin]

    # Sort lines
    sorted_lines = sort_lines(input_lines, args.locale)

    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.writelines(sorted_lines)
    else:
        for line in sorted_lines:
            print(line, end='')

if __name__ == "__main__":
    main()
