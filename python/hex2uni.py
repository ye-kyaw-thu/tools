import sys

# Sometimes, we need to know hex values when you are working with Python2x programs
# Written by Ye, LST Lab., NECTEC, Thailand
# Ref: https://gehrcke.de/2014/02/command-line-argument-binary-data/
# How to run: 
# e.g. python2.7 ./hex2uni.py $'\xe1\x80\x80\xe1\x80\xae\xe1\x80\x9c\xe1\x80\xba'
# output: ကီလ်

# this also work!
print(bytes.decode(b"\xe1\x80\x80\xe1\x80\xae\xe1\x80\x9c\xe1\x80\xba", 'utf-8'))

for argument in sys.argv[1:]:
    decoded_argument = argument.decode("utf-8")
    print (decoded_argument)
