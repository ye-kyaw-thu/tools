import sys
import argparse
import qrcode

# making QR-code image(s)
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Reference: https://www.youtube.com/watch?v=-GmJLI122ZM

# How to run:
# echo "https://github.com/ye-kyaw-thu" | python ./mk-QR-code.py
# python ./mk-QR-code.py < ./links4QRcode.txt

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')

args=parser.parse_args()
textLines=args.inputFile.readlines()

count=0
for line in textLines:
   count +=1
   qrImage = qrcode.make(line)
   qrImage.save ("qrcode-"+str(count)+".jpg")
   




