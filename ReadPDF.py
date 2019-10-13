# Read in PDF as raw text, parse for individual questions
import re, os, random
from tika import parser


def readTika(filename):
    rawText = parser.from_file(filename)
    return rawText['content']


def extractQuestionsFromSingleDoc(doc_text):
    # so given a list of each "line" in the PDF document, pull out the ones that are questions
    # and/or parts of questions
    # print(doc_text)
    encounteredQuestion = False
    questions = []
    questionToAdd = []
    print(doc_text)
    # for line in doc_text.splitlines():
    for line in doc_text:
        # need to mark beginning of questions and end of questions
        if re.match(r"[0-9]+. ", line):

            if encounteredQuestion:
                encounteredQuestion = False
                questions.append(questionToAdd)
                questionToAdd = []

            if not encounteredQuestion:
                encounteredQuestion = True
            questionToAdd.append(line)

        elif encounteredQuestion:
            if line.strip() != "":
                questionToAdd.append(line)

    return questions


def extractAllQuestions(documents):
    allQuestions = []

    for doc in documents:
        allQuestions.append(extractQuestionsFromSingleDoc(doc))

    return allQuestions


def latexToPDF(list_of_questions):
    # 1) needs to select 10 randomly selected questions from list
    # 2) write those questions on a specific line of our base_test.tex template line 37, index 36
    # 3) generate a new PDF from that .tex file
    # 4) ???
    # 5) profit?

    # 1) select 10 random questions

    test_questions = ""
    for i in range(10):
        assignment = random.choice(list_of_questions)
        selectedQ = random.choice(assignment)
        for line in selectedQ:
            test_questions += line + "\n"
        test_questions += "\n\n\n\n\n"
        # remove randomly chosen problem from the pool
        # assignment.remove([selectedQ])

    # 2) write questions to line 37, index 36
    base_tex = [line for line in open("base_test.tex", "r")]
    base_tex[36] = test_questions
    generated = open("generated.tex", "w")
    generated.writelines(base_tex)
    generated.close()

    os.system("pdflatex generated.tex generated.pdf")


# not really a function, directory will change based on the frontend and backend connections
basedir = os.getcwd()
directories = [f for f in os.listdir("hw") if not f.__contains__("soln")
               and not f.__contains__("solutions")]
docs = []
for d in directories:
    # docs.append(readTika(basedir + "/hw/" + d))
    docs.append(open(basedir + "/hw/" + d, "r").readlines())


latexToPDF(extractAllQuestions(docs))








