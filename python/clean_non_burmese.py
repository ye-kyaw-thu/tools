"""

Useful for cleaning invisible characters such as ZWNJ, ZWSP, non Burmese characters, Burmese numbers and all symbols.
(ဒီ python code က ဗမာစာ NLP အလုပ်အတွက် တကယ်အသုံးဝယ်ပါတယ်။ 
နံပါတ်တွေကိုလည်း ဖယ်ထားတယ်။ syllable dictionary ဆောက်ဖို့နဲ့ language model မဆောက်ခင်မှာ cleaning လုပ်ဖို့အတွက် သုံးခဲ့တယ်။)
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 10 Feb 2024

Usage Example:  

## Call --help

(LM) yekyaw.thu@gpu:~/exp/normalization/mk_syl_dict$ python ./clean_non_burmese.py --help
usage: clean_non_burmese.py [-h] [--input INPUT] [--output OUTPUT] [--verbose]
                            [--space_cleaning]

Remove unwanted characters from text while preserving the overall structure

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Input file path
  --output OUTPUT       Output file path
  --verbose             Print counts of removed characters
  --space_cleaning, -s  Clean up space characters (remove leading/trailing spaces,
                        multiple spaces)
(LM) yekyaw.thu@gpu:~/exp/normalization/mk_syl_dict$

## without Space Cleaning

Note: အောက်ပါအတိုင်း run ရင် ဘယ်နေရာက စာလုံးတွေကို ဖျက်သွားတယ် ဆိုတာကို လူအတွက် manual စစ်ရတာ လွယ်တယ်။ သို့သော် space အပိုတွေ အနေနဲ့ ရှိနေလိမ့်မယ်။   

python ./clean_non_burmese.py --input ./all_file.syl --output ./all_file.syl.clean --verbose
Removed 342155 unwanted characters

## Running with --space_cleaning

တကယ်ကတော့ အောက်ပါအတိုင်း --space_cleaning ဆိုတဲ့ option ကို ဖြည့်ပြီး run တာကမှ output cleaned file မှာ မလိုအပ်တဲ့ extra space တွေ ရှိမနေမှာ။  

(base) yekyaw.thu@gpu:~/exp/normalization/mk_syl_dict$ python ./clean_non_burmese.py --input ./all_file.syl --output ./all_file.syl.clean.sc --verbose --space_cleaning
Removed 342155 unwanted characters

Checked with wc:  

(base) yekyaw.thu@gpu:~/exp/normalization/mk_syl_dict$ wc all_file.syl*
   338597   4346925  41676004 all_file.syl
   338597   4017777  40789462 all_file.syl.clean
   338596   4017777  40466632 all_file.syl.clean.sc
  1015790  12382479 122932098 total
(base) yekyaw.thu@gpu:~/exp/normalization/mk_syl_dict$

"""

import sys
import argparse
import errno
import re

def remove_special_chars(text, space_cleaning=False, verbose=False):
    # Unicode representations for special characters
    zwnj = '\u200C'  # Zero Width Non-Joiner
    zwsp = '\u200B'  # Zero Width Space
    hsp = '\u00AD'   # Half Space (Soft Hyphen)
    soft_hyphen = '\u00AD'
    word_joiner = '\u2060'
    backspace = '\u0008'
    object_replacement_character = '\uFEFF'

    # Combine all special invisible characters into one string
    special_chars = zwnj + zwsp + hsp + soft_hyphen + word_joiner + backspace + object_replacement_character

    # Regex pattern for removing non-Burmese characters while keeping Burmese script and specified characters
    allowed_burmese_range = 'က-အ'
    additional_allowed_chars = 'ျြွှောါိီုူဲံ့း်္ဿဣဤဥဦဧဩဪ၌၍၏၎'
    preserve_structure_chars = ' \n'
    removal_pattern = f'[^{allowed_burmese_range}{additional_allowed_chars}{preserve_structure_chars}]'

    # Counters for verbose mode
    count_removed = len(re.findall(removal_pattern, text))

    # Removing the characters
    cleaned_text = re.sub(removal_pattern, '', text)

    # Space cleaning, improved to preserve newlines
    if space_cleaning:
        # Process each line individually to preserve newlines
        lines = cleaned_text.splitlines()
        cleaned_lines = []
        for line in lines:
            # Remove leading and trailing spaces and replace multiple spaces with a single space in each line
            cleaned_line = re.sub(r'\s+', ' ', line).strip()
            cleaned_lines.append(cleaned_line)
        cleaned_text = '\n'.join(cleaned_lines)

    if verbose:
        print(f"Removed {count_removed} unwanted characters")

    return cleaned_text

def main():
    parser = argparse.ArgumentParser(description='Remove unwanted characters from text while preserving the overall structure')
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--verbose', action='store_true', help='Print counts of removed characters')
    parser.add_argument('--space_cleaning', '-s', action='store_true', help='Clean up space characters (remove leading/trailing spaces, multiple spaces)')
    args = parser.parse_args()

    # Read from input file or stdin
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = sys.stdin.read()

    # Process the text
    cleaned_text = remove_special_chars(text, space_cleaning=args.space_cleaning, verbose=args.verbose)

    # Write to output file or stdout
    try:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)
        else:
            sys.stdout.write(cleaned_text)
    except BrokenPipeError:
        sys.stdout.close()
        sys.stderr.close()

if __name__ == "__main__":
    main()
