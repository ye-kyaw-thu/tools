# -*- coding: utf-8 -*-
"""
Last updated: Jul 11, 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar

Input ပေးလိုက်တဲ့ ဖိုင်ထဲမှာ ပါတဲ့ စာကြောင်းတွေကို တစ်ကြောင်းချင်းစီ language detectation လုပ်ပြီး % တွက်ပေးမယ့် ပရိုဂရမ်ပါ။  
Version 1 program will make language detection with langdetect library.
Note: Some undetected low-resourced languages such as Burmese and Khmer will be under the unknown.

How to use:
python detect_language_ver1.py multi_lingual_text.txt
"""

import sys
import os
import re
from collections import Counter
from langdetect import detect

language_codes = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'ca': 'Catalan',
    'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'el': 'Greek',
    'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'fa': 'Persian', 'fi': 'Finnish',
    'fr': 'French', 'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian',
    'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam',
    'mr': 'Marathi', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi',
    'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak',
    'sl': 'Slovenian', 'so': 'Somali', 'sq': 'Albanian', 'sv': 'Swedish', 'sw': 'Swahili',
    'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Tagalog', 'tr': 'Turkish', 'uk': 'Ukrainian',
    'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-cn': 'Chinese Simplified', 'zh-tw': 'Chinese Traditional'
}

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = text.strip()  # remove spaces at the beginning and at the end of string
    return text

def detect_language(text):
    try:
        lang = detect(text)
        if lang in language_codes:
            return language_codes[lang]
        else:
            return 'unknown'
    except:
        return 'unknown'

def detect_languages(text):
    languages = []
    for sentence in text:
        sentence = clean_text(sentence)
        if sentence:  # check if sentence is not empty
            language = detect_language(sentence)
            languages.append(language)
    return languages

def print_languages(languages):
    language_counter = Counter(languages)
    total_count = sum(language_counter.values())
    for lang, count in language_counter.items():
        percent = (count / total_count) * 100
        print(f"{lang}: {percent:.2f}%")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} [input_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"File does not exist: {input_file}")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.readlines()

    languages = detect_languages(text)
    print_languages(languages)

if __name__ == "__main__":
    main()
