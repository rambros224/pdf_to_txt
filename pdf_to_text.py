# a heuristic excerise 
# this script should translate a pdf to text using proper modules
# requriements - (preferably python environment) .. pip install 

import fitz #PyMuPDF
from deep_translator import GoogleTranslator # can use this for english to x.. needs deep-translator

import os
import argparse

# command parser to pass arguments at cli
parser=argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="the pdf document")
parser.add_argument("--output", type=str, help="the output text document filename")
args=parser.parse_args()

# the pdf
pdf_path=args.input
output_path=args.output


def extract_text_from_pdf(pdf_path):
	text=""
	with fitz.open(pdf_path) as doc:
		for page in doc:
			text += page.get_text("text")+"\n"
	return text

text=extract_text_from_pdf(pdf_path)
with open(output_path, "w", encoding="utf-8") as file:
	file.write(text)

# ------------------------------
# not used, but useful
def translate_text(text, target_language="fr"):
	return GoogleTranslator(source="auto", target=target_language.translate(text))
