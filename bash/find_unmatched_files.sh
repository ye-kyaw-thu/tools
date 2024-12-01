#!/bin/bash

# to find files with one extension (-e1 or --extension1) that do not have a corresponding file with another extension (-e2 or --extension2)

# Written by Ye Kyaw Thu, LU Lab., Myanmar
# Last updated: 1 Dec 2024
# How to run: bash find_unmatched_files.sh -e1 epub -e2 pdf /path/to/directory

function usage() {
    echo "Usage: $0 -e1 <extension1> -e2 <extension2> [directory]"
    echo
    echo "Options:"
    echo "  -e1, --extension1   First file extension to compare (e.g., epub)"
    echo "  -e2, --extension2   Second file extension to compare (e.g., pdf)"
    echo "  [directory]         Directory to search (default: current directory)"
    echo "  -h, --help          Show this help message"
    exit 1
}

EXT1=""
EXT2=""
DIR="."

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -e1|--extension1) EXT1="$2"; shift ;;
        -e2|--extension2) EXT2="$2"; shift ;;
        -h|--help) usage ;;
        *) DIR="$1" ;;
    esac
    shift
done

if [[ -z "$EXT1" || -z "$EXT2" ]]; then
    echo "Error: Both -e1 and -e2 are required."
    usage
fi

# Find unmatched files
find "$DIR" -type f -name "*.$EXT1" | while read -r file1; do
    base_name="${file1%.$EXT1}"
    if [[ ! -e "${base_name}.$EXT2" ]]; then
        echo "$file1"
    fi
done
