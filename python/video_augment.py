import os
import cv2
import numpy as np
import argparse
import sys

## Written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.
## Demo of video augmentation with temporal, noise, spatial and brightness_contrast
## Last updated: 15 June 2023
## How to run:
##
## time python ./video_augment.py --input_folder ./videos --output_folder ./videos/temporal --augment temporal
## time python ./video_augment.py --input_folder ./videos --output_folder ./videos/noise --augment noise
## time python ./video_augment.py --input_folder ./videos --output_folder ./videos/spatial --augment spatial
## time python ./video_augment.py --input_folder ./videos --output_folder ./videos/brightness_contrast --augment brightness_contrast

def add_temporal(frame, speed_factor=2):
    """Add temporal augmentation to the frame"""
    return [frame]*speed_factor

def add_spatial(frame, horizontal_shift=100, vertical_shift=100):
    """Add spatial augmentation to the frame"""
    M = np.float32([[1, 0, horizontal_shift], [0, 1, vertical_shift]])
    frame = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))
    return frame

def add_noise(frame, mean=0, std_dev=50):
    """Add random noise to the frame"""
    noise = np.random.normal(mean, std_dev, frame.shape).astype(np.uint8)
    frame = cv2.add(frame, noise)
    return frame

def change_brightness_contrast(frame, brightness=100, contrast=100):
    """Change the brightness and contrast of the frame"""
    frame = np.int16(frame)
    frame = frame * (contrast/127+1) - contrast + brightness
    frame = np.clip(frame, 0, 255)
    frame = np.uint8(frame)
    return frame

def process_video(video_path, output_path, args):
    """Read video and apply augmentation"""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            if args.augment == "temporal":
                frames = add_temporal(frame, args.speed_factor)
                for frame in frames:
                    out.write(frame)
            elif args.augment == "spatial":
                frame = add_spatial(frame, args.horizontal_shift, args.vertical_shift)
                out.write(frame)
            elif args.augment == "noise":
                frame = add_noise(frame, args.noise_mean, args.noise_std)
                out.write(frame)
            elif args.augment == "brightness_contrast":
                frame = change_brightness_contrast(frame, args.brightness, args.contrast)
                out.write(frame)
        else:
            break

    cap.release()
    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, required=True)
    parser.add_argument('--output_folder', type=str, required=True)
    parser.add_argument('--augment', type=str, choices=["temporal", "spatial", "noise", "brightness_contrast"], required=True)
    parser.add_argument('--force', type=str, choices=["yes", "no"], default="no", help="Default is 'no'.")

    parser.add_argument('--speed_factor', type=int, default=2, help="For temporal augmentation, number of times a frame is duplicated. Default is 2.")
    parser.add_argument('--horizontal_shift', type=int, default=100, help="For spatial augmentation, horizontal shift in pixels. Default is 100.")
    parser.add_argument('--vertical_shift', type=int, default=100, help="For spatial augmentation, vertical shift in pixels. Default is 100.")
    parser.add_argument('--noise_mean', type=float, default=0.0, help="For noise augmentation, mean of the gaussian noise. Default is 0.0.")
    parser.add_argument('--noise_std', type=float, default=50.0, help="For noise augmentation, standard deviation of the gaussian noise. Default is 50.0.")
    parser.add_argument('--brightness', type=int, default=100, help="For brightness and contrast augmentation, increase in brightness level. Default is 100.")
    parser.add_argument('--contrast', type=int, default=100, help="For brightness and contrast augmentation, increase in contrast level. Default is 100.")

    args = parser.parse_args()

    if not os.path.exists(args.input_folder):
        print(f"Input folder '{args.input_folder}' does not exist.")
        sys.exit(1)

    if args.force == "no" and os.path.exists(args.output_folder):
        print(f"Output folder '{args.output_folder}' already exists. To overwrite, use --force yes.")
        sys.exit(1)

    os.makedirs(args.output_folder, exist_ok=True)

    for file in os.listdir(args.input_folder):
        if file.endswith(".mp4"):
            process_video(os.path.join(args.input_folder, file), os.path.join(args.output_folder, file[:-4]+"-"+args.augment+".mp4"), args)

