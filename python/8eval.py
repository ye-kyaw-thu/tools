# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:43:04 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand

"""

import sys
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from nltk.translate.nist_score import sentence_nist, corpus_nist
from nltk.translate.ribes_score import sentence_ribes, corpus_ribes
from nltk.translate.chrf_score import sentence_chrf, corpus_chrf
from nltk.translate.gleu_score import sentence_gleu, corpus_gleu
from nltk.metrics.distance import edit_distance
from rouge import Rouge

import pyter
import argparse

from nltk.translate.bleu_score import SmoothingFunction

def calculate_sentence_scores(reference, hypothesis):
    reference_list = [reference.split()] 
    hypothesis_list = hypothesis.split()

    smoothie = SmoothingFunction().method4
    bleu = sentence_bleu(reference_list, hypothesis_list, smoothing_function=smoothie)
    ribes = sentence_ribes(reference_list, hypothesis_list)
    chrf = sentence_chrf(reference, hypothesis)

    # Lower the n-gram order to 3 for NIST score
    # 2, 3 is better for one sentence level evaluation
    # 4 တို့ဘာတို့ ထားရင် Error တက်ပြီး score မထုတ်ပေးနိုင် ဖြစ်တတ်လို့
    nist = sentence_nist(reference_list, hypothesis_list, 3)

    wer_score = edit_distance(reference, hypothesis) / max(len(reference), len(hypothesis))
    gleu = sentence_gleu(reference_list, hypothesis_list)
    ter = pyter.ter(reference, hypothesis)
    rouge = Rouge()
    rouge_scores = rouge.get_scores(hypothesis, reference)
    
    print(f"Sentence BLEU score: {bleu}")
    print(f"Sentence RIBES score: {ribes}")
    print(f"Sentence chrF++ score: {chrf}")
    print(f"Sentence NIST score: {nist}")
    print(f"Sentence WER score: {wer_score}")
    print(f"Sentence GLEU score: {gleu}")
    print(f"Sentence TER score: {ter}")
    print(f"Sentence ROUGE scores: {rouge_scores}")


def calculate_corpus_scores(reference_file, hypothesis_file):
    with open(reference_file, "r", encoding='utf-8') as ref_file, open(hypothesis_file, "r", encoding='utf-8') as hyp_file:
        references = [[line.strip().split()] for line in ref_file]
        hypotheses = [line.strip().split() for line in hyp_file]
        references_str = [' '.join(ref[0]) for ref in references]
        hypotheses_str = [' '.join(hyp) for hyp in hypotheses]

    bleu = corpus_bleu(references, hypotheses)
    ribes = corpus_ribes(references, hypotheses)
    chrf = corpus_chrf(references_str, hypotheses_str)
    nist = corpus_nist(references, hypotheses)
    wer_scores = [edit_distance(ref[0], hyp) / max(len(ref[0]), len(hyp)) for ref, hyp in zip(references, hypotheses)]
    wer_score = sum(wer_scores) / len(wer_scores)
    gleu = corpus_gleu(references, hypotheses)
    ter_scores = [pyter.ter(hyp, ref[0]) for ref, hyp in zip(references, hypotheses)]
    ter = sum(ter_scores) / len(ter_scores)
    rouge = Rouge()

    # if you change avg=False, you will get ROUGE score for each sentence
    rouge_scores = rouge.get_scores(hypotheses_str, references_str, avg=True)

    print(f"Corpus BLEU score: {bleu}")
    print(f"Corpus RIBES score: {ribes}")
    print(f"Corpus chrF++ score: {chrf}")
    print(f"Corpus NIST score: {nist}")
    print(f"Corpus WER score: {wer_score}")
    print(f"Corpus GLEU score: {gleu}")
    print(f"Corpus TER score: {ter}")
    print(f"Average Corpus ROUGE scores: {rouge_scores}")

parser = argparse.ArgumentParser(description='Calculate various translation scores.')
parser.add_argument('--level', type=str, help='Level of translation (sentence or corpus).')
parser.add_argument('--reference', type=str, help='Reference translation.')
parser.add_argument('--hypothesis', type=str, help='Hypothesis translation.')

args = parser.parse_args()

if args.level == "sentence":
    calculate_sentence_scores(args.reference, args.hypothesis)
elif args.level == "corpus":
    calculate_corpus_scores(args.reference, args.hypothesis)

