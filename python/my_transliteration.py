"""

Transliteration with ALALC and Sawada mappings.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 14 Jan 2024.

Reference:
https://online-resources.aa-ken.jp/resources/detail/IOR000125
http://www.aa.tufs.ac.jp/~sawadah/burroman2.pdf

How to run:
python ./my_transliteration.py --help
python ./my_transliteration.py --input ./test2.txt --method sawada
python ./my_transliteration.py --input ./test2.txt --method alalc

python ./my_transliteration.py --input ./test2.txt --method sawada --show_parallel
python ./my_transliteration.py --input ./test2.txt --method alalc --show_parallel

For Debugging:
python ./my_transliteration.py --input ./test2.txt --method sawada --verbose
python ./my_transliteration.py --input ./test2.txt --method alalc --verbose
"""

import argparse
import sys

sawada_transliteration_map = {
        # Include multi-character sequences first
        'ဦ': 'uu', 'ော': 'o', 'ို': 'ui', 'ဩော့': 'o.',
                'ော်': 'o’','က': 'k', 'ခ': 'kh', 'ဂ': 'g',
                'ဃ': 'gh', 'င': 'ng', 'စ': 'c', 'ဆ': 'ch',
                'ဇ': 'j', 'ဈ': 'jh','ည': 'N~', 'ဋ': 'T',
                'ဌ': 'Th', 'ဍ': 'D', 'ဎ': 'Dh', 'ဏ': 'N',
                'တ': 't', 'ထ': 'th', 'ဒ': 'd','ဓ': 'dh',
                'န': 'n', 'ပ': 'p', 'ဖ': 'ph', 'ဗ': 'b',
                'ဘ': 'bh', 'မ': 'm', 'ယ': 'y', 'ရ': 'r',
                'လ': 'l', 'ဝ': 'w', 'သ': 's', 'ဟ': 'h',
                'အ': '@', 'ဣ': 'i', 'ဤ': 'ii', 'ဥ': 'u',
                'ဧ': 'e', 'ဩ': 'o', 'ဪ': 'o’', 'ှ': 'h',
                'ျ': 'y', 'ြ':'r', 'ွ': 'w', '္': '=',
                'ိ': 'i', 'ု': 'u', 'ေ': 'e', 'ာ': 'aa',
                                'ါ': 'aa', 'ဉ': 'n~',
                'ီ': 'ii', 'ူ': 'uu', '်': '’', 'ဲ': 'Y',
                'ံ': 'M', '့': '.', 'း': ':', 'ဿ': 's=s',
                '၏': '\\i’', '၍': '\\rw’', '၌': '\\nh’', '၎': '\\l',
                '၊': '|', '။': '||',
                                '၁': '1', '၂': '2', '၃': '3', '၄': '4', '၅': '5',
                                '၆': '6', '၇': '7', '၈': '8', '၉': '9', '၀': '0'
}


alalc_transliteration_map = {
        'ဦ': 'ū', 'ော': 'o', 'ို': 'ui', 'ဩော့': 'o‘',
                'ော်': 'o‘', 'က': 'k', 'ခ': 'kh', 'ဂ': 'g',
                'ဃ': 'gh', 'င': 'ṅ', 'စ': 'c', 'ဆ': 'ch',
                'ဇ': 'j', 'ဈ': 'jh', 'ည': 'ññ', 'ဋ': 'ṭ',
                'ဌ': 'ṭh', 'ဍ': 'ḍ', 'ဎ': 'ḍh', 'ဏ': 'ṇ',
                'တ': 't', 'ထ': 'th', 'ဒ': 'd', 'ဓ': 'dh', 'န': 'n',
                'ပ': 'p', 'ဖ': 'ph', 'ဗ': 'b', 'ဘ': 'bh',
                'မ': 'm', 'ယ': 'y', 'ရ': 'r', 'လ': 'l',
                'ဝ': 'v', 'သ': 's', 'ဟ': 'h', 'အ': '‘A', '္': '',
                'ာ': 'ā','ါ': 'ā', 'ဉ': 'ñ', 'ိ': 'i', 'ီ': 'ī', 'ု': 'u',
                'ူ': 'ū', 'ေ': 'e', 'ဲ': 'ai', 'ဣ': 'i',
                'ဤ': 'ī', 'ဥ': 'u', 'ဧ': 'e', 'ဩ': 'o',
                'ဪ': 'o‘','ျ': 'y', 'ြ': 'r', 'ွ': 'w',
                'ှ': 'h','်': '’', 'ံ': 'ṃ','့': '.', 'း': '"',
                'ဿ': 'ss', '၏': 'e*', '၍': 'r*', '၌': 'n*', '၎': 'l*',
                '၊': ',', '။': '.',
                                '၁': '1', '၂': '2', '၃': '3', '၄': '4', '၅': '5',
                                '၆': '6', '၇': '7', '၈': '8', '၉': '9', '၀': '0'
}

def transliterate(text, mapping, verbose):
    result = ""
    i = 0
    while i < len(text):
        matched = False
        for length in range(3, 0, -1):
            if i + length <= len(text) and text[i:i+length] in mapping:
                result += mapping[text[i:i+length]]
                if verbose:
                    print(f"Matched: '{text[i:i+length]}' -> '{mapping[text[i:i+length]]}'")
                i += length
                matched = True
                break
        if not matched:
            result += mapping.get(text[i], text[i])
            if verbose:
                print(f"No match for: '{text[i]}' -> '{mapping.get(text[i], text[i])}'")
            i += 1
    return result

def sawada_transliteration(burmese_text, verbose=False):
    return transliterate(burmese_text, sawada_transliteration_map, verbose)

def alalc_transliteration(burmese_text, verbose=False):
    return transliterate(burmese_text, alalc_transliteration_map, verbose)

def transliterate_burmese(input_text, method, verbose):
    if method == 'sawada':
        return sawada_transliteration(input_text, verbose)
    elif method == 'alalc':
        return alalc_transliteration(input_text, verbose)
    else:
        raise ValueError("Unknown transliteration method: " + method)

def main():
    parser = argparse.ArgumentParser(description='Transliterate Burmese script to Roman script.')
    parser.add_argument('--input', type=str, help='Input file name containing Burmese text.')
    parser.add_argument('--output', type=str, help='Output file name for the transliterated text.')
    parser.add_argument('--method', type=str, choices=['sawada', 'alalc'], default='sawada',
                        help='Choose the transliteration method: "sawada" or "alalc".')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode to show matched and unmatched characters.')
    parser.add_argument('--show_map', action='store_true', help='Show the transliteration mapping tables.')
    parser.add_argument('--show_parallel', action='store_true', help='Show input and transliterated sentences side by side.')

    args = parser.parse_args()

    # Show the mapping tables if --show_map is used
    if args.show_map:
        print("Sawada's Transliteration Map:")
        print(sawada_transliteration_map)
        print("\nALA-LC Transliteration Map:")
        print(alalc_transliteration_map)
        return

    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            burmese_text = file.read()
    else:
        burmese_text = sys.stdin.read()

    romanized_text = transliterate_burmese(burmese_text, args.method, args.verbose)

    if args.show_parallel:
        burmese_sentences = burmese_text.split('\n')
        romanized_sentences = romanized_text.split('\n')
        for burmese_sentence, romanized_sentence in zip(burmese_sentences, romanized_sentences):
            print(burmese_sentence)
            print(romanized_sentence)
            print()
    elif args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(romanized_text)
    else:
        print(romanized_text)

if __name__ == "__main__":
    main()
