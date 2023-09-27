## Written by Ye Kyaw Thu, LU Lab., Myanmar
## for replacing pipe character with space
## myPOS corpus မှာ compound word တွေကို pipe နဲ့ ခြားပြီး ရေးထားတာမို့ အဲဒီအပိုင်ကို ရှင်းဖို့အတွက် သုံးခဲ့တယ်

import sys

def replace_pipe_with_space(text):
    return text.replace("|", " ")

def main():
    # Check if input is being provided via stdin (e.g., piping using `|`)
    # ဒီမှာ စစ်ထားတာက ဖိုင်ထဲမှာ အစားဝင်ထိုးမယ့် pipe character နဲ့ မဆိုင်ပါဘူး။
    # input filename နဲ့ ပေးတာမဟုတ်ပဲ Linux မှာ cat လို command နဲ့ ရိုက်ထုတ်ပြီးမှ
    # python program ကို | နဲ့ လက်ဆင့်ကမ်းတာမျိုး လုပ်ကြတာမို့လို့၊ အဲဒီအပိုင်းကို စစ်ထားတာပါ။
    if not sys.stdin.isatty():
        for line in sys.stdin:
            print(replace_pipe_with_space(line), end="")
    # Check if a filename argument is provided
    elif len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            for line in file:
                print(replace_pipe_with_space(line), end="")
    else:
        print("Please provide an input file or pipe in the data.")

if __name__ == "__main__":
    main()
