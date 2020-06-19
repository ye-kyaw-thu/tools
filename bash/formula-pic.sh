#!/bin/bash
# for making a formula picture file with the help of TeX typesetting engine
# written by Ye Kyaw Thu, Language Understanding Lab., Pyin Oo Lwin, Myanmar
# Last updated: 19 June 2020 
# How to run: bash ./mytext2pic.sh <input-file>
# See following running examples:
#
# bash ./formula-pic.sh "\tilde{e} = arg \max_{e} P(e|f) = arg \max_{e} P(f|e) P(e)"
# Ref: https://en.wikipedia.org/wiki/Statistical_machine_translation
# Statistical MT formula, f is source language (e.g. French), e is target language (e.g. English)
#
# bash ./formula-pic.sh "W^* = arg \max_{W} P(W/X) = arg \max_{W} P(X/W) P(W)"
# Ref: https://en.wikipedia.org/wiki/Speech_recognition
# Ref: https://www.inf.ed.ac.uk/teaching/courses/asr/2013-14/asr01-intro.pdf
# Statistical ASR formula, X is the sequence of acoustic feature vectors (observations)
# and W denotes a word sequence, the most likely word sequence W∗
#
# bash ./formula-pic.sh "X = arg \max P(X|Y, \theta)"
# Ref: https://en.wikipedia.org/wiki/Speech_synthesis
# DeepLearning based TTS formula, where "theta"  is the model parameter.

# Ref: https://tex.stackexchange.com/questions/34054/tex-to-image-over-command-line/34058#34058
# Ref: http://phyletica.org/tex-equations-on-cmd-line/

# preparing latex file named "formula.tex"
echo "\documentclass[border=2pt]{standalone}" > formula.tex
echo "\usepackage{amsmath}" >> formula.tex
echo "\usepackage{varwidth}" >> formula.tex
echo "\begin{document}" >> formula.tex
echo "\begin{varwidth}{\linewidth}" >> formula.tex
echo "\[ $1 \]" >> formula.tex
echo "\end{varwidth}" >> formula.tex
echo "\end{document}" >> formula.tex

# compile ./formula.tex with xelatex. You can use other latex engine such as pdflatex
xelatex ./formula.tex

# converting pdf to png, if you need you update "-density" and "-quality" options of convert command
# Note: The convert program is a member of the ImageMagick suite of tools and if you don't have you have to install ImageMagick package on your computer
convert -density 300 formula.pdf -quality 90 formula.png

# if you don't need the output latex file, uncomment following statement
# rm ./formula.tex

