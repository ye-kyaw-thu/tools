import sys
import numpy as np

# for comparing each numpy array element
# written by Ye Kyaw Thu, Okayama Prefectural University, Japan
# How to run: python ./numpy-array-element-compare.py <filename> <filename>
# e.g. python ./numpy-array-element-compare.py ./file1.txt ./file2.txt

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1, open(file2) as f2:
   for x, y in zip(f1, f2):
     
     npX = np.array(x.split(" "), dtype=np.str)
     npY = np.array(y.split(" "), dtype=np.str)
     out = np.char.equal(npX, npY)
     print(out)
