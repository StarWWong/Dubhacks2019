# Dubhacks2019
This project was done for a one-day hackathon. The goal of the project was to take homework and exam PDFs, identify problems and generate a practice exam based on those questions.

```generated.pdf``` is the newly generated practice exam, and ```generated.tex``` is a LaTeX file used to generate and modify the exam during execution.

Homework PDFs are placed in the "hw pdfs" file.

---
To run, cd to the directory and run ```python3 ReadPDF.py```
---
Requirements:
You will need an installation of LaTeX and the tika package for python3.
Install tika: ```pip3 install tika```
Install LaTeX: ```https://www.latex-project.org/get/```

(note – we used the MacTeX package for Mac)
