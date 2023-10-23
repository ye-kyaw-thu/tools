## Written by Ye Kyaw Thu, LU Lab., Myanmar
## For drawing a graph of sentence level hatespeech tag distributions
## Last updated: 23 Oct 2023
## How to run:
## E.g. python ./compare_sentence_tag_distributions.py -p ./sentence/ -g ./sentence_compare.png

## File/Folder information for your reference
## I saved GPT-2 model output files under sentence/ folder as follows
## (base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script$ tree sentence
## sentence
## ├── Test-1
## ├── Test-2
## ├── Test-3
## ├── Test-4
## └── Test-5

## File format information is as follows:
## (base) ye@lst-gpu-3090:~/exp/myHatespeech/eval/script/sentence$ head -n 3 Test-5
## မနက် ၅ နာရီ ခု ထိ မ လာ ဘူး ၅ မိနစ် ၅ နာရီ ထိ ပျက် သွား အောင် ပေး တာ လား လီး ပဲ ဟေ့ မအေလိုး တွေ    ab
## မီး ပျက် သွား ပြီ ပြန် ဖျက် သလို ပဲ     no
## မီး လာ ရ မှာ မီး ပေး ပြီး ၅ မိနစ် တောင် မ ပြည့် တော့ ဘူး မအေလိုး တွေ မီး နာရီ ပြန် ပျက် တယ် ဆို တော့ မ သိ ရင် လည်း နာရီဝက် လည်း ပျက် ပြီ လီး ပဲ ဟေ့       ab


import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def read_files(directory):
    tag_counts = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                tag = line.strip().split('\t')[-1]
                tag_counts.setdefault(filename, {}).setdefault(tag, 0)
                tag_counts[filename][tag] += 1
    return tag_counts

def plot_comparison(tag_counts, output_filename):
    df = pd.DataFrame(tag_counts).T.fillna(0)
    df = df.sort_index()  # Sort by filenames in alphabetical order
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 7))
    ax.set_ylabel('Tag Count')
    ax.set_xlabel('GPT-2 Model-Generated Hate Speech Sentences')
    ax.set_title('Sentence-level Hate Speech Tag Distributions Across Model Test Outputs')
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
