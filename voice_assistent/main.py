import speech_recognition as sr
from gtts import gTTS
import pygame
import pyjokes
import webbrowser
import datetime
import os

pygame.mixer.init()

def speak(text):
        myobj = gTTS(text=text,lang="en",slow=False)
        myobj.save("response.mp3")
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove("response.mp3")
def wish_user():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good Morning Shahan Waheed! ")
    elif current_hour < 18:
        speak("Good Afternoon Shahan Waheed! ")
    else:
        speak("Good Evening Shahan Waheed! ")
    speak("Your voice assistent is ready, Say something.")
def take_command():
    try:
        with sr.Microphone() as source:  
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source,timeout=5,phrase_time_limit=10)
            print("Audio captured successfully.")
            command = recognizer.recognize_google(audio)
            command = command.lower().strip()
        return command
    except sr.WaitTimeoutError:
        print("No speech detected.Please try again.")
    except sr.UnknownValueError:
        print("Sorry,I can't understand command.")
    except sr.RequestError as e:
        print(f"Could not connect to the connection service, {e}")
def assistant():
    wish_user()
    while True:
        command = take_command()                        
        if command == "open wikipedia":
            speak("Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.org/")
        elif command == "open youtube":
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif command == "open google":
            speak("Opening google...")
            webbrowser.open("https://www.google.com/")
        elif command == "time":
            speak(f"Current time is:{datetime.datetime.now().strftime('%I:%M %p')}")
        elif command == "joke":
            joke = pyjokes.get_joke()
            speak(joke)
        elif command == "goodbye":
            speak("Goodbye, Have a nice day.")
            break                
        else:
            print("Sorry, I don't understand that command.")   
assistant("")
            
