#!/bin/bash

# Cryptography testing with Blowfish
# written by Ye Kyaw Thu, 
# Visiting Professor, NECTEC, Thailand

# Usage: ./blowfish.sh <text-filename> <pass phrase> <enc|dec>
# Encoding example: ./blowfish.sh plain.txt abc enc
# (Output filename is out.enc)

# Decoding example: ./blowfish.sh out.enc abc dec

# Blowfish is a symmetric-key block cipher, designed in 1993 by Bruce Schneie
# reference: https://en.wikipedia.org/wiki/Blowfish_(cipher)
# reference: Developing Console Application with Bash by Andy Carlson, Linux Journal Issue #282, October 2017

# Accept input from a file or from STDIN (standard input)
# "-" is for STDIN
if [ -f "$1" ]; then
   input="$1"; passcode="$2";
else 
   input="-"; passcode="$1";
fi

# assign last command line argument to the variable lastARG
lastARG=${!#} 

# if command line argument is < 2, usage will echo
# here, -z is for checking NULL variable
if [ $# -lt 2 ] || [ -z "$input" ] || [ -z "$passcode" ]; then
   echo "usage: ./blowfish.sh <file> <password> <enc|dec>";
else   
   if [ $lastARG == "enc" ]; then
      # encoding with blowfish
      cat $input | openssl enc -e -blowfish -pass pass:$passcode > out.enc;
   elif [ $lastARG == "dec" ]; then
      # decoding
      cat $1 | openssl enc -d -blowfish -pass pass:$2 > ${1%%.enc};
   else
      echo "Last option should be \"enc\" or \"dec\"";
   fi
fi
