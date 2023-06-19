# Written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
# Create a new folder and copy augmented video files based on their classes (i.e. basename of the file)
# If you want to move instead of copy, update the code: shutil.copy to shutil.move
# Last updated: 19 June 2023

import os
import shutil
import sys
import argparse

def get_classes_from_dir(base_dir):
    class_names = set()
    for file_name in os.listdir(base_dir):
        if not os.path.isdir(os.path.join(base_dir, file_name)):
            class_name = os.path.splitext(file_name)[0]
            class_names.add(class_name)
    return list(class_names)

def write_index_file(class_index, output_dir):
    with open(os.path.join(output_dir, 'index.txt'), 'w', encoding='utf8') as f:
        for class_name, index in class_index.items():
            f.write(f'{class_name} : {index}\n')

def main(base_dir, output_folder, use_index):
    base_dir = os.path.expanduser(base_dir)
    output_dir = os.path.join(os.path.dirname(base_dir), output_folder)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get class names
    classes = get_classes_from_dir(base_dir)

    # Create a class index if the --index option is set
    class_index = {class_name: index for index, class_name in enumerate(classes, 1)} if use_index else None

    # Write the index file if the --index option is set
    if class_index:
        write_index_file(class_index, output_dir)

    for root, dirs, files in os.walk(base_dir):
        for class_name in classes:
            # Use the class index for the class directory name if the --index option is set
            class_dir_name = str(class_index[class_name]) if class_index else class_name

            # Create class directory
            class_dir = os.path.join(output_dir, class_dir_name)
            os.makedirs(class_dir, exist_ok=True)

            # Copy files
            for filename in files:
                if filename.startswith(class_name):
                    shutil.copy(os.path.join(root, filename), os.path.join(class_dir, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort files into class directories.')
    parser.add_argument('base_dir', help='The directory containing the files to sort.')
    parser.add_argument('output_folder', help='The directory to output the class directories to.')
    parser.add_argument('-i', '--index', action='store_true', help='Use indexed class names instead of the original names.')
    args = parser.parse_args()
    
    main(args.base_dir, args.output_folder, args.index)
