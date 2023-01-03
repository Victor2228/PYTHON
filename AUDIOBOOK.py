import pyttsx3
import PyPDF2
with open('after-twenty-years.pdf', 'rb') as book:
    content_all = ""
    reader = PyPDF2.PdfReader(book)
    speaker = pyttsx3.init()
    speaker.setProperty("rate", 150)
    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()
        content_all += content
    speaker.save_to_file(content_all, "After-Twenty-Years.mp3")
    speaker.runAndWait()
