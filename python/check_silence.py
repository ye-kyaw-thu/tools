## Written by Ye Kyaw Thu, LST, NECTEC, Thailand
## Last updated: 4 July 2023
## Check whether audio files are silent
## How to run:
## python ./check_silence.py --input_folder ./test_out/

import os
import argparse
import soundfile as sf
import numpy as np

def check_silence(input_folder, silence_threshold=0.001):
    for filename in os.listdir(input_folder):
        if filename.endswith('.wav'):
            file_path = os.path.join(input_folder, filename)
            data, _ = sf.read(file_path)

            rms = np.sqrt(np.mean(data**2))
            if rms < silence_threshold:
                print(f'{filename} might be silent, RMS={rms}')
            else:
                print(f'{filename} is not silent, RMS={rms}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check whether audio files are silent.')
    parser.add_argument('--input_folder', type=str, required=True, help='Path to the input folder contai>

    args = parser.parse_args()
    check_silence(args.input_folder)
  
