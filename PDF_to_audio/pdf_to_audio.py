import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

start_page = int(input(f"Enter the starting page to read from 0 to {pages}: "))
range_of_pages = int(input("Enter the number of pages : "))

for num in range(start_page, start_page + range_of_pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()