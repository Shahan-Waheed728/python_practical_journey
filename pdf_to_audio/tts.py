from pypdf import PdfReader
from gtts import gTTS
import os
try:
    with open('Atomichabits.pdf','rb') as f:
        pdfReader = PdfReader(f)
        while True:
            try:
                page = int(input("Enter page to read: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if 1 <= page <= len(pdfReader.pages):
                break
            print(f"Please enter a number between 1 and {len(pdfReader.pages)}")
        from_page = pdfReader.pages[page-1]
        text = from_page.extract_text()
        if not text or not text.strip():
            print("No extractable text found on this page.")
        print("Content is extracting...")
        language = "en"
        myobj = gTTS(text = text , lang = language ,slow = False)
        myobj.save(f"page_{page}.mp3")
        os.system(f"start page_{page}.mp3")
except FileNotFoundError:
    print("Specified file does not exist.")    
except IndexError:
    print("Index out of range.")
except Exception as e:
    print(f"An unexpected error: {e}")
