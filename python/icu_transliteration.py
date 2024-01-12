"""

ICU based transliteration.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 12 Jan 2024

Reference:
https://gist.github.com/dpk/8325992

How to use:
python ./icu_transliteration.py --help
echo "Ψάπφω" | python icu_transliteration.py --translit_id Greek-Latin
echo "Ψάπφω" | python icu_transliteration.py --translit_id Greek-Latin --reverse
echo "ချစ်စုစုထွန်း" | python icu_transliteration.py --translit_id Myanmar-Latin
python ./icu_transliteration.py --input ./my_names.txt -t Myanmar-Latin
python ./icu_transliteration.py --input ./thai_names.txt -t Thai-Latin
python ./icu_transliteration.py --input ./hiragana_names.txt -t Hiragana-Latin
python ./icu_transliteration.py --input ./katakana_names.txt -t Katakana-Latin

"""

import icu
import argparse
import sys

def list_supported_locales():
    """List all supported transliteration locales."""
    for locale in icu.Transliterator.getAvailableIDs():
        print(locale)

def transliterate_text(input_text, translit_id, reverse):
    """Transliterate a string based on the specified transliteration ID."""
    try:
        if reverse:
            transliterator = icu.Transliterator.createInstance(translit_id, icu.UTransDirection.REVERSE)
        else:
            transliterator = icu.Transliterator.createInstance(translit_id)
    except icu.ICUError as e:
        print(f"Error creating transliterator with ID '{translit_id}': {e}")
        sys.exit(1)

    return transliterator.transliterate(input_text)

def main():
    parser = argparse.ArgumentParser(description='Perform text transliteration using ICU')
    parser.add_argument('--input', help='Input file path')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('-t', '--translit_id', default='Any-Latin', help='Transliteration ID (default: Any-Latin)')
    parser.add_argument('--reverse', action='store_true', help='Perform reverse transliteration')
    parser.add_argument('--show_locales', action='store_true', help='Show all supported transliteration locales')

    args = parser.parse_args()

    if args.show_locales:
        list_supported_locales()
        return

    # Read input
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            input_text = file.read()
    else:
        input_text = sys.stdin.read()

    # Transliterate text
    transliterated_text = transliterate_text(input_text, args.translit_id, args.reverse)

    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(transliterated_text)
    else:
        print(transliterated_text)

if __name__ == "__main__":
    main()
