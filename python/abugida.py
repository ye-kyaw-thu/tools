# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:50:50 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.
Reference: https://en.wikipedia.org/wiki/Abugida

## How to run

For help screen:  
python abugida.py -h

For printing numbers, consonants and vowels of Northern Indian languages:  
python abugida.py -g ni

For priting numbers, consonants and vowels of Myanmar language or Burmese:
python abugida.py --l my

Note: This program is to show some common nature of writing system between Abugida languages to my students. 
And thus it is not cover all the characters. 
If you want to show all the characters such as independent vowels and symbols etc. freely update by yourself.
"""

import argparse

languages = {
    'my': {'name': 'Burmese', 'numbers': range(0x1040, 0x104A), 'consonants': range(0x1000, 0x1022), 'vowels': range(0x102B, 0x1030)},
    'th': {'name': 'Thai', 'numbers': range(0x0E50, 0x0E5A), 'consonants': range(0x0E01, 0x0E2E), 'vowels': range(0x0E30, 0x0E3A)},
    'km': {'name': 'Khmer', 'numbers': range(0x17E0, 0x17EA), 'consonants': range(0x1780, 0x17B6), 'vowels': range(0x17B7, 0x17C6)},
    'lo': {'name': 'Laos', 'numbers': range(0x0ED0, 0x0EDA), 'consonants': range(0x0E81, 0x0EAE), 'vowels': range(0x0EB0, 0x0EB9)},
    'hi': {'name': 'Hindi', 'numbers': range(0x0966, 0x096F), 'consonants': range(0x0915, 0x0939), 'vowels': range(0x0905, 0x0914)},
    'mr': {'name': 'Marathi', 'numbers': range(0x0966, 0x096F), 'consonants': range(0x0915, 0x0939), 'vowels': range(0x0905, 0x0914)},
    'bn': {'name': 'Bengali', 'numbers': range(0x09E6, 0x09EF), 'consonants': range(0x0995, 0x09B9), 'vowels': range(0x0985, 0x0994)},
    'si': {'name': 'Sinhala', 'numbers': range(0x0DE6, 0x0DEF), 'consonants': range(0x0D9A, 0x0DB1), 'vowels': range(0x0D85, 0x0D96)},
    'ml': {'name': 'Malayalam', 'numbers': range(0x0D66, 0x0D6F), 'consonants': range(0x0D15, 0x0D39), 'vowels': range(0x0D05, 0x0D14)},
    'ta': {'name': 'Tamil', 'numbers': range(0x0BE6, 0x0BEF), 'consonants': range(0x0B95, 0x0BB9), 'vowels': range(0x0B85, 0x0B94)},
    'te': {'name': 'Telugu', 'numbers': range(0x0C66, 0x0C6F), 'consonants': range(0x0C15, 0x0C39), 'vowels': range(0x0C05, 0x0C14)},
    'kn': {'name': 'Kannada', 'numbers': range(0x0CE6, 0x0CEF), 'consonants': range(0x0C95, 0x0CB9), 'vowels': range(0x0C85, 0x0C94)},
    'bl': {'name': 'Balinese', 'numbers': range(0x1B50, 0x1B59), 'consonants': range(0x1B05, 0x1B33), 'vowels': range(0x1B35, 0x1B43)},
    'jv': {'name': 'Javanese', 'numbers': range(0xA9D0, 0xA9D9), 'consonants': range(0xA984, 0xA9B2), 'vowels': range(0xA9B4, 0xA9BF)},
    'sd': {'name': 'Sundanese', 'numbers': range(0x1BB0, 0x1BB9), 'consonants': range(0x1B83, 0x1BA0), 'vowels': range(0x1BA1, 0x1BA6)},
    'as': {'name': 'Assamese', 'numbers': range(0x09E6, 0x09EF), 'consonants': range(0x0995, 0x09B9), 'vowels': range(0x0985, 0x0994)},
    'gu': {'name': 'Gujarati', 'numbers': range(0x0AE6, 0x0AEF), 'consonants': range(0x0A95, 0x0AB9), 'vowels': range(0x0A85, 0x0A94)},
    'pa': {'name': 'Gurmukhi', 'numbers': range(0x0A66, 0x0A6F), 'consonants': range(0x0A15, 0x0A39), 'vowels': range(0x0A05, 0x0A14)},
    'or': {'name': 'Odia', 'numbers': range(0x0B66, 0x0B6F), 'consonants': range(0x0B15, 0x0B39), 'vowels': range(0x0B05, 0x0B14)},
    'bo': {'name': 'Tibetan', 'numbers': range(0x0F20, 0x0F29), 'consonants': range(0x0F40, 0x0F6C), 'vowels': range(0x0F72, 0x0F80)},
}

language_groups = {
    'ni': ['as', 'bn', 'hi', 'gu', 'pa', 'or', 'bo'],
    'si': ['si', 'ml', 'ta', 'te', 'kn'],
    'm': ['my', 'km', 'th', 'lo'],
    't': ['bl', 'jv', 'sd'],
}

def print_language(lang_code):
    lang = languages[lang_code]
    print(f"\nLanguage: {lang['name']}\n")
    print("Numbers:")
    for i in lang['numbers']:
        print(chr(i), end=" ")
    print("\nConsonants:")
    for i in lang['consonants']:
        print(chr(i), end=" ")
    print("\nVowels:")
    for i in lang['vowels']:
        print(chr(i), end=" ")
    print("\n")

def print_all():
    for code in languages:
        print_language(code)

def print_group(group_code):
    for code in language_groups[group_code]:
        print_language(code)

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-a', '--all', action='store_true', help='Print all characters for each language')
    
    lang_help_text = 'Print characters for one language. Available languages are: ' + \
                     ', '.join([f"{code} ({languages[code]['name']})" for code in languages])
    parser.add_argument('-l', '--language', type=str, help=lang_help_text)
    
    group_help_text = 'Print characters for a group of languages. Available groups are: ' + \
                      ', '.join([f"{code} ({', '.join([languages[lang]['name'] for lang in language_groups[code]])})" for code in language_groups] + \
                                ["Here, ni for Northern Indian languages, si for Southern Indian languages, m for SouthEast Asian, mainland languages and t for SouthEase Asian, maritime languages"])
    parser.add_argument('-g', '--group', type=str, help=group_help_text)
    
    args = parser.parse_args()

    if args.all:
        print_all()
    elif args.language:
        if args.language in languages:
            print_language(args.language)
        else:
            print(f"Unknown language: {args.language}")
    elif args.group:
        if args.group in language_groups:
            print_group(args.group)
        else:
            print(f"Unknown group: {args.group}")

if __name__ == '__main__':
    main()
