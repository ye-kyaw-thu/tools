import sys
import gensim.models

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Word2Vec model building for segmented text file.
# input file က စာကြောင်း တစ်ကြောင်းစီ ရိုက်ထားပြီးတော့ 
# စာလုံး (e.g. word or syllable) ဖြတ်ထားပြီးသား ဖြစ်ရမယ်
#
# Last updated: 6 Oct 2022
# How to run:
# ./word2vec.py <corpus-file> <model-file> <bin|txt>
# python ./word2vec.py ../mypos-ver.3.0.word.txt w2v.model.bin bin
# python ./word2vec.py ../mypos-ver.3.0.word.txt w2v.model.txt txt

# References:
# Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. 2013a. Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781.
# https://pypi.org/project/gensim/

training_corpus = sys.argv[1]
model_filename = sys.argv[2]
filetype = sys.argv[3]

with open(training_corpus,'r') as f:
    plain_text = f.read()

sentences = plain_text.split("\n")  # Assume one sentence per line
tokenized = []

for sentence in sentences:
    # White-space-based word splitting, replace with a better tokenizer
    tokens = sentence.strip().split(' ')
    tokenized.append(tokens)

# Here, sample for subsampling rate, negative for negative samples, min_count for minimum threshold, workers for parallelize to all cores, hs=0 for no hierarchical softmax
# default values min_count is 5, workers=1
model = gensim.models.Word2Vec(sentences=tokenized, vector_size=100, window=3, sample=0.01, epochs=10, negative=3, min_count=2, workers=1, hs=0)

if (filetype == "bin"):
   model.save(model_filename)
elif (filetype == "txt"):
   model.wv.save_word2vec_format(model_filename, binary= False, write_header= False)


