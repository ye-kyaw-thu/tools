# Written by Ye Kyaw Thu
# for conversion video format m4v to mp4
# Last updated: 20 June 2023
#
# How to run:
# (base) rnd@gpu:~/demo/vr/exp/word$ time python m4v_to_mp4.py --input Words --output allmp4

import os
import subprocess
import argparse

def convert_videos(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    m4v_files = [f for f in os.listdir(input_folder) if f.endswith('.m4v')]
    mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    converted_files = 0
    for file in m4v_files:
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file.replace('.m4v', '.mp4'))
        try:
            subprocess.run(['ffmpeg', '-i', input_file, '-vcodec', 'copy', '-acodec', 'copy', output_file], check=True)
            converted_files += 1
        except subprocess.CalledProcessError:
            print(f'Conversion failed for {file}')

    for file in mp4_files:
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file)
        try:
            subprocess.run(['cp', input_file, output_file], check=True)
        except subprocess.CalledProcessError:
            print(f'Copy failed for {file}')

    print(f'Total no. of successfully converted m4v files: {converted_files}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert m4v videos to mp4.')
    parser.add_argument('--input', type=str, help='Input folder path')
    parser.add_argument('--output', type=str, help='Output folder path')

    args = parser.parse_args()

    convert_videos(args.input, args.output)
