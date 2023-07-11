# -*- coding: utf-8 -*-
"""
Last updated: Jul 11, 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar

Version 2.0
Solving the problem of Unknown (i.e. problem of Ver. 1.0).

How to run:
python detect_language_ver2.py multi_lingual_text.txt
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

language_unicode_ranges = {
    'Latin': ('\u0020', '\u007E'),
    'Latin Extended-A': ('\u0100', '\u017F'),
    'Latin Extended-B': ('\u0180', '\u024F'),
    'IPA Extensions': ('\u0250', '\u02AF'),
    'Spacing Modifier Letters': ('\u02B0', '\u02FF'),
    'Combining Diacritical Marks': ('\u0300', '\u036F'),
    'Greek and Coptic': ('\u0370', '\u03FF'),
    'Cyrillic': ('\u0400', '\u04FF'),
    'Cyrillic Supplement': ('\u0500', '\u052F'),
    'Armenian': ('\u0530', '\u058F'),
    'Hebrew': ('\u0590', '\u05FF'),
    'Arabic': ('\u0600', '\u06FF'),
    'Syriac': ('\u0700', '\u074F'),
    'Arabic Supplement': ('\u0750', '\u077F'),
    'Thaana': ('\u0780', '\u07BF'),
    'N\'Ko': ('\u07C0', '\u07FF'),
    'Samaritan': ('\u0800', '\u083F'),
    'Mandaic': ('\u0840', '\u085F'),
    'Syriac Supplement': ('\u0860', '\u086F'),
    'Arabic Extended-A': ('\u08A0', '\u08FF'),
    'Devanagari': ('\u0900', '\u097F'),
    'Bengali': ('\u0980', '\u09FF'),
    'Gurmukhi': ('\u0A00', '\u0A7F'),
    'Gujarati': ('\u0A80', '\u0AFF'),
    'Oriya': ('\u0B00', '\u0B7F'),
    'Tamil': ('\u0B80', '\u0BFF'),
    'Telugu': ('\u0C00', '\u0C7F'),
    'Kannada': ('\u0C80', '\u0CFF'),
    'Malayalam': ('\u0D00', '\u0D7F'),
    'Sinhala': ('\u0D80', '\u0DFF'),
    'Thai': ('\u0E00', '\u0E7F'),
    'Lao': ('\u0E80', '\u0EFF'),
    'Tibetan': ('\u0F00', '\u0FFF'),
    'Myanmar': ('\u1000', '\u109F'),
    'Georgian': ('\u10A0', '\u10FF'),
    'Hangul Jamo': ('\u1100', '\u11FF'),
    'Ethiopic': ('\u1200', '\u137F'),
    'Ethiopic Supplement': ('\u1380', '\u139F'),
    'Cherokee': ('\u13A0', '\u13FF'),
    'Unified Canadian Aboriginal Syllabics': ('\u1400', '\u167F'),
    'Ogham': ('\u1680', '\u169F'),
    'Runic': ('\u16A0', '\u16FF'),
    'Tagalog': ('\u1700', '\u171F'),
    'Hanunoo': ('\u1720', '\u173F'),
    'Buhid': ('\u1740', '\u175F'),
    'Tagbanwa': ('\u1760', '\u177F'),
    'Khmer': ('\u1780', '\u17FF'),
    'Mongolian': ('\u1800', '\u18AF'),
    'Unified Canadian Aboriginal Syllabics Extended': ('\u18B0', '\u18FF'),
    'Limbu': ('\u1900', '\u194F'),
    'Tai Le': ('\u1950', '\u197F'),
    'New Tai Lue': ('\u1980', '\u19DF'),
    'Khmer Symbols': ('\u19E0', '\u19FF'),
    'Buginese': ('\u1A00', '\u1A1F'),
    'Tai Tham': ('\u1A20', '\u1AAF'),
    'Combining Diacritical Marks Extended': ('\u1AB0', '\u1AFF'),
    'Balinese': ('\u1B00', '\u1B7F'),
    'Sundanese': ('\u1B80', '\u1BBF'),
    'Batak': ('\u1BC0', '\u1BFF'),
    'Lepcha': ('\u1C00', '\u1C4F'),
    'Ol Chiki': ('\u1C50', '\u1C7F'),
    'Cyrillic Extended-C': ('\u1C80', '\u1C8F'),
    'Georgian Extended': ('\u1C90', '\u1CBF'),
    'Sundanese Supplement': ('\u1CC0', '\u1CCF'),
    'Vedic Extensions': ('\u1CD0', '\u1CFF'),
    'Phonetic Extensions': ('\u1D00', '\u1D7F'),
    'Phonetic Extensions Supplement': ('\u1D80', '\u1DBF'),
    'Combining Diacritical Marks Supplement': ('\u1DC0', '\u1DFF'),
    'Latin Extended Additional': ('\u1E00', '\u1EFF'),
    'Greek Extended': ('\u1F00', '\u1FFF'),
    'General Punctuation': ('\u2000', '\u206F'),
    'Superscripts and Subscripts': ('\u2070', '\u209F'),
    'Currency Symbols': ('\u20A0', '\u20CF'),
    'Combining Diacritical Marks for Symbols': ('\u20D0', '\u20FF'),
    'Letterlike Symbols': ('\u2100', '\u214F'),
    'Number Forms': ('\u2150', '\u218F'),
    'Arrows': ('\u2190', '\u21FF'),
    'Mathematical Operators': ('\u2200', '\u22FF'),
    'Miscellaneous Technical': ('\u2300', '\u23FF'),
    'Control Pictures': ('\u2400', '\u243F'),
    'Optical Character Recognition': ('\u2440', '\u245F'),
    'Enclosed Alphanumerics': ('\u2460', '\u24FF'),
    'Box Drawing': ('\u2500', '\u257F'),
    'Block Elements': ('\u2580', '\u259F'),
    'Geometric Shapes': ('\u25A0', '\u25FF'),
    'Miscellaneous Symbols': ('\u2600', '\u26FF'),
    'Dingbats': ('\u2700', '\u27BF'),
    'Miscellaneous Mathematical Symbols-A': ('\u27C0', '\u27EF'),
    'Supplemental Arrows-A': ('\u27F0', '\u27FF'),
    'Braille Patterns': ('\u2800', '\u28FF'),
    'Supplemental Arrows-B': ('\u2900', '\u297F'),
    'Miscellaneous Mathematical Symbols-B': ('\u2980', '\u29FF'),
    'Supplemental Mathematical Operators': ('\u2A00', '\u2AFF'),
    'Miscellaneous Symbols and Arrows': ('\u2B00', '\u2BFF'),
    'Glagolitic': ('\u2C00', '\u2C5F'),
    'Latin Extended-C': ('\u2C60', '\u2C7F'),
    'Coptic': ('\u2C80', '\u2CFF'),
    'Georgian Supplement': ('\u2D00', '\u2D2F'),
    'Tifinagh': ('\u2D30', '\u2D7F'),
    'Ethiopic Extended': ('\u2D80', '\u2DDF'),
    'Cyrillic Extended-A': ('\u2DE0', '\u2DFF'),
    'Supplemental Punctuation': ('\u2E00', '\u2E7F'),
    'CJK Radicals Supplement': ('\u2E80', '\u2EFF'),
    'Kangxi Radicals': ('\u2F00', '\u2FDF'),
    'Ideographic Description Characters': ('\u2FF0', '\u2FFF'),
    'CJK Symbols and Punctuation': ('\u3000', '\u303F'),
    'Hiragana': ('\u3040', '\u309F'),
    'Katakana': ('\u30A0', '\u30FF'),
    'Bopomofo': ('\u3100', '\u312F'),
    'Hangul Compatibility Jamo': ('\u3130', '\u318F'),
    'Kanbun': ('\u3190', '\u319F'),
    'Bopomofo Extended': ('\u31A0', '\u31BF'),
    'CJK Strokes': ('\u31C0', '\u31EF'),
    'Katakana Phonetic Extensions': ('\u31F0', '\u31FF'),
    'Enclosed CJK Letters and Months': ('\u3200', '\u32FF'),
    'CJK Compatibility': ('\u3300', '\u33FF'),
    'CJK Unified Ideographs Extension A': ('\u3400', '\u4DBF'),
    'Yijing Hexagram Symbols': ('\u4DC0', '\u4DFF'),
    'CJK Unified Ideographs': ('\u4E00', '\u9FFF'),
    'Yi Syllables': ('\uA000', '\uA48F'),
    'Yi Radicals': ('\uA490', '\uA4CF'),
    'Lisu': ('\uA4D0', '\uA4FF'),
    'Vai': ('\uA500', '\uA63F'),
    'Cyrillic Extended-B': ('\uA640', '\uA69F'),
    'Bamum': ('\uA6A0', '\uA6FF'),
    'Modifier Tone Letters': ('\uA700', '\uA71F'),
    'Latin Extended-D': ('\uA720', '\uA7FF'),
    'Syloti Nagri': ('\uA800', '\uA82F'),
    'Common Indic Number Forms': ('\uA830', '\uA83F'),
    'Phags-pa': ('\uA840', '\uA87F'),
    'Saurashtra': ('\uA880', '\uA8DF'),
    'Devanagari Extended': ('\uA8E0', '\uA8FF'),
    'Kayah Li': ('\uA900', '\uA92F'),
    'Rejang': ('\uA930', '\uA95F'),
    'Hangul Syllables': ('\uAC00', '\uD7AF'),
    'High Surrogates': ('\uD800', '\uDB7F'),
    'High Private Use Surrogates': ('\uDB80', '\uDBFF'),
    'Low Surrogates': ('\uDC00', '\uDFFF'),
    'Private Use Area': ('\uE000', '\uF8FF'),
    'CJK Compatibility Ideographs': ('\uF900', '\uFAFF'),
    'Alphabetic Presentation Forms': ('\uFB00', '\uFB4F'),
    'Arabic Presentation Forms-A': ('\uFB50', '\uFDFF'),
    'Variation Selectors': ('\uFE00', '\uFE0F'),
    'Vertical Forms': ('\uFE10', '\uFE1F'),
    'Combining Half Marks': ('\uFE20', '\uFE2F'),
    'CJK Compatibility Forms': ('\uFE30', '\uFE4F'),
    'Small Form Variants': ('\uFE50', '\uFE6F'),
    'Arabic Presentation Forms-B': ('\uFE70', '\uFEFF'),
    'Halfwidth and Fullwidth Forms': ('\uFF00', '\uFFEF'),
    'Specials': ('\uFFF0', '\uFFFF')
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

def detect_unicode_script(char):
    for script, (start, end) in language_unicode_ranges.items():
        if start <= char <= end:
            return script
    return None

def detect_dominant_script(sentence):
    script_counts = Counter(detect_unicode_script(c) for c in sentence if detect_unicode_script(c) is not None)
    if not script_counts:  # The sentence does not contain any characters from known scripts
        return None
    return script_counts.most_common(1)[0][0]

def detect_languages(text):
    languages = []
    guess_languages = []
    for sentence in text:
        sentence = clean_text(sentence)
        if sentence:  # check if sentence is not empty
            language = detect_language(sentence)
            if language == 'unknown':
                guess_languages.append(detect_dominant_script(sentence))
            else:
                languages.append(language)
    return languages, guess_languages

def print_languages(languages, guess_languages):
    language_counter = Counter(languages)
    guess_language_counter = Counter(guess_languages)
    total_count = sum(language_counter.values()) + sum(guess_language_counter.values())
    for lang, count in language_counter.items():
        percent = (count / total_count) * 100
        print(f"{lang}: {percent:.2f}%")
    for lang, count in guess_language_counter.items():
        percent = (count / total_count) * 100
        print(f"Guess, {lang}: {percent:.2f}%")

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

    languages, guess_languages = detect_languages(text)
    print_languages(languages, guess_languages)

if __name__ == "__main__":
    main()
