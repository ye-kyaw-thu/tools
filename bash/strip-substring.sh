#!/bin/bash

# for striping substring from the front or back of a given string
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# How to use: ./strip-substring.sh [fs|bs|fl|bl] "string" "sub_string"
# Here, fs=front-shortest, bs=back-shortest, fl=front-longest, bl=back-longest 
# e.g.1: ./strip-substring.sh fs "ကျားဆိုမှကျား" "*ကျား"
# e.g.2: ./strip-substring.sh bs "ကျားဆိုမှကျား" "*ကျား"
# e.g.3: ./strip-substring.sh fl "ကျားဆိုမှကျား" "*ကျား"
# e.g.4: ./strip-substring.sh bl "ကျားဆိုမှကျား" "*ကျား" 

strip_option=$1;
string=$2;
sub_string=$3;

case $strip_option in
   front-shortest|fs)
      echo "strip_option:$strip_option, string:$string, sub_string:$sub_string";
      # stripping from front (shortest match)
      echo "stripping from front (shortest match)";
      # e.g. echo ${test#*.}
       echo ${string#$sub_string};
      ;;
   back-shortest|bs)
      # stripping from back (shortest match)
      echo "stripping from back (shortest match)";
      #echo ${test%.*}
      echo ${string%$sub_string};
      ;;
   front-longest|fl)
      # stripping from front (longest match)
      echo "stripping from front (longest match)";
      #echo ${test##*.}
      echo ${string##$sub_string};        
      ;; 
   back-longest|bl)
      # stripping from back (longest match)
      echo "stripping from back (longest match)";
      #echo ${test%%.*}
      echo ${string%%$sub_string};
      ;; 
   *)
      echo "options: front-shortest|fs, back-shortest|bs, front-longest|fl and back-longest|bl"
      ;;
esac

