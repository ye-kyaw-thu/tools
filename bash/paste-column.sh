#!/bin/bash

# for pasting column by column of two input files
# Note: equal no. of columns are expected!
# Written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# How to run: ./paste-column.sh <input-file1> <input-file2>
# e.g. ./paste-column.sh ./f1.10lines ./f2.10lines 

# e.g. cat file1
#က ကြိုး ကြာ
#က ချောင် လွမ်း နန်း
#
# e.g. cat file2
#Ka Kyoe Kyar
#Ka Chaung Lwan Nan
#
# e.g. ./paste-column.sh file1 file2
#က_Ka ကြိုး_Kyoe ကြာ_Kyar
#က_Ka ချောင်_Chaung လွမ်း_Lwan နန်း_Nan

# Description of exec command
# from: https://www.computerhope.com/unix/bash/exec.htm
# exec is useful when you want to run a command, 
# but you don't want a bash shell to be the parent process. 
# When you exec a command, it replaces bash entirely

# open input files (i.e. $1 and $2) with file descriptor 3 and 4 for reading
exec 3<$1 4<$2

# reading line by line from file descriptors 3 and 4
while read -u 3 line3 ; read -u 4 line4 
do 
   # printf command will print %s argument line by line
    echo $(paste -d_ <(printf '%s\n' $line3) <(printf '%s\n' $line4))
done
