## Written by Ye Kyaw Thu, LU Lab., Myanmar
## for testing English and Burmese OCR
## last updated: 25 Nov 2023

import argparse
import pytesseract
from PIL import Image

def perform_ocr(image_path, language='eng'):
    """
    Perform OCR on an image file and return the extracted text.

    :param image_path: Path to the image file.
    :param language: Language code for OCR.
    :return: Extracted text as a string.
    """
    try:
        # Load the image from the given path
        image = Image.open(image_path)

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(image, lang=language)

        return extracted_text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='OCR Script to extract text from an image.')

    # Add the arguments
    parser.add_argument('image_path', type=str, help='Path to the image file.')
    parser.add_argument('-o', '--output', type=str, help='Output file to save the extracted text.')
    parser.add_argument('-l', '--language', type=str, default='eng', help='Language for OCR (default: eng).')

    # Execute the parse_args() method
    args = parser.parse_args()

    extracted_text = perform_ocr(args.image_path, args.language)

    if args.output:
        # If output file is specified, write the text to the file
        with open(args.output, 'w') as file:
            file.write(extracted_text)
        print(f"Extracted text written to {args.output}")
    else:
        # Otherwise, print the text
        print("Extracted Text:\n", extracted_text)

if __name__ == "__main__":
    main()
