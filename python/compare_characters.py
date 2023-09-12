import sys

def count_characters_per_line(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            char_counts = [len(line.strip()) for line in lines]
            return char_counts
    except FileNotFoundError:
        print(f"Couldn't open input file {file_path}!")

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_characters.py <bengali-file> <braille-file>")
        sys.exit(1)

    bengali_file = sys.argv[1]
    braille_file = sys.argv[2]

    bengali_char_counts = count_characters_per_line(bengali_file)
    braille_char_counts = count_characters_per_line(braille_file)

    if bengali_char_counts and braille_char_counts:
        total_bengali_chars = sum(bengali_char_counts)
        total_braille_chars = sum(braille_char_counts)

        print(f"Total Bengali characters: {total_bengali_chars}")
        print(f"Total Braille characters: {total_braille_chars}")

        if total_bengali_chars > total_braille_chars:
            percentage_difference = ((total_bengali_chars - total_braille_chars) / total_braille_chars) * 100
            print(f"Bengali has {percentage_difference:.2f}% more characters than Braille.")
        elif total_braille_chars > total_bengali_chars:
            percentage_difference = ((total_braille_chars - total_bengali_chars) / total_bengali_chars) * 100
            print(f"Braille has {percentage_difference:.2f}% more characters than Bengali.")
        else:
            print("Both files have an equal number of characters.")
    else:
        print("Character count couldn't be calculated.")

if __name__ == "__main__":
    main()

