import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Microphone is ready!")
    print("Say something...")
    audio = recognizer.listen(source,timeout = 5, phrase_time_limit = 10)
    print("Audio captured successfully!")    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.WaitTimeoutError:
        print("No speech detected.Please try again.")
    except sr.UnknownValueError:
        print("Sorry, I can't understand the audio.")
    except sr.RequestError as e:
        print(f"Could not connect to the recognition service, {e}")