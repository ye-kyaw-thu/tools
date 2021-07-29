import sys
import re
import argparse

# Converting input CSV Myanmar sentences into Map-1 (Phonetic Mapping), Map-2 (Sound Mapping) and Map-3 (Vowel Position Mapping)
# Written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
# Released Date: 28 July 2021
# How to run:
# e.g. $ python ./csv-str2mapping123.py --help
# e.g. $ python ./csv-str2mapping123.py --csvFile head.train.csv --map 1
# e.g. $ cat head.train.csv | python ./csv-str2mapping123.py --map 3

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

parser=argparse.ArgumentParser()
parser.add_argument('-i', '--csvFile', default=sys.stdin, type=argparse.FileType('r'), nargs='?')
parser.add_argument('-m', '--map', type=int, default=1, help="assign mapping type, 1 for Phonetic, 2 for Sound and 3 for Vowel Position")

args=parser.parse_args()
textLines=args.csvFile.readlines()
csvHeaderLine = textLines.pop(0) #pop only the first line
print(csvHeaderLine, end = '')

def main (command_line=None):
    for line in textLines:
        lineCleaned = line.rstrip("\n")
        f1, f2, f3, f4, f5, f6 = lineCleaned.split(',')
        if args.map == 1:
            f4mapped = map1(f4.rstrip("\n"))
            f5mapped = map1(f5.rstrip("\n"))
            fields = [f1, f2, f3, f4mapped, f5mapped, f6]
            print(','.join(fields))
        elif args.map == 2:
            f4mapped = map2(f4.rstrip("\n"))
            f5mapped = map2(f5.rstrip("\n"))
            fields = [f1, f2, f3, f4mapped, f5mapped, f6]
            print(','.join(fields))
        elif args.map ==3:
            f4mapped = map3(f4.rstrip("\n"))
            f5mapped = map3(f5.rstrip("\n"))
            fields = [f1, f2, f3, f4mapped, f5mapped, f6]
            print(','.join(fields))
     
if __name__ == "__main__":
    main ()

