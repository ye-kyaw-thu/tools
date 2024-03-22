"""
For making hatespeech dictionary from the following tagged sentences:

(hs-fasttext) ye@lst-gpu-server-197:~/ye/exp/hs-fasttext$ head ./hs_data_Mar19.txt.fasttext.f2
ဖော်လော်မော်/ab မ ဟုတ် လို့ ပေါ့ 🤣 🤣
နား ကို မ လည် တာ
ဆောက်မြင်ကပ်/ab ထင် တာ ပဲ
ကွမ်းယာ မှာ ထည့် စား တဲ့ စမုန်စပါး ထင် တယ်
ဖလော်မော်/ab next version
ငါ လည်း သိ ချင် နေ တာ 😁 အဲ့လို စကား တွေ ကျ နားမလည် လို့ သင် ပေး ကြ ပါ ဦး 😂
ငါ မ သိ လို့ ကိုကို့ ကို မေး ကြည့် တာ ကိုကို က လည်း baby က လွဲ ရင် မ သိ ဘူး တဲ့ 🥺
ဖော်လော်မော်/ab နဲ့ ညီမ တော် တယ် လေ 😬
sမွေး/ab ကြီး တဲ့ 😂
$မွှေး/ab ပါ

Written by Ye Kyaw Thu, NECTEC, Thailand.
Last updated: 22 Mar 2024
Usage:
python ./mk_hatespeech_dict.py --help
python ./mk_hatespeech_dict.py --input ./hs_data_Mar19.txt.fasttext.f2 \
--output hs_dict.txt

"""

import argparse
import sys

def extract_tags(input_file, output_file=None, input_delimiter='/', output_delimiter='\t'):
    tags_dict = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            words = line.split()
            for word in words:
                if '/' in word:
                    word_parts = word.split('/')
                    word_text = word_parts[0]
                    word_tags = word_parts[1].split('|')  # Split tags if they are present
                    if word_text in tags_dict:
                        tags_dict[word_text].extend(word_tags)  # If word already exists in dictionary, append tags
                    else:
                        tags_dict[word_text] = word_tags  # Otherwise, create a new entry

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word, tags in tags_dict.items():
                unique_tags = list(set(tags))  # Remove duplicates
                f.write(word + output_delimiter + '|'.join(unique_tags) + '\n')
    else:
        try:
            for word, tags in tags_dict.items():
                unique_tags = list(set(tags))  # Remove duplicates
                print(word + output_delimiter + '|'.join(unique_tags))
        except BrokenPipeError:
            # Ignore BrokenPipeError and exit gracefully
            sys.stdout.close()
            sys.stderr.close()
            sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract tagged words and create a hate speech word dictionary.")
    parser.add_argument("-i", "--input", type=str, help="Input file path", required=True)
    parser.add_argument("-o", "--output", type=str, help="Output file path", default=None)
    parser.add_argument("--input_delimiter", type=str, help="Input delimiter", default="/")
    parser.add_argument("--output_delimiter", type=str, help="Output delimiter", default="\t")
    args = parser.parse_args()

    extract_tags(args.input, args.output, args.input_delimiter, args.output_delimiter)
