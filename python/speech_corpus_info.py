# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:00:11 2023

@author: Ye Kyaw Thu, LU Lab., Myanmar
I plan to update with detail examples ...  
speech corpus တွေရဲ့ format တွေက အမျိုးမျိုးရှိလို့ စလေ့လာတဲ့သူအတွက်က အချိန်ပေးရတာမို့။
အချိန်ရတဲ့အခါမှာ corpus ရဲ့ စုစုပေါင်းနာရီနဲ့ transcription information အသေးစိတ်ကို ဖြည့်မယ်။  
"""

import argparse

corpus_info = {
    "timit": {
        "name": "TIMIT",
        "description": "TIMIT is designed to provide speech data for acoustic-phonetic studies and for the development and evaluation of automatic speech recognition systems.",
        "audio_format": ".WAV files sampled at 16 kHz",
        "transcription_format": "Orthographic transcriptions, time-aligned phonetic transcriptions"
    },
    "librispeech": {
        "name": "LibriSpeech",
        "description": "LibriSpeech is a corpus of approximately 1000 hours of 16kHz read English speech, prepared by Vassil Panayotov with the assistance of Daniel Povey. The data is derived from read audiobooks from the LibriVox project.",
        "audio_format": ".flac files sampled at 16 kHz",
        "transcription_format": "Orthographic transcriptions"
    },
    "voxforge": {
        "name": "VoxForge",
        "description": "VoxForge was set up to collect transcribed speech for use with Free and Open Source Speech Recognition Engines (on Linux, Windows and Mac).",
        "audio_format": ".wav files sampled at 16 kHz",
        "transcription_format": "Orthographic transcriptions in .txt files"
    },
    "commonvoice": {
        "name": "Common Voice",
        "description": "Common Voice is a project by Mozilla that allows people to donate their voices to an open repository. The dataset includes a large number of short spoken sentences from a diverse range of contributors.",
        "audio_format": ".mp3 files",
        "transcription_format": "Orthographic transcriptions in .tsv files"
    },
    "tedlium": {
        "name": "TED-LIUM",
        "description": "The TED-LIUM corpus is a dataset of TED talks, automatically aligned with transcriptions. It's useful for training models for automatic speech recognition.",
        "audio_format": ".sph files",
        "transcription_format": "Orthographic transcriptions in .stm files"
    },
    "yesno": {
        "name": "YesNo",
        "description": "The YesNo corpus includes 60 recordings of one individual saying yes or no in Hebrew. Each recording is eight words long.",
        "audio_format": ".wav files sampled at 8 kHz",
        "transcription_format": "Orthographic transcriptions in .txt files"
    },
    "libritts": {
    "name": "LibriTTS",
    "description": "LibriTTS is a corpus derived from LibriSpeech and Wikipedia. It is intended for TTS research and includes noise cleaned transcripts and speaker information.",
    "audio_format": ".wav files",
    "transcription_format": "Orthographic transcriptions in .tsv files",
    "transcription_examples": [
        "1 | file_path_1 | This is the first sentence. | speaker_1",
        "2 | file_path_2 | This is another sentence. | speaker_2",
        "3 | file_path_3 | Yet another sentence here. | speaker_1",
        "4 | file_path_4 | This sentence is different. | speaker_2",
        "5 | file_path_5 | This is the last example sentence. | speaker_1"
    ]
},
}

def print_corpus_info(corpus):
    info = corpus_info[corpus]
    print(f"Corpus: {info['name']}")
    print(f"Description: {info['description']}")
    print(f"Audio format: {info['audio_format']}")
    print(f"Transcription format: {info['transcription_format']}")
    if 'transcription_examples' in info:
        print("Transcription examples:")
        for example in info['transcription_examples']:
            print(f"  {example}")
    print()

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("corpus", nargs='?', help="Name of the speech corpus", choices=list(corpus_info.keys()))
    parser.add_argument("-l", "--list", action="store_true", help="List all available speech corpus formats")
    args = parser.parse_args()

    if args.list:
        print("Available corpus formats:")
        for corpus in corpus_info.keys():
            print_corpus_info(corpus)
    elif args.corpus:
        print_corpus_info(args.corpus)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
