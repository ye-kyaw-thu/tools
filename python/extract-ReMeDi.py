"""
ReMeDi corpus က medical domain dialogue တရုတ်စကားပြောဒေတာပါ။  
အဲဒီ corpus ကနေ ကိုယ်လိုချင်တဲ့ dialogue ID ရယ်၊ ဒေါက်တာကပြောတဲ့ စာကြောင်းရယ်၊ လူနာက ပြောတဲ့စာကြောင်းတွေရယ်ကို ဆွဲထုတ်ဖို့အတွက် ရေးခဲ့တဲ့ code ပါ။  
Last updated: 8 Mar 2024
Usage: python extract_sentences.py <json_file> <output_file>
"""

import json
import sys

def extract_sentences(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    extracted_sentences = []

    for dialogue in data:
        dialogue_id = dialogue['dialogue']
        dialogue_sentences = []

        for info in dialogue['information']:
            turn = info['turn']
            role = info['role']
            sentence = info['sentence']
            dialogue_sentences.append((turn, role, sentence))

        extracted_sentences.append((dialogue_id, dialogue_sentences))

    return extracted_sentences

def write_to_file(sentences, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for dialogue_id, dialogue_sentences in sentences:
            file.write(f"Dialogue {dialogue_id}:\n")
            for turn, role, sentence in dialogue_sentences:
                file.write(f"{role}: {sentence}\n")
            file.write("\n")  # Add a newline after each dialogue

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_sentences.py <json_file> <output_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    output_file = sys.argv[2]

    extracted_sentences = extract_sentences(json_file)
    write_to_file(extracted_sentences, output_file)

    print("Sentences extracted and saved to", output_file)
