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
