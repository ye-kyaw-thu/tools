# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:29:27 2023
@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand

Mean Opinion Score Evaluation Script for TTS experiments.

How to run:
$ python MOS_eval.py --help

$ python MOS_eval.py <wavefiles_folder> <log_folder>
$ python MOS_eval.py wavefiles log

"""

import random
import argparse
import os
import datetime
from pydub import AudioSegment
from pydub.playback import play

def play_audio(audio_file, replay_limit):
    # Function to play the audio file
    sound = AudioSegment.from_file(audio_file)
    play(sound)

def get_mos_rating():
    # Function to get MOS rating from the user
    while True:
        try:
            rating = int(input("Rate the speech quality on a scale of 1-5 (1: Bad, 5: Excellent): "))
            if rating < 1 or rating > 5:
                print("Invalid rating. Please enter a number between 1 and 5.")
            else:
                return rating
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_speech(audio_folder):
    # Main function to conduct MOS evaluation
    scores = []
    
    print("Welcome to the MOS evaluation!")
    print("You will listen to the synthesized speech and rate its quality.")
    print("Please rate each speech sample on a scale of 1-5.")
    print("Press 'Q' to quit the evaluation.\n")
    
    # Get the list of audio files in the provided folder
    audio_files = [os.path.join(audio_folder, filename) for filename in os.listdir(audio_folder) if filename.endswith(".wav")]
    
    # Shuffle the audio files to randomize the order
    random.shuffle(audio_files)
    
    for audio_file in audio_files:
        print("Speech Sample:", audio_file)
        replay_limit = 3
        play_count = 0
        
        while play_count < replay_limit:
            play_audio(audio_file, replay_limit)
            play_count +=1
            if play_count >= replay_limit:
                break
            else:                
                replay_choice = input("Do you want to replay the audio? (Y/N): ")
                if replay_choice.lower() == "n":
                    break
   
        rating = get_mos_rating()
        scores.append((audio_file, rating))
        print()
        
    average_score = sum(score for _, score in scores) / len(scores)
    return scores, average_score

def save_evaluation_log(scores, average_score, user_info, log_folder):
    # Function to save the evaluation log to a file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"mos_evaluation_log_{timestamp}.txt"
    log_filepath = os.path.join(log_folder, log_filename)
    
    with open(log_filepath, "w") as log_file:
        log_file.write("MOS Evaluation Log\n")
        log_file.write("Date: {}\n\n".format(timestamp))
        
        log_file.write("User Information:\n")
        log_file.write("Name: {}\n".format(user_info.get("name", "")))
        log_file.write("Age: {}\n".format(user_info.get("age", "")))
        log_file.write("Sex: {}\n".format(user_info.get("sex", "")))
        log_file.write("Native Language: {}\n".format(user_info.get("native_language", "")))
        log_file.write("Second Language: {}\n".format(user_info.get("second_language", "")))
        log_file.write("Other Languages: {}\n".format(", ".join(user_info.get("other_languages", []))))
        
        log_file.write("\nScores:\n")
        for audio_file, score in scores:
            log_file.write("Audio File: {}\n".format(audio_file))
            log_file.write("Score: {}\n".format(score))
            log_file.write("\n")
        
        log_file.write("Total Audio Files: {}\n".format(len(scores)))
        log_file.write("Average MOS Score: {:.2f}\n".format(average_score))
        
    print("Evaluation log saved as:", log_filepath)

def parse_command_line_args():
    # Function to parse command line arguments
    parser = argparse.ArgumentParser(description="MOS Evaluation Program")
    parser.add_argument("audio_folder", help="Path to the audio folder")
    parser.add_argument("log_folder", help="Path to the log folder")
    args = parser.parse_args()
    return args.audio_folder, args.log_folder

def main():
    # Get command line arguments
    audio_folder_path, log_folder_path = parse_command_line_args()
    
    # Check if log_folder_path exists, if not, create it.
    if not os.path.exists(log_folder_path):
        os.makedirs(log_folder_path)

    # Get user information
    user_info = {}
    user_info["name"] = input("Enter your name: ")
    user_info["age"] = input("Enter your age: ")
    user_info["sex"] = input("Enter your sex: ")
    user_info["native_language"] = input("Enter your native language: ")
    user_info["second_language"] = input("Enter your second language: ")
    other_languages = input("Enter other languages you understand well (comma-separated): ")
    user_info["other_languages"] = [lang.strip() for lang in other_languages.split(",")]

    scores, average_score = evaluate_speech(audio_folder_path)
    save_evaluation_log(scores, average_score, user_info, log_folder_path)

if __name__ == "__main__":
    main()
