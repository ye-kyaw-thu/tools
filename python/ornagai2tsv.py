#!/usr/bin/env python3

"""
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Conversion of Ornagai html file to TSV.

Note:
    Before you run ornagai2tsv.py:  
    pip install mobi --break-system-packages
    mobiunpack ./ornagai.mobi ./extracted  
    find . -type f -name "*.html" -o -name "*.htm" -o -name "*.txt"

Usage:
    # default TSV with header:
    python ornagai2tsv.py -i book.html -o dictionary.tsv

    # Custom delimiter (|||) without header:
    python ornagai2tsv.py -i book.html -o dictionary.txt -d "|||" --no-header

    # Custom delimiter (|||) without header:
    python ornagai2tsv.py -i book.html | head -n 20
"""

import sys
import argparse
import re
from html import unescape

def extract_entries(html_content):
    """Extract dictionary entries using regex patterns"""
    entries = []
    
    # Pattern to match each dictionary entry
    entry_pattern = re.compile(
        r'<idx:entry[^>]*>.*?<idx:orth[^>]*value="([^"]*)"[^>]*>.*?<dd>(.*?)</dd>.*?</idx:entry>',
        re.DOTALL
    )
    
    # Pattern to clean up HTML tags
    tag_pattern = re.compile(r'<[^>]+>')
    
    # Pattern to clean up multiple spaces
    space_pattern = re.compile(r'\s+')
    
    for match in entry_pattern.finditer(html_content):
        word = match.group(1).strip()
        definition_html = match.group(2)
        
        # Remove HTML tags but keep text content
        definition = tag_pattern.sub(' ', definition_html)
        definition = unescape(definition)
        
        # Clean up whitespace
        definition = space_pattern.sub(' ', definition).strip()
        
        if word and definition:
            entries.append((word, definition))
    
    return entries

def convert_html_to_text(html_file, output_file, delimiter='\t', include_header=True):
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Parsing dictionary content...", file=sys.stderr)
        entries = extract_entries(content)
        
        print(f"Found {len(entries)} dictionary entries", file=sys.stderr)
        
        # Write header if requested
        if include_header:
            output_file.write(f"word{delimiter}definition\n")
        
        # Write entries
        for word, definition in entries:
            # Escape any existing delimiters in the content
            safe_word = word.replace(delimiter, ' ')
            safe_definition = definition.replace(delimiter, ' ')
            output_file.write(f"{safe_word}{delimiter}{safe_definition}\n")
            
    except Exception as e:
        print(f"Error processing HTML file: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Convert Ornagai dictionary HTML to delimited text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input HTML file (from mobiunpack)',
        type=str
    )
    parser.add_argument(
        '-o', '--output',
        help='Output text file (default: stdout)',
        type=str,
        default=None
    )
    parser.add_argument(
        '-d', '--delimiter',
        help='Field delimiter (default: tab)',
        type=str,
        default='\t'
    )
    parser.add_argument(
        '--no-header',
        help='Omit header row',
        action='store_false',
        dest='include_header'
    )
    
    args = parser.parse_args()
    
    # Output handling
    output_file = sys.stdout
    if args.output:
        try:
            output_file = open(args.output, 'w', encoding='utf-8')
        except IOError:
            print(f"Error: Cannot write to output file: {args.output}", file=sys.stderr)
            sys.exit(1)
    
    try:
        convert_html_to_text(
            args.input, 
            output_file,
            delimiter=args.delimiter,
            include_header=args.include_header
        )
    except Exception as e:
        print(f"Error during conversion: {str(e)}", file=sys.stderr)
        sys.exit(1)
    finally:
        if args.output:
            output_file.close()

if __name__ == "__main__":
    main()

