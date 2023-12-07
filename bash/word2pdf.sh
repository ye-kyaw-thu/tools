#!/bin/bash

# Written by Ye Kyaw Thu, LU Lab., Myanmar
# For Word file to PDF file conversion
# Note: You need Libreoffice.
# How to run:
# ./convert_word_to_pdf.sh -i input.docx -o output.pdf

while [[ $# -gt 0 ]]; do
    case "$1" in
        -i|--input)
            input_file="$2"
            shift 2
            ;;
        -o|--output)
            output_file="$2"
            shift 2
            ;;
        *)
            echo "Invalid argument: $1"
            exit 1
            ;;
    esac
done

if [ -z "$input_file" ] || [ -z "$output_file" ]; then
    echo "Usage: $0 -i|--input input_file -o|--output output_file"
    exit 1
fi

if [[ ! -f "$input_file" ]]; then
    echo "Input file does not exist: $input_file"
    exit 1
fi

libreoffice --headless --convert-to pdf "$input_file"
echo "Converted $input_file to $output_file"

mv "${input_file%.*}.pdf" "$output_file"
