# !/usr/bin/python

# ref: https://github.com/pymupdf/PyMuPDF
# ref: https://stackabuse.com/working-with-pdfs-in-python-adding-images-and-watermarks/
# Written by Ye Kyaw Thu, Affiliate Professor, CADT, Cambodia
# For adding signature image to a PDF file pages
# Last updated: 18 Aug 2022

import fitz

pdf = fitz.open("NCR-NT-2022-17333-EN.pdf")
output_file = "output.pdf"
img = open("sign.png", "rb").read()

# define the position (upper-right corner)
#image_rectangle = fitz.Rect(450,20,550,120)
# define lower-rightcorner
image_rectangle = fitz.Rect(450,700,650,800)

# insert the sign image
for i in range(0, pdf.page_count):
   page_no = pdf[i]
   page_no.insert_image(image_rectangle, stream=img)


pdf.save(output_file)
