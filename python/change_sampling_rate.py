## Written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC
## Last updated: 2 July 2023
## Changing sampling rate of wavefiles
## How to read:
## python ./change_sampling_rate.py --input_folder ./wavs --output_folder ./wavs_22khz --target_sample_rate 22050

import os
import argparse
import librosa
import soundfile as sf
import glob

def resample_audio(input_folder, output_folder, target_sample_rate):
    # Check if output_folder exists, if not create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all wav files in the input_folder
    wav_files = glob.glob(os.path.join(input_folder, '*.wav'))

    num_successfully_converted = 0

    for wav_file in wav_files:
        # Load the audio file with original sr
        audio, sr = librosa.load(wav_file, sr=None)
        
        # Resample the audio to the target_sample_rate
        audio_resampled = librosa.resample(y=audio, orig_sr=sr, target_sr=target_sample_rate)
        
        # Save the resampled audio
        output_file_path = os.path.join(output_folder, os.path.basename(wav_file))
        sf.write(output_file_path, audio_resampled, target_sample_rate)
        
        num_successfully_converted += 1

    print(f"Successfully converted {num_successfully_converted} files from original sampling rate to {target_sample_rate} Hz")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_folder", type=str, required=True, help="Path to input folder containing WAV files")
    parser.add_argument("--output_folder", type=str, required=True, help="Path to output folder where converted WAV files will be saved")
    parser.add_argument("--target_sample_rate", type=int, required=True, help="Target sampling rate to convert audio files to")
    args = parser.parse_args()

    resample_audio(args.input_folder, args.output_folder, args.target_sample_rate)
