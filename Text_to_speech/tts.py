# Text to Speech Conversion
from gtts import gTTS,lang,gTTSError
import os
try:
    text = input("Enter text for speech: ")
    while (text.lower().strip() == ""):
        text = input("Enter some text for speech: ")    
    language = input("Enter language code: ").lower()
    while(language.strip() == ""):
        language = input("Enter code again: ").lower()
    while(language not in lang.tts_langs()):
        language = input("Enter correct code: ").lower()
    myobj = gTTS(text = text,lang = language, slow = False)
    myobj.save("welcome.mp3")
    print("Speech file saved successfully!")
    os.system("start welcome.mp3")
except gTTSError as e:
    print(f"Google TTS error encountered: {e}")
    print("Please check your internet connection.")
except Exception as e:
    print(f"An unexpected error occured: {e}")
