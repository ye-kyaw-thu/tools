import sys
import re
import argparse

import subprocess
import math
from collections import Counter
import jellyfish
import epitran

# Edit distance calculation with Map-1 (Phonetic Mapping), Map-2 (Sound Mapping) and Map-3 (Vowel Position Mapping)
# Input file should be CSV file  
# Support six edit-distance calculations (levenshtein, damerau_levenshtein, hamming_distance, jaro_winkler, cosine, jaccard)
# Written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
# Released Date: 30 July 2021
# How to run:
# $ python ./str2my-edit-distances.py --help
# $ python ./str2my-edit-distances.py --map 1 --distance 'levenshtein' ./head.train.csv 4 5
# $ python ./str2my-edit-distances.py --map 2 --distance 'levenshtein' ./head.train.csv 4 5
# $ python ./str2my-edit-distances.py --map 3 --distance 'levenshtein' ./head.train.csv 4 5
# $ python ./str2my-edit-distances.py --map 3 --distance 'cosine' ./head.train.csv 4 5
# $ python ./str2my-edit-distances.py --field_delimiter ',' --skip_header 1 --map 1 --distance 'levenshtein' --original_strings 0 ./head.train.csv 4 5
# $ python ./str2my-edit-distances.py --field_delimiter $'\t' --skip_header 0 --map 1 --distance 'levenshtein' --original_strings 0 ./f4-5.tab.txt 1 2
#
# If you used this tool, please cite following papers:
# Khaing Hsu Wai, Ye Kyaw Thu, Swe Zin Moe, Hnin Aye Thant, Thepchai Supnithi, "Myanmar (Burmese) String Similarity Measures based on Phoneme Similarity", Journal of Intelligent Informatics and Smart Technology, April 1st Issue, 2020, pp. 27-34. (submitted December 21, 2019; accepted March 6, 2020; revised March 16, 2020; published online April 30, 2020) JIIST 2020 Journal Paper
#
# Khaing Hsu Wai, Ye Kyaw Thu, Hnin Aye Thant, Swe Zin Moe and Thepchai Supnithi, "String Similarity Measures for Myanmar Language (Burmese)", The First Workshop on NLP Solutions for Under Resourced Languages (NSURL 2019), 11-13 September 2019, Trento, Italy

### Proposed Mapping1: Phonetic Mapping
map1_dict  = [
    ('[a-zA-Z]', 'L'),
    ('[ကခ]', 'က'),
    ('[ဂဃ]', 'ဂ'),
    ('[စဆ]', 'စ'),
    ('[ဇဈ]', 'ဇ'),
    ('[ဋတ]', 'တ'),
    ('[ဌထ]', 'ထ'),
    ('[ဍဎ]', 'ဍ'),
    ('[ဏန]', 'န'),
    ('[ဒဓ]', 'ဒ'),
    ('[ပဖ]', 'ပ'),
    ('[ဗဘ]', 'ဘ'),
    ('[ယရ]', 'ရ'),
    ('[လဠ]', 'လ'),
    ('[သဿ]', 'သ'),
    ('ျ|ြ', 'y'),
    ('ွ|ှ', ''),
    ('ဣ|ဤ|၏|ိ|ီ|ည်', 'i'),
    ('က်|ပ်|တ်', 'd'),
    ('န်|မ်|ံ','n'),
    ('ဲ|ရ်', 'e'),
    ('ဥ|ဦ|ု|ူ', 'u'),
    ('ာ|ါ', 'r'),
    ('ဧ|ေ', 'a'),
    ('့|း', ''),
     ('္', ''),
    ('ဩ|ဪ|သြ|သြော်', 'o'),
    ('၎င်း|၎', '၎'),
    ('၊|။', 's'),
    ('င်္|င်|င|ဉ်', 'in'),
    ('\?|\!|\.|\*|\-|\=|\&|\%|\$|#|"|\<|\>|\{|\}|\[|\]|\,|\+|\-', '$'),
    ('\s+', ' ')
]

def map1(s):
    for pattern, value in map1_dict:
        s = re.sub(pattern, value, s)
    return s

### Proposed Mapping 2: Sound Mapping
map2_dict  = [
    ('[a-zA-Z]', 'L'),
    ('[ကခဂဃငဟအ]', 'က'),
    ('[ညဉ]', 'ည'),
    ('[စဆဇဈ]', 'စ'),
    ('[ဋဌဍဏဎတထဒဓန]', 'တ'),
    ('[ပဖဗဘမ]', 'ပ'),
    ('[ယရ]', 'ရ'),
    ('[လဠ]', 'လ'),
    ('[သဿ]', 'သ'),
    ('ျ|ြ', 'y'),
    ('ွ|ှ', ''),
    ('ဣ|ဤ|၏|ိ|ီ|ည်', 'i'),
    ('က်|ပ်|တ်', 'd'),
    ('န်|မ်|ံ','n'),
    ('ဲ|ရ်', 'e'),
    ('ဥ|ဦ|ု|ူ', 'u'),
    ('ာ|ါ', 'r'),
    ('ဧ|ေ', 'a'),
    ('့|း', ''),
     ('္', ''),
    ('ဩ|ဪ|သြ|သြော်', 'o'),
    ('၎င်း|၎', '၎'),
    ('၊|။', 's'),
    ('င်္|င်|င|ဉ်', 'in'),
    ('\?|\!|\.|\*|\-|\=|\&|\%|\$|#|"|\<|\>|\{|\}|\[|\]|\,|\+|\-', '$'),
    ('\s+', ' ')
]

def map2(s):
    for pattern, value in map2_dict:
        s = re.sub(pattern, value, s)
    return s

