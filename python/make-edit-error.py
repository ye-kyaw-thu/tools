import string
import random
import sys

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# make spelling errors based on edit-distance
# Reference: https://norvig.com/spell-correct.html
# Reference: https://stackoverflow.com/questions/51079986/generate-misspelled-words-typos 
# Reference: https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# Last updated: 21 Oct 2022
# How to run: python3 make-edit-error.py <input-file> [1 or 2 or r]
# Here, "1" for edit-distance 1, "2" for edit-distance 2 and "r" for random (i.e. 1 or 2 for each input line)

file = open(sys.argv[1], 'r')
ed = sys.argv[2]

def split(word):
   splitted_word =[(word[:i], word[i:]) for i in range(len(word) + 1)]
   return splitted_word

def delete(word):
   deleted_word = [l + r[1:] for l,r in split(word) if r]
   return deleted_word

def swap(word):
   swapped_word = [l + r[1] + r[0] + r[2:] for l, r in split(word) if len(r)>1]
   return swapped_word

def insert(word):
   inserted_word = [l + c + r for l, r in split(word) for c in random.choice(word + " ")]
   return inserted_word

def replace(word):
   #print("replace function")
   replaced_word = [l + c + r[1:] for l, r in split(word) if r for c in random.choice(word) if((l+c+r[1:]) != word)]
   #replaced_word = [l + c + r[1:] for l, r in split(word) if r for c in random.choice(word)]
   return replaced_word

def edit1(word):
   #print("1")
   func = random.choice([replace, delete, swap, insert])
   #print("Function: ", func)
   edit1_word = func(word)
   return edit1_word

def edit2(word):
   #print("2")
   edit2_word = [e2 for e1 in edit1(word) for e2 in edit1(e1)]
   return edit2_word

for line in file:

   input_word = line.strip()
   #print(input_word)
   if (ed == "1"):
      edit1_word = random.choice(edit1(input_word))
      print(input_word, '\t', edit1_word)
   elif (ed == "2"):
      edit2_word = random.choice(edit2(input_word))
      print(input_word, '\t', edit2_word)
   elif (ed == "r"):
      random_edit = random.choice([1, 2])
      if (random_edit == 1):
         edit1_word = random.choice(edit1(input_word))
         print(input_word, '\t', edit1_word)
      else:
         edit2_word = random.choice(edit2(input_word))
         print(input_word, '\t', edit2_word)

file.close()

