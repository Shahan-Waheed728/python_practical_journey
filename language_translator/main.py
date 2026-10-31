import speech_recognition as sr
from  googletrans import Translator
from gtts import gTTS
import asyncio
import os 
recog = sr.Recognizer()
mic = sr.Microphone()
# def speak(text):
# text = "Good morning"
# myobj = gTTS(text,lang="en",slow=False)
# myobj.save("response.mp3")
# os.system("start response.mp3")
translator = Translator()
with mic as source:
    print("Microphone is ready!")
    print("Say something...")
    audio = recog.listen(source,timeout=5,phrase_time_limit=10)
    text = recog.recognize_google(audio)
    result = text.lower().strip()
    async def main():
        async with Translator() as translator:
            text = result
            output = await translator.translate(text,src="en",dist="hi")
            print(f"Original text: {text}")
            print(f"Translated text: {output}")
    asyncio.run(main())