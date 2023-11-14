## Written by Ye Kyaw Thu, LU Lab., Myanmar
## for text mining with keyword
## last updated: 14 Nov 2023

import requests
from bs4 import BeautifulSoup
import re
import argparse

def download_sentences(url, keyword, num_sentences):
    # Send a GET request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text and split into sentences
    text = soup.get_text()
    sentences = re.split(r'[\u104A\u104B]+', text)  # Split on PotHtee and PotMa

    # Filter sentences that contain the keyword
    keyword_sentences = [sentence for sentence in sentences if keyword in sentence]

    # Limit the number of sentences if specified
    return keyword_sentences[:num_sentences]

def process_urls(urls, keyword, num_sentences, output_filename):
    output_data = []
    for url in urls:
        sentences = download_sentences(url, keyword, num_sentences)
        output_data.extend(sentences)

    if output_filename:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for sentence in output_data:
                file.write(sentence + '\n')
    else:
        for sentence in output_data:
            print(sentence)

def main():
    parser = argparse.ArgumentParser(description='Download sentences from webpages containing a specific keyword.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', type=str, help='URL of the webpage to scrape')
    group.add_argument('--url_file', type=str, help='File containing URLs to scrape, one per line')
    parser.add_argument('--keyword', type=str, required=True, help='Keyword to search in sentences')
    parser.add_argument('--num_sentences', type=int, default=10, help='Number of sentences to return')
    parser.add_argument('--output_filename', type=str, help='File to save the downloaded sentences (optional, prints to stdout if not specified)')

    args = parser.parse_args()

    if args.url:
        urls = [args.url]
    else:
        with open(args.url_file, 'r') as file:
            urls = [line.strip() for line in file.readlines()]

    process_urls(urls, args.keyword, args.num_sentences, args.output_filename)

if __name__ == '__main__':
    main()
