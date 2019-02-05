import sys

# for checking no of tokens difference between parallel sentences
# written by Ye Kyaw Thu
# How to run: python ./chk-token.py <filename1> <filename2>
# eg 1: python ./chk-token.py ./writing.txt ./reading.txt $'\t'
# eg 2: python ./chk-token.py ./writing.txt ./reading.txt $'\n'

f1 = sys.argv[1]
f2 = sys.argv[2]
sp = sys.argv[3]

fp1=open(f1,"r")
fp2=open(f2,"r")

for line1, line2 in zip(fp1, fp2):
   if line1.count(' ')!=line2.count(' '):
      print(line1.strip() + sp + line2.strip())
        
fp1.close()
fp2.close()
