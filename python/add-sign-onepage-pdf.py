# !/usr/bin/python

# ref: https://github.com/pymupdf/PyMuPDF
# ref: https://stackabuse.com/working-with-pdfs-in-python-adding-images-and-watermarks/
# Written by Ye Kyaw Thu, Affiliate Professor, CADT, Cambodia
# For adding signature image to one page PDF file 
# Used for my NECTEC salary document signing
# Last updated: 19 Sept 2022
# How to run: python add-sign-onepage-pdf.py

import fitz

pdf = fitz.open("nov.pdf")
output_file = "nov-signed.pdf"
img = open("sign.png", "rb").read()

image_rectangle = fitz.Rect(80,500,250,650)

page_no = pdf[0]
page_no.insert_image(image_rectangle, stream=img)

pdf.save(output_file)