### Proposed Mapping3: Vowel Position Mapping
map3_dict  = [
    ('[a-zA-Z]', 'F'),
    ('[က-အ]', 'c'),
    ('ျ|ြ', 'y'),
    ('ေ', 'l'),
    ('ိ|ီ|ဲ|ံ', 'u'),
    ('ွ|ှ|ု|ူ', 'd'),
    ('ာ|ါ|့|း', 'r'),
    ('္', 'p'),
     ('်', 'k'),
    ('[ဣဤဥဦဧဩဪဿ၌၍၏]', 'I'),
    ('၊|။', 's'),
    ('[၀-၉]', 'n'),
    ('\?|\!|\.|\*|\-|\=|\&|\%|\$|#|"|\<|\>|\{|\}|\[|\]|\,|\+|\-', '$'),
    ('[0-9]', 'D')
]

#change into Myanmar syllable combination structure
def map3(s):
    for pattern, value in map3_dict:
        s = re.sub(pattern, value, s)
    return s

# get words
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

# Text to Vector Conversion
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def ngrams(sequence, n):
    sequence = list(sequence)
    count = max(0, len(sequence) - n + 1)
    return [tuple(sequence[i:i+n]) for i in range(count)] 

def jaccard_similarity(list1,list2):
    intersection=len(list(set(list1).intersection(list2)))
    #print(list(set(list1).intersection(list2)))
    union=(len(list1)+len(list2))-intersection
    return float(intersection/union)

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[lenstr1-1,lenstr2-1]

def calc_distance(string1, string2, method):
    if method == "levenshtein":
        distance=jellyfish.levenshtein_distance(string1, string2)
    elif method == "damerau_levenshtein":
        distance= damerau_levenshtein_distance(string1, string2)
    elif method == "hamming_distance":
        distance= jellyfish.hamming_distance(string1, string2)
    elif method == "jaro_winkler":
        distance= jellyfish.jaro_winkler(string1, string2)
    elif method == "cosine":
        vector1 = text_to_vector(string1)
        vector2 = text_to_vector(string2)
        distance = get_cosine(vector1, vector2)
    elif method=="jaccard":
        x_set=ngrams(string1, 1)
        y_set=ngrams(string2, 1)
        distance = jaccard_similarity(x_set, y_set)

    return distance

parser=argparse.ArgumentParser()
parser.add_argument('inputFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?', help="input filename of the CSV file")
parser.add_argument('string1_field', type=int, default='1', help="field number of String1 in the CSV file, default=1") 
parser.add_argument('string2_field', type=int, default='2', help="field number of String2 in the CSV file, default=2") 

parser.add_argument('-m', '--map', type=int, default=1, help="""assign mapping type, "1" for Phonetic, "2" for Sound and "3" for Vowel Position, "0" for skip mapping process (e.g. when you calculate baseline edit distance with raw Myanmar sentences, you can also use --map 0 for English sentences)""")
parser.add_argument('-d', '--distance', type=str, default='levenshtein', help="assign distance measures: levenshtein, damerau_levenshtein, hamming_distance, jaro_winkler, cosine, jaccard")
parser.add_argument('-f', '--field_delimiter', type=str, default=',', help="""assign field delimiter such as $'\\t' for <TAB>, ',' for comma, default="," """)
parser.add_argument('-s', '--skip_header', type=int, default=1, help="""skip CSV header line or no distance calculation for the first line. "1" for true and "0" for false, default=1""")
parser.add_argument('-o', '--original_strings', type=int, default=1, help="""printing original input string1 and string2, "1" for true and "0" for false, default=1""")

args=parser.parse_args()
textLines=args.inputFile.readlines()

# check for skipping 1st line
if args.skip_header == 1:
    csvHeaderLine = textLines.pop(0) #pop only the first line
    # print(csvHeaderLine, end = '') # if you want you can print out the header of CSV file

# assign field delimiter
delimiter=args.field_delimiter

def main (command_line=None):
    for line in textLines:
       # counting number of fields
        fields = line.split(delimiter)
        #print("Fields:", fields) # for debugging
        if len(fields) >= 2:
            string1 = fields[args.string1_field-1]
            string2 = fields[args.string2_field-1]
        #string1="this"
        #string2="is"
        if args.map == 1:
            string1map1 = map1(string1.rstrip("\n"))
            string2map1 = map1(string2.rstrip("\n"))        
            result=calc_distance(string1map1, string2map1, args.distance)
            if args.original_strings == 0:
                fields = [string1map1, string2map1, str(result)]
            elif args.original_strings == 1:
                fields = [string1, string2, str(result)]
                            
            print(','.join(fields))
            
        elif args.map == 2:
            string1map2 = map2(string1.rstrip("\n"))
            string2map2 = map2(string2.rstrip("\n"))        
            result=calc_distance(string1map2, string2map2, args.distance)
            if args.original_strings == 0:
                fields = [string1map2, string2map2, str(result)]
            elif args.original_strings == 1:
                fields = [string1, string2, str(result)]
                
            print(','.join(fields))            
            
        elif args.map ==3:
            string1map3 = map3(string1.rstrip("\n"))
            string2map3 = map3(string2.rstrip("\n"))        
            result=calc_distance(string1map3, string2map3, args.distance)
            if args.original_strings == 0:
                fields = [string1map3, string2map3, str(result)]
            elif args.original_strings == 1:
                fields = [string1, string2, str(result)]
                
            print(','.join(fields))            
        elif args.map ==0:
            result=calc_distance(string1.rstrip("\n"), string2.rstrip("\n"), args.distance)
            fields = [string1, string2, str(result)]            
            
            print(','.join(fields))                    
     
if __name__ == "__main__":
    main ()
