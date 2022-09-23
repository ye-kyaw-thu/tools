from skimage import io
import sys

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Printing resolution of an image
# Last updated: 23 Sept 2022
# How to run:
# $ python ./print-img-resolution.py ./piza.jpg 
# Resolution:  1152 X 2048 
# Channel: 3

img = io.imread(sys.argv[1])
resolution = img.shape
print("Resolution: ", resolution[0], "X", resolution[1], "\nChannel:", resolution[2])
