## Written by Ye Kyaw Thu, LU Lab., Myanmar
## For drawing a graph of word/phrase level hatespeech tag distributions
## Last updated: 23 Oct 2023

## File/Folder information for your reference
## (base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script$ tree word_phrase/
## word_phrase/
##├── Test-1
##├── Test-2
##├── Test-3
##├── Test-4
##└── Test-5

## File format information for your reference
##
## (base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/word_phrase$ head -n3 ./Test-2
## မနက် ၅ နာရီ ခု ထိ မ လာ ဘူး ၅ မိနစ် ၅ နာရီ ထိ ပျက် သွား အောင် ပေး တာ လား လီး/ab ပဲ ဟေ့ မအေလိုး/ab တွေ
## မီး ပျက် သွား ပြီ ပြန် ဖျက် သလို ပဲ
## မီး လာ ရ မှာ မီး ပေး ပြီး ၅ မိနစ် တောင် မ ပြည့် တော့ ဘူး မအေလိုး/ab တွေ မီး နာရီ ပြန် ပျက် တယ် ဆို တော့ မ သိ ရင် လည်း နာရီဝက် လည်း ပျက် ပြီ လီး/ab ပဲ ဟေ့
##

import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import re

def read_files(directory):
    tag_counts = {}
    tag_pattern = re.compile(r'\/([a-z]+(?:\|[a-z]+)*)')
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                tags_found = tag_pattern.findall(line)
                for tag_group in tags_found:
                    for tag in tag_group.split('|'):
                        tag_counts.setdefault(filename, {}).setdefault(tag, 0)
                        tag_counts[filename][tag] += 1
    return tag_counts

def plot_comparison(tag_counts, output_filename):
    df = pd.DataFrame(tag_counts).T.fillna(0)
    df = df.sort_index()  # Sort by filenames in alphabetical order
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 7))
    ax.set_ylabel('Tag Count')
    ax.set_xlabel('GPT Model Test Outputs')
    ax.set_title('Word/Phrase-level Hate Speech Tag Distributions Across Model Test Outputs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare Hate Speech Tag Distributions Among Files.')
    parser.add_argument('-p', '--path', required=True, help='Path to the folder containing the files.')
    parser.add_argument('-g', '--graph_filename', required=True, help='Output graph filename.')
    args = parser.parse_args()

    tag_counts = read_files(args.path)
    plot_comparison(tag_counts, args.graph_filename)
