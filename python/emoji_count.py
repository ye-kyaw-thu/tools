"""
For counting emojis.
Written by Ye Kyaw Thu, LU Lab, Myanmar.
Last updated: 26 April 2024

Usage:
python ./emoji_count.py --input ./myHatespeech_checked_data_22Jan.txt.f1

"""

import argparse

def is_emoji(char):
    # Emoji Unicode ranges
    emoji_ranges = [
        (0x1F300, 0x1F5FF),
        (0x1F600, 0x1F64F),
        (0x1F680, 0x1F6FF),
        (0x1F700, 0x1F77F),
        (0x1F780, 0x1F7FF),
        (0x1F800, 0x1F8FF),
        (0x1F900, 0x1F9FF),
        (0x1FA00, 0x1FA6F),
        (0x1FA70, 0x1FAFF),
        (0x2600, 0x26FF),
        (0x2700, 0x27BF),
        (0xFE00, 0xFE0F),
        (0x1F1E6, 0x1F1FF)
    ]
    code = ord(char)
    return any(start <= code <= end for start, end in emoji_ranges)

def count_unique_emojis(input_file):
    emoji_counts = {}
    total_emojis = 0
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            emojis = [char for char in line if is_emoji(char)]
            total_emojis += len(emojis)
            for emoji in emojis:
                if emoji not in emoji_counts:
                    emoji_counts[emoji] = 1
                else:
                    emoji_counts[emoji] += 1
    return emoji_counts, total_emojis

def main():
    parser = argparse.ArgumentParser(description="Count unique emoji characters from a UTF-8 input file.")
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    emoji_counts, total_emojis = count_unique_emojis(input_file)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write("Unique Emojis Counts:\n")
            for emoji, count in emoji_counts.items():
                outfile.write(f"{emoji}: {count}\n")
            outfile.write(f"Total Unique Emojis: {len(emoji_counts)}\n")
            outfile.write(f"Total Emojis: {total_emojis}\n")
        print(f"Results saved to {output_file}")
    else:
        print("Unique Emojis Counts:")
        for emoji, count in emoji_counts.items():
            print(f"{emoji}: {count}")
        print(f"Total Unique Emojis: {len(emoji_counts)}")
        print(f"Total Emojis: {total_emojis}")

if __name__ == "__main__":
    main()
