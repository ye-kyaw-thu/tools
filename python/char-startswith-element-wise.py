import sys
import numpy as np

# for element-wise counting startswith X
# written by Ye Kyaw Thu, Okayama Prefectural University, Japan
# How to run: python char-startswith-element-wise.py <filename> <character or word>
# e.g. python ./char-startswith-element-wise.py ./my.txt ပ

file1 = sys.argv[1]
search_char = sys.argv[2]
with open(file1) as f1:
   for line in f1:
     npLine = np.array(line.split(" "), dtype=np.str)
     result = np.char.count(npLine, search_char)
     print(result)
