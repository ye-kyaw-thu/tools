#!/bin/bash

## NLLB Lib based Translation
## Written by Ye Kyaw Thu, NECTEC, Thailand.
## Usage:
## ./nllb-translate.sh --input input.txt --source eng_Latn --target spa_Latn
## ./nllb-translate.sh --input input.txt --source eng_Latn --target spa_Latn --output output.txt
## time ./nllb-translate.sh --input data/
## baseline/ref_baseline.txt --source tha_Thai --target mya_Mymr --output output_th-my.txt


# Function to display usage
usage() {
    echo "Usage: $0 --input <inputfile> --source <source_lang> --target <target_lang> [--output <outputfile>] [--delimiter <delimiter>]"
    exit 1
}

# Parse command line arguments
INPUT=""
OUTPUT=""
SOURCE=""
TARGET=""
DELIMITER=$'\t'  # Default delimiter is a tab character

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --input) INPUT="$2"; shift ;;
        --output) OUTPUT="$2"; shift ;;
        --source) SOURCE="$2"; shift ;;
        --target) TARGET="$2"; shift ;;
        --delimiter) DELIMITER="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; usage ;;
    esac
    shift
done

# Check if input file, source language, and target language are provided
if [[ -z "$INPUT" || -z "$SOURCE" || -z "$TARGET" ]]; then
    echo "Error: Input file, source language, and target language are required."
    usage
fi

# Check if input file exists
if [[ ! -f "$INPUT" ]]; then
    echo "Error: Input file does not exist."
    exit 1
fi

# Function to translate text
translate() {
    local text="$1"
    curl -s -N 'https://winstxnhdw-nllb-api.hf.space/api/v3/translate' \
         -H 'Content-Type: application/json' \
         -d "{\"text\": \"$text\", \"source\": \"$SOURCE\", \"target\": \"$TARGET\"}" | jq -r '.result'
}

# Read input file and process each line
if [[ -z "$OUTPUT" ]]; then
    # Output to screen
    while IFS= read -r line; do
        translated=$(translate "$line")
        echo -e "${line}${DELIMITER}${translated:-$line}"
    done < "$INPUT"
else
    # Output to file
    while IFS= read -r line; do
        translated=$(translate "$line")
        echo -e "${line}${DELIMITER}${translated:-$line}" >> "$OUTPUT"
    done < "$INPUT"
fi
