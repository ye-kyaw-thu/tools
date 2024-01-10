"""
For Myanmar language proverb extraction from json file.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 10 Jan 2024
Refernce json file: https://github.com/sannlynnhtun-coding/Burma-Project-Ideas/tree/main/05.%20Myanmar%20Proverbs

"""

import json
import argparse

def extract_data(json_data, title_id, proverb_id=None):
    proverbs = json_data['Tbl_MMProverbs']
    extracted_data = []

    if proverb_id is not None:
        extracted_data = [p for p in proverbs if p['TitleId'] == title_id and p['ProverbId'] == proverb_id]
    else:
        extracted_data = [p for p in proverbs if p['TitleId'] == title_id]

    return extracted_data

def main():
    parser = argparse.ArgumentParser(description='Extract ProverbName, ProverbDesp, or both from JSON file based on TitleId and optionally ProverbId.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    parser.add_argument('--titleid', type=int, required=True, help='Extract based on TitleId')
    parser.add_argument('--proverbid', type=int, help='Extract based on ProverbId (requires --titleid)')
    parser.add_argument('--output', type=str, help='Output file name (optional, if not provided, print to stdout)')
    parser.add_argument('--content', choices=['ProverbName', 'ProverbDesp', 'Both'], default='ProverbName', help='Type of content to extract (default: ProverbName)')
    args = parser.parse_args()

    if args.proverbid and not args.titleid:
        parser.error("--proverbid requires --titleid")

    with open(args.json_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    extracted_data = extract_data(json_data, args.titleid, args.proverbid)

    if args.content == 'Both':
        content_to_display = ["{}: {}".format(p['ProverbName'], p['ProverbDesp']) for p in extracted_data]
    else:
        content_to_display = [p[args.content] for p in extracted_data]

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            for line in content_to_display:
                file.write(line + '\n')
    else:
        for line in content_to_display:
            print(line)

if __name__ == '__main__':
    main()
