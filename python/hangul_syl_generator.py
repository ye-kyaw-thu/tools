import argparse

# Written by Ye Kyaw Thu, LU Lab., Myanmar
# Last updated: 23 Dec 2023
# How to run:
# python hangul_syl_generator.py --consonant ㄱ
# python hangul_syl_generator.py --vowel ㅏ
# python hangul_syl_generator.py --consonant ㄱ --vowel ㅏ
# python hangul_syl_generator.py --output output.txt
# python hangul_syl_generator.py --help
# python ./hangul_syl_generator.py --format list
# python ./hangul_syl_generator.py --format list --pronunciation
# python ./hangul_syl_generator.py -p -u -s
# python hangul_syl_generator.py -u | grep "힣"
# 힣 ||| U+D7A3


# Reference: 
# https://en.wikipedia.org/wiki/Hangul_Syllables
# https://en.wikipedia.org/wiki/Hangul_consonant_and_vowel_tables
# https://forum.unilang.org/viewtopic.php?t=24384
# https://unicode.org/charts/PDF/U1100.pdf
# https://www.compart.com/en/unicode/block/U+AC00

# Hangul Unicode Blocks
HANGUL_START = 0xAC00

# Basic and Complex Hangul Consonants and Vowels
basic_consonants = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
basic_vowels = ["ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ"]

complex_consonants = ["ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ"]
complex_vowels = ["ㅐ", "ㅒ", "ㅔ", "ㅖ", "ㅘ", "ㅙ", "ㅚ", "ㅝ", "ㅞ", "ㅟ", "ㅢ"]

# Combine basic and complex characters
consonants = basic_consonants + complex_consonants
vowels = basic_vowels + complex_vowels

# Correct list of final consonants (Jongseong) in modern Hangul
final_consonants = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

# Romanization mapping
romanization_map = {
    "ㄱ": "g", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "d", "ㄸ": "tt", "ㄹ": "r", "ㅁ": "m", "ㅂ": "b", "ㅃ": "pp",
    "ㅅ": "s", "ㅆ": "ss", "ㅇ": "", "ㅈ": "j", "ㅉ": "jj", "ㅊ": "ch", "ㅋ": "k", "ㅌ": "t", "ㅍ": "p", "ㅎ": "h",
    "ㅏ": "a", "ㅑ": "ya", "ㅓ": "eo", "ㅕ": "yeo", "ㅗ": "o", "ㅛ": "yo", "ㅜ": "u", "ㅠ": "yu", "ㅡ": "eu", "ㅣ": "i",
    "ㅐ": "ae", "ㅒ": "yae", "ㅔ": "e", "ㅖ": "ye", "ㅘ": "wa", "ㅙ": "wae", "ㅚ": "oe", "ㅝ": "wo", "ㅞ": "we", "ㅟ": "wi", "ㅢ": "ui"
}

# Function to create a Hangul syllable
def create_hangul_syllable(choseong, jungseong, jongseong=None):
    choseong_index = consonants.index(choseong) if choseong in consonants else 0
    jungseong_index = vowels.index(jungseong) if jungseong in vowels else 0
    jongseong_index = final_consonants.index(jongseong) if jongseong in final_consonants else 0

    # Calculate Unicode value
    syllable = HANGUL_START + (choseong_index * 588) + (jungseong_index * 28) + jongseong_index
    return chr(syllable)

# Generate all possible Hangul syllables based on given consonant and/or vowel
def generate_hangul_syllables(choseong=None, jungseong=None, pronunciation=False, show_unicode=False, show_sequence=False):
    choseong_list = [choseong] if choseong else consonants
    jungseong_list = [jungseong] if jungseong else vowels
    all_syllables = []

    for ch in choseong_list:
        for jg in jungseong_list:
            for jg_final in final_consonants:
                syllable = create_hangul_syllable(ch, jg, jg_final)
                display = [syllable]

                if pronunciation:
                    romanized = romanization_map[ch] + romanization_map[jg] + romanization_map.get(jg_final, "")
                    display.append(romanized)

                if show_unicode:
                    unicode_val = f"U+{ord(syllable):04X}"
                    display.append(unicode_val)

                if show_sequence:
                    combination = f"{ch}/{jg}/{jg_final if jg_final else 'None'}"
                    display.append(combination)

                all_syllables.append(' ||| '.join(display))

    return all_syllables

# Command-line argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate Hangul syllables.')
    parser.add_argument('--consonant', '-c', help='Specify a consonant character.')
    parser.add_argument('--vowel', '-v', help='Specify a vowel character.')
    parser.add_argument('--output', '-o', help='Output file to save the syllables.')
    parser.add_argument('--format', '-f', choices=['list', 'line'], default='line', help='Output format: list or line (default: line).')
    parser.add_argument('--pronunciation', '-p', action='store_true', help='Include romanization for each syllable.')
    parser.add_argument('--unicode', '-u', action='store_true', help='Show Unicode values of each syllable.')
    parser.add_argument('--sequence', '-s', action='store_true', help='Show all characters of each consonant.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Generate syllables based on provided arguments
    syllables = generate_hangul_syllables(args.consonant, args.vowel, args.pronunciation, args.unicode, args.sequence)

    # Output formatting
    output = '\n'.join(syllables) if args.format == 'line' else str(syllables)

    # Output handling
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(output)
        print(f"Syllables saved to {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()
