import sys
from skimage import io
from skimage import color
from skimage import data
from pylab import *

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Convert RGB to Greyscale
# Last updated: 23 Sept 2022
# How to run:
# $ python ./RGB2grey.py ./piza.jpg 

img = io.imread(sys.argv[1])
io.imshow(img)
io.show() # show the original image file

img_converted = color.rgb2grey(img)

io.imshow(img_converted)
io.show() # show the converted greyscale file

io.imsave("out.jpg", img_converted)

