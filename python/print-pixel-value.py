from skimage import io
import sys

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Printing pixel values of an image
# Last updated: 23 Sept 2022
# How to run:
# $ python ./print-pixel-value.py ./piza.jpg 

img = io.imread(sys.argv[1])
#print(img.flatten()) # print abstruct version
print(*img.flatten(), sep=', ') # print all elements or pixel values with comma separator

