import sys
import numpy as np

# for element-wise character counting
# written by Ye Kyaw Thu, Okayama Prefectural University, Japan
# How to run: python ./numpy-array-element-compare.py <filename> <character>
# e.g. python ./char-count-element-wise.py ./file1.txt a
# e.g. python ./char-count-element-wise.py ./my.txt လား

file1 = sys.argv[1]
search_char = sys.argv[2]
with open(file1) as f1:
   for line in f1:
     npLine = np.array(line.split(" "), dtype=np.str)
     result = np.char.count(npLine, search_char)
     print(result)
