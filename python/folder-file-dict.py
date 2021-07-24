import glob
import os

# Read full path recursively and build a dictionary
# with folder path key and filenname list as value
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Date: 22 July 2021
# How to run:
# e.g. $ python ./folder-file-dict.py

def get_dir_filename():
    #files = glob.glob('dataset2/**/*.wav', recursive=True)
    #files = glob.glob('tt/**/*.txt', recursive=True)
    files = glob.glob('dataset2/ot-data/**/*.wav', recursive=True)

    data = {}
    for fullpath in files:
        #print("fullpath:", fullpath)
        filename = os.path.basename(fullpath)
        #print("filename:", filename)
        foldername = os.path.dirname(fullpath)
        #print("foldername:", foldername)
        #label = fullpath.split("-")[-1].split(".")[0]
        if foldername in data:
            data[foldername].append(filename)
        else:
            data[foldername] = [filename]

    return data


def main():
    #data = get_dir_overview()
    data = get_dir_filename()
    print(data)
    
if __name__ == "__main__":
    main()
    
