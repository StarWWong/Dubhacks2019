# Read in PDF as raw text, parse for individual questions
import re

import textract
import PyPDF2

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def read(filename):

    pdfFileObj = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages
    count = 0
    text = ""
    # The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    # This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
    if text != "":
        text = text
    # If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
    else:
        text = textract.process(fileurl, method='tesseract', language='eng')
    # Now we have a text variable which contains all the text derived from our PDF file.
    # Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
    # Now, we will clean our text variable, and return it as a list of keywords.
    # The word_tokenize() function will break our text phrases into #individual words
    tokens = word_tokenize(text)
    # we'll create a new list which contains punctuation we wish to clean
    punctuations = ['(', ')', ';', ':', '[', ']', ',']
    # We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
    stop_words = stopwords.words('english')
    # We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

    print(text)


def readTika(filename):

    from tika import parser

    rawText = parser.from_file(filename)

    return rawText['content']

document = readTika("/Users/adkn/Sync/Projects/Build/Dubhacks2019/hw test/hw1_w18.pdf")

def extractQuestions(doc_text):
    # so given a list of each "line" in the PDF document, pull out the ones that are questions
    # and/or parts of questions
    # print(doc_text)
    encounteredQuestion = False
    questions = []
    questionToAdd = ""
    for line in doc_text.splitlines():
        # need to mark beginning of questions and end of questions
        if re.match(r"[0-9]+. ", line):

            if encounteredQuestion:
                encounteredQuestion = False
                questions.append(questionToAdd)
                questionToAdd = ""

            if not encounteredQuestion:
                encounteredQuestion = True
            questionToAdd += line + "\n"

        elif encounteredQuestion:
            questionToAdd += line + "\n"



    return questions

q = extractQuestions(document)
print(q[0]) # question1, with parts a, i, ii, b, iii, etc...
print("=====================")
print(q[1]) # same for question2, so on.
# todo clean up whitespace in output. Capture of exponents is still broken but we'll run with it.



